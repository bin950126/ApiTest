import allure
import pytest
from core.ApiService import ApiService
from utils.YamlUtils import YamlUtil


@allure.feature("site")
class TestParther:
    # 创建站点
    @pytest.mark.parametrize("data", YamlUtil().extract_case('site.yaml', 'create_site'))
    def test_create_site(self, data):
        ApiService().handle_case(data)

    # 更新站点信息
    @pytest.mark.parametrize("data", YamlUtil().extract_case('site.yaml', 'update_site'))
    def test_update_site(self, data):
        ApiService().handle_case(data)

    # 上传站点图片
    @pytest.mark.parametrize("data", YamlUtil().extract_case('site.yaml', 'upload_site_image'))
    def test_upload_site_image(self, data):
        ApiService().handle_case(data)

    # 删除站点图片
    @pytest.mark.parametrize("data", YamlUtil().extract_case('site.yaml', 'delete_site_image'))
    def test_delete_site_image(self, data):
        ApiService().handle_case(data)

    # 删除站点
    @pytest.mark.parametrize("data", YamlUtil().extract_case('site.yaml', 'delete_site'))
    def test_delete_site(self, data):
        ApiService().handle_case(data)