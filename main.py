# import requests

# # The API endpoint (no body needed, just query params)
# url = "https://www.thesportsdb.com/api/v1/json/123/searchteams.php"
# params = {"t": "Arsenal"}  # Query parameter

# response = requests.get(url, params=params)

# if response.status_code == 200:
#     data = response.json()
#     print(data)  # Prints team data for Arsenal
    
# else:
#     print(f"Error: {response.status_code}")



# import requests

# url = "https://www.thesportsdb.com/api/v1/json/123/searchteams.php"
# params = {"t": "Arsenal"}  # Search for Arsenal

# response = requests.get(url, params=params)  # Timeout after 10 sec
# response.raise_for_status()  # Raise an error for bad status codes (4xx/5xx)

# data = response.json()
# user_input = input("Enter league name to search for leagueID in Arsenal: ")


# if data.get('teams'):
#     print("All Leagues for Arsenal:")
#     for team in data['teams']:
#         id_league = team.get('idLeague2')
#         league_name = team.get('strLeague2', 'Unknown League')
#         print(f"League ID: {id_league} | League Name: {league_name}")
# else:
#     print("No team data found for Arsenal.")


import requests

url = "https://www.thesportsdb.com/api/v1/json/123/searchteams.php"
params = {"t": "Arsenal"}
response = requests.get(url, params=params)

if response.status_code == 200:
    result = response.json()
    user_input = input("Enter league name to get its ID: ")
    team = result['teams'][0]
    if user_input.lower() in team['strLeague2'].lower():
        print(team['idLeague2'])
    else:
        print("League not found.")