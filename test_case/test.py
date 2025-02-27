import requests
import time
import os

LOG_FILE = "geolocation_log.txt"
LAST_TIMESTAMP_FILE = "last_timestamp.txt"

ASSETS = ["MOVIEBIKE050", "A7"]  # 需要查询的资产编号


def get_latest_geolocation(asset_no):
    """获取指定资产的 geolocation 数据"""
    url = f"https://api-rental-stg.moovmobility.co/asset/assets/{asset_no}"
    headers = {"Authorization": "Bearer AF39F06E18174DFBA13373ACF4587AF6"}
    result = requests.get(url, headers=headers)

    if result.status_code == 200:
        response_data = result.json()
        geolocation = response_data.get("data", {}).get("geolocation", {}).get("current", {})
        return geolocation.get("timestamp"), geolocation.get("businessType")
    else:
        print(f"请求失败 ({asset_no}):", result.status_code, result.text)
        return None, None


def get_last_recorded_timestamp(asset_no):
    """从文件读取上次记录的 timestamp"""
    file_path = f"{LAST_TIMESTAMP_FILE}_{asset_no}.txt"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read().strip()
    return None


def save_last_recorded_timestamp(asset_no, timestamp):
    """将新的 timestamp 记录到文件"""
    file_path = f"{LAST_TIMESTAMP_FILE}_{asset_no}.txt"
    with open(file_path, "w") as file:
        file.write(timestamp)


def log_geolocation(asset_no):
    """检查并记录 geolocation 数据"""
    timestamp, business_type = get_latest_geolocation(asset_no)

    if timestamp and business_type:
        last_timestamp = get_last_recorded_timestamp(asset_no)

        # 只有当 timestamp 发生变化时才记录
        if timestamp != last_timestamp:
            log_entry = f"Timestamp: {timestamp}, BusinessType: {business_type}, Asset: {asset_no}\n"

            with open(LOG_FILE, "a") as log_file:
                log_file.write(log_entry)

            # 更新最后记录的 timestamp
            save_last_recorded_timestamp(asset_no, timestamp)

            print("新数据记录成功:", log_entry.strip())
        else:
            print(f"{asset_no}: Timestamp 未变化，跳过记录")
    else:
        print(f"{asset_no}: 数据不完整，未记录")


# 每 1 分钟运行一次
while True:
    for asset in ASSETS:
        log_geolocation(asset)
    time.sleep(300)
