import os
import requests
import json

api_key = os.getenv('PHISHIN_API')

def get_phishin_data(endpoint:str) -> str:
    phishnet_endpoint = f'http://phish.in/api/v1/{endpoint}.json'
    
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    
    payload = {
        
    }

    response = requests.get(
        url=phishnet_endpoint,
        headers=headers,
        params=payload
    )

    parsed = json.loads(response.text)
    json_obj = json.dumps(parsed, indent=4)
    print(json_obj)
    
    return json_obj

print(get_phishin_data('songs'))