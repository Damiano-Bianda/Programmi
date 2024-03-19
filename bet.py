import http.client
import json
import os

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "8134d65abc9274eb04fa005356d3da82"
    }

'''conn.request("GET", "/countries", headers=headers)
{
      "name": "Italy",
      "code": "IT",
      "flag": "https://media.api-sports.io/flags/it.svg"
'''

'''"league": {
        "id": 135,
        "name": "Serie A",
        "type": "League",
        "logo": "https://media.api-sports.io/football/leagues/135.png"
      },
      "country": {
        "name": "Italy",
        "code": "IT",
        "flag": "https://media.api-sports.io/flags/it.svg"
      },
      "seasons": [
        {
          "year": 2010,
          "start": "2010-08-28",
          "end": "2011-05-22",
          "current": false,
          "coverage": {                         copertura
            "fixtures": {                       partite
              "events": true,                   eventi
              "lineups": true,                  formazioni
              "statistics_fixtures": false,     statistiche_partite
              "statistics_players": false       statistiche_giocatori
            },
            "standings": true,                  classifiche
            "players": true,                    giocatori
            "top_scorers": true,                
            "top_assists": true,
            "top_cards": true,
            "injuries": false,                  infortuni
            "predictions": true,                previsioni
            "odds": false                       quote
          }
        },
2010-2023 
2010 = 2010-11
conn.request("GET", "/leagues?code=IT", headers=headers)'''

'''
{
  "get": "fixtures/rounds",
  "parameters": {
    "season": "2010",
    "league": "135"
  },
  "errors": [],
  "results": 38,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    "Regular Season - 1",
    "Regular Season - 2",
    "Regular Season - 3",
    "Regular Season - 4",
    "Regular Season - 5",
    "Regular Season - 6",
    "Regular Season - 7",
    "Regular Season - 8",
    "Regular Season - 9",
    "Regular Season - 10",
    "Regular Season - 11",
    "Regular Season - 12",
    "Regular Season - 13",
    "Regular Season - 14",
    "Regular Season - 15",
    "Regular Season - 16",
    "Regular Season - 17",
    "Regular Season - 18",
    "Regular Season - 19",
    "Regular Season - 20",
    "Regular Season - 21",
    "Regular Season - 22",
    "Regular Season - 23",
    "Regular Season - 24",
    "Regular Season - 25",
    "Regular Season - 26",
    "Regular Season - 27",
    "Regular Season - 28",
    "Regular Season - 29",
    "Regular Season - 30",
    "Regular Season - 31",
    "Regular Season - 32",
    "Regular Season - 33",
    "Regular Season - 34",
    "Regular Season - 35",
    "Regular Season - 36",
    "Regular Season - 37",
    "Regular Season - 38"
  ]
}
conn.request("GET", "/fixtures/rounds?season=2010&league=135&current=false", headers=headers)'''

'''conn.request("GET", "/fixtures?league=135&season=2010", headers=headers)

res = conn.getresponse()
data = res.read()
str = data.decode("utf-8")
print(str)

json.loads(str)'''

def save_season(id, anno):
    nome_file = f"{id}_{anno}.txt"
    # Controlla se il file esiste già
    if os.path.isfile(nome_file):
        print(f"Il file '{nome_file}' esiste già.")
    else:
      conn = http.client.HTTPSConnection("v3.football.api-sports.io")
      headers = {
          'x-rapidapi-host': "v3.football.api-sports.io",
          'x-rapidapi-key': "8134d65abc9274eb04fa005356d3da82"
      }
      conn.request("GET", f"/fixtures?league={id}&season={anno}", headers=headers)
      res = conn.getresponse()
      data = res.read()
      str = data.decode("utf-8")
      with open(nome_file, 'w') as f:
          f.write(str)
      print(f"File '{nome_file}' creato con successo.")
for i in range(2010,2023):
  save_season(135, i)