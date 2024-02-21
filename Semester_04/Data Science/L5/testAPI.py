import requests
import pandas as pd
#conda install requests
#conda install flask
# Send GET request to API endpoint
#replace with any available public data
#can get public API from https://github.com/public-apis/public-apis
response = requests.get('https://api.jikan.moe/v4/anime/1/full')
# Parse JSON response
data = response.json()

print(data)
df = pd.json_normalize(data)
print(df)
print(df.columns)

try:
    # Send GET request to API endpoint
    ##https://api.jikan.moe/v4/anime/{id}/full
    response = requests.get('https://meowfacts.herokuapp.com/')
    response.raise_for_status()  # Raise an exception for HTTP errors
    data2 = response.json()  # Parse JSON response
except requests.exceptions.RequestException as e:
    print('Error:', e)
    data2 = None


