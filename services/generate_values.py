import random
import calendar
import time
from sensor_data import SensorData
from utitlities.constant_fields import fetch_constant
import requests
import asyncio


def generate_random_values(user_id):
    heart_rate = random.randint(40, 100)
    resp_rate = random.randint(10, 40)
    activity = random.randint(0, 10)
    gmt = time.gmtime()
    timestamp = calendar.timegm(gmt)
    sensor_data = SensorData(user_id, timestamp, heart_rate, resp_rate, activity)
    return sensor_data


def generate_every_second(user_id):
    i = 0
    while True and i < 3600:
        json_data = generate_random_values(user_id).to_json()
        asyncio.run(api_call_to_store_data(json_data))
        time.sleep(1)
        i += 1


async def api_call_to_store_data(json_data):
    requests.post(fetch_constant(constant_name="BASE_URL") + '/vitals_input', json=json_data)


if __name__ == '__main__':
    generate_every_second("abcd")
