# coding: utf-8

from jpartyfb.models import League, Season, TeamSeason, Game

import random
import copy

DEADLOCK_COUNT_LIMIT = 25

def get_opponents_times_played(num_divisions_per_conference, num_weeks_regular_season, num_teams_per_division):

    opponent_type_to_opponent_num_dict = {}

    if num_teams_per_division == 6 and num_divisions_per_conference == 2:

        if num_weeks_regular_season == 14:
            opponent_type_to_opponent_num_dict['same_division_twice'] = 1
            opponent_type_to_opponent_num_dict['same_division_once'] = 4
            opponent_type_to_opponent_num_dict['same_conference_twice'] = 0
            opponent_type_to_opponent_num_dict['same_conference_once'] = 4
            opponent_type_to_opponent_num_dict['different_conference_once'] = 4

        if num_weeks_regular_season == 15:
            opponent_type_to_opponent_num_dict['same_division_twice'] = 1
            opponent_type_to_opponent_num_dict['same_division_once'] = 4
            opponent_type_to_opponent_num_dict['same_conference_twice'] = 0
            opponent_type_to_opponent_num_dict['same_conference_once'] = 5
            opponent_type_to_opponent_num_dict['different_conference_once'] = 4

        if num_weeks_regular_season == 16:
            opponent_type_to_opponent_num_dict['same_division_twice'] = 3
            opponent_type_to_opponent_num_dict['same_division_once'] = 2
            opponent_type_to_opponent_num_dict['same_conference_twice'] = 1
            opponent_type_to_opponent_num_dict['same_conference_once'] = 2
            opponent_type_to_opponent_num_dict['different_conference_once'] = 4

        if num_weeks_regular_season == 17:
            opponent_type_to_opponent_num_dict['same_division_twice'] = 3
            opponent_type_to_opponent_num_dict['same_division_once'] = 2
            opponent_type_to_opponent_num_dict['same_conference_twice'] = 0
            opponent_type_to_opponent_num_dict['same_conference_once'] = 5
            opponent_type_to_opponent_num_dict['different_conference_once'] = 4

        if num_weeks_regular_season == 18:
            opponent_type_to_opponent_num_dict['same_division_twice'] = 3
            opponent_type_to_opponent_num_dict['same_division_once'] = 2
            opponent_type_to_opponent_num_dict['same_conference_twice'] = 0
            opponent_type_to_opponent_num_dict['same_conference_once'] = 5
            opponent_type_to_opponent_num_dict['different_conference_once'] = 5

    return opponent_type_to_opponent_num_dict


def get_team_opponents(opponent_type_str, conference_division_idx_to_team_id_list_dict, this_team_id, team_id_to_conference_division_idx_dict):

    this_team_conf_div_key_str = team_id_to_conference_division_idx_dict[this_team_id]
    this_team_key_parts_list = this_team_conf_div_key_str.split("_")

    this_team_conference_id = int(this_team_key_parts_list[0])
    this_team_division_id = int(this_team_key_parts_list[1])

    this_team_opponents_id_list = []

    for conf_div_key_str, team_id_list in conference_division_idx_to_team_id_list_dict.items():

        key_parts_list = conf_div_key_str.split("_")
        this_conference_id = int(key_parts_list[0])
        this_division_id = int(key_parts_list[1])

        if opponent_type_str == "intraconference":

            if this_team_conference_id == this_conference_id and this_team_division_id != this_division_id:
                this_team_opponents_id_list += team_id_list

        if opponent_type_str == "interconference":

            if this_team_conference_id != this_conference_id:
                this_team_opponents_id_list += team_id_list

    return this_team_opponents_id_list


def create_season_schedule(league_id, season_id):

    #first,we need to get the league settings
    try:
        league_obj = League.objects.using("xactly_dev").filter(id=league_id)
    except Exception:
        return -1

    num_weeks_regular_season = league_obj[0].num_weeks_regular_season
    num_teams_per_conference = league_obj[0].num_teams_per_conference
    num_divisions_per_conference = league_obj[0].num_divisions_per_conference
    neutral_site_setting = league_obj[0].neutral_site_setting

    num_teams_per_division = num_teams_per_conference / num_divisions_per_conference

    #get the teams associated with this league_id and season_id
    try:
        team_obj_list = TeamSeason.objects.using("xactly_dev").filter(league_id=league_id, season_id=season_id)
    except Exception:
        return -1

    conference_division_idx_to_team_id_list_dict = {}
    conference_index_to_team_id_list_dict = {}
    team_id_to_conference_division_idx_dict = {}

    team_id_to_all_opponents_type_dict_list_dict = {}

    for this_team_obj in team_obj_list:

        this_team_id = this_team_obj.id

        team_id_to_all_opponents_type_dict_list_dict[this_team_id] = {'same_division_twice':[], 'same_division_once':[], 'same_conference_once':[], 'same_conference_twice':[], 'different_conference_once':[]}

        this_conference_id = this_team_obj.team.conference.id
        this_division_id = this_team_obj.team.division.id

        if this_conference_id not in conference_index_to_team_id_list_dict:
            conference_index_to_team_id_list_dict[this_conference_id] = []

        conf_div_str_key = str(this_conference_id) + "_" + str(this_division_id)
        if conf_div_str_key not in conference_division_idx_to_team_id_list_dict:
            conference_division_idx_to_team_id_list_dict[conf_div_str_key] = []

        conference_division_idx_to_team_id_list_dict[conf_div_str_key].append(this_team_id)
        conference_index_to_team_id_list_dict[this_conference_id].append(this_team_id)

        team_id_to_conference_division_idx_dict[this_team_id] = conf_div_str_key

    #create a list of all team_ids in this league, ordered such that all ids of 1 conference appear before any of the ids from the other conference
    team_id_by_conference_list = conference_index_to_team_id_list_dict[1] + conference_index_to_team_id_list_dict[2]

    #get number of different opponents based on conf/div alignment and number of regular season games
    opponent_type_to_opponent_num_dict = get_opponents_times_played(num_divisions_per_conference, num_weeks_regular_season, num_teams_per_division)

    #we need this counter in order to assign opponents to teams across all divisions
    division_team_id = 0

    with open("logger_same_division.txt", 'w') as writefile:

        #this will determine whether all games have been scheduled
        all_games_scheduled = False

        while all_games_scheduled == False:

            division_team_id = 0
            deadlock_counter = 0

            #first, set opponent games for teams in the same division
            for this_team_obj in team_obj_list:

                division_team_id += 1

                if division_team_id > num_teams_per_division:
                    division_team_id = 1

                this_team_id = this_team_obj.id
                writefile.write("Current this_team_id: " + str(this_team_id) + "\n")
                this_team_conf_div_key_str = team_id_to_conference_division_idx_dict[this_team_id]
                writefile.write("Current conf_div_key: " + str(this_team_conf_div_key_str) + "\n")

                this_team_divisional_opponents_id_list = conference_division_idx_to_team_id_list_dict[this_team_conf_div_key_str]
                this_team_divisional_opponents_id_list_copy = copy.deepcopy(this_team_divisional_opponents_id_list)

                writefile.write("this_team_divisional_opponents_id_list_copy: " + str(this_team_divisional_opponents_id_list_copy) + "\n")

                #remove this_team_id from this_team_divisional_opponents_id_list
                this_team_divisional_opponents_id_list_copy = this_team_divisional_opponents_id_list_copy[division_team_id:]

                #we need to decide which of the teams the current team will play twice. This will be determined randomly
                #to some extent, but for the later teams in the division, they will not have a choice.
                #we need to create the pool of candidate division teams that this team can choose from

                writefile.write("this_team_id current twice opponents list: " + str(team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_division_twice']) + "\n")
                writefile.write("this_team_id current once opponents list: " + str(team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_division_once']) + "\n")

                candidate_team_id_list = list(set(this_team_divisional_opponents_id_list_copy) - set(team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_division_twice']))

                writefile.write("current candidate_team_id_list: " + str(candidate_team_id_list) + "\n")

                number_of_teams_to_select = opponent_type_to_opponent_num_dict['same_division_twice'] - len(team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_division_twice'])

                writefile.write("num_teams_2_select: " + str(number_of_teams_to_select) + "\n")

                #we want to randomly select opponents, but need to ensure that the selection fits within scheduling constraints
                this_selection_list_valid = False
                this_remaining_list_valid = False

                while this_selection_list_valid == False or this_remaining_list_valid == False:

                    if deadlock_counter == DEADLOCK_COUNT_LIMIT:
                        break

                    writefile.write("New Iteration through while loop...\n")

                    selected_team_id_list = random.sample(candidate_team_id_list, number_of_teams_to_select)

                    writefile.write("selected_team_id_list: " + str(selected_team_id_list) + '\n')

                    # the teams that weren't chosen will go into the "same_division_once" bucket for this team_id
                    remaining_team_id_list = list(set(candidate_team_id_list) - set(selected_team_id_list))

                    writefile.write("remaining_team_id_list: " + str(remaining_team_id_list) + '\n')

                    #if this_team_id has had all of their same division twice opponents already selected, then
                    #skip this step
                    if len(team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_division_twice']) < opponent_type_to_opponent_num_dict['same_division_twice']:

                        #we need to make sure that the teams selected can fit this_team_id into their schedule
                        for this_selected_id in selected_team_id_list:

                            if len(team_id_to_all_opponents_type_dict_list_dict[this_selected_id]['same_division_twice']) == opponent_type_to_opponent_num_dict['same_division_twice']:
                                writefile.write("invalid selected_team_id_list: offending value for: " + str(this_selected_id) + "\n")
                                this_selection_list_valid = False

                                deadlock_counter += 1
                                break

                        else:
                            writefile.write("valid selected_team_id_list!!\n")
                            this_selection_list_valid = True

                    else:
                        this_selection_list_valid = True

                    # if this_team_id has had all of their same division once opponents already selected, then
                    # skip this step
                    if len(team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_division_once']) < opponent_type_to_opponent_num_dict['same_division_once']:

                        for this_remaining_id in remaining_team_id_list:
                            if len(team_id_to_all_opponents_type_dict_list_dict[this_remaining_id]['same_division_once']) == opponent_type_to_opponent_num_dict['same_division_once']:
                                writefile.write("invalid remaining_team_id_list: offending value for: " + str(this_remaining_id) + "\n")
                                this_remaining_list_valid = False

                                deadlock_counter += 1
                                break
                        else:
                            writefile.write("valid remaining_team_id_list!!\n")
                            this_remaining_list_valid = True
                    else:
                        this_remaining_list_valid = True

                if deadlock_counter == DEADLOCK_COUNT_LIMIT:

                    writefile.write("We've hit the deadlock count limit: reset everything and start again\n")
                    #we will reset everything

                    team_id_list = list(team_id_to_conference_division_idx_dict.keys())

                    for this_team_id in team_id_list:
                        team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_division_twice'] = []
                        team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_division_once'] = []

                    break

                writefile.write("adding opponents to data structures...\n")
                writefile.write("*******************************************************\n")

                #add each team_id in selected_team_id_list into team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_division_twice']
                for this_selected_id in selected_team_id_list:
                    team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_division_twice'].append(this_selected_id)

                #add remaining team_id_list to team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_division_once']
                for this_remaining_id in remaining_team_id_list:
                    team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_division_once'].append(this_remaining_id)

                #finally, we have to add to the lists of the opponents of this_team_id
                for this_selected_id in selected_team_id_list:
                    team_id_to_all_opponents_type_dict_list_dict[this_selected_id]['same_division_twice'].append(this_team_id)

                for this_remaining_id in remaining_team_id_list:
                    team_id_to_all_opponents_type_dict_list_dict[this_remaining_id]['same_division_once'].append(this_team_id)

            if deadlock_counter < DEADLOCK_COUNT_LIMIT:
                all_games_scheduled = True


    #next, schedule intraconference games
    with open("logger_same_conference.txt", 'w') as writefile2:

        # this will determine whether all games have been scheduled
        all_games_scheduled = False

        while all_games_scheduled == False:

            conference_team_id = 0
            deadlock_counter = 0
            blow_it_up = False
            verify_count = 0

            # first, set opponent games for teams in the same division
            for this_team_id in team_id_by_conference_list:

                conference_team_id += 1

                writefile2.write("Current this_team_id: " + str(this_team_id) + "\n")
                this_team_conf_div_key_str = team_id_to_conference_division_idx_dict[this_team_id]
                writefile2.write("Current conf_div_key: " + str(this_team_conf_div_key_str) + "\n")

                this_team_opponents_id_list = get_team_opponents("intraconference", conference_division_idx_to_team_id_list_dict, this_team_id, team_id_to_conference_division_idx_dict)
                this_team_opponents_id_list_copy = copy.deepcopy(this_team_opponents_id_list)

                writefile2.write("this_team_opponents_id_list_copy: " + str(this_team_opponents_id_list_copy) + "\n")

                opponent_ids_to_remove = []

                # remove opponents that have filled their conference_once list
                for opponent_idx, this_opponent_id in enumerate(this_team_opponents_id_list_copy):

                    writefile2.write("Current value of this_opponent_id: " + str(this_opponent_id) + "\n")

                    if len(team_id_to_all_opponents_type_dict_list_dict[this_opponent_id]['same_conference_once']) == opponent_type_to_opponent_num_dict['same_conference_once']:
                        writefile2.write("about to remove " + str(this_opponent_id) + " from being considered a candidate team: " + "\n")
                        opponent_ids_to_remove.append(this_opponent_id)

                    else:
                        writefile2.write("team_id_to_all_opponents_type_dict_list_dict[" + str(this_opponent_id) + "]['same_conference_once']: " + str(team_id_to_all_opponents_type_dict_list_dict[this_opponent_id]['same_conference_once']) + "\n")

                for this_opponent_id_to_remove in opponent_ids_to_remove:
                    this_team_opponents_id_list_copy.remove(this_opponent_id_to_remove)

                writefile2.write("this_team_id current same conference once opponents list: " + str(team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_conference_once']) + "\n")

                number_of_teams_to_select_once = opponent_type_to_opponent_num_dict['same_conference_once'] - len(team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_conference_once'])

                if number_of_teams_to_select_once > 0:
                    candidate_team_id_list = list(set(this_team_opponents_id_list_copy) - set(team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_conference_once']))
                else:
                    candidate_team_id_list = []

                writefile2.write("current candidate_team_id_list: " + str(candidate_team_id_list) + "\n")

                number_of_teams_to_select_twice = opponent_type_to_opponent_num_dict['same_conference_twice'] - len(team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_conference_twice'])

                writefile2.write("num_teams_2_select_once: " + str(number_of_teams_to_select_once) + "\n")
                writefile2.write("num_teams_2_select_twice: " + str(number_of_teams_to_select_twice) + "\n")

                # we want to randomly select opponents, but need to ensure that the selection fits within scheduling constraints
                this_selection_once_list_valid = False
                this_selection_twice_list_valid = False

                while this_selection_once_list_valid == False or this_selection_twice_list_valid == False:

                    if deadlock_counter == DEADLOCK_COUNT_LIMIT:
                        break

                    writefile2.write("New Iteration through while loop...\n")

                    try:
                        selected_team_id_list = random.sample(candidate_team_id_list, number_of_teams_to_select_once)
                    except Exception:
                        # we may be in a deadlock situation
                        deadlock_counter += 1

                    writefile2.write("selected_team_id_list: " + str(selected_team_id_list) + '\n')

                    # if same_conference_twice > 0, then randomly choose teams
                    if opponent_type_to_opponent_num_dict['same_conference_twice'] > 0:

                        this_twice_team_opponents_id_list_copy = copy.deepcopy(this_team_opponents_id_list)

                        twice_opponent_ids_to_remove_list = []
                        writefile2.write("Checking same conference twice schedule constraints...\n")

                        #remove opponents that are no longer eligible to be on the conference twice list
                        for opponent_idx, this_opponent_id in enumerate(this_twice_team_opponents_id_list_copy):

                            writefile2.write("Current value of this_opponent_id: " + str(this_opponent_id) + "\n")

                            if len(team_id_to_all_opponents_type_dict_list_dict[this_opponent_id]['same_conference_twice']) == opponent_type_to_opponent_num_dict['same_conference_twice']:
                                writefile2.write("about to remove " + str(this_opponent_id) + " from being considered a candidate team: it has already been selected" + "\n")
                                twice_opponent_ids_to_remove_list.append(this_opponent_id)
                            elif this_opponent_id in selected_team_id_list:
                                writefile2.write("about to remove " + str(this_opponent_id) + " from being considered a candidate team - it is already in selected_team_id_list!\n")
                                twice_opponent_ids_to_remove_list.append(this_opponent_id)
                            else:
                                writefile2.write("team_id_to_all_opponents_type_dict_list_dict[" + str(this_opponent_id) + "]['same_conference_twice']: " + str(team_id_to_all_opponents_type_dict_list_dict[this_opponent_id]['same_conference_twice']) + "\n")

                        for this_opponent_id_to_remove in twice_opponent_ids_to_remove_list:
                            this_twice_team_opponents_id_list_copy.remove(this_opponent_id_to_remove)


                        #same_conference_twice_candidate_id_list = list(set(this_team_opponents_id_list_copy) - set(selected_team_id_list))
                        writefile2.write("same_conference_twice_candidate_id_list: " + str(this_twice_team_opponents_id_list_copy) + "\n")

                        try:
                            same_conference_twice_team_id_list = random.sample(this_twice_team_opponents_id_list_copy, number_of_teams_to_select_twice)
                        except Exception:
                            # we may be in a deadlock situation
                            writefile2.write("Not enough teams to select...deadlock_counter incrementing...\n")
                            deadlock_counter += 1
                            continue
                    else:
                        same_conference_twice_team_id_list = []

                    writefile2.write("same_conference_twice team_id selected: " + str(same_conference_twice_team_id_list) + '\n')

                    # if this_team_id has had all of their same conference once opponents already selected, then
                    # skip this step
                    if len(team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_conference_once']) < opponent_type_to_opponent_num_dict['same_conference_once']:

                        # we need to make sure that the teams selected can fit this_team_id into their schedule
                        for this_selected_id in selected_team_id_list:

                            if len(team_id_to_all_opponents_type_dict_list_dict[this_selected_id]['same_conference_once']) == opponent_type_to_opponent_num_dict['same_conference_once']:
                                writefile2.write("invalid selected_team_id_list: offending value for: " + str(this_selected_id) + "\n")
                                this_selection_once_list_valid = False

                                deadlock_counter += 1
                                continue

                        else:
                            writefile2.write("valid selected_team_id_list!!\n")
                            this_selection_once_list_valid = True

                    else:
                        this_selection_once_list_valid = True

                    # if this_team_id has had all of their same conference twice opponents already selected, then
                    # skip this step
                    if opponent_type_to_opponent_num_dict['same_conference_twice'] > 0:

                        # we need to make sure that the teams selected can fit this_team_id into their schedule
                        for this_selected_twice_id in same_conference_twice_team_id_list:

                            writefile2.write("team_id_to_all_opponents_type_dict_list_dict[" + str(this_selected_twice_id) + "]['same_conference_twice'] = " + str(team_id_to_all_opponents_type_dict_list_dict[this_selected_id]['same_conference_twice']) + "\n")

                            if len(team_id_to_all_opponents_type_dict_list_dict[this_selected_twice_id]['same_conference_twice']) == opponent_type_to_opponent_num_dict['same_conference_twice']:
                                 writefile2.write("invalid same_conference_twice_candidate_id_list: offending value for: " + str(this_selected_twice_id) + "\n")
                                 this_selection_twice_list_valid = False

                                 deadlock_counter += 1
                                 break

                        else:
                            writefile2.write("valid same_conference_twice_candidate_id_list!!\n")
                            this_selection_twice_list_valid = True

                    else:
                        this_selection_twice_list_valid = True

                if deadlock_counter == DEADLOCK_COUNT_LIMIT:

                    writefile2.write("We've hit the deadlock count limit: reset everything and start again\n")
                    # we will reset everything

                    team_id_list = list(team_id_to_conference_division_idx_dict.keys())

                    for this_team_id in team_id_list:
                        team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_conference_once'] = []
                        team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_conference_once'] = []
                        team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_conference_twice'] = []
                        team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_conference_twice'] = []
                    break

                writefile2.write("adding opponents to data structures...\n")
                writefile2.write("*******************************************************\n")

                # add each team_id in selected_team_id_list
                for this_selected_id in selected_team_id_list:
                    team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_conference_once'].append(this_selected_id)
                    team_id_to_all_opponents_type_dict_list_dict[this_selected_id]['same_conference_once'].append(this_team_id)

                # do the same for same_conference_twice opponents, if applicable
                if opponent_type_to_opponent_num_dict['same_conference_twice'] > 0:
                    for this_selected_twice_id in same_conference_twice_team_id_list:
                        team_id_to_all_opponents_type_dict_list_dict[this_team_id]['same_conference_twice'].append(this_selected_twice_id)
                        team_id_to_all_opponents_type_dict_list_dict[this_selected_twice_id]['same_conference_twice'].append(this_team_id)

                #do a check to see if team assignments are correct
                if conference_team_id == num_teams_per_conference:

                    verify_count += 1

                    # we'll need to take half of team_id_by_conference_list
                    if verify_count == 1:
                        team_ids_to_verify_list = team_id_by_conference_list[:num_teams_per_conference]
                    else:
                        team_ids_to_verify_list = team_id_by_conference_list[num_teams_per_conference:-1]

                    writefile2.write("Checking to see if conference's games were assigned correctly\n")
                    writefile2.write("this_team_opponents_id_list: " + str(team_ids_to_verify_list) + "\n")

                    # check to see if we have assigned the games correctly for a given conference
                    # if not, then break and run the while loop again
                    for one_opponent_id in team_ids_to_verify_list:

                        writefile2.write("This opponent_id is: " + str(one_opponent_id) + "\n")

                        if len(team_id_to_all_opponents_type_dict_list_dict[one_opponent_id]['same_conference_once']) != opponent_type_to_opponent_num_dict['same_conference_once'] or len(team_id_to_all_opponents_type_dict_list_dict[one_opponent_id]['same_conference_twice']) != opponent_type_to_opponent_num_dict['same_conference_twice']:

                            writefile2.write("We got it wrong...try again!\n")

                            # blow it up and try again
                            tid_list = list(team_id_to_conference_division_idx_dict.keys())

                            for this_tid in tid_list:
                                team_id_to_all_opponents_type_dict_list_dict[this_tid]['same_conference_once'] = []
                                team_id_to_all_opponents_type_dict_list_dict[this_tid]['same_conference_once'] = []
                                team_id_to_all_opponents_type_dict_list_dict[this_tid]['same_conference_twice'] = []
                                team_id_to_all_opponents_type_dict_list_dict[this_tid]['same_conference_twice'] = []

                            blow_it_up = True
                            break

                    if blow_it_up == True:
                        break

                    writefile2.write("All teams assigned correctly!\n")

                    # if we get here, then continue normally
                    conference_team_id = 1

            if deadlock_counter < DEADLOCK_COUNT_LIMIT and blow_it_up == False:
                all_games_scheduled = True


    #next, we need to assign interconference opponents
    with open("logger_different_conference.txt", 'w') as writefile2:

        # this will determine whether all games have been scheduled
        all_games_scheduled = False

        while all_games_scheduled == False:

            conference_team_id = 0
            deadlock_counter = 0
            blow_it_up = False

            #first, set opponent games for teams in the same division
            for this_team_id in team_id_by_conference_list:

                conference_team_id += 1

                if conference_team_id > num_teams_per_conference:

                    writefile2.write("Checking to see if conference's opponents were assigned correctly\n")

                    writefile2.write("this_team_opponents_id_list: " + str(this_team_opponents_id_list) + "\n")

                    #check to see if we have assigned the games correctly for a given conference
                    #if not, then break and run the while loop again
                    for one_opponent_id in this_team_opponents_id_list:

                        writefile2.write("This opponent_id is: " + str(one_opponent_id) + "\n")

                        if len(team_id_to_all_opponents_type_dict_list_dict[one_opponent_id]['different_conference_once']) != opponent_type_to_opponent_num_dict['different_conference_once']:

                            writefile2.write("We got it wrong...try again!")

                            #blow it up and try again
                            tid_list = list(team_id_to_conference_division_idx_dict.keys())

                            for this_tid in tid_list:
                                team_id_to_all_opponents_type_dict_list_dict[this_tid]['different_conference_once'] = []
                                team_id_to_all_opponents_type_dict_list_dict[this_tid]['different_conference_once'] = []

                            blow_it_up = True
                            break

                    if blow_it_up == True:
                        break

                    writefile2.write("All teams assigned correctly!\n")

                    #if we get here, then continue normally
                    conference_team_id = 1

                writefile2.write("Current this_team_id: " + str(this_team_id) + "\n")
                this_team_conf_div_key_str = team_id_to_conference_division_idx_dict[this_team_id]
                writefile2.write("Current conf_div_key: " + str(this_team_conf_div_key_str) + "\n")

                #in order to create this_team_interconference_opponents_id_list, we need to get all team_id lists
                #from the other conference

                this_team_opponents_id_list = get_team_opponents("interconference", conference_division_idx_to_team_id_list_dict, this_team_id, team_id_to_conference_division_idx_dict)
                this_team_opponents_id_list_copy = copy.deepcopy(this_team_opponents_id_list)

                writefile2.write("this_team_opponents_id_list_copy: " + str(this_team_opponents_id_list_copy) + "\n")

                opponent_ids_to_remove = []

                #remove opponents that have filled their conference_once list
                for opponent_idx, this_opponent_id in enumerate(this_team_opponents_id_list_copy):

                    writefile2.write("Current value of this_opponent_id: " + str(this_opponent_id) + "\n")

                    if len(team_id_to_all_opponents_type_dict_list_dict[this_opponent_id]['different_conference_once']) == opponent_type_to_opponent_num_dict['different_conference_once']:
                        writefile2.write("about to remove " +  str(this_opponent_id) + " from being considered a candidate team: " + "\n")
                        opponent_ids_to_remove.append(this_opponent_id)

                    else:
                        writefile2.write("team_id_to_all_opponents_type_dict_list_dict[" + str(this_opponent_id) + "]['different_conference_once']: " + str(team_id_to_all_opponents_type_dict_list_dict[this_opponent_id]['different_conference_once']) + "\n")

                for this_opponent_id_to_remove in opponent_ids_to_remove:
                    this_team_opponents_id_list_copy.remove(this_opponent_id_to_remove)

                writefile2.write("this_team_id current different conference once opponents list: " + str(team_id_to_all_opponents_type_dict_list_dict[this_team_id]['different_conference_once']) + "\n")

                number_of_teams_to_select_once = opponent_type_to_opponent_num_dict['different_conference_once'] - len(team_id_to_all_opponents_type_dict_list_dict[this_team_id]['different_conference_once'])

                if number_of_teams_to_select_once > 0:
                    candidate_team_id_list = list(set(this_team_opponents_id_list_copy) - set(team_id_to_all_opponents_type_dict_list_dict[this_team_id]['different_conference_once']))
                else:
                    candidate_team_id_list = []

                writefile2.write("current candidate_team_id_list: " + str(candidate_team_id_list) + "\n")
                writefile2.write("num_teams_2_select_once: " + str(number_of_teams_to_select_once) + "\n")

                # we want to randomly select opponents, but need to ensure that the selection fits within scheduling constraints
                this_selection_once_list_valid = False
                this_selection_twice_list_valid = False

                while this_selection_once_list_valid == False:

                    if deadlock_counter == DEADLOCK_COUNT_LIMIT:
                        break

                    writefile2.write("New Iteration through while loop...\n")

                    try:
                        selected_team_id_list = random.sample(candidate_team_id_list, number_of_teams_to_select_once)
                    except Exception:
                        #we may be in a deadlock situation
                        deadlock_counter += 1


                    writefile2.write("selected_team_id_list: " + str(selected_team_id_list) + '\n')

                    # if this_team_id has had all of their same conference once opponents already selected, then
                    # skip this step
                    if len(team_id_to_all_opponents_type_dict_list_dict[this_team_id]['different_conference_once']) < opponent_type_to_opponent_num_dict['different_conference_once']:

                        # we need to make sure that the teams selected can fit this_team_id into their schedule
                        for this_selected_id in selected_team_id_list:

                            if len(team_id_to_all_opponents_type_dict_list_dict[this_selected_id]['different_conference_once']) == opponent_type_to_opponent_num_dict['different_conference_once']:
                                writefile2.write("invalid selected_team_id_list: offending value for: " + str(this_selected_id) + "\n")
                                this_selection_once_list_valid = False

                                deadlock_counter += 1
                                continue

                        else:
                            writefile2.write("valid selected_team_id_list!!\n")
                            this_selection_once_list_valid = True

                    else:
                        this_selection_once_list_valid = True

                if deadlock_counter == DEADLOCK_COUNT_LIMIT:

                    writefile2.write("We've hit the deadlock count limit: reset everything and start again\n")
                    # we will reset everything

                    team_id_list = list(team_id_to_conference_division_idx_dict.keys())

                    for this_team_id in team_id_list:
                        team_id_to_all_opponents_type_dict_list_dict[this_team_id]['different_conference_once'] = []
                        team_id_to_all_opponents_type_dict_list_dict[this_team_id]['different_conference_once'] = []

                    break

                writefile2.write("adding opponents to data structures...\n")
                writefile2.write("*******************************************************\n")

                # add each team_id in selected_team_id_list
                for this_selected_id in selected_team_id_list:
                    team_id_to_all_opponents_type_dict_list_dict[this_team_id]['different_conference_once'].append(this_selected_id)
                    team_id_to_all_opponents_type_dict_list_dict[this_selected_id]['different_conference_once'].append(this_team_id)


            if deadlock_counter < DEADLOCK_COUNT_LIMIT and blow_it_up == False:
                all_games_scheduled = True


    endyyyyy
    return 1
