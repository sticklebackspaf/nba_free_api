#!user/bin/env python3
from cfg.rapi import rapi_key, rapi_host, rapi_url, rapi_stats, headers
from src.utils import dates_filler, paginate, data_summaries

url = rapi_url + rapi_stats

def stats_getter(st_date, en_date):
    '''
    Retrieves stats summary for the date period entered
    Args:
        st_date:.....

    Returns
        agg_df (:obj: pd.df): dataframe of team summary with home and visitor view
    '''
    # for two dates fill in all of the range in between
    dt_list = dates_filler.fill(st_date, en_date)

    # paginate pages 
    full_json = paginate.params(date1=dt_list, headers=headers, rapi_ep=rapi_stats)

    # aggregate the response data
    agg_df = data_summaries.summary(full_json)

    return agg_df
