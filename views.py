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

from jpartyfb.forms import JPartyFBInputForm, CreateLeagueForm1
from jpartyfb.models import DefaultTeams, City, League, Division, Conference

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
    for this_default_team in DefaultTeams.objects.using("xactly_dev").filter(id__lte=(number_of_teams_conf_select * 2)).order_by("id"):
        this_default_team_nickname = this_default_team.nickname
        this_default_team_city_name = this_default_team.city.city_name
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

    return team_html_str


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

    team_html_str = build_choose_teams_html(number_of_divisions_select, number_of_teams_conf_select, number_of_teams_per_division)

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

    for division_idx, this_division_name in enumerate(division_name_list):

        this_conference_name = division_to_conference_dict[this_division_name]
        this_conference_id = conference_name_to_id_dict[this_conference_name]

        try:
            Division.objects.using("xactly_dev").create(id=division_id, division_name=this_division_name,
                                                          conference_id=this_conference_id, first_season_id=-1, league_id=league_id)

        except Exception:
            return HttpResponse(-3)

        division_id += 1


    #status_and_variable_name_list = [result_status, variable_name_dict, unmatched_variables_dict]
    #status_variable_names_json = json.dumps(status_and_variable_name_list)

    return HttpResponse(1)