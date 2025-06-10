import requests

# The API endpoint (no body needed, just query params)
url = "https://www.thesportsdb.com/api/v1/json/123/searchteams.php"
params = {"t": "Arsenal"}  # Query parameter

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)  # Prints team data for Arsenal
else:
    print(f"Error: {response.status_code}")