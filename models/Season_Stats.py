class Season_Stats:
    def __init__(self):
        self.player_id = None 
        self.season_id = None 
        self.team_abbreviation = None 
        self.FGM = None 
        self.FGA = None 
        self.FG_PCT = None 
        self.FG3M = None 
        self.FG3A = None 
        self.FG3_PCT = None 
        self.FTM = None 
        self.FTA = None 
        self.FT_PCT = None 
        self.REB = None 
        self.AST = None 
        self.STL = None 
        self.BLK = None 
        self.PTS = None 

    def set_player_id(self, id): 
        self.player_id = id 

    def get_player_id(self): 
        return self.player_id

    def set_team_abbreviation(self, abb): 
        self.team_abbreviation = abb

    def get_team_abbreviation(self): 
        return self.team_abbreviation

    