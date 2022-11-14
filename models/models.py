from class_models.Active_Players import Active_Players
from class_models.All_Players import All_Players
from class_models.Career_Stats import Career_Stats
from class_models.Season_Stats import Season_Stats
from class_models.Teams import Teams
from tabledatagateway import TDG

class DBMapper:
    """
    method
    """

    def __init__(self):
        self.tdg = TDG()
        self.active_players = Active_Players()
        self.all_players = All_Players()
        self.career_stats = Career_Stats()
        self.season_stats = Season_Stats()
        self.teams = Teams()

    def find_player_names(self, player_name):
        """
        method
        """
        self.all_players.set_full_name(player_name)
        records = self.tdg.find_player_names(self.all_players.get_full_name())
        return records

    def gsw_active_players(self):
        """
        method
        """
        records = self.tdg.gsw_active_players()
        return records

    def gsw_points_filter(self, points):
        """
        method
        """
        self.career_stats.set_PTS(points)
        records = self.tdg.gsw_points_filter(self.career_stats.get_PTS())
        return records

    def blocks_leader(self):
        """
        method
        """
        records = self.tdg.blocks_leader()
        return records

    def fg_percent_filter(self, fg_percent):
        """
        method
        """
        self.season_stats.set_FG_PCT(fg_percent)
        records = self.tdg.fg_percent_filter(self.season_stats.get_FG_PCT())
        return records

