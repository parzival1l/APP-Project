# -*- coding: utf-8 -*-
"""API-APP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tNkgCY_OWJY2Y8ziR6fHewdh2xdYggBL
"""

!pip install nba_api

import pandas as pd 
from nba_api.stats.endpoints import playercareerstats, playerawards
from nba_api.stats.static import teams, players

# Anthony Davis
career = playercareerstats.PlayerCareerStats(player_id='203076')

# get_teams returns a list of 30 dictionaries, each an NBA team.
nba_teams = pd.json_normalize(teams.get_teams())
print('Number of teams fetched: {}'.format(nba_teams.shape))

nba_teams.to_excel("nba_teams.xlsx")

all_players = pd.json_normalize(players.get_players())
active_players = pd.json_normalize(players.get_active_players())

active_players_json = players.get_active_players()

active_player_ids = [x['id'] for x in active_players_json]

active_player_season_stats = pd.DataFrame(columns = career.get_data_frames()[0].columns.tolist())
active_players_career_stats = pd.DataFrame(columns = career.get_data_frames()[1].columns.tolist())

from tqdm import tqdm

len(active_player_ids)

for id in tqdm(active_player_ids[:200]): 
  dfats = playercareerstats.PlayerCareerStats(player_id=id).get_data_frames()
  active_player_season_stats = pd.concat([active_player_season_stats, dfats[0]])
  active_players_career_stats = pd.concat([active_players_career_stats, dfats[1]])

for id in tqdm(active_player_ids[201:400]): 
  dfats = playercareerstats.PlayerCareerStats(player_id=id).get_data_frames()
  active_player_season_stats = pd.concat([active_player_season_stats, dfats[0]])
  active_players_career_stats = pd.concat([active_players_career_stats, dfats[1]])

for id in tqdm(active_player_ids[401:]): 
  dfats = playercareerstats.PlayerCareerStats(player_id=id).get_data_frames()
  active_player_season_stats = pd.concat([active_player_season_stats, dfats[0]])
  active_players_career_stats = pd.concat([active_players_career_stats, dfats[1]])

active_player_season_stats.to_excel("career_stats.xlsx")

"""Queries : 
Query 1 : 
1. List all active players playing for GSW
2. How many points has Stephen Curry scored in total ?
3. Which player has the most blocks in his carrer ? 
4. List the names of players who have scored more than 20000 points for their career ? 
"""



active_player_season_stats.shape

active_players_career_stats.shape

active_players_career_stats.to_excel("career_stats.xlsx")

active_player_season_stats.to_excel("season_stats.xlsx")

active_player_season_stats



all_players[['id','full_name','first_name','last_name']].to_excel("all_players.xlsx")

active_players[['id','full_name','first_name','last_name']].to_excel("active_players.xlsx")

[player for player in active_players if player['full_name'] == 'Stephen Curry']

from nba_api.stats.endpoints import playercareerstats
# Anthony Davis
career = playercareerstats.PlayerCareerStats(player_id='203076')
career.get_data_frames()[0]

career.get_data_frames()[1]

career.get_data_frames()[4]





active_players = players.get_active_players()
active_players[0]



len(active_players)

for player in active_players[:1]:
  player['id']