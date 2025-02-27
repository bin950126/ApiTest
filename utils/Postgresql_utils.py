import psycopg2
from psycopg2.extras import DictCursor

from utils.log_utils import logger

DB_CONFIG = {
    'host': 'pg-rental-stg.cmexs9p0ooav.ap-southeast-1.rds.amazonaws.com',
    'port': '5432',
    'dbname': 'rental',
    'user': 'rental_qa',
    'password': 'MSZXp82cfwuVB/OygS7/S9ymxK4sbZevatN4gklJ3i9M3F+s'
}


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(**DB_CONFIG)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor(cursor_factory=DictCursor)

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    # 查询单个结果
    def select_query(self, sql, params=None):
        logger.info(f"执行sql: {sql}")
        self.cursor.execute(sql, params)
        result = self.cursor.fetchone()
        logger.info(f"sql执行结果：{result}")
        return result

    # 查询多个结果
    def select_query_all(self, sql, params=None):
        logger.info(f"执行sql: {sql}")
        self.cursor.execute(sql, params)
        result = [dict(row) for row in self.cursor.fetchall()]  # 转换为字典
        logger.info(f"sql执行结果：{result}")
        return result

    def execute_query(self, sql, params=None):
        try:
            logger.info(f"执行sql: {sql}")
            self.cursor.execute(sql, params)
            self.connection.commit()
        except Exception as e:
            logger.error(f"执行sql出错: {e}")
            self.connection.rollback()


DB = Database()

if __name__ == '__main__':
    db = Database()
    result = db.select_query(
        "SELECT count(*) as order_num  FROM renting_order WHERE partner_id = 190 and status = 'closed'")
    print(result[0])
