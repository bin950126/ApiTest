import allure
import pytest
from core.ApiService import ApiService
from utils.YamlUtils import YamlUtil


@allure.feature("用户中心")
class TestCustomer:
    # 删除用户
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'delete_customer'))
    def test_delete_customer(self, data):
        ApiService().handle_case(data)

    # 获取验证码
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'get_Verification_code'))
    def test_get_Verification_code(self, data):
        ApiService().handle_case(data)

    # 注册用户
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'customer_register'))
    def test_customer_register(self, data):
        ApiService().handle_case(data)

    # 设定密码
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'change_password'))
    def test_change_password(self, data):
        ApiService().handle_case(data)

    # 验证手机号是否已注册
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'verify_PhoneNo_Registered'))
    def test_verify_PhoneNo_Registered(self, data):
        ApiService().handle_case(data)

    # 账号登录
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'customer_login'))
    def test_customer_login(self, data):
        ApiService().handle_case(data)

    # 获取用户基础信息
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'get_customer_info'))
    def test_get_customer_info(self, data):
        ApiService().handle_case(data)

    # 更新用户基础信息
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'update_customer_info'))
    def test_update_customer_info(self, data):
        ApiService().handle_case(data)

    # 提交身份验证
    @pytest.mark.parametrize("data_set", zip(
        YamlUtil().extract_case('user_center.yaml', 'identity_verification'),
        YamlUtil().extract_case('user_center.yaml', 'images_front_side'),
        YamlUtil().extract_case('user_center.yaml', 'images_back_side'),
        YamlUtil().extract_case('user_center.yaml', 'images_selfie')
    ))
    def test_identity_verification(self, data_set):
        identity_verification, images_front_side, images_back_side, images_selfie = data_set  # 解包数据集
        ApiService().handle_case(identity_verification)
        ApiService().handle_case(images_front_side)
        ApiService().handle_case(images_back_side)
        ApiService().handle_case(images_selfie)

    # 绑定信用卡
    @pytest.mark.parametrize("data_set", zip(
        YamlUtil().extract_case('user_center.yaml', 'get_providers'),
        YamlUtil().extract_case('user_center.yaml', 'get_payment_method_setup'),
        YamlUtil().extract_case('user_center.yaml', 'create_PaymentMethod'),
        YamlUtil().extract_case('user_center.yaml', 'bind_PaymentMethod')
    ))
    def test_bind_PaymentMethod(self, data_set):
        get_providers, get_payment_method_setup, create_PaymentMethod, bind_PaymentMethod = data_set  # 解包数据集
        ApiService().handle_case(get_providers)
        ApiService().handle_case(get_payment_method_setup)
        ApiService().handle_case(create_PaymentMethod)
        ApiService().handle_case(bind_PaymentMethod)

    # 邮箱重复时返回错误信息
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'update_customer_email'))
    def test_update_customer_email(self, data):
        ApiService().handle_case(data)

    # 更新whatsapp_number
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'update_customer_whatsapp_number'))
    def test_update_customer_whatsapp_number(self, data):
        ApiService().handle_case(data)

    # 发送邮箱验证
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'launch_email_verification'))
    def test_launch_email_verification(self, data):
        ApiService().handle_case(data)

    # 通过验证码重置密码
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'reset_password_bycode'))
    def test_reset_password_bycode(self, data):
        ApiService().handle_case(data)

    # 通过原密码重置密码
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'reset_password_ByPassword'))
    def test_reset_password_ByPassword(self, data):
        ApiService().handle_case(data)

    # 加入Parther
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'joinPartner'))
    def test_joinPartner(self, data):
        ApiService().handle_case(data)

    # 查看已加入的Parther
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'grt_joinPartner'))
    def test_grt_joinPartner(self, data):
        ApiService().handle_case(data)

    # 退出Parther
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'leavePartner'))
    def test_leavePartner(self, data):
        ApiService().handle_case(data)

    # 关闭营销邮件
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'close_Marketing'))
    def test_close_Marketing(self, data):
        ApiService().handle_case(data)

    # 开启营销邮件
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'open_Marketing'))
    def test_open_Marketing(self, data):
        ApiService().handle_case(data)

    # 查看帮助信息
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'get_help_center'))
    def test_get_help_center(self, data):
        ApiService().handle_case(data)

    # 查看服务协议
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'get_terms_conditions'))
    def test_get_terms_conditions(self, data):
        ApiService().handle_case(data)

    # 查看隐私政策
    @pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'get_privacy_policy'))
    def test_get_privacy_policy(self, data):
        ApiService().handle_case(data)


