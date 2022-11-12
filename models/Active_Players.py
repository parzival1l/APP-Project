class Active_Players:
    def __init__(self):
        self.id = None 
        self.full_name = None 
        self.first_name = None 
        self.last_name = None

    def set_full_name(self, name): 
        self.full_name = name 
    
    def get_full_name(self): 
        return self.full_name
    
    def set_id(self, id): 
        self.id = id 

    def get_id(self): 
        return self.id 
    