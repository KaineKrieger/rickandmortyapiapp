# importing the requests function to do the getting api part
import requests

# base is the website for the api
base = "https://rickandmortyapi.com/api/"

# there are more endpoints i could make but for now its just character, check the website docs when you come back to make an app out of this
endpoint = "character"

# THIS DOESNT mean the url by itself its making the new url from the base while adding aditional endpoints, check docs for formatting
url = base + endpoint

# calling the api for data
response = requests.get(url)

character_selection = str(input("give me a number in the range 1-826: "))

response = requests.get(url + "/" + character_selection)

# basic boolean to make sure it works.
if response.ok:
    
    print(response.text)

else:
    print(response.status_code)

