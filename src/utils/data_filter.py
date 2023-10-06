#!user/bin/env python3
import pandas as pd

from cfg.games import game_kp_flds

def field_filter(json_data):

    try:

        df_json = pd.json_normalize(json_data)

        df = df_json[game_kp_flds]

        data = df.to_dict(orient='records')

    except Exception as e:
        if json_data == []:
            return json_data
        else:
            raise e

    return data