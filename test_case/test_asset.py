import allure
import pytest
from core.ApiService import ApiService
from utils.YamlUtils import YamlUtil


@allure.feature("asset")
class TestParther:
    @pytest.mark.parametrize("data", YamlUtil().extract_case('asset.yaml', 'create_asset_category_a'))
    def test_create_asset_category_a(self, data):
        ApiService().handle_case(data)

    @pytest.mark.parametrize("data", YamlUtil().extract_case('asset.yaml', 'create_asset_category_b'))
    def test_create_asset_category_b(self, data):
        ApiService().handle_case(data)
