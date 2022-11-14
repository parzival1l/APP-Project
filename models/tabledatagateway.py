import sqlite3

class TDG:
    def __init__(self):
        pass
    
    def connection_establish(self):
        """
        Function to setup the DB connection and return the cursor object.
        """
        conn = sqlite3.connect("/Users/nandy/Git_repos/APP-Project/data/NBA_database.db")
        cur = conn.cursor()
        return cur 

    def find_player_names(self, player_name):
        """
        Function to find the total points a player has scored taking in the player name as parameters
        """    
        cursor = self.connection_establish()
        query = f"SELECT  B.full_name, A.PTS from Career_Stats AS A JOIN All_Players as B where B.full_name == '{player_name}' and B.id = A.PLAYER_ID;"
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    def gsw_active_players(self):
        """
        Function to find the active players playing for GSW
        """
        cursor = self.connection_establish()
        query = 'SELECT A.full_name from Active_Players as A where A.id in (SELECT PLAYER_ID from Season_Stats where TEAM_ABBREVIATION = "GSW" );'
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    def gsw_points_filter(self, points):
        """
        Function to find all players who have scored more the give points total for their carrers.
        """
        cursor = self.connection_establish()
        query = f"SELECT B.full_name, A.PTS from All_Players as B, Career_Stats AS A where B.id = A.PLAYER_ID and A.PTS > '{points}';"
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    def blocks_leader(self):
        """
        Function to return the current career leader in blocked shots.
        """
        cursor = self.connection_establish()
        query = 'SELECT  B.full_name, A.BLK from Career_Stats AS A JOIN All_Players as B where B.id = A.PLAYER_ID and A.BLK = (SELECT MAX(BLK) from Career_Stats);'
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    def fg_percent_filter(self, fg_percent):
        """
        Function to return all the players shooting more than a given percent for the season 2021-22 in descending order.
        """
        cursor = self.connection_establish()        
        query = f"SELECT A.PLAYER_ID, B.full_name, A.FG_PCT from All_Players as B, Season_Stats AS A WHERE (B.id = A.PLAYER_ID and A.FG_PCT > '{fg_percent}' and A.SEASON_ID = '2020-21')  ORDER BY A.FG_PCT  DESC;"            
        cursor.execute(query)
        records = cursor.fetchall()
        return records