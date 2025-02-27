import jsonpath


class AssertUtils:

    @staticmethod
    def equals(check_value, expect_value):
        """相等"""
        assert check_value == expect_value, f'{check_value} == {expect_value}'

    def equals_multiple(self, check_value, expect_values):
        """判断实际值是否等于期望值中的某一个"""
        assert check_value in expect_values, f'{check_value} not in {expect_values}'

    @staticmethod
    def less_than(check_value, expect_value):
        """小于"""
        assert check_value < expect_value, f'{check_value} < {expect_value})'

    @staticmethod
    def less_than_or_equals(check_value, expect_value):
        """小于等于"""
        assert check_value <= expect_value, f'{check_value} <= {expect_value})'

    @staticmethod
    def greater_than(check_value, expect_value):
        """大于"""
        assert check_value > expect_value, f'{check_value} > {expect_value})'

    @staticmethod
    def greater_than_or_equals(check_value, expect_value):
        """大于等于"""
        assert check_value >= expect_value, f'{check_value} >= {expect_value})'

    @staticmethod
    def not_equals(check_value, expect_value):
        """不等于"""
        assert check_value != expect_value, f'{check_value} != {expect_value})'

    @staticmethod
    def contains(check_value, expect_value):
        """包含"""
        assert expect_value in check_value, f'{expect_value} in {check_value})'

    @staticmethod
    def startswith(check_value, expect_value):
        """以什么开头"""
        assert str(check_value).startswith(str(expect_value)), f'{str(check_value)} startswith {str(expect_value)})'

    @staticmethod
    def endswith(check_value, expect_value):
        """以什么结尾"""
        assert str(check_value).endswith(str(expect_value)), f'{str(check_value)} endswith {str(expect_value)})'

    @staticmethod
    def length(check_value, expect_value):
        """校验数量"""
        assert len(check_value) == expect_value, f'{str(check_value)} == {str(expect_value)})'

    def extract_by_jsonpath(self, extract_value: dict, extract_expression: str): # noqa
        """根据jsonpath表达式提取数据
        :param extract_value: res.json()
        :param extract_expression: $.data.registrationToken
        :return: 提取的数据
        """
        extract_value = jsonpath.jsonpath(extract_value, extract_expression)
        if not extract_expression:
            return
        elif len(extract_value) == 1:
            return extract_value[0]
        else:
            return extract_value

    def validate_response(self, result, validate):
        """校验结果"""
        for check in validate:
            for check_type, check_value in check.items():
                # 实际结果
                actual_value = self.extract_by_jsonpath(result, check_value[0])
                # 预期结果
                expect_value = check_value[1]
                # 校验
                if check_type in ["eq", "equals", "equal"]:
                    if isinstance(expect_value, list):
                        self.equals_multiple(actual_value, expect_value)
                    else:
                        self.equals(actual_value, expect_value)
                elif check_type in ["lt", "less_than"]:
                    self.less_than(actual_value, expect_value)
                elif check_type in ["le", "less_or_equals"]:
                    self.less_than_or_equals(actual_value, expect_value)
                elif check_type in ["gt", "greater_than"]:
                    self.greater_than(actual_value, expect_value)
                elif check_type in ["ne", "not_equal"]:
                    self.not_equals(actual_value, expect_value)
                elif check_type in ["contains"]:
                    self.contains(actual_value, expect_value)
                elif check_type in ["startswith"]:
                    self.startswith(actual_value, expect_value)
                elif check_type in ["endswith"]:
                    self.endswith(actual_value, expect_value)
                elif check_type in ["length"]:
                    self.length(actual_value, expect_value)
                else:
                    print(f'{check_type}  not valid check type')
