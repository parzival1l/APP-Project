from All_Players import All_Players
from Career_Stats import Career_Stats
from Active_Players import Active_Players
from Season_Stats import Season_Stats
from Teams import Teams
from flask import *
import sqlite3

class San : 
    def __init__(self):
        # self.allplayers = 
        pass

    def find_player_names(self,player_name): 
        conn = sqlite3.connect("D:/My Important Documents/Activities in Concordia University/SOEN 6441_APP_Fall2022/APP-Project/models/static/stylesNBA_database.db")
        cur = conn.cursor()
        query = 'SELECT  B.full_name, A.PTS from Career_Stats AS A JOIN All_Players as B where B.full_name == "{}" and B.id = A.PLAYER_ID;'.format(player_name)
        cur.execute(query)
        records = cur.fetchall()
        print(records)
        return records



if __name__ == "__main__": 
    s1 = San()
    r = s1.find_player_names("Stephen Curry")
    print(type(r))
    print(r)

