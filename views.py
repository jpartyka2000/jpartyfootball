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

from jpartyfb.forms import JPartyFBInputForm, CreateLeagueForm1
from jpartyfb.models import DefaultTeams, City

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
        team_html_str += "<td width='50%' align='center' style='background-color: #eeeeee;' id='td_division_eastern_" + str(conf_division_idx) + "' class='td_division'>"
        team_html_str += "<input type='text' id='Eastern_division_" + str(
            conf_division_idx) + "' name='eastern_division_" + str(
            conf_division_idx) + "' class='division' maxlength='35' value='" + "Eastern " + conf_division_name + "' style='width: 220px; border: none; background: transparent; text-align:center; font-weight: bold;' />"
        team_html_str += "</td>"

        # now western division
        team_html_str += "<td width='50%' align='center' style='background-color: #eeeeee;' id='td_division_western_" + str(conf_division_idx) + "' class='td_division'>"
        team_html_str += "<input type='text' id='Western_division_" + str(
            conf_division_idx) + "' name='western_division_" + str(
            conf_division_idx) + "' class='division' maxlength='35' value='" + "Western " + conf_division_name + "' style='width: 220px; border: none; background: transparent; text-align:center; font-weight: bold;' />"
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

    #extract form information and pass it into the choose_teams page
    try:
        injury_checkbox = request.POST['injury_checkbox']
    except Exception:
        injury_checkbox = 'off'

    try:
        weather_checkbox = request.POST['weather_checkbox']
    except Exception:
        weather_checkbox = 'off'

    number_of_playoff_teams_select = int(request.POST['number_of_playoff_teams_select'])
    number_of_weeks_select = int(request.POST['number_of_weeks_select'])
    number_of_teams_conf_select = int(request.POST['number_of_teams_conf_select'])
    number_of_divisions_select = int(request.POST['number_of_divisions_select'])

    number_of_teams_per_division = number_of_teams_conf_select / number_of_divisions_select

    team_html_str = build_choose_teams_html(number_of_divisions_select, number_of_teams_conf_select, number_of_teams_per_division)


    #sdsddsds
    context = {}

    welcome_message = "Choose Your Teams"
    context['injury_mode'] = injury_checkbox
    context['weather_mode'] = weather_checkbox
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
    injury_hidden = request.POST['injury_hidden']
    weather_hidden = request.POST['weather_hidden']
    number_of_weeks_hidden = request.POST['number_of_weeks_hidden']
    number_of_playoff_teams_hidden = request.POST['number_of_playoff_teams_hidden']
    number_of_teams_conf_hidden = request.POST['number_of_teams_conf_hidden']
    number_of_divisions_conf_hidden = request.POST['number_of_divisions_conf_hidden']

    context = {}

    welcome_message = "Choose Your Teams"
    context['welcome_message'] = welcome_message

    return render(request, 'jpartyfb/choose_teams.html', context)