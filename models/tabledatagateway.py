import sqlite3

class TDG:
    def __init__(self):
        pass
    
    def connection_establish(self):
        conn = sqlite3.connect("/Users/nandy/Git_repos/APP-Project/data/NBA_database.db")
        cur = conn.cursor()
        return cur 

    def find_player_names(self, player_name):
        """
        method
        """        
        cursor = self.connection_establish()
        query = 'SELECT  B.full_name, A.PTS from Career_Stats AS A JOIN All_Players as B where B.full_name == "{}" and B.id = A.PLAYER_ID;'.format(
            player_name)
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    def gsw_active_players(self):
        """
        method
        """
        cursor = self.connection_establish()
        query = 'SELECT A.full_name from Active_Players as A where A.id in (SELECT PLAYER_ID from Season_Stats where TEAM_ABBREVIATION = "GSW" );'
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    def gsw_points_filter(self, points):
        """
        method
        """
        cursor = self.connection_establish()
        query = "SELECT B.full_name, A.PTS from All_Players as B, Career_Stats AS A where B.id = A.PLAYER_ID and A.PTS > {};".format(
            points)
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    def blocks_leader(self):
        """
        method
        """
        cursor = self.connection_establish()
        query = 'SELECT  B.full_name, A.BLK from Career_Stats AS A JOIN All_Players as B where B.id = A.PLAYER_ID and A.BLK = (SELECT MAX(BLK) from Career_Stats);'
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    def fg_percent_filter(self, fg_percent):
        """
        method
        """
        cursor = self.connection_establish()        
        query = "SELECT A.PLAYER_ID, B.full_name, A.FG_PCT from All_Players as B, Season_Stats AS A WHERE (B.id = A.PLAYER_ID and A.FG_PCT > {} and A.SEASON_ID = '2020-21')  ORDER BY A.FG_PCT  DESC;".format(
            fg_percent)
        cursor.execute(query)
        records = cursor.fetchall()
        return records