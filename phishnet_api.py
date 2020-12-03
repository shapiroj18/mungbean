import os
import requests
import json

auth_key = os.getenv('API_KEY')


def get_phishnet_data(endpoint:str, payload:dict) -> str:
    phishnet_endpoint = f'https://api.phish.net/v3/{endpoint}'

    response = requests.get(
        url=phishnet_endpoint,
        params=payload
    )

    parsed = json.loads(response.text)
    json_obj = json.dumps(parsed, indent=4)
    print(json_obj)
    
    return json_obj

def post_phishnet_data(endpoint:str, payload:dict) -> str:
    phishnet_endpoint = f'https://api.phish.net/v3/{endpoint}'

    # obtaining an authkey - https://phishnet.api-docs.io/v3/the-phish-net-api/obtaining-an-authkey

    response = requests.post(
        url=phishnet_endpoint,
        data=payload
    )

    parsed = json.loads(response.text)
    json_obj = json.dumps(parsed, indent=4)
    print(json_obj)
    
    return json_obj


def main() -> None:
    # get_phishnet_data('setlists/get',
    #                   payload = {
    #                     'apikey': auth_key,
    #                     'showdate': '1997-12-29'
    #                     }
    #                   )
    
    post_phishnet_data('jamcharts/get',
                       payload = {
                        'apikey': auth_key,
                        'songid': 2501
                        }
                       )
    
    pass
 
if __name__ == "__main__":
    main() 