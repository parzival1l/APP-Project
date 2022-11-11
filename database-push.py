import sqlite3
import pandas as pd

try:
    sqliteConnection = sqlite3.connect("/Users/nandy/Git_repos/APP-Project/NBA_data.db")
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    # cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        # sqliteConnection.close()
        print("The SQLite connection is closed")


df_teams = pd.read_excel("/Users/nandy/Documents/App-data/nba_teams.xlsx")
print(df_teams.columns)

sqliteConnection = sqlite3.connect("/Users/nandy/Git_repos/APP-Project/NBA_database.db")
cur = sqliteConnection.cursor()

# df_teams.to_sql('Teams', sqliteConnection, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
print(pd.read_sql('select * from Teams', sqliteConnection))
sqliteConnection.commit()
# sqliteConnection.close()