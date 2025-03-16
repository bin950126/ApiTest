import allure
import pytest
from core.ApiService import ApiService
from utils.YamlUtils import YamlUtil


@allure.feature("B2C订单")
class TestCustomer:
    # 获取车辆租赁信息
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'asset_rentalinfo'))
    def test_asset_rentalinfo(self, data):
        ApiService().handle_case(data)

    # 支付押金
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'pay_deposit'))
    def test_pay_deposit(self, data):
        ApiService().handle_case(data)

    # 创建订单
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'rental_asset'))
    def test_rental_asset(self, data):
        ApiService().handle_case(data)

    # 查看进行中的订单
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'ongoing_orders'))
    def test_ongoing_orders(self, data):
        ApiService().handle_case(data)

    # 第一笔订单提交还车申请
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'submit_return_confirm1'))
    def test_submit_return_confirm1(self, data):
        ApiService().handle_case(data)

    # 确认还车
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'confirm_return'))
    def test_confirm_return(self, data):
        ApiService().handle_case(data)

    # 第二笔订单提交还车申请
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'submit_return_confirm2'))
    def test_submit_return_confirm2(self, data):
        ApiService().handle_case(data)

    # 第二笔订单取消还车申请
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'cancel_return'))
    def test_cancel_return(self, data):
        ApiService().handle_case(data)

    # 还车关闭订单
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'submit_return'))
    def test_submit_return(self, data):
        ApiService().handle_case(data)

    # 更换订单中的车辆
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'replace_asset'))
    def test_replace_asset(self, data):
        ApiService().handle_case(data)

    # 查看订单车辆更换记录
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'usage_records'))
    def test_usage_records(self, data):
        ApiService().handle_case(data)

    # 强制关闭第二笔订单
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'force_close_order'))
    def test_force_close_order(self, data):
        ApiService().handle_case(data)

    # 查看已关闭订单
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'get_closed_orders'))
    def test_get_closed_orders(self, data):
        ApiService().handle_case(data)

    # 退还租金
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'refund_rent'))
    def test_refund_rent(self, data):
        ApiService().handle_case(data)

    # 退还押金
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'refund_deposit'))
    def test_refund_deposit(self, data):
        ApiService().handle_case(data)

    # 申请退还押金
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'apply_deposit_refund'))
    def test_apply_deposit_refund(self, data):
        ApiService().handle_case(data)

    # 获取退还押金申请id
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'deposit_application_id'))
    def test_deposit_application_id(self, data):
        ApiService().handle_case(data)

    #
    # # 通过退还押金申请
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'approve_deposit_refund'))
    def test_approve_deposit_refund(self, data):
        ApiService().handle_case(data)

    # 查看订单交易记录
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'transactions_orders'))
    def test_transactions_orders(self, data):
        ApiService().handle_case(data)

    # 查看押金交易记录
    @pytest.mark.parametrize("data", YamlUtil().extract_case('B2C_order.yaml', 'transactions_deposits'))
    def test_transactions_deposits(self, data):
        ApiService().handle_case(data)
