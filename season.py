from match_day import MatchDay

class Season:
    def __init__(self, data):
        self.data = data
        self.match_days_count = round_values = len({item["league"]["round"] for item in data})

    def get_match_day(self, match_day_index):
        match_day = [item for item in self.data if item["league"]["round"].endswith(f" {match_day_index}")]
        return MatchDay(match_day)
    
    # return the ranking at the end of the match day (starting from 0)
    def get_ranking(self, match_day_index):
        '''
        TODO
        gestione gol per classifica
        '''
        ranking = {}
        for match in self.data:
            ranking[match['teams']['home']['id']] = 0
            ranking[match['teams']['away']['id']] = 0

        for match_day_idx in range(0, match_day_index):
            match_day = self.get_match_day(match_day_idx).data
            for match in match_day:
                if match['fixture']['status']['short'] != 'FT':
                    continue
                home = match['goals']['home']
                away = match['goals']['away']
                if home > away:
                    home = 3
                    away = 0
                elif home == away:
                    home = 1
                    away = 1
                else:
                    home = 0
                    away = 3
                ranking[match['teams']['home']['id']] = ranking[match['teams']['home']['id']] + home
                ranking[match['teams']['away']['id']] = ranking[match['teams']['away']['id']] + away
                
        
        tuple_list = [(team_id, punti) for team_id, punti in ranking.items()]
        # Ordinamento della lista di tuple in modo decrescente in base ai punti
        sorted_list = sorted(tuple_list, key=lambda x: x[1], reverse=True)
        # Creazione della lista finale con il formato richiesto
        return [{'team_id': team_id, 'points': punti} for team_id, punti in sorted_list]