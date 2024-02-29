import requests
import json
base = "https://rickandmortyapi.com/api/"
endpoint = "character"
url = base + endpoint
response = requests.get(url)

if response.ok:
    
    print(response.text)

else:
    print(response.status_code)

