import json

import requests

from utils.log_utils import logger
from utils.read import base_data


class RestClient:
    def __init__(self):
        self.base_url = base_data.read_ini()['host']['base_url']

    def do_request(self, url, method, **kwargs):
        response = self.request(url, method, **kwargs).json()
        logger.info(f"接口的返回内容:>>>\n{json.dumps(response, indent=4, ensure_ascii=False)}")
        return response

    def request(self,  url, method, **kwargs):
        full_url = url if url.startswith(("https://", "https://")) else self.base_url + url
        self.request_log(full_url, method, **kwargs)
        if method == 'POST':
            return requests.post(full_url, **kwargs)
        if method == 'GET':
            return requests.get(full_url, **kwargs)
        if method == 'PUT':
            return requests.put(full_url, **kwargs)
        if method == 'DELETE':
            return requests.delete(full_url, **kwargs)
        if method == 'PATCH':
            return requests.patch(full_url, **kwargs)

    def request_log(self, url, method, **kwargs):
        json_data = kwargs.get('json')
        params = kwargs.get('params')
        data = kwargs.get('data')
        files = kwargs.get('files')
        logger.info(f"接口请求的地址: {url}")
        logger.info(f"接口请求方式: {method}")
        if json_data is not None:
            logger.info(f"接口请求的json参数:  \n{json.dumps(json_data, indent=4, ensure_ascii=False)}")
        if params is not None:
            logger.info(f"接口请求的params参数:  \n{json.dumps(params, indent=4, ensure_ascii=False)}")
        if data is not None:
            logger.info(f"接口请求的data参数:  \n{json.dumps(data, indent=4, ensure_ascii=False)}")
        if files is not None:
            # 由于文件是二进制数据，直接 json.dumps 会报错。我们打印文件名或其他信息
            file_info = {key: f"文件: {file.name if hasattr(file, 'name') else str(file)}" for key, file in
                         files.items()}
            logger.info(f"接口请求的files参数:  \n{json.dumps(file_info, indent=4, ensure_ascii=False)}")
        logger.info(f"接口请求的请求头:\n{json.dumps(kwargs.get('headers'), indent=4, ensure_ascii=False)}")
