"""Provides RuneliteWrapper

RuneliteWrapper fetches data from the Runelite API routes. In particular, it takes data from 
the /latest, /mapping, /5m, /1h, and /timeseries routes. The requests module is used to
access the API routes. The response returns JSON which contains market information 
such as price and volume of items.
"""

import requests

# Runelite API endpoints
endpoints = {
    'latest':'https://prices.runescape.wiki/api/v1/osrs/latest',
    'mapping':'https://prices.runescape.wiki/api/v1/osrs/mapping',
    '5m':'https://prices.runescape.wiki/api/v1/osrs/5m',
    '1h':'https://prices.runescape.wiki/api/v1/osrs/1h',
    'timeseries':'https://prices.runescape.wiki/api/v1/osrs/timeseries?timestep={timestep}&id={id}',
}

# HTTP headers
headers = {
    'User-Agent': 'Descriptive User Agent',
    'From': 'email@gmail.com'
}

def get_latest_data():
    """
    Returns JSON from /latest route.
    """
    return requests.get(endpoints['latest'], headers=headers).json() 

def get_mapping_data():
    """
    Returns JSON from /mapping route.
    """    
    return requests.get(endpoints['mapping'], headers=headers).json()

def get_five_min_data():
    """
    Returns JSON from /5m route.
    """        
    return requests.get(endpoints['5m'], headers=headers).json()

def get_one_hour_data():
    """
    Returns JSON from /1h route.
    """
    return requests.get(endpoints['1h'], headers=headers).json()

def timeseries_data(timestep, id):
    """
    Returns JSON from /timeseries route

    :param timestep: Timestep of the time-series. Valid options are "5m", "1h" and "6h".
    :param id: Item id to return a time-series for.
    """
    return requests.get(endpoints['timeseries'].format(timestep=timestep, id=id), headers=headers).json()
