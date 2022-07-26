# coding: utf-8

from jpartyfb.models import PlayerSpecsQb, PlayerSpecsRb, PlayerSpecsWr, PlayerSpecsFb, PlayerSpecsTe, PlayerSpecsOl, \
    PlayerSpecsDl, PlayerSpecsLb, PlayerSpecsCb, PlayerSpecsSf, PlayerSpecsK, PlayerSpecsP, PlayerSpecsStd, PlayerSpecsSto, \
    Season, Team, Player, PlayerTeam

from operator import itemgetter

import json
import random

DRAFT_VALUE_BASELINE_QB = 50
DRAFT_VALUE_BASELINE_RB = 49
DRAFT_VALUE_BASELINE_WR = 49
DRAFT_VALUE_BASELINE_TE = 45
DRAFT_VALUE_BASELINE_FB = 35
DRAFT_VALUE_BASELINE_OL = 47
DRAFT_VALUE_BASELINE_DL = 49
DRAFT_VALUE_BASELINE_LB = 45
DRAFT_VALUE_BASELINE_CB = 44
DRAFT_VALUE_BASELINE_SF = 44
DRAFT_VALUE_BASELINE_K = 35
DRAFT_VALUE_BASELINE_P = 35
DRAFT_VALUE_BASELINE_STD = 30
DRAFT_VALUE_BASELINE_STO = 30

NUMBER_OF_DRAFT_ROUNDS = 8

#we need this to help teams draft the best players according to their biggest position needs
player_position_to_starter_count_dict = {}
player_position_to_starter_count_dict['qb'] = 1
player_position_to_starter_count_dict['rb'] = 1
player_position_to_starter_count_dict['te'] = 1
player_position_to_starter_count_dict['fb'] = 1
player_position_to_starter_count_dict['wr'] = 2
player_position_to_starter_count_dict['ol'] = 5
player_position_to_starter_count_dict['k'] = 1
player_position_to_starter_count_dict['p'] = 1
player_position_to_starter_count_dict['dl'] = 5
player_position_to_starter_count_dict['lb'] = 2
player_position_to_starter_count_dict['cb'] = 2
player_position_to_starter_count_dict['sf'] = 2
player_position_to_starter_count_dict['sto'] = 2
player_position_to_starter_count_dict['std'] = 2

ROUND_1_PLAYER_SEARCH_LIMIT = 50
ROUND_2_PLAYER_SEARCH_LIMIT = 100

def calculate_player_draft_value(this_player_id, this_player_primary_position):

    player_stats_obj = None
    baseline_rank_value = 0
    critical_attribute_list = []

    if this_player_primary_position == 'dl':

        try:
            player_stats_obj = PlayerSpecsDl.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_DL
        critical_attribute_list = ['block_power_rating','tackle_rating']

    elif this_player_primary_position == 'cb':

        try:
            player_stats_obj = PlayerSpecsCb.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_CB
        critical_attribute_list = ['speed_rating','route_rating']

    elif this_player_primary_position == 'fb':

        try:
            player_stats_obj = PlayerSpecsFb.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_FB
        critical_attribute_list = ['speed_rating','strength_rating']

    elif this_player_primary_position == 'k':

        try:
            player_stats_obj = PlayerSpecsK.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_K
        critical_attribute_list = ['leg_rating','accuracy_rating']

    elif this_player_primary_position == 'lb':

        try:
            player_stats_obj = PlayerSpecsLb.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_LB
        critical_attribute_list = ['speed_rating','tackle_rating']

    elif this_player_primary_position == 'ol':

        try:
            player_stats_obj = PlayerSpecsOl.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_OL
        critical_attribute_list = ['block_power_rating','block_agility_rating']

    elif this_player_primary_position == 'p':

        try:
            player_stats_obj = PlayerSpecsP.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_P
        critical_attribute_list = ['leg_rating','hangtime_rating']

    elif this_player_primary_position == 'qb':

        try:
            player_stats_obj = PlayerSpecsQb.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_QB
        critical_attribute_list = ['arm_strength_rating','arm_accuracy_rating']

    elif this_player_primary_position == 'rb':

        try:
            player_stats_obj = PlayerSpecsRb.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_RB
        critical_attribute_list = ['speed_rating','elusiveness_rating']

    elif this_player_primary_position == 'sf':

        try:
            player_stats_obj = PlayerSpecsSf.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_SF
        critical_attribute_list = ['speed_rating','route_rating']

    elif this_player_primary_position == 'std':

        try:
            player_stats_obj = PlayerSpecsStd.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_STD
        critical_attribute_list = ['agility_rating','tackle_rating']

    elif this_player_primary_position == 'sto':

        try:
            player_stats_obj = PlayerSpecsSto.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_STO
        critical_attribute_list = ['speed_rating','elusiveness_rating']

    elif this_player_primary_position == 'te':

        try:
            player_stats_obj = PlayerSpecsTe.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_TE
        critical_attribute_list = ['catching_rating','block_power_rating']

    elif this_player_primary_position == 'wr':

        try:
            player_stats_obj = PlayerSpecsWr.objects.using('xactly_dev').filter(player_id=this_player_id)
        except Exception:
            return 0.0

        baseline_rank_value = DRAFT_VALUE_BASELINE_WR
        critical_attribute_list = ['catching_rating','route_rating']

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

        attribute_sum = 0
        attribute_weight = 0.0

        for this_attribute_name, this_attribute_value in this_year_dict.items():
            if this_attribute_name in critical_attribute_list:
                attribute_weight = 1.25
            else:
                attribute_weight = 1.0

            attribute_sum += attribute_weight * int(this_attribute_value)

        this_year_average_spec_final_value =  round(attribute_sum / len(this_year_dict.values()), 3)

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


def determine_draft_picks(league_id, season_id):

    team_id_to_team_name_dict = {}
    team_id_to_draft_order_dict = {}
    team_id_to_draft_pick_dict_dict = {}  #k: team_id, val: dict of round num -> player_id
    team_id_to_draft_player_score_dict_dict = {}

    #this data structure holds all the information about a team's current roster that would be needed
    #to make intelligent draft selections
    team_id_to_position_player_info_list_dict_dict = {}

    # create data structure indicating how much the team improves with a drafted player
    # over the worst starter at a given position
    team_id_to_player_improvement_score_dict_dict = {}

    #first, get all teams in this league by querying Team table
    try:
        team_obj_list = Team.objects.using("xactly_dev").filter(league_id=league_id)
    except Exception:
        team_obj_list = None

    if team_obj_list is not None:

        #initialize data structures keyed by team_id
        for this_team_obj in team_obj_list:
            this_team_id = this_team_obj.id
            this_team_nickname = this_team_obj.nickname

            team_id_to_team_name_dict[this_team_id] = this_team_nickname
            team_id_to_draft_order_dict[this_team_id] = -1
            team_id_to_draft_pick_dict_dict[this_team_id] = {}
            team_id_to_draft_player_score_dict_dict[this_team_id] = {}
            team_id_to_position_player_info_list_dict_dict[this_team_id] = {}
            team_id_to_player_improvement_score_dict_dict[this_team_id] = {}

            for i in range(1, NUMBER_OF_DRAFT_ROUNDS + 1):
                team_id_to_draft_pick_dict_dict[this_team_id][i] = -1
    else:
        return -1

    #next, get season number of this season. If we are in season 1 of this league, then we will randomly determine
    #drafting order for teams. Otherwise, it will be determined by league rankings of the teams.

    try:
        season_obj = Season.objects.using("xactly_dev").filter(id=season_id)
    except Exception:
        season_obj = None

    this_season_year = -1

    if season_obj is not None:

        this_season_year = season_obj[0].season_year

        if season_obj[0].season_year == 1:

            #randomly determine team drafting order
            team_id_draft_order_list = random.sample(team_id_to_draft_order_dict.keys(), len(team_id_to_draft_order_dict.keys()))

            for this_draft_order_num in team_id_draft_order_list:
                team_id_to_draft_order_dict[this_team_id] = this_draft_order_num

        else:
            #we will need to query for the previous season's records and set draft order based on team rankings
            pass
    else:
        return -1

    #next, we need to get each team's score of the draftable players. I will calculate this by taking the player rank and deviating from
    #it randomly by +- 6

    try:
        draft_player_obj_list = Player.objects.using("xactly_dev").filter(league_id=league_id, playing_status=0).order_by("-draft_value")
    except Exception:
        draft_player_obj_list = None

    #we need to make sure that any selected players are taken off the board immediately
    player_id_to_draft_availability = {}

    if draft_player_obj_list is not None:

        for this_draft_player in draft_player_obj_list:

            this_draft_player_base_value = this_draft_player.draft_value
            this_draft_player_id = this_draft_player.id

            player_id_to_draft_availability[this_draft_player_id] = True

            for this_team_id in team_id_to_draft_player_score_dict_dict.keys():

                #create team-based deviation
                team_based_deviation = random.randint(-6, 6)
                team_id_to_draft_player_score_dict_dict[this_team_id][this_draft_player_id] = this_draft_player_base_value + team_based_deviation

    else:
        return -1

    #get all players in this league that are already on teams and create data structure to hold their information

    try:
        roster_player_team_obj_list = PlayerTeam.objects.using("xactly_dev").filter(league_id=league_id)
    except Exception:
        roster_player_team_obj_list = None

    if roster_player_team_obj_list is not None:

        baseline_rank_value = -1
        critical_attribute_list = []

        for this_roster_player_team_obj in roster_player_team_obj_list:

            this_team_id = this_roster_player_team_obj.team_id
            this_player_id = this_roster_player_team_obj.player_id
            this_player_primary_position = this_roster_player_team_obj.player.primary_position

            #get data to allow roster player to be ranked
            if this_player_primary_position == 'dl':

                try:
                    player_stats_obj = PlayerSpecsDl.objects.using('xactly_dev').filter(player_id=this_player_id)
                except Exception:
                    return -1

                baseline_rank_value = DRAFT_VALUE_BASELINE_DL
                critical_attribute_list = ['block_power_rating', 'tackle_rating']

            elif this_player_primary_position == 'cb':

                try:
                    player_stats_obj = PlayerSpecsCb.objects.using('xactly_dev').filter(player_id=this_player_id)
                except Exception:
                    return -1

                baseline_rank_value = DRAFT_VALUE_BASELINE_CB
                critical_attribute_list = ['speed_rating', 'route_rating']

            elif this_player_primary_position == 'fb':

                try:
                    player_stats_obj = PlayerSpecsFb.objects.using('xactly_dev').filter(player_id=this_player_id)
                except Exception:
                    return -1

                baseline_rank_value = DRAFT_VALUE_BASELINE_FB
                critical_attribute_list = ['speed_rating', 'strength_rating']

            elif this_player_primary_position == 'k':

                try:
                    player_stats_obj = PlayerSpecsK.objects.using('xactly_dev').filter(player_id=this_player_id)
                except Exception:
                    return -1

                baseline_rank_value = DRAFT_VALUE_BASELINE_K
                critical_attribute_list = ['leg_rating', 'accuracy_rating']

            elif this_player_primary_position == 'lb':

                try:
                    player_stats_obj = PlayerSpecsLb.objects.using('xactly_dev').filter(player_id=this_player_id)
                except Exception:
                    return -1

                baseline_rank_value = DRAFT_VALUE_BASELINE_LB
                critical_attribute_list = ['speed_rating', 'tackle_rating']

            elif this_player_primary_position == 'ol':

                try:
                    player_stats_obj = PlayerSpecsOl.objects.using('xactly_dev').filter(player_id=this_player_id)
                except Exception:
                    return -1

                baseline_rank_value = DRAFT_VALUE_BASELINE_OL
                critical_attribute_list = ['block_power_rating', 'block_agility_rating']

            elif this_player_primary_position == 'p':

                try:
                    player_stats_obj = PlayerSpecsP.objects.using('xactly_dev').filter(player_id=this_player_id)
                except Exception:
                    return -1

                baseline_rank_value = DRAFT_VALUE_BASELINE_P
                critical_attribute_list = ['leg_rating', 'hangtime_rating']

            elif this_player_primary_position == 'qb':

                try:
                    player_stats_obj = PlayerSpecsQb.objects.using('xactly_dev').filter(player_id=this_player_id)
                except Exception:
                    return -1

                baseline_rank_value = DRAFT_VALUE_BASELINE_QB
                critical_attribute_list = ['arm_strength_rating', 'arm_accuracy_rating']

            elif this_player_primary_position == 'rb':

                try:
                    player_stats_obj = PlayerSpecsRb.objects.using('xactly_dev').filter(player_id=this_player_id)
                except Exception:
                    return -1

                baseline_rank_value = DRAFT_VALUE_BASELINE_RB
                critical_attribute_list = ['speed_rating', 'elusiveness_rating']

            elif this_player_primary_position == 'sf':

                try:
                    player_stats_obj = PlayerSpecsSf.objects.using('xactly_dev').filter(player_id=this_player_id)
                except Exception:
                    return -1

                baseline_rank_value = DRAFT_VALUE_BASELINE_SF
                critical_attribute_list = ['speed_rating', 'route_rating']

            elif this_player_primary_position == 'std':

                try:
                    player_stats_obj = PlayerSpecsStd.objects.using('xactly_dev').filter(player_id=this_player_id)
                except Exception:
                    return -1

                baseline_rank_value = DRAFT_VALUE_BASELINE_STD
                critical_attribute_list = ['agility_rating', 'tackle_rating']

            elif this_player_primary_position == 'sto':

                try:
                    player_stats_obj = PlayerSpecsSto.objects.using('xactly_dev').filter(player_id=this_player_id)
                except Exception:
                    return -1

                baseline_rank_value = DRAFT_VALUE_BASELINE_STO
                critical_attribute_list = ['speed_rating', 'elusiveness_rating']

            elif this_player_primary_position == 'te':

                try:
                    player_stats_obj = PlayerSpecsTe.objects.using('xactly_dev').filter(player_id=this_player_id)
                except Exception:
                    return -1

                baseline_rank_value = DRAFT_VALUE_BASELINE_TE
                critical_attribute_list = ['catching_rating', 'block_power_rating']

            elif this_player_primary_position == 'wr':

                try:
                    player_stats_obj = PlayerSpecsWr.objects.using('xactly_dev').filter(player_id=this_player_id)
                except Exception:
                    return -1

                baseline_rank_value = DRAFT_VALUE_BASELINE_WR
                critical_attribute_list = ['catching_rating', 'route_rating']

            #get career arc from player_stats_obj
            this_player_career_arc_dict_str = player_stats_obj[0].career_arc_dict

            this_player_career_arc_dict_str = this_player_career_arc_dict_str.replace("\'", "\"")
            this_player_career_arc_dict_list = json.loads(this_player_career_arc_dict_str)

            #get the dict in this_player_career_arc_dict_list corresponding to the value of this_season_year
            #keep in mind that I will have to subtract 1 from the value of this_season_year when used as an index

            this_player_career_arc_this_season_dict = this_player_career_arc_dict_list[this_season_year - 1]

            #compute roster player value
            attribute_sum = 0
            attribute_weight = 0.0

            for this_attribute_name, this_attribute_value in this_player_career_arc_this_season_dict.items():
                if this_attribute_name in critical_attribute_list:
                    attribute_weight = 1.25
                else:
                    attribute_weight = 1.0

                attribute_sum += attribute_weight * int(this_attribute_value)

            this_player_calculated_value = round(attribute_sum / len(this_player_career_arc_this_season_dict.values()), 3) + baseline_rank_value

            # create dict for this player
            this_player_info_dict = {'player_id': this_player_id, 'player_value': this_player_calculated_value}

            #initialize primary_position key in team_id_to_position_player_info_list_dict_dict
            if this_player_primary_position not in team_id_to_position_player_info_list_dict_dict[this_team_id]:
                team_id_to_position_player_info_list_dict_dict[this_team_id][this_player_primary_position] = [this_player_info_dict]
            else:
                team_id_to_position_player_info_list_dict_dict[this_team_id][this_player_primary_position].append(this_player_info_dict)

                #sort list of dicts by player_value in descending order
                team_id_to_position_player_info_list_dict_dict[this_team_id][this_player_primary_position] = sorted(team_id_to_position_player_info_list_dict_dict[this_team_id][this_player_primary_position], key=lambda x: x['player_value'], reverse=True)


    else:
        return -1

    # here, we can finally start the actual drafting process.
    overall_pick_number_to_player_id_dict = {}

    overall_pick_number = 0

    for round_num in range(1, NUMBER_OF_DRAFT_ROUNDS + 1):

        for round_pick_number, this_team_id in enumerate(team_id_draft_order_list, 1):

            overall_pick_number += 1
            overall_pick_number_to_player_id_dict[overall_pick_number] = -1

            #go through all players in draft
            for this_draft_player_idx, this_draft_player_obj in enumerate(draft_player_obj_list, 1):

                #we will not look through every player when drafting in the first 2 rounds
                if round_num == 1 and this_draft_player_idx == ROUND_1_PLAYER_SEARCH_LIMIT:
                    break

                if round_num == 2 and this_draft_player_idx == ROUND_2_PLAYER_SEARCH_LIMIT:
                    break

                #get draft player id and value
                this_draft_player_id = this_draft_player_obj.id

                if player_id_to_draft_availability[this_draft_player_id] == False:

                    # make the improvement score for this player_id = -9998, so that they can't be selected again by any team
                    team_id_to_player_improvement_score_dict_dict[this_team_id][this_draft_player_id] = -9998
                    continue

                this_draft_player_value = this_draft_player_obj.draft_value
                this_draft_player_primary_position = this_draft_player_obj.primary_position

                if this_draft_player_id not in team_id_to_player_improvement_score_dict_dict[this_team_id]:
                    team_id_to_player_improvement_score_dict_dict[this_team_id][this_draft_player_id] = -9999

                #we will not consider this player depending upon position and round, as indicated here:
                if round_num < 3 and this_draft_player_primary_position in ['fb','p','k','sto','std']:
                    continue

                this_team_position_player_list = team_id_to_position_player_info_list_dict_dict[this_team_id][this_draft_player_primary_position]

                #we only need the worst starter, as indicated by player_position_to_starter_count_dict
                this_team_worst_starter_dict = this_team_position_player_list[player_position_to_starter_count_dict[this_draft_player_primary_position] - 1]

                this_team_worst_starter_player_score = this_team_worst_starter_dict['player_value']
                this_team_draft_player_score = team_id_to_draft_player_score_dict_dict[this_team_id][this_draft_player_id]

                if team_id_to_player_improvement_score_dict_dict[this_team_id][this_draft_player_id] == -9999:
                    this_draft_player_improvement_score = this_team_draft_player_score - this_team_worst_starter_player_score
                    team_id_to_player_improvement_score_dict_dict[this_team_id][this_draft_player_id] = this_draft_player_improvement_score

            #we will look at the draft player with the highest improvement score and select them
            this_team_id_player_id_selected = sorted(team_id_to_player_improvement_score_dict_dict[this_team_id].items(), key=itemgetter(1), reverse=True)[0][0]

            #we need to update draft_player_obj_list to indicate that this player has already been selected
            player_id_to_draft_availability[this_team_id_player_id_selected] = False

            overall_pick_number_to_player_id_dict[overall_pick_number] = this_team_id_player_id_selected

            #we will need to perform an update on Player to make player_status = 0 for this player_id
            #we will need to insert a new row into PlayerTeam for this player_id
            #we will need to insert a new row into draft pick for this pick

    dffdfdfdfdf

















