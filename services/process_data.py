import os
import pandas as pd
from services.convert import convert_into_timestamp
from services.mapping import multi_index_map


def processor(agg_min):
    file_name = "input.csv"
    output_file = 'output.csv'
    agg_sec = agg_min * 60
    if not os.path.exists(file_name):
        return {"resp": "input.csv File does not exists."}
    wearable_dataframe = pd.read_csv(file_name)
    if len(wearable_dataframe) == 0:
        return {"resp": "No Data Found"}
    user_name = wearable_dataframe['user_id'][0]
    wearable_dataframe.to_json("input_date.json", orient='records')

    wearable_dataframe['datetime'] = pd.to_datetime(wearable_dataframe['timestamp'], unit='s')
    wearable_dataframe_agg = wearable_dataframe[['datetime', 'heart_rate', 'respiration_rate', 'activity']].groupby(
        [wearable_dataframe['datetime'].dt.round('{}S'.format(agg_sec))]).agg(
        ['mean', 'min', 'max']).reset_index(drop=True)
    wearable_dataframe_agg['seg_start'] = wearable_dataframe_agg.loc[:, 'datetime']['min'].apply(convert_into_timestamp)
    wearable_dataframe_agg['seg_end'] = wearable_dataframe_agg.loc[:, 'datetime']['max'].apply(convert_into_timestamp)
    wearable_dataframe_agg.drop(('datetime', 'mean'), axis=1, inplace=True)
    wearable_dataframe_agg.drop(('datetime', 'min'), axis=1, inplace=True)
    wearable_dataframe_agg.drop(('datetime', 'max'), axis=1, inplace=True)
    wearable_dataframe_agg["user_id"] = user_name
    if os.path.exists(output_file):
        os.remove(output_file)
    wearable_dataframe_agg.to_csv(output_file, index=False)
    df = multi_index_map(pd.read_csv(output_file, skipinitialspace=True, header=[0, 1]))
    return df.to_dict(orient="records")
