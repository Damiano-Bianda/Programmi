from match_result import MatchResult

class MatchDay:
    def __init__(self, data):
        self.data = data
    
    def _is_match(self, match, team_id):
        return match['teams']['home']['id'] == team_id or match['teams']['away']['id'] == team_id

    def get_match_result(self, team_id):
        for match in self.data:
            if self._is_match(match, team_id):
                return MatchResult(match)
        raise Exception(f"Match result not found for team {team_id}")
    
    def is_match_finished(self, team_id):
        for match in self.data:
            if self._is_match(match, team_id):
                return match['fixture']['status']['short'] == 'FT'
        raise Exception(f"Match result not found for team {team_id}")