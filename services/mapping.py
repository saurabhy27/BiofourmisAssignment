import pandas as pd


def multi_index_map(df):
    df_resp = pd.DataFrame(
        columns=['user_id', 'seg_start', 'seg_end', 'avg_hr', 'min_hr', 'max_hr', 'avg_rr', 'min_rr', 'max_rr',
                 'avg_activity', 'min_activity', 'max_activity'])

    df_resp['user_id'] = df['user_id']['Unnamed: 11_level_1']
    df_resp['seg_start'] = df['seg_start']['Unnamed: 9_level_1']
    df_resp['seg_end'] = df['seg_end']['Unnamed: 10_level_1']

    df_resp['avg_hr'] = df['heart_rate']['mean']
    df_resp['min_hr'] = df['heart_rate']['min']
    df_resp['max_hr'] = df['heart_rate']['max']

    df_resp['avg_rr'] = df['respiration_rate']['mean']
    df_resp['min_rr'] = df['respiration_rate']['min']
    df_resp['max_rr'] = df['respiration_rate']['max']

    df_resp['avg_activity'] = df['activity']['mean']
    df_resp['min_activity'] = df['activity']['min']
    df_resp['max_activity'] = df['activity']['max']
    return df_resp
