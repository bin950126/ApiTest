import allure
import pytest
from core.ApiService import ApiService
from utils.YamlUtils import YamlUtil


@allure.feature("marketing")
class TestParther:
    @pytest.mark.parametrize("data", YamlUtil().extract_case('marketing.yaml', 'create_pricin_paid'))
    def test_create_pricin_paid(self, data):
        ApiService().handle_case(data)

    @pytest.mark.parametrize("data", YamlUtil().extract_case('marketing.yaml', 'create_pricin_free'))
    def test_create_pricin_free(self, data):
        ApiService().handle_case(data)

    @pytest.mark.parametrize("data", YamlUtil().extract_case('marketing.yaml', 'create_discount'))
    def test_create_discount(self, data):
        ApiService().handle_case(data)

    @pytest.mark.parametrize("data", YamlUtil().extract_case('marketing.yaml', 'create_deposits_category_a'))
    def test_create_deposits_paid(self, data):
        ApiService().handle_case(data)

    @pytest.mark.parametrize("data", YamlUtil().extract_case('marketing.yaml', 'create_deposits_category_b'))
    def test_create_deposits_category_b(self, data):
        ApiService().handle_case(data)
