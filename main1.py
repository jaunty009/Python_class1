# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/won")
# def read_root():
#     return {"message": "Hello World"}

# @app.post("/items/")
# async def create_item(first_name, last_name, idLeague):
    
#  url = "https://www.thesportsdb.com/api/v1/json/123/searchteams.php"
#     params = {"t": "Arsenal"}
#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         result = response.json()
#         # user_input = input("Enter league name to get its ID: ")
#         team = result['teams'][0]
#         if user_input.lower() in team['strLeague2'].lower():
#             print(team['idLeague2'])
#         else:
#             print("League not found.")
#     ph = {"name": first_name + last_name, "League":}
#     return ph



from fastapi import FastAPI, Form
import requests

app = FastAPI()

@app.get("/won")
def read_root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(first_name, last_name, league_name):
    url = "https://www.thesportsdb.com/api/v1/json/123/searchteams.php"
    params = {"t": "Arsenal"}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        result = response.json()
        team = result['teams'][0]

        if league_name.lower() in team.get('strLeague2', '').lower():
            league_id = team.get('idLeague2', '')
            print(team['idLeague2'])
        else:
            print("League not found")
    else:
        print("API call failed")

    ph = {"name": first_name + last_name, "League": league_id}
    return ph
