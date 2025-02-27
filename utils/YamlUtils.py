import os

import yaml


class YamlUtil:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data/')

    def read_extract_yaml(self):
        with open(self.data_path + 'extract.yaml', mode='r', encoding='utf8') as f:
            value = yaml.safe_load(f)
            return value

    def read_testcase_yaml(self, yaml_name, key_name=None):
        with open(self.data_path + yaml_name, mode='r', encoding='utf8') as f:
            value = yaml.safe_load(f)
            if key_name:
                return value[key_name]
        return value

    def extract_case(self, yaml_name, key_name):
        case_value = self.read_testcase_yaml(yaml_name, key_name)[0]
        new_case = []
        for value in case_value['case_info']:
            new_case.append({'request_info': case_value['request_info'], 'case_info': value})
        return new_case

    def write_yaml(self, data): # noqa
        with open(self.data_path + 'extract.yaml', mode='a', encoding='utf8') as f:
            # 读取之前的yaml文件
            old_data = self.read_extract_yaml()
            if old_data:
                # 和新传入的数据合并
                for key, value in data.items():
                    old_data[key] = value
                # 清空文件内容
                self.clear_extract_yaml()
                # 写入更新后的数据
                yaml.dump(data=old_data, stream=f, allow_unicode=True, sort_keys=False)
            else:
                # 写入数据
                yaml.dump(data=data, stream=f, allow_unicode=True, sort_keys=False)

    def clear_extract_yaml(self):
        """清理extract.yaml文件"""
        with open(self.data_path + 'extract.yaml', mode='w', encoding='utf8') as f:
            f.truncate()


if __name__ == '__main__':
    # date = YamlUtil().extract_case('user_center.yaml', 'get_code')
    # print(date)
    data = {'name': '张三11', 'age': 20, 'data': {'name': '李四', 'age': 21}}
    print(YamlUtil().write_yaml(data))
    # print(YamlUtil().read_extract_yaml())
