import pytest

from core.ApiService import ApiService
from core.rest_client_new import RestClient
from utils.Postgresql_utils import DB
from utils.YamlUtils import YamlUtil
from utils.log_utils import logger
from utils.read import base_data


@pytest.fixture(scope="function", autouse=True)
def func():
    logger.info("开始执行测试")
    yield
    logger.info("测试结束")


# 获取推荐码sql
def get_referral_code(phone_no):
    sql = f"SELECT referral_code FROM customer_customer WHERE phone_no = '{phone_no}'"
    result = DB.select_query(sql)
    return result[0] if result else None


# 删除用户sql
def delete_user(phone_no):
    sql = f"delete FROM customer_customer WHERE phone_no = '{phone_no}'"
    result = DB.execute_query(sql)
    logger.info(f"sql执行结果：{result}")
    return result[0] if result else None


# 封号sql
def update_user(phone_no):
    sql = f"update customer_customer set is_archived = true WHERE phone_no = '{phone_no}'"
    result = DB.execute_query(sql)
    logger.info(f"sql执行结果：{result}")
    return result[0] if result else None


# 获取订单数量sql
@pytest.fixture
def order_num():
    sql = f"SELECT count(*) as order_num  FROM renting_order WHERE partner_id = 190 and status = 'closed'"
    result = DB.select_query(sql)
    return result[0] if result else None


@pytest.mark.parametrize("data", YamlUtil().extract_case('user_center.yaml', 'get_Verification_code'))
@pytest.fixture
def login_token(data):
    # 登录
    login_data = {
        "username": "+12025010704",
        "password": "010704"
    }
    headers = data['request_info']['headers']
    client = RestClient()
    result = client.do_request(url="/customer/auth/login", method='POST', headers=headers, json=login_data)
    token = result['data']['token']
    headers = {"Authorization": f"Bearer {token}"}
    yield headers
