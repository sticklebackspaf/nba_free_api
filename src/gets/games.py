#!user/bin/env python3
import requests

from cfg.rapi import rapi_url, rapi_game, rapi_stats, headers
from  src.utils import cache_checker, paginate, data_filter, data_summaries

def id_getter(value):
    '''
    Retrieves the game id data being requested
    Args:
        value (int): game id
    Returns
        json_filt(:obj: json): json containing data for the given game id
    '''
    ##### handling match level
    # create url with id appended
    url = rapi_url + rapi_game + value

    # get match level data from url with headers
    response = requests.get(url, headers=headers, timeout=5)

    # print if cache is used or not
    cache_checker.check(response)

    # convert response obj to json
    json_data = response.json()

    # filtering to require keys
    json_filt = data_filter.field_filter(json_data)

    # getting the player data for the game id
    json_filt = player_getter(json_filt, value)

    return json_filt

def date_getter(date1):
    '''
    Retrieves the game(s) data for the date being requested
    Args:
        date1 (str): date for of game(s)
    Returns
        data_with_players(:obj: :list:): contains all game and player pts data for date
    '''
    # paginating dates although those seen only have 1 page
    full_json = paginate.params(date1=date1, headers=headers, rapi_ep=rapi_game)
    
    # filtering to require keys
    data = data_filter.field_filter(full_json)

    # looping over each match and retreiving the player data
    data_with_players = []

    # data is a list of dicts at this point
    for d in data:

        # will try to add the player data but in the event this fails
        # return the original dict
        try:
            data_with_players.extend(player_getter([d], d['id']))
        except Exception as e:
            data_with_players.extend(d)
            
    return data_with_players

def player_getter(json_filt,value):

    ##### getting sum of player points
    player_data = paginate.params(headers=headers,rapi_ep=rapi_stats,game_ids=value)

    # get player points sum total (not sure on the requirement, doing both)
    json_filt[0]['player_points_tot'] = sum([x['pts'] for x in player_data if isinstance(x['pts'],int)])

    # getting sum by player (api should be at player level so sum is value)
    json_filt[0]['player_points'] = data_summaries.player_summary(player_data)

    return json_filt