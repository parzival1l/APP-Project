import sqlite3

from Active_Players import Active_Players
from All_Players import All_Players
from Career_Stats import Career_Stats
from flask import *
from Season_Stats import Season_Stats
from Teams import Teams


class San:
    """
    """

    def __init__(self):
        # self.allplayers =
        pass

    def find_player_names(self, player_name):
        """
        method
        """
        # conn = sqlite3.connect("D:/My Important Documents/Activities in Concordia University/SOEN 6441_APP_Fall2022/APP-Project/NBA_database.db")
        conn = sqlite3.connect(
            "/Users/nandy/Git_repos/APP-Project/NBA_database.db")

        cur = conn.cursor()
        query = 'SELECT  B.full_name, A.PTS from Career_Stats AS A JOIN All_Players as B where B.full_name == "{}" and B.id = A.PLAYER_ID;'.format(
            player_name)
        cur.execute(query)
        records = cur.fetchall()
        return records

    def gsw_active_players(self):
        """
        method
        """
        conn = sqlite3.connect(
            "/Users/nandy/Git_repos/APP-Project/NBA_database.db")
        cur = conn.cursor()
        query = 'SELECT A.full_name from Active_Players as A where A.id in (SELECT PLAYER_ID from Season_Stats where TEAM_ABBREVIATION = "GSW" );'
        cur.execute(query)
        records = cur.fetchall()
        return records

    def gsw_points_filter(self, points):
        """
        method
        """
        conn = sqlite3.connect(
            "/Users/nandy/Git_repos/APP-Project/NBA_database.db")
        cur = conn.cursor()
        query = "SELECT B.full_name, A.PTS from All_Players as B, Career_Stats AS A where B.id = A.PLAYER_ID and A.PTS > {};".format(
            points)
        cur.execute(query)
        records = cur.fetchall()
        return records

    def blocks_leader(self):
        """
        method
        """
        conn = sqlite3.connect(
            "/Users/nandy/Git_repos/APP-Project/NBA_database.db")
        cur = conn.cursor()
        query = 'SELECT  B.full_name, A.BLK from Career_Stats AS A JOIN All_Players as B where B.id = A.PLAYER_ID and A.BLK = (SELECT MAX(BLK) from Career_Stats);'
        cur.execute(query)
        records = cur.fetchall()
        return records

    def fg_percent_filter(self, fg_percent):
        """
        method
        """
        conn = sqlite3.connect(
            "/Users/nandy/Git_repos/APP-Project/NBA_database.db")
        cur = conn.cursor()
        query = "SELECT A.PLAYER_ID, B.full_name, A.FG_PCT from All_Players as B, Season_Stats AS A WHERE (B.id = A.PLAYER_ID and A.FG_PCT > {} and A.SEASON_ID = '2020-21')  ORDER BY A.FG_PCT  DESC;".format(
            fg_percent)
        cur.execute(query)
        records = cur.fetchall()
        return records

if __name__ == "__main__":
    s1 = San()
    r = s1.find_player_names("Stephen Curry")
    print(type(r))
    print(r)
