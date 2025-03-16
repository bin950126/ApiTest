import allure
import pytest
from core.ApiService import ApiService
from utils.YamlUtils import YamlUtil


@allure.feature("parther")
class TestParther:
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'user_login'))
    def test_user_login(self, data):
        ApiService().handle_case(data)

    # Parther已存在会报409，暂时不测试
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'create_parther'))
    def test_create_parther(self, data):
        ApiService().handle_case(data)

    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'update_parther'))
    def test_update_parther(self, data):
        ApiService().handle_case(data)

    # collect_returnrules配置已存在会报409，暂时不测试
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'collect_returnrules'))
    def test_collect_returnrules(self, data):
        ApiService().handle_case(data)

    # 更新collect_returnrules
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'update_collect_returnrules'))
    def test_updeate_collect_returnrules(self, data):
        ApiService().handle_case(data)

    # partner_operations配置已存在会报409，暂时不测试
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'partner_operations'))
    def test_partner_operations(self, data):
        ApiService().handle_case(data)

    # 更新partner_operations
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'updeate_partner_operations'))
    def test_updeate_partner_operations(self, data):
        ApiService().handle_case(data)

    # 新增terms_conditions
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'add_terms_conditions'))
    def test_add_terms_conditions(self, data):
        ApiService().handle_case(data)

    # 更新terms_conditions
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'update_terms_conditions'))
    def test_update_terms_conditions(self, data):
        ApiService().handle_case(data)

    # 删除terms_conditions
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'delete_terms_conditions'))
    def test_delete_terms_conditions(self, data):
        ApiService().handle_case(data)

    # 新增privacy_policy
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'add_privacy_policy'))
    def test_add_privacy_policy(self, data):
        ApiService().handle_case(data)

    # 更新privacy_policy
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'update_privacy_policy'))
    def test_update_privacy_policy(self, data):
        ApiService().handle_case(data)

    # 删除privacy_policy
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'delete_privacy_policy'))
    def test_delete_privacy_policy(self, data):
        ApiService().handle_case(data)

    # 新增help_center
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'add_help_center'))
    def test_add_help_center(self, data):
        ApiService().handle_case(data)

    # 上传help_center_images
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'add_help_center_images'))
    def test_add_help_center_images(self, data):
        ApiService().handle_case(data)

    # 更新help_center
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'update_help_center'))
    def test_update_help_center(self, data):
        ApiService().handle_case(data)

    # 删除help_center
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'delete_help_center'))
    def test_delete_help_center(self, data):
        ApiService().handle_case(data)

    # 绑定信用卡
    @pytest.mark.parametrize("data_set", zip(
        YamlUtil().extract_case('parther.yaml', 'get_providers'),
        YamlUtil().extract_case('parther.yaml', 'get_payment_method_setup'),
        YamlUtil().extract_case('parther.yaml', 'create_PaymentMethod'),
        YamlUtil().extract_case('parther.yaml', 'bind_PaymentMethod')
    ))
    def test_bind_PaymentMethod(self, data_set):
        get_providers, get_payment_method_setup, create_PaymentMethod, bind_PaymentMethod = data_set  # 解包数据集
        ApiService().handle_case(get_providers)
        ApiService().handle_case(get_payment_method_setup)
        ApiService().handle_case(create_PaymentMethod)
        ApiService().handle_case(bind_PaymentMethod)

    # 删除信用卡
    @pytest.mark.parametrize("data", YamlUtil().extract_case('parther.yaml', 'delete_PaymentMethod'))
    def test_delete_PaymentMethod(self, data):
        ApiService().handle_case(data)