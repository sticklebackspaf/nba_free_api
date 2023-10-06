#!user/bin/env python3
import datetime as dt

def fill(st_date, en_date):

    st = dt.datetime.strptime(st_date, '%Y-%m-%d')
    en = dt.datetime.strptime(en_date, '%Y-%m-%d')

    dt_list = [dt.datetime.strftime(st+dt.timedelta(days=x), '%Y-%m-%d') for x in range((en-st).days+1)]

    if len(dt_list)==0:
        return st_date

    return dt_list