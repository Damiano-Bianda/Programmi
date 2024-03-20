class MatchResult:
    def __init__(self, data):
        self.data = data

    def has_won(self, team):
        return self.data['teams']['home']['id'] == team \
            and self.data['goals']['home'] > self.data['goals']['away'] \
                or self.data['teams']['away']['id'] == team \
                    and self.data['goals']['away'] > self.data['goals']['home']
    
    def has_drawn(self, team):
        return self.data['goals']['home'] == self.data['goals']['away']
    
    def has_lost(self, team):
        return not self.has_won(team) and not self.has_drawn(team)
