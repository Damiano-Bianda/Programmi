import json
from season import Season

def load_season(id, anno):
    nome_file = f"{id}_{anno}.txt"
    with open(nome_file, 'r') as f:
        data = json.load(f)
    season = Season(data['response'])
    return season

season = load_season(135, 2010)

'''Ottenere rapporto scommessa vinta su scommesse totali 
se ogni giornata scelgo vincente le prime in classifica (per numero di punti)'''

result = {}

for match_day_index in range(1, season.match_days_count):
    match_day = season.get_match_day(match_day_index - 1)
    match_day_ranking = match_day.get_ordered_match_day_ranking()
    first_ranks = []
    
    max_points = match_day_ranking[0].points
    for rank in match_day_ranking:
        if rank.points == max_points:
            first_ranks.add(rank)
        else:
            break

    for rank in first_ranks:
        team_id = rank.team_id
        match_result = match_day.get_match_result(rank.team_id)
        if team_id == match_result.get_winner_team_id():
            bet_count = result[team_id]
            if bet_count:
                result[team_id].win = bet_count.win + 1
                result[team_id].total = bet_count.total + 1
            else:
                result[team_id] = {win: 0, total: 1}