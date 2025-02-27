import json
import re
from utils.AssertUtils import AssertUtils
from utils.YamlUtils import YamlUtil
from utils.log_utils import logger


class ExtractUtils:
    def __init__(self):
        self.jsonpath_utils = AssertUtils()
        self.yaml_utils = YamlUtil()

    def extract_data(self, result, extract):
        """
        根据extract表达式提取数据，预期结果内容并存入yaml
        :param result: result.json()
        :param extract: $.data.registrationToken
        :return:
        """
        if extract:
            for key, extract in extract.items():
                try:
                    value = self.jsonpath_utils.extract_by_jsonpath(result, extract)
                    # 写入value到yaml文件中
                    self.yaml_utils.write_yaml({key: value})
                except Exception as e:
                    logger.error(f"变量[{key}]写入extract.yaml文件失败：请检查error信息：{e}")

    def get_extract_value(self, key):
        """获取yaml文件中指定key的值"""
        try:
            data = self.yaml_utils.read_extract_yaml()
            return data[key]
        except Exception as e:
            logger.error(f"获取变量[{key}]的值失败：请检查error信息：{e}")

    def increment_extract_value(self, key):
        """获取yaml文件中指定key的值，并对提取的数字加1"""
        try:
            data = self.yaml_utils.read_extract_yaml()
            value = data[key]

            # 判断提取的值是否为数字，如果是则加1
            if isinstance(value, str) and re.match(r'.*\d+', value):  # 如果字符串中有数字
                # 找到数字并加1
                new_value = re.sub(r'\d+', lambda x: str(int(x.group()) + 1), value)
                return new_value
            return value
        except Exception as e:
            logger.error(f"获取变量[{key}]的值失败：请检查error信息：{e}")
            return None

    def process_data(self, data):  # noqa
        """处理函数表达式"""
        for i in range(data.count('${')):
            if '${' in data and '}' in data:
                start_index = data.index('${')
                end_index = data.index('}')
                # 获取函数中的方法
                func_full_name = data[start_index:end_index + 1]
                # 获取函数名
                func_name = data[start_index + 2:data.index('(')]
                # 获取函数参数
                func_params = data[data.index('(') + 1:data.index(')')]
                # 调用函数提取数据
                extract_data = getattr(self, func_name)(*func_params.split(',') if func_params else "")
                # 替换函数表达式为提取数据
                data = data.replace(func_full_name, str(extract_data))
        return data

    def extract_url(self, url):
        if '${' in url and '}' in url:
            return self.process_data(url)

        return url

    def extract_case_info(self, case_info):
        # 转换成str类型
        str_case_info = json.dumps(case_info)
        data = self.process_data(str_case_info)
        # 换会json类型
        return json.loads(data)

    def extract_headers(self, headers):
        # 转换成str类型
        str_headers = json.dumps(headers)
        data = self.process_data(str_headers)
        # 换会json类型
        return json.loads(data)


if __name__ == '__main__':
    print(ExtractUtils().process_data('${increment_extract_value(plan_asset)}'))


