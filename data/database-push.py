import sqlite3
import pandas as pd

class Data_push:
    def __init__(self) -> None:
        self.path = "/Users/nandy/Git_repos/APP-Project/data/NBA_database.db"

    def test_connection(self):
        """
        Function to test the SQL connection for the database path mentioned 
        """
        try:
            conn = sqlite3.connect(self.path)
            cursor = conn.cursor()
            print("Database created and Successfully Connected to SQLite")

            select_q = "select sqlite_version();"
            cursor.execute(select_q)
            record = cursor.fetchall()
            print("SQLite Database Version is: ", record)
            # cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if (conn):
                # sqliteConnection.close()
                print("The SQLite connection is closed")

    def insert_table(self, table, table_name):
        """
        Function to insert the table into the db passed as paramter. 
        """
        conn = sqlite3.connect(self.path)
        # cur = conn.cursor()
        table.to_sql(table_name, conn, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
        print(pd.read_sql('select * from {}'.format(table_name), conn))
        conn.commit()

if __name__ == "__main__" : 
    DB = Data_push()
    path = "/Users/nandy/Documents/App-data/"
    db_names = {
        "Teams":"nba_teams.xlsx",
        "Active_Players":"active_players.xlsx",
        "All_Players":"all_players.xlsx",
        "Career_Stats":"career_stats_final.xlsx",
        "Season_Stats":"season_stats_final.xlsx"
    }
    DB.test_connection()
# iterate over the file names and insert them into the SQL tables - Schema and tables have already been setup and the codes can be found in the database_schema.sql
    for key,value in db_names.items():
        DB.insert_table(pd.read_excel(path + db_names[value]), key)
    