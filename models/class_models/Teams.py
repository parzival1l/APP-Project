class Teams:
    def __init__(self):
        self.team_id = None 
        self.full_name = None 
        self.abbreviation = None 
        self.nickname = None
        self.city = None
        self.state = None
        self.year_founded = None

    def set_team_id(self, id): 
        self.team_id = id 
    
    def get_team_id(self): 
        return self.team_id 

    def set_abbreviaiton(self, abb): 
        self.abbreviation = abb
    
    def get_abbreviaiton(self): 
        return self.abbreviation
    
    def set_full_name(self, name): 
        self.full_name = name 
    
    def get_full_name(self): 
        return self.full_name