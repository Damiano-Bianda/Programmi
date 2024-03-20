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

for match_day_index in range(10, season.match_days_count):

    ranking_pre_match_day = season.get_ranking(match_day_index - 1)
    first_ranks = []
    max_points = ranking_pre_match_day[0]['points']
    for rank in ranking_pre_match_day:
        if rank['points'] == max_points:
            first_ranks.append(rank)
        else:
            break
        
    match_day = season.get_match_day(match_day_index)
    for rank in first_ranks:
        team_id = rank['team_id']
        
        try:
            if not match_day.is_match_finished(team_id):
                continue
        except Exception as e:
            print(e)
            continue
        
        try:
            match_result = match_day.get_match_result(rank['team_id'])
        except Exception as e:
            print(e)
            continue
        
        if team_id not in result:
            result[team_id] ={'win': 0, 'draw':0, 'lost':0, 'total': 0}

        if match_result.has_won(team_id):
            result[team_id]['win'] = result[team_id]['win'] + 1
        elif match_result.has_drawn(team_id):
            result[team_id]['draw'] = result[team_id]['draw'] + 1
        elif match_result.has_lost(team_id):
            result[team_id]['lost'] = result[team_id]['lost'] + 1
        
        result[team_id]['total'] = result[team_id]['total'] + 1

#print(result)
print(json.dumps(result, indent=4))