from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, HttpResponseRedirect
from django.core.servers.basehttp import FileWrapper
from django.views.static import serve
from django.views.decorators.csrf import csrf_exempt

import datetime
import os
import re
import pandas as pd
import time
import json
import random
import names

from jpartyfb.forms import JPartyFBInputForm, CreateLeagueForm1
from jpartyfb.models import *

from PlayerCreation import PlayerCreation
from PlayerCreation import create_player_career_arc

def build_choose_teams_html(number_of_divisions_select, number_of_teams_conf_select, number_of_teams_per_division):

    division_num_to_team_list_dict = {}

    for i in range(1, number_of_divisions_select * 2 + 1):
        division_num_to_team_list_dict[i] = []

    #if user wants 28, 30 or 32 teams, then we will need to provide dummy teams, since we only have 24 teams
    #by default
    if number_of_teams_conf_select == 14:
        #add on teams to last division
        division_num_to_team_list_dict[number_of_divisions_select * 2].append(["Add Team Name"] * 4)
        division_num_to_team_list_dict[number_of_divisions_select * 2] = [item for sublist in division_num_to_team_list_dict[number_of_divisions_select * 2] for item in sublist]

    if number_of_teams_conf_select == 15:
        #add 6 new teams to last division
        division_num_to_team_list_dict[number_of_divisions_select * 2].append(["Add Team Name"] * 6)
        division_num_to_team_list_dict[number_of_divisions_select * 2] = [item for sublist in division_num_to_team_list_dict[number_of_divisions_select * 2] for item in sublist]

    if number_of_teams_conf_select == 16:

        if number_of_divisions_select == 2:
            division_num_to_team_list_dict[number_of_divisions_select * 2].append(["Add Team Name"] * 8)
            division_num_to_team_list_dict[number_of_divisions_select * 2] = [item for sublist in division_num_to_team_list_dict[number_of_divisions_select * 2] for item in sublist]

        if number_of_divisions_select == 4:
            division_num_to_team_list_dict[number_of_divisions_select * 2 - 1].append(["Add Team Name"] * 4)
            division_num_to_team_list_dict[number_of_divisions_select * 2].append(["Add Team Name"] * 4)
            division_num_to_team_list_dict[number_of_divisions_select * 2 - 1] = [item for sublist in division_num_to_team_list_dict[number_of_divisions_select * 2 - 1] for item in sublist]
            division_num_to_team_list_dict[number_of_divisions_select * 2] = [item for sublist in division_num_to_team_list_dict[number_of_divisions_select * 2] for item in sublist]


    division_counter = 1
    city_nickname_to_city_id_dict = {}

    for this_default_team in DefaultTeams.objects.using("xactly_dev").filter(id__lte=(number_of_teams_conf_select * 2)).order_by("id"):
        this_default_team_nickname = this_default_team.nickname
        this_default_team_city_name = this_default_team.city.city_name
        this_default_team_city_id = this_default_team.city.city_id

        city_nickname_to_city_id_dict[this_default_team_nickname] = this_default_team_city_id

        division_num_to_team_list_dict[division_counter].append(this_default_team_city_name + " " + this_default_team_nickname)

        if len(division_num_to_team_list_dict[division_counter]) == number_of_teams_per_division:
            division_counter += 1

    conf_division_name_list = []

    for i in range(1, number_of_divisions_select + 1):
        conf_division_name_list.append("Division " + str(i))

    # create table html for show_teams.html here - it's too complex for django templating language
    team_html_str = ""

    color_to_rgb_list_dict = {'blue':['#CCE5FF','#99CCFF'], 'red':['#FFCCCC','#FFAAAA']}

    for conf_division_idx, conf_division_name in enumerate(conf_division_name_list, 1):
        team_html_str += "<table cellpadding='5' width='100%' border='1'><tr>"

        # print out division header html - first easter division
        team_html_str += "<td width='50%' align='center' style='background-color: blue;' id='td_division_eastern_" + str(conf_division_idx) + "' class='td_division'>"
        team_html_str += "<input type='text' id='Eastern_division_" + str(
            conf_division_idx) + "' name='eastern_division_" + str(
            conf_division_idx) + "' class='division' maxlength='35' value='" + "Eastern " + conf_division_name + "' style='width: 220px; border: none; background: transparent; text-align:center; font-weight: bold; color: white;' />"
        team_html_str += "</td>"

        # now western division
        team_html_str += "<td width='50%' align='center' style='background-color: red;' id='td_division_western_" + str(conf_division_idx) + "' class='td_division'>"
        team_html_str += "<input type='text' id='Western_division_" + str(
            conf_division_idx) + "' name='western_division_" + str(
            conf_division_idx) + "' class='division' maxlength='35' value='" + "Western " + conf_division_name + "' style='width: 220px; border: none; background: transparent; text-align:center; font-weight: bold; color: white;' />"
        team_html_str += "</td>"

        # close division html row
        team_html_str += "</tr>"

        # open team html row - each row is a conference division of teams
        color_key_str = ""
        conference_str = ""

        for actual_division_number, division_team_list in division_num_to_team_list_dict.items():

            if actual_division_number == conf_division_idx or actual_division_number == conf_division_idx + number_of_divisions_select:

                if actual_division_number < conf_division_idx * 2:
                    team_html_str += "<tr>"
                    color_list = color_to_rgb_list_dict["blue"]
                    conference_str = "Eastern"
                else:
                    color_list = color_to_rgb_list_dict["red"]
                    conference_str = "Western"

                team_html_str += "<td><table align='center' style='background-color: white;' width='100%'>"
                for this_team_div_idx, this_team_name in enumerate(division_team_list, 1):

                    if this_team_div_idx % 2 == 1:
                        this_team_row_color = color_list[0]
                    else:
                        this_team_row_color = color_list[1]

                    team_html_str += "<tr style='background-color: " + this_team_row_color + ";'>"

                    team_html_str += "<td width='50%' align='center' id='td_team_" + str(this_team_div_idx) + "_" + conference_str + "_division_" + str(conf_division_idx) + "' class='td_team'>"
                    team_html_str += "<input type='text' id='" + conference_str + "_division_" + str(conf_division_idx) + "_team_" + str(this_team_div_idx) + "' name='" + conference_str + "_division_" + str(conf_division_idx) + "_team_" + str(this_team_div_idx) + "' class='team' maxlength='35' value='" + this_team_name + "' style='width: 220px; border: none; background: transparent; text-align:center; font-weight: bold;' />"
                    team_html_str += "</td></tr>"

                team_html_str += "</table></td>"

                if conf_division_idx * 2 == actual_division_number:
                    team_html_str += "</tr>"

    team_html_str += "</table>"

    return team_html_str, city_nickname_to_city_id_dict


def initialize_spec_db_table_ids(player_position_list):

    player_position_to_db_id_dict = {}

    for this_position in player_position_list:
        player_position_to_db_id_dict[this_position] = -1

    # get initial db table ids for all position spec db tables
    try:
        player_specs_dl_id = int(
            PlayerSpecsDl.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_dl_id = 1

    player_position_to_db_id_dict['dl'] = player_specs_dl_id

    try:
        player_specs_cb_id = int(
            PlayerSpecsCb.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_cb_id = 1

    player_position_to_db_id_dict['cb'] = player_specs_cb_id

    try:
        player_specs_fb_id = int(
            PlayerSpecsFb.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_fb_id = 1

    player_position_to_db_id_dict['fb'] = player_specs_fb_id

    try:
        player_specs_k_id = int(
            PlayerSpecsK.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_k_id = 1

    player_position_to_db_id_dict['k'] = player_specs_k_id

    try:
        player_specs_lb_id = int(
            PlayerSpecsLb.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_lb_id = 1

    player_position_to_db_id_dict['lb'] = player_specs_lb_id

    try:
        player_specs_ol_id = int(
            PlayerSpecsOl.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_ol_id = 1

    player_position_to_db_id_dict['ol'] = player_specs_ol_id

    try:
        player_specs_p_id = int(
            PlayerSpecsP.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_p_id = 1

    player_position_to_db_id_dict['p'] = player_specs_p_id

    try:
        player_specs_qb_id = int(
            PlayerSpecsQb.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_qb_id = 1

    player_position_to_db_id_dict['qb'] = player_specs_qb_id

    try:
        player_specs_rb_id = int(
            PlayerSpecsRb.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_rb_id = 1

    player_position_to_db_id_dict['rb'] = player_specs_rb_id

    try:
        player_specs_sf_id = int(
            PlayerSpecsSf.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_sf_id = 1

    player_position_to_db_id_dict['sf'] = player_specs_sf_id

    try:
        player_specs_std_id = int(
            PlayerSpecsStd.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_std_id = 1

    player_position_to_db_id_dict['std'] = player_specs_std_id

    try:
        player_specs_sto_id = int(
            PlayerSpecsSto.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_sto_id = 1

    player_position_to_db_id_dict['sto'] = player_specs_sto_id

    try:
        player_specs_te_id = int(
            PlayerSpecsTe.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_te_id = 1

    player_position_to_db_id_dict['te'] = player_specs_te_id

    try:
        player_specs_wr_id = int(
            PlayerSpecsWr.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_wr_id = 1

    player_position_to_db_id_dict['wr'] = player_specs_wr_id

    return player_position_to_db_id_dict

@ensure_csrf_cookie
def index(request):

    context = {}

    welcome_message = "Welcome to JParty Football!"
    form = JPartyFBInputForm()
    
    context['form'] = form
    context['welcome_message'] = welcome_message
    return render(request, 'jpartyfb/index.html', context)


@ensure_csrf_cookie
def play_football(request):
    context = {}

    welcome_message = "Play Football!"
    context['welcome_message'] = welcome_message

    return render(request, 'jpartyfb/play_football.html', context)

@ensure_csrf_cookie
def manage_leagues(request):
    context = {}

    welcome_message = "Manage Leagues"
    context['welcome_message'] = welcome_message

    return render(request, 'jpartyfb/manage_leagues.html', context)

@ensure_csrf_cookie
def view_stats(request):
    context = {}

    welcome_message = "View Stats"
    context['welcome_message'] = welcome_message

    return render(request, 'jpartyfb/view_stats.html', context)

@ensure_csrf_cookie
def create_new_league(request):
    context = {}

    welcome_message = "Create New League"
    form = CreateLeagueForm1()

    context['form'] = form
    context['welcome_message'] = welcome_message

    return render(request, 'jpartyfb/create_new_league.html', context)

@ensure_csrf_cookie
def start_new_season(request):
    context = {}

    welcome_message = "Start New Season"
    context['welcome_message'] = welcome_message

    return render(request, 'jpartyfb/start_new_season.html', context)

@ensure_csrf_cookie
def edit_league_settings(request):
    context = {}

    welcome_message = "Edit League Settings"
    context['welcome_message'] = welcome_message

    return render(request, 'jpartyfb/edit_league_settings.html', context)

@csrf_exempt
def process_create_league_form_1(request):

    league_name = request.POST['league_name']

    #extract form information and pass it into the choose_teams page
    try:
        injury_checkbox = request.POST['injury_checkbox']
    except Exception:
        injury_checkbox = 'off'

    try:
        weather_checkbox = request.POST['weather_checkbox']
    except Exception:
        weather_checkbox = 'off'

    try:
        female_checkbox = request.POST['female_checkbox']
    except Exception:
        female_checkbox = 'off'

    number_of_playoff_teams_select = int(request.POST['number_of_playoff_teams_select'])
    number_of_weeks_select = int(request.POST['number_of_weeks_select'])
    number_of_teams_conf_select = int(request.POST['number_of_teams_conf_select'])
    number_of_divisions_select = int(request.POST['number_of_divisions_select'])

    number_of_teams_per_division = number_of_teams_conf_select / number_of_divisions_select

    team_html_str, city_nickname_to_city_id_dict = build_choose_teams_html(number_of_divisions_select, number_of_teams_conf_select, number_of_teams_per_division)

    context = {}

    welcome_message = "Choose Your Teams"
    context['league_name'] = league_name
    context['injury_mode'] = injury_checkbox
    context['weather_mode'] = weather_checkbox
    context['female_mode'] = female_checkbox
    context['welcome_message'] = welcome_message
    context['number_of_playoff_teams'] = number_of_playoff_teams_select
    context['number_of_weeks'] = number_of_weeks_select
    context['number_of_teams_conf'] = number_of_teams_conf_select
    context['number_of_divisions_conf'] = number_of_divisions_select
    context['number_of_teams_per_division'] = number_of_teams_per_division
    context['city_nickname_to_city_id_dict'] = city_nickname_to_city_id_dict
    context['team_html_str'] = team_html_str

    return render(request, 'jpartyfb/choose_teams.html', context)


@csrf_exempt
def process_create_league_form_final(request):

    #extract form information and pass it into the choose_teams page
    league_name = request.POST['league_name_hidden']
    injury_setting = request.POST['injury_hidden']
    weather_setting = request.POST['weather_hidden']
    female_setting = request.POST['female_hidden']
    number_of_weeks_setting = request.POST['number_of_weeks_hidden']
    number_of_playoff_teams_setting = request.POST['number_of_playoff_teams_hidden']
    number_of_teams_conf_setting = request.POST['number_of_teams_conf_hidden']
    number_of_divisions_conf_setting = request.POST['number_of_divisions_conf_hidden']

    conference_name_list_str = request.POST['conference_name_list']
    conference_name_list = json.loads(conference_name_list_str)

    division_name_list_str = request.POST['division_name_list']
    division_name_list = json.loads(division_name_list_str)

    team_name_list_str = request.POST['team_name_list']
    team_name_list = json.loads(team_name_list_str)

    division_to_conference_dict_str = request.POST['division_to_conference_dict']
    division_to_conference_dict = json.loads(division_to_conference_dict_str)

    team_to_division_dict_str = request.POST['team_to_division_dict']
    team_to_division_dict = json.loads(team_to_division_dict_str)

    team_to_conference_dict_str = request.POST['team_to_conference_dict']
    team_to_conference_dict = json.loads(team_to_conference_dict_str)

    city_nickname_to_city_id_dict_str = request.POST['city_nickname_to_city_id_dict']
    city_nickname_to_city_id_dict = json.loads(city_nickname_to_city_id_dict_str)

    #create league abbrevation. If the league has >= 2 words, then use the first letter of each word
    #if it has only one word, then use the first 3 letters of that word

    league_name_parts_list = league_name.split()
    league_name_abbrev_letter_list = []
    league_name_abbrev_str = ""

    if len(league_name_parts_list) >= 2:

        for one_part in league_name_parts_list:
            league_name_abbrev_letter_list.append(one_part[0])

        league_name_abbrev_str = ''.join(league_name_abbrev_letter_list)

    else:

        league_name_abbrev_str = league_name[:3]

    league_name_abbrev_str =  league_name_abbrev_str.upper()

    #start inserting form data into database tables
    #get latest League row
    try:
        league_id = int(
            League.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        league_id = 1

    try:
        League.objects.using("xactly_dev").create(id=league_id, name=league_name, abbreviation=league_name_abbrev_str, weather_setting=weather_setting, injury_setting=injury_setting, female_setting=female_setting)
    except Exception:
        return HttpResponse(-1)

    #next, insert conference rows for this league
    try:
        conference_id = int(
            Conference.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        conference_id = 1

    #we need this for proper insertions into the Division table
    conference_name_to_id_dict = {}

    for conference_idx, this_conference_name in enumerate(conference_name_list):

        conference_name_to_id_dict[this_conference_name] = conference_id

        try:
            Conference.objects.using("xactly_dev").create(id=conference_id, conference_name=this_conference_name,
                                                          league_id=league_id)

        except Exception:
            return HttpResponse(-2)

        conference_id += 1

    #now insert division rows for this league
    try:
        division_id = int(
            Division.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        division_id = 1

    #we need this for proper insertions into the Team table
    division_name_to_id_dict = {}

    for division_idx, this_division_name in enumerate(division_name_list):

        this_conference_name = division_to_conference_dict[this_division_name]
        this_conference_id = conference_name_to_id_dict[this_conference_name]
        division_name_to_id_dict[this_division_name] = division_id

        try:
            Division.objects.using("xactly_dev").create(id=division_id, division_name=this_division_name,
                                                          conference_id=this_conference_id, first_season_id=-1, league_id=league_id)

        except Exception:
            return HttpResponse(-3)

        division_id += 1

    # next insert team rows for this league
    try:
        team_id = int(
            Team.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        team_id = 1

    #also insert team_city rows for this league
    try:
        team_city_id = int(
            TeamCity.objects.using('xactly_dev').latest('team_city_id').team_city_id) + 1
    except Exception:
        team_city_id = 1

    team_id_to_city_stadium_id_list_dict = {}

    #we will need this for player table insertions below
    team_name_to_team_id_dict = {}

    player_name_to_combined_attr_score_dict = {}

    for team_idx, this_team_name in enumerate(team_name_list):

        team_name_to_team_id_dict[this_team_name] = team_id

        this_team_conference_name = team_to_conference_dict[this_team_name]
        this_team_conference_id = conference_name_to_id_dict[this_team_conference_name]
        this_team_division_name = team_to_division_dict[this_team_name]
        this_team_division_id = division_name_to_id_dict[this_team_division_name]

        this_team_name_parts_list = this_team_name.split()

        if this_team_name_parts_list[0] == "Dallas":
            this_team_nickname = this_team_name_parts_list[1] + " " + this_team_name_parts_list[2]
        else:
            this_team_nickname = this_team_name_parts_list[-1]

        this_team_city_id = city_nickname_to_city_id_dict[this_team_nickname]

        stadium_row = Stadium.objects.using("xactly_dev").get(city_id=this_team_city_id)
        this_team_stadium_id = stadium_row.stadium_id

        team_id_to_city_stadium_id_list_dict[team_id] = [this_team_city_id, this_team_stadium_id]

        try:
            Team.objects.using("xactly_dev").create(id=team_id, nickname=this_team_nickname,
                                                    first_season_id=-1, current_season_wins=0, current_season_losses=0,
                                                    stadium_id=this_team_stadium_id, conference_id=this_team_conference_id,
                                                    division_id=this_team_division_id,league_id=league_id)
        except Exception:
            return HttpResponse(-4)

        try:
            TeamCity.objects.using("xactly_dev").create(team_city_id=team_city_id, team_id=team_id,
                                                    city_id=this_team_city_id,
                                                    first_season_id=-1,stadium_id=this_team_stadium_id)
        except Exception:
            return HttpResponse(-5)

        team_id += 1
        team_city_id += 1

    # get latest id value of player
    try:
        player_id = int(Player.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_id = 1

    try:
        player_team_id = int(PlayerTeam.objects.using('xactly_dev').latest('player_team_id').player_team_id) + 1
    except Exception:
        player_team_id = 1

    player_name_to_info_dict_dict = {}

    player_position_to_db_id_dict = initialize_spec_db_table_ids(PlayerCreation.player_position_list)

    #create players and insert them into player DBs for each team in the league
    for this_team_name in team_name_list:

        this_team_id = team_name_to_team_id_dict[this_team_name]
        team_numbers_used = set()

        for player_position in PlayerCreation.roster_position_count_list:

            player_name_uniqueness_verified = False
            player_number_uniqueness_verified = False

            # age is dependent on the player_position
            player_age = -1

            if player_position in ['p', 'k']:
                player_age = round(float(PlayerCreation.pk_age_norm_dist_obj.rvs()))
            elif player_position == 'rb':
                player_age = round(float(PlayerCreation.rb_age_norm_dist_obj.rvs()))
            else:
                player_age = round(float(PlayerCreation.otherpos_age_norm_dist_obj.rvs()))

            # secondary position will be chosen at random
            secondary_position_list = [this_position for this_position in PlayerCreation.player_position_list if
                                       this_position != player_position]

            secondary_position_random_value = random.randint(0, len(secondary_position_list) - 1)
            secondary_position = secondary_position_list[secondary_position_random_value]

            # assign number based on position

            while player_number_uniqueness_verified == False:

                this_position_number_bounds_list = PlayerCreation.position_to_number_bounds_list_dict[player_position]
                player_number = random.randint(this_position_number_bounds_list[0],
                                               this_position_number_bounds_list[1])

                if player_number not in team_numbers_used:
                    team_numbers_used.add(player_number)
                    player_number_uniqueness_verified = True

            # height in inches is determined via a normal dist

            height_feet = -1
            height_inches = -1

            height_feet_random_value = random.randint(0, 9)

            if height_feet_random_value <= 7 or player_position in ['ol', 'dl']:
                height_feet = 6
                height_inches = round(float(PlayerCreation.six_feet_tall_inches_norm_dist_obj.rvs()))
            else:
                height_feet = 5
                height_inches = round(float(PlayerCreation.five_feet_tall_inches_norm_dist_obj.rvs()))

            # weight in lbs is position dependent - ols and dls have one dist, everyone else has another
            # it is also height dependent - the taller the player, the more the player is likely to weigh

            if height_feet == 5 and height_inches <= 8 and player_position in ['dl', 'ol']:
                weight_lbs = round(PlayerCreation.low_5_ft_lb_weight_dist.rvs())
            elif height_feet == 5 and height_inches <= 8 and player_position not in ['dl', 'ol']:
                weight_lbs = round(PlayerCreation.low_5_ft_nlb_weight_dist.rvs())
            elif height_feet == 5 and height_inches > 8 and player_position in ['dl', 'ol']:
                weight_lbs = round(PlayerCreation.high_5_ft_lb_weight_dist.rvs())
            elif height_feet == 5 and height_inches > 8 and player_position not in ['dl', 'ol']:
                weight_lbs = round(PlayerCreation.high_5_ft_nlb_weight_dist.rvs())
            elif height_feet == 6 and height_inches <= 6 and player_position in ['dl', 'ol']:
                weight_lbs = round(PlayerCreation.low_6_ft_lb_weight_dist.rvs())
            elif height_feet == 6 and height_inches <= 6 and player_position not in ['dl', 'ol']:
                weight_lbs = round(PlayerCreation.low_6_ft_nlb_weight_dist.rvs())
            elif height_feet == 6 and height_inches > 6 and player_position in ['dl', 'ol']:
                weight_lbs = round(PlayerCreation.high_6_ft_lb_weight_dist.rvs())
            elif height_feet == 6 and height_inches > 6 and player_position not in ['dl', 'ol']:
                weight_lbs = round(PlayerCreation.high_6_ft_nlb_weight_dist.rvs())

            #while player_name_uniqueness_verified == False:

            gender_value = random.randint(0, 1)

            if gender_value == 0:
                given_gender = "male"
            else:
                given_gender = "female"

            # let's say that 1 out of every 50 players uses a middle initial
            using_middle_initial_value = random.randint(0, 49)

            if using_middle_initial_value == 25:
                middle_initial_letter_idx = random.randint(0, 25)
                middle_initial = chr(ord('A') + middle_initial_letter_idx) + ". "
            else:
                middle_initial = ""

            player_name = names.get_full_name(gender=given_gender)

            if middle_initial != "":
                player_name_parts = player_name.split()
                player_name = player_name_parts[0] + ' ' + middle_initial + player_name_parts[1]

            if player_name not in list(player_name_to_info_dict_dict.keys()):
                player_name_uniqueness_verified = True

            player_name_parts = player_name.split()
            player_first_name = player_name_parts[0]
            player_last_name = player_name_parts[-1]

            # alma mater
            school_random_value = random.randint(0, 99)
            fbs_random_value = random.randint(0, len(PlayerCreation.fbs_school_list) - 1)
            fcs_random_value = random.randint(0, len(PlayerCreation.fcs_school_list) - 1)
            d2_random_value = random.randint(0, len(PlayerCreation.d2_school_list) - 1)
            d3_random_value = random.randint(0, len(PlayerCreation.d3_school_list) - 1)

            school_name = ""
            school_value = -1

            if school_value <= 74:
                school_name = PlayerCreation.fbs_school_list[fbs_random_value]
            elif school_value > 74 and school_value <= 92:
                school_name = PlayerCreation.fcs_school_list[fcs_random_value]
            elif school_value > 92 and school_value < 99:
                school_name = PlayerCreation.d2_school_list[d2_random_value]
            else:
                school_name = PlayerCreation.d3_school_list[d3_random_value]

            this_player_attribute_list = []
            this_player_attribute_list = PlayerCreation.position_to_player_attribute_list_dict[player_position]
            this_player_attribute_value_dict = {}

            player_name_to_combined_attr_score_dict[player_name] = -1

            for this_attribute in this_player_attribute_list:

                # check for customized distributions
                if player_position == "fb" and this_attribute in ['speed_rating', 'elusiveness_rating']:
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.fb_speed_elusiveness_norm_dist_obj.rvs()), 2)
                elif player_position == "fb" and this_attribute == 'strength_rating':
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.fb_strength_norm_dist_obj.rvs()), 2)
                elif player_position == "te" and this_attribute == 'speed_rating':
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.te_speed_norm_dist_obj.rvs()), 2)
                elif player_position == "te" and this_attribute in ['strength_rating', 'block_power_rating']:
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.te_strength_bpwr_dist_obj.rvs()), 2)
                elif player_position == "wr" and this_attribute == "speed_rating":
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.wr_speed_norm_dist_obj.rvs()), 2)
                elif player_position == "sf" and this_attribute == "speed_rating":
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.sf_speed_norm_dist_obj.rvs()), 2)
                elif player_position == "sf" and this_attribute == "tackle_rating":
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.lb_tackle_norm_dist_obj.rvs()), 2)
                else:
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.player_ability_norm_dist_obj.rvs()),2)

                player_name_to_combined_attr_score_dict[player_name] += this_player_attribute_value_dict[this_attribute]

            #create player career arc
            this_player_career_arc_list_dict = create_player_career_arc(player_position, player_age, player_name, this_player_attribute_value_dict)

            #first, create and save Player db object
            this_player_dict = {}
            this_player_dict["id"] = player_id
            this_player_dict["first_name"] = player_first_name
            this_player_dict["middle_initial"] = middle_initial
            this_player_dict["last_name"] = player_last_name
            this_player_dict["number"] = player_number
            this_player_dict["age"] = int(player_age)
            this_player_dict["first_season_id"] = 1
            this_player_dict["last_season_id"] = -1
            this_player_dict["injury_status"] = 0
            this_player_dict["alma_mater"] = school_name
            this_player_dict["primary_position"] = player_position
            this_player_dict["secondary_position"] = secondary_position
            this_player_dict["draft_position"] = "0.0"
            this_player_dict["salary"] = 0
            this_player_dict["height"] = str(int(height_feet)) + "'" + str(int(height_inches))
            this_player_dict["weight"] = weight_lbs
            this_player_dict["league_id"] = league_id

            #create Player db object
            this_player_db_obj = Player(**this_player_dict)
            this_player_db_obj.save(using="xactly_dev")

            #Create PlayerTeam db object
            this_player_team_db_obj = PlayerTeam(player_team_id=player_team_id, player_id=player_id, team_id=this_team_id, season_id=1)
            this_player_team_db_obj.save(using="xactly_dev")

            #Create specs object for this player_position
            this_player_position_specs_db_obj = None

            player_specs_db_obj = None
            exception_str = ""

            try:

                if player_position == 'qb':
                    player_specs_db_obj = PlayerSpecsQb(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'rb':
                    player_specs_db_obj = PlayerSpecsRb(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'fb':
                    player_specs_db_obj = PlayerSpecsFb(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'wr':
                    player_specs_db_obj = PlayerSpecsWr(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'te':
                    player_specs_db_obj = PlayerSpecsTe(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'k':
                    player_specs_db_obj = PlayerSpecsK(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'lb':
                    player_specs_db_obj = PlayerSpecsLb(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'ol':
                    player_specs_db_obj = PlayerSpecsOl(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'p':
                    player_specs_db_obj = PlayerSpecsP(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'cb':
                    player_specs_db_obj = PlayerSpecsCb(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'dl':
                    player_specs_db_obj = PlayerSpecsDl(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'sf':
                    player_specs_db_obj = PlayerSpecsSf(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'sto':
                    player_specs_db_obj = PlayerSpecsSto(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'std':
                    player_specs_db_obj = PlayerSpecsStd(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)

                player_specs_db_obj.save(using="xactly_dev")

            except Exception as e:
                exception_str = str(e)
                return HttpResponse(e)


            player_position_to_db_id_dict[player_position] += 1

            player_id += 1
            player_team_id += 1


    return HttpResponse("booyah!")