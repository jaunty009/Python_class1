# import requests

# # The API endpoint (no body needed, just query params)
# url = "https://www.thesportsdb.com/api/v1/json/123/searchteams.php"
# params = {"t": "Arsenal"}  # Query parameter

# response = requests.get(url, params=params)

# if response.status_code == 200:
#     data = response.json()
#     print(data)  # Prints team data for Arsenal
#     user_input = input(idLeague) 
# else:
#     print(f"Error: {response.status_code}")



import requests

url = "https://www.thesportsdb.com/api/v1/json/123/searchteams.php"
params = {"t": "Arsenal"}  # Search for Arsenal

response = requests.get(url, params=params)  # Timeout after 10 sec
response.raise_for_status()  # Raise an error for bad status codes (4xx/5xx)

data = response.json()

if data.get('teams'):
    print("All Leagues for Arsenal:")
    for team in data['teams']:
        id_league = team.get('idLeague3')
        league_name = team.get('strLeague3', 'Unknown League')
        print(f"League ID: {id_league} | League Name: {league_name}")
else:
    print("No team data found for Arsenal.")