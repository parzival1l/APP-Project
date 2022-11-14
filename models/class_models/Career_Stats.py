class Career_Stats:
    def __init__(self):
        self.player_id = None 
        self.GP = None 
        self.GS = None 
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

    def set_PTS(self, pts): 
        self.PTS = pts

    def get_PTS(self): 
        return self.PTS

    