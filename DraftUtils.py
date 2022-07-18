# coding: utf-8

from jpartyfb.models import PlayerSpecsQb, PlayerSpecsRb, PlayerSpecsWr, PlayerSpecsFb, PlayerSpecsTe, PlayerSpecsOl, \
    PlayerSpecsDl, PlayerSpecsLb, PlayerSpecsCb, PlayerSpecsSf, PlayerSpecsK, PlayerSpecsP, PlayerSpecsStd, PlayerSpecsSto

import json
import random

DRAFT_VALUE_BASELINE_QB = 50
DRAFT_VALUE_BASELINE_RB = 48
DRAFT_VALUE_BASELINE_WR = 47
DRAFT_VALUE_BASELINE_TE = 44
DRAFT_VALUE_BASELINE_FB = 35
DRAFT_VALUE_BASELINE_OL = 48
DRAFT_VALUE_BASELINE_DL = 48
DRAFT_VALUE_BASELINE_LB = 44
DRAFT_VALUE_BASELINE_CB = 43
DRAFT_VALUE_BASELINE_SF = 43
DRAFT_VALUE_BASELINE_K = 35
DRAFT_VALUE_BASELINE_P = 35
DRAFT_VALUE_BASELINE_STD = 30
DRAFT_VALUE_BASELINE_STO = 30

def calculate_player_draft_value(this_player_id, this_player_primary_position):

    player_stats_obj = None
    baseline_rank_value = 0

    if this_player_primary_position == 'dl':

        try:
            player_stats_obj = PlayerSpecsDl.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_DL

    elif this_player_primary_position == 'cb':

        try:
            player_stats_obj = PlayerSpecsCb.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_CB

    elif this_player_primary_position == 'fb':

        try:
            player_stats_obj = PlayerSpecsFb.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_FB

    elif this_player_primary_position == 'k':

        try:
            player_stats_obj = PlayerSpecsK.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_K

    elif this_player_primary_position == 'lb':

        try:
            player_stats_obj = PlayerSpecsLb.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_LB

    elif this_player_primary_position == 'ol':

        try:
            player_stats_obj = PlayerSpecsOl.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_OL

    elif this_player_primary_position == 'p':

        try:
            player_stats_obj = PlayerSpecsP.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_P

    elif this_player_primary_position == 'qb':

        try:
            player_stats_obj = PlayerSpecsQb.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_QB

    elif this_player_primary_position == 'rb':

        try:
            player_stats_obj = PlayerSpecsRb.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_RB

    elif this_player_primary_position == 'sf':

        try:
            player_stats_obj = PlayerSpecsSf.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_SF

    elif this_player_primary_position == 'std':

        try:
            player_stats_obj = PlayerSpecsStd.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_STD

    elif this_player_primary_position == 'sto':

        try:
            player_stats_obj = PlayerSpecsSto.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_STO

    elif this_player_primary_position == 'te':

        try:
            player_stats_obj = PlayerSpecsTe.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_TE

    elif this_player_primary_position == 'wr':

        try:
            player_stats_obj = PlayerSpecsWr.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_WR

    #get the career_arc dict from player_stats_obj
    this_player_career_arc_dict_str = player_stats_obj[0].career_arc_dict

    #replace single quotes with double quotes and then convert to dict using json
    this_player_career_arc_dict_str = this_player_career_arc_dict_str.replace("\'", "\"")
    this_player_career_arc_dict_list = json.loads(this_player_career_arc_dict_str)

    #get first 3 years of specs
    this_player_career_arc_first_3_years_list_dict = this_player_career_arc_dict_list[:3]

    # calculate rank of player - using position, query the relevant spec db table and look at the first 3 years of their arc
    # the first year numbers are exact, the second year numbers are off by +-4, and the third year numbers are off
    # by +-8

    avg_stat_rating_list = []
    trend_prediction_str = ""

    for year_idx, this_year_dict in enumerate(this_player_career_arc_first_3_years_list_dict, 1):

        this_year_average_spec_value_list = this_year_dict.values()
        this_year_average_spec_final_value = round(sum(this_year_average_spec_value_list) / len(this_year_average_spec_value_list), 3)

        if year_idx == 2:

            # I want to simulate scouts misjudging a prospect, so change the average value by +- 4 randomly

            trend_int = random.randint(-4, 4)
            this_year_average_spec_final_value += trend_int

            if trend_int < 0:
                trend_prediction_str = "negative"
            elif trend_int > 0:
                trend_prediction_str = "positive"
            else:
                trend_prediction_str = "zero"

        elif year_idx == 3:

            # I want to simulate scouts misjudging a prospect, so change the average value by up to +- 8 randomly
            #the trend from year 2 should factor into the misjudgement for year 3

            if trend_prediction_str == "negative":
                trend_int = random.randint(-8, -4)
            elif trend_prediction_str == "positive":
                trend_int = random.randint(4, 8)
            else:
                trend_int = random.randint(-2, 2)

            this_year_average_spec_final_value += trend_int

        avg_stat_rating_list.append(this_year_average_spec_final_value)

    #average values in avg_stat_rating_list
    overall_avg_stat_rating = sum(avg_stat_rating_list) / len(avg_stat_rating_list)

    #finally, add overall_avg_stat_rating to one of the DRAFT_VALUE_BASELINE_X constants above,based on player_position
    player_draft_value = round(overall_avg_stat_rating + baseline_rank_value, 3)

    return player_draft_value





