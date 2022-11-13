import sqlite3
import pandas as pd

# try:
#     sqliteConnection = sqlite3.connect("/Users/nandy/Git_repos/APP-Project/NBA_data.db")
#     cursor = sqliteConnection.cursor()
#     print("Database created and Successfully Connected to SQLite")

#     sqlite_select_Query = "select sqlite_version();"
#     cursor.execute(sqlite_select_Query)
#     record = cursor.fetchall()
#     print("SQLite Database Version is: ", record)
#     # cursor.close()

# except sqlite3.Error as error:
#     print("Error while connecting to sqlite", error)
# finally:
#     if (sqliteConnection):
#         # sqliteConnection.close()
#         print("The SQLite connection is closed")


# df_teams = pd.read_excel("/Users/nandy/Documents/App-data/nba_teams.xlsx")
# print(df_teams.columns)

# df_active_players = pd.read_excel("/Users/nandy/Documents/App-data/active_players.xlsx")
# print(df_active_players.columns)

# df_all_players = pd.read_excel("/Users/nandy/Documents/App-data/all_players.xlsx")
# print(df_all_players.columns)

career_stats = pd.read_excel("/Users/nandy/Documents/App-data/career_stats_final.xlsx")
print(career_stats.columns)

season_stats = pd.read_excel("/Users/nandy/Documents/App-data/season_stats_final.xlsx")
print(season_stats.columns)

sqliteConnection = sqlite3.connect("D:/My Important Documents/Activities in Concordia University/SOEN 6441_APP_Fall2022/APP-Project/NBA_database.db")
cur = sqliteConnection.cursor()

season_stats.to_sql('Season_Stats', sqliteConnection, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
print(pd.read_sql('select * from Season_Stats', sqliteConnection))

career_stats.to_sql('Career_Stats', sqliteConnection, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
print(pd.read_sql('select * from Career_Stats', sqliteConnection))

sqliteConnection.commit()
# sqliteConnection.close()