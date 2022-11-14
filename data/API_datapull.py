!pip install nba_api
from tqdm import tqdm
import pandas as pd 
from nba_api.stats.endpoints import playercareerstats, playerawards
from nba_api.stats.static import teams, players

class Data_curate:

  def __init__(self) -> None:
    pass

  def get_teams(self) : 
    """
    get_teams returns a list of 30 dictionaries, each an NBA team.
    """
    nba_teams = pd.json_normalize(teams.get_teams())
    print('Number of teams fetched: {}'.format(nba_teams.shape))
    return nba_teams

  def get_players(self) : 
    """
    Get the list of active players in the NBA in both JSON and pandas format along with historical players. 
    """
    all_players = pd.json_normalize(players.get_players())
    active_players = pd.json_normalize(players.get_active_players())
    active_players_json = players.get_active_players()

    return all_players, active_players, active_players_json
    
  def get_stats(self, active_players_json):
    """
    Get the active player's career totals and season totals.
    """
    #get dataframe column values of a random player . 
    career = playercareerstats.PlayerCareerStats(player_id='203076')
    
    active_player_ids = [x['id'] for x in active_players_json]
    active_player_season_stats = pd.DataFrame(columns = career.get_data_frames()[0].columns.tolist())
    active_players_career_stats = pd.DataFrame(columns = career.get_data_frames()[1].columns.tolist())

    for id in tqdm(active_player_ids): 
      df_stats = playercareerstats.PlayerCareerStats(player_id=id).get_data_frames()
      active_player_season_stats = pd.concat([active_player_season_stats, df_stats[0]])
      active_players_career_stats = pd.concat([active_players_career_stats, df_stats[1]])
    
    return active_player_season_stats, active_players_career_stats 
    
if __name__ == "__name__" : 
  nba_api = Data_curate()
  nba_api.get_teams().to_excel("teams.xlsx")

  all_players, active_players, active_players_json = nba_api.get_players() 
  all_players.to_excel("all_players.xlsx")
  active_players.to_excel("active_players.xlsx")

  season_stats, career_stats  = nba_api.get_stats(active_players_json)
  season_stats.to_excel("season_stats.xlsx")
  career_stats.to_excel("career_stats.xlsx")