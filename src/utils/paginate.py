#!user/bin/env python3
import requests

from cfg.rapi import rapi_url
from  src.utils import cache_checker

def params(headers:str, rapi_ep:str, game_ids=None, date1=None, page=1):

    full_json = []
    querystring = {"page":page,
                    "per_page":"25",
                    "dates[]":date1,
                    "game_ids[]":game_ids}

    def page_pagi(page, headers, rapi_ep):
        
        querystring["page"]=page

        print(querystring["page"])

        url = rapi_url + rapi_ep

        response = requests.get(url, headers=headers, params=querystring, timeout=5)

        print(response.url)

        # cache_checker.check(response)

        json_data = response.json()

        full_json.extend(json_data['data'])

        next_pg = json_data['meta']['next_page']

        if next_pg is None:
            return
        
        return page_pagi(page=next_pg, headers=headers, rapi_ep=rapi_ep)
    
    page_pagi(page=page, headers=headers, rapi_ep=rapi_ep)

    print(len(full_json))

    return full_json