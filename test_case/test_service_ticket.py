import allure
import pytest
from core.ApiService import ApiService
from utils.YamlUtils import YamlUtil


@allure.feature("B2C Service Ticket")
class TestParther:
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_service_ticket.yaml', 'create_service_ticket'))
    def test_create_service_ticket(self, data):
        ApiService().handle_case(data)