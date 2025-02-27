import os

import allure
import pytest

from core.rest_client_new import RestClient
from utils.AssertUtils import AssertUtils
from utils.ExtractUtils import ExtractUtils
from utils.YamlUtils import YamlUtil


class ApiService:
    def __init__(self):
        self.session = RestClient()
        self.extract = ExtractUtils()
        self.file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "file/")

    def handle_case(self, test_date, login_token=None):
        # 获取URL
        url = self.extract.extract_url(test_date['request_info']['url'])
        # 获取请请求方法
        method = test_date['request_info']['method']
        # 获取请求头
        headers = test_date['request_info']['headers']
        if login_token:
            headers.update(login_token)
        else:
            headers = self.extract.extract_headers(test_date['request_info']['headers'])
        # # 获取casetitle
        # case_title = test_date['request_info']['case_title']
        # # 记录case_title，listener.py中加了代码清除报告中的parameters
        # allure.dynamic.title(case_title)
        # 获取case_info
        case_info = test_date['case_info']
        # 获取variables
        validate = case_info.pop('validate', None)
        # 获取extract
        extract = case_info.pop('extract', None)

        # 获取case_title，只有当存在时才记录报告
        case_title = case_info.pop('case_title', None)
        if case_title:
            allure.dynamic.title(case_title)

        # 从extract中提取变量，更新case_info
        case_info = self.extract.extract_case_info(case_info)
        # 获取文件上传
        file, files = case_info.pop('files', None), None
        if file is not None:
            for fk, fv in file.items():
                files = {fk: (fv, open(self.file_path + fv, mode='rb'), 'image/jpeg')}
        # 发送请求
        result = self.session.do_request(url=url, method=method, headers=headers, files=files, **case_info)
        # 将extract写入yaml文件
        self.extract.extract_data(result, extract)
        # 验证结果
        AssertUtils().validate_response(result, validate)
        return result
        # 获取request_body
