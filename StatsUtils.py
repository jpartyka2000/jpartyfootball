# coding: utf-8

from jpartyfb.models import PlayerSpecsQb, PlayerSpecsRb, PlayerSpecsWr, PlayerSpecsFb, PlayerSpecsTe, PlayerSpecsOl, \
    PlayerSpecsDl, PlayerSpecsLb, PlayerSpecsCb, PlayerSpecsSf, PlayerSpecsK, PlayerSpecsP, PlayerSpecsStd, PlayerSpecsSto, \
    Season, Team, TeamSeason, Player, PlayerTeam, City

from jpartyfb import PlayerCreation, DraftUtils

from operator import itemgetter

import json
import random

def calculate_team_preseason_power_rankings(league_id, season_id):

    status_code = 1
    team_id_to_power_ranking_dict = {}

    #get all players by querying PlayerTeam for this league_id and season_id
    try:
        player_team_obj_list = PlayerTeam.objects.using('default').filter(league_id=league_id, season_id=season_id).order_by("team_id")
    except Exception:
        return -1, team_id_to_power_ranking_dict

    team_id_to_player_value_list_dict = {}

    for this_player_team_obj in player_team_obj_list:
        this_player_id = this_player_team_obj.player_id
        this_player_primary_position = this_player_team_obj.player.primary_position
        this_team_id = this_player_team_obj.team_id
        first_season_id = this_player_team_obj.player.first_season_id

        current_season_index = season_id - first_season_id

        this_player_value = calculate_this_season_player_value(this_player_id, current_season_index, this_player_primary_position)

        if this_team_id not in team_id_to_player_value_list_dict:
            team_id_to_player_value_list_dict[this_team_id] = []

        team_id_to_player_value_list_dict[this_team_id].append(this_player_value)

    #calculate power rankings for each team and add to TeamSeason
    for this_team_id, this_player_value_list in team_id_to_player_value_list_dict.items():

        this_team_power_ranking = round(1.0 * sum(this_player_value_list) / len(this_player_value_list), 2)

        #add to team_id_to_power_ranking_dict
        team_id_to_power_ranking_dict[this_team_id] = this_team_power_ranking

        #update TeamSeason row with this_team_power_ranking for this season_id
        try:
            TeamSeason.objects.using('default').filter(league_id=league_id, season_id=season_id, team_id=this_team_id).update(preseason_power_ranking=this_team_power_ranking)
        except Exception:
            return -1, {}

    return status_code, team_id_to_power_ranking_dict


def calculate_this_season_player_value(this_player_id, current_season_index, this_player_primary_position):
    player_stats_obj = None
    baseline_rank_value = 0
    critical_attribute_list = []

    if this_player_primary_position == 'dl':

        try:
            player_stats_obj = PlayerSpecsDl.objects.using('default').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DraftUtils.DRAFT_VALUE_BASELINE_DL
        critical_attribute_list = ['block_power_rating', 'tackle_rating']

    elif this_player_primary_position == 'cb':

        try:
            player_stats_obj = PlayerSpecsCb.objects.using('default').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DraftUtils.DRAFT_VALUE_BASELINE_CB
        critical_attribute_list = ['speed_rating', 'route_rating']

    elif this_player_primary_position == 'fb':

        try:
            player_stats_obj = PlayerSpecsFb.objects.using('default').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DraftUtils.DRAFT_VALUE_BASELINE_FB
        critical_attribute_list = ['speed_rating', 'strength_rating']

    elif this_player_primary_position == 'k':

        try:
            player_stats_obj = PlayerSpecsK.objects.using('default').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DraftUtils.DRAFT_VALUE_BASELINE_K
        critical_attribute_list = ['leg_rating', 'accuracy_rating']

    elif this_player_primary_position == 'lb':

        try:
            player_stats_obj = PlayerSpecsLb.objects.using('default').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DraftUtils.DRAFT_VALUE_BASELINE_LB
        critical_attribute_list = ['speed_rating', 'tackle_rating']

    elif this_player_primary_position == 'ol':

        try:
            player_stats_obj = PlayerSpecsOl.objects.using('default').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DraftUtils.DRAFT_VALUE_BASELINE_OL
        critical_attribute_list = ['block_power_rating', 'block_agility_rating']

    elif this_player_primary_position == 'p':

        try:
            player_stats_obj = PlayerSpecsP.objects.using('default').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DraftUtils.DRAFT_VALUE_BASELINE_P
        critical_attribute_list = ['leg_rating', 'hangtime_rating']

    elif this_player_primary_position == 'qb':

        try:
            player_stats_obj = PlayerSpecsQb.objects.using('default').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DraftUtils.DRAFT_VALUE_BASELINE_QB
        critical_attribute_list = ['arm_strength_rating', 'arm_accuracy_rating']

    elif this_player_primary_position == 'rb':

        try:
            player_stats_obj = PlayerSpecsRb.objects.using('default').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DraftUtils.DRAFT_VALUE_BASELINE_RB
        critical_attribute_list = ['speed_rating', 'elusiveness_rating']

    elif this_player_primary_position == 'sf':

        try:
            player_stats_obj = PlayerSpecsSf.objects.using('default').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DraftUtils.DRAFT_VALUE_BASELINE_SF
        critical_attribute_list = ['speed_rating', 'route_rating']

    elif this_player_primary_position == 'std':

        try:
            player_stats_obj = PlayerSpecsStd.objects.using('default').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DraftUtils.DRAFT_VALUE_BASELINE_STD
        critical_attribute_list = ['agility_rating', 'tackle_rating']

    elif this_player_primary_position == 'sto':

        try:
            player_stats_obj = PlayerSpecsSto.objects.using('default').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DraftUtils.DRAFT_VALUE_BASELINE_STO
        critical_attribute_list = ['speed_rating', 'elusiveness_rating']

    elif this_player_primary_position == 'te':

        try:
            player_stats_obj = PlayerSpecsTe.objects.using('default').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DraftUtils.DRAFT_VALUE_BASELINE_TE
        critical_attribute_list = ['catching_rating', 'block_power_rating']

    elif this_player_primary_position == 'wr':

        try:
            player_stats_obj = PlayerSpecsWr.objects.using('default').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DraftUtils.DRAFT_VALUE_BASELINE_WR
        critical_attribute_list = ['catching_rating', 'route_rating']

    # get the career_arc dict from player_stats_obj
    this_player_career_arc_dict_str = player_stats_obj[0].career_arc_dict

    # replace single quotes with double quotes and then convert to dict using json
    this_player_career_arc_dict_str = this_player_career_arc_dict_str.replace("\'", "\"")
    this_player_career_arc_dict_list = json.loads(this_player_career_arc_dict_str)

    #we need to get the current season's dict in this_player_career_arc_dict_list
    this_year_dict = this_player_career_arc_dict_list[current_season_index]

    #calculate player value using their current season

    avg_stat_rating_list = []
    trend_prediction_str = ""

    attribute_sum = 0
    attribute_weight = 0.0

    for this_attribute_name, this_attribute_value in this_year_dict.items():
        if this_attribute_name in critical_attribute_list:
            attribute_weight = 1.25
        else:
            attribute_weight = 1.0

        attribute_sum += attribute_weight * int(this_attribute_value)

    this_year_player_final_value = round(attribute_sum / len(this_year_dict.values()), 3)

    player_value = round(this_year_player_final_value + baseline_rank_value, 3)

    return player_value







