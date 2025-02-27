import allure
import pytest
from core.ApiService import ApiService
from utils.YamlUtils import YamlUtil


@allure.feature("category")
class TestParther:
    # 创建已存在的category回报409，暂时不测试
    @pytest.mark.parametrize("data", YamlUtil().extract_case('category.yaml', 'create_category'))
    def test_create_category(self, data):
        ApiService().handle_case(data)

    @pytest.mark.parametrize("data", YamlUtil().extract_case('category.yaml', 'update_category'))
    def test_update_category(self, data):
        ApiService().handle_case(data)
