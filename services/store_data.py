import pandas as pd
from services.sensor_data import SensorData
import os
from utitlities.constant_fields import fetch_constant


def store_in_csv(json_date):
    sensor = SensorData()
    sensor = sensor.to_obj(json_date)
    file_name = "input.csv"
    resp = os.path.isfile(file_name)
    if resp:
        wearable_dataframe = pd.read_csv(file_name)
    else:
        wearable_dataframe = pd.DataFrame(
            columns=['user_id', 'timestamp', 'heart_rate', 'respiration_rate', 'activity'])
    wearable_dataframe.loc[len(wearable_dataframe)] = [sensor.get_user_id(), sensor.get_timestamp(),
                                                       sensor.get_heart_rate(), sensor.get_respiration_rate(),
                                                       sensor.get_activity()]
    wearable_dataframe.to_csv(file_name, index=False)
    return True
