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

from operator import itemgetter

from jpartyfb.forms import CreateLeagueForm1
from jpartyfb.models import *

from PlayerCreation import PlayerCreation
from PlayerCreation import create_player_career_arc, create_players

from LeagueLayout import build_choose_teams_html
from DraftUtils import calculate_player_draft_value

def retract_prior_db_commits(db_commit_to_delete_id_dict):

    #retract commits going backwards, since the dbs with rows inserted later may depend on rows submitted earlier
    if "PlayerSpec" in db_commit_to_delete_id_dict:

        for player_position, first_player_position_id in db_commit_to_delete_id_dict["PlayerSpec"].items():

            if player_position == 'qb':
                PlayerSpecsQb.objects.using("xactly_dev").filter(id__gte=first_player_position_id).delete()
            elif player_position == 'rb':
                PlayerSpecsRb.objects.using("xactly_dev").filter(id__gte=first_player_position_id).delete()
            elif player_position == 'fb':
                PlayerSpecsFb.objects.using("xactly_dev").filter(id__gte=first_player_position_id).delete()
            elif player_position == 'wr':
                PlayerSpecsWr.objects.using("xactly_dev").filter(id__gte=first_player_position_id).delete()
            elif player_position == 'te':
                PlayerSpecsTe.objects.using("xactly_dev").filter(id__gte=first_player_position_id).delete()
            elif player_position == 'k':
                PlayerSpecsK.objects.using("xactly_dev").filter(id__gte=first_player_position_id).delete()
            elif player_position == 'lb':
                PlayerSpecsLb.objects.using("xactly_dev").filter(id__gte=first_player_position_id).delete()
            elif player_position == 'ol':
                PlayerSpecsOl.objects.using("xactly_dev").filter(id__gte=first_player_position_id).delete()
            elif player_position == 'p':
                PlayerSpecsP.objects.using("xactly_dev").filter(id__gte=first_player_position_id).delete()
            elif player_position == 'cb':
                PlayerSpecsCb.objects.using("xactly_dev").filter(id__gte=first_player_position_id).delete()
            elif player_position == 'dl':
                PlayerSpecsDl.objects.using("xactly_dev").filter(id__gte=first_player_position_id).delete()
            elif player_position == 'sf':
                PlayerSpecsSf.objects.using("xactly_dev").filter(id__gte=first_player_position_id).delete()
            elif player_position == 'sto':
                PlayerSpecsSto.objects.using("xactly_dev").filter(id__gte=first_player_position_id).delete()
            elif player_position == 'std':
                PlayerSpecsStd.objects.using("xactly_dev").filter(id__gte=first_player_position_id).delete()

    if "PlayerTeam" in db_commit_to_delete_id_dict:
        first_player_team_id = db_commit_to_delete_id_dict["PlayerTeam"]
        PlayerTeam.objects.using("xactly_dev").filter(player_team_id__gte=first_player_team_id).delete()

    if "Player" in db_commit_to_delete_id_dict:
        first_player_id = db_commit_to_delete_id_dict["Player"]
        Player.objects.using("xactly_dev").filter(id__gte=first_player_id).delete()

    if "Season" in db_commit_to_delete_id_dict:
        first_season_id = db_commit_to_delete_id_dict["Season"]
        Season.objects.using("xactly_dev").filter(id__gte=first_season_id).delete()

    if "TeamCity" in db_commit_to_delete_id_dict:

        first_team_city_id = db_commit_to_delete_id_dict["TeamCity"]
        TeamCity.objects.using("xactly_dev").filter(team_city_id__gte=first_team_city_id).delete()

    if "Team" in db_commit_to_delete_id_dict:

        first_team_id = db_commit_to_delete_id_dict["Team"]
        Team.objects.using("xactly_dev").filter(id__gte=first_team_id).delete()

    if "Division" in db_commit_to_delete_id_dict:

        first_division_id = db_commit_to_delete_id_dict["Division"]
        Division.objects.using("xactly_dev").filter(id__gte=first_division_id).delete()

    if "Conference" in db_commit_to_delete_id_dict:

        first_conference_id = db_commit_to_delete_id_dict["Conference"]
        Conference.objects.using("xactly_dev").filter(id__gte=first_conference_id).delete()

    if "League" in db_commit_to_delete_id_dict:

        first_league_id = db_commit_to_delete_id_dict["League"]
        League.objects.using("xactly_dev").filter(id__gte=first_league_id).delete()


def create_draft_players(league_id):

    # first, query the Team table to construct team_name_list and team_name_to_team_id_dict

    try:
        team_obj_list = Team.objects.using("xactly_dev").filter(league_id=league_id)
    except Exception:
        team_obj_list = None

    team_name_to_team_id_dict = {}
    team_name_list = []

    for this_team in team_obj_list:

        this_team_id = this_team.id
        this_team_nickname = this_team.nickname

        # we need to get the city
        try:
            team_city_obj = TeamCity.objects.using("xactly_dev").filter(team_id=this_team_id, league_id=league_id)
        except Exception:
            team_city_obj = None

        if team_city_obj is not None:
            this_team_city = team_city_obj[0].city.city_name

        this_team_fullname = this_team_city + " " + this_team_nickname

        team_name_list.append(this_team_fullname)
        team_name_to_team_id_dict[this_team_fullname] = this_team_id

    # get female setting for this league_id
    try:
        league_obj = League.objects.using("xactly_dev").filter(id=league_id)
    except Exception:
        league_obj = None

    female_setting = ""

    if league_obj is not None:
        female_setting = league_obj[0].female_setting

    db_commit_to_delete_id_dict = {}

    status_code, exception_str, db_commit_to_delete_id_dict = create_players(team_name_list, team_name_to_team_id_dict,
                                                                             league_id, female_setting,
                                                                             db_commit_to_delete_id_dict, "draft")
    if exception_str != "":
        retract_prior_db_commits(db_commit_to_delete_id_dict)
        return -1
    else:
        return 0

@ensure_csrf_cookie
def index(request):

    context = {}

    welcome_message = "Welcome to JParty Football!"
    
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
def show_league_form_1(request, source=None):
    context = {}

    if source is None:
        source = 'els'

    form = CreateLeagueForm1()

    is_league_season_active = False

    if source == 'els':

        #if we are editing league settings, we need to get the league_id whose settings we are editing
        league_id = int(request.session['league_id'])
        context['league_id'] = league_id

        league_settings_dict = {}

        try:
            league_obj = League.objects.using("xactly_dev").filter(id=league_id)

            league_name = league_obj[0].name
            weather_setting = league_obj[0].weather_setting
            injury_setting = league_obj[0].injury_setting
            female_setting = league_obj[0].female_setting
            neutral_site_setting = league_obj[0].neutral_site_setting

            number_of_playoff_teams_select = league_obj[0].num_playoff_teams_per_conference
            number_of_weeks_select = league_obj[0].num_weeks_regular_season
            number_of_teams_conf_select = league_obj[0].num_teams_per_conference
            number_of_divisions_select = league_obj[0].num_divisions_per_conference

            league_settings_dict['weather_setting'] = "checked" if weather_setting == True else ""
            league_settings_dict['injury_setting'] = "checked" if injury_setting == True else ""
            league_settings_dict['female_setting'] = "checked" if female_setting == True else ""
            league_settings_dict['neutral_site_setting'] = "checked" if neutral_site_setting == True else ""

        except Exception:
            league_settings_dict = {}

        #get latest season associated with this league_id and determine whether it is active or not

        try:
            season_obj = Season.objects.using("xactly_dev").filter(league_id=league_id).order_by("-id")

            if season_obj[0].start_time is None:
                is_league_season_active = False

        except Exception:
           pass

        context['league_settings_dict'] = league_settings_dict

        #set value of league name
        form.fields["league_name"].initial = league_name

        #set values of all select fields
        form.fields["number_of_playoff_teams_select"].initial = number_of_playoff_teams_select
        form.fields["number_of_weeks_select"].initial = number_of_weeks_select
        form.fields["number_of_teams_conf_select"].initial = number_of_teams_conf_select
        form.fields["number_of_divisions_select"].initial = number_of_divisions_select

        number_of_playoff_teams_del_value_list = []

        #It is illegal to edit league settings to have fewer of a setting. I won't make those choices available
        #except in the case of number of divisions

        for this_choice_idx, this_choice_tuple in enumerate(form.fields['number_of_playoff_teams_select'].widget.choices):

            this_tuple_value = int(this_choice_tuple[0])

            if this_tuple_value == number_of_playoff_teams_select:
                break

            if this_tuple_value < number_of_playoff_teams_select:
                number_of_playoff_teams_del_value_list.append(this_choice_tuple)

        form.fields['number_of_playoff_teams_select'].widget.choices = [this_tuple for this_tuple in form.fields['number_of_playoff_teams_select'].widget.choices if this_tuple not in number_of_playoff_teams_del_value_list ]

        number_of_weeks_del_value_list = []

        for this_choice_idx, this_choice_tuple in enumerate(form.fields['number_of_weeks_select'].widget.choices):

            this_tuple_value = int(this_choice_tuple[0])

            if this_tuple_value == number_of_weeks_select:
                break

            if this_tuple_value < number_of_weeks_select:
                number_of_weeks_del_value_list.append(this_choice_tuple)

        form.fields['number_of_weeks_select'].widget.choices = [this_tuple for this_tuple in form.fields['number_of_weeks_select'].widget.choices if this_tuple not in number_of_weeks_del_value_list]

        number_of_teams_conf_del_value_list = []

        for this_choice_idx, this_choice_tuple in enumerate(form.fields['number_of_teams_conf_select'].widget.choices):

            this_tuple_value = int(this_choice_tuple[0])

            if this_tuple_value == number_of_teams_conf_select:
                break

            if this_tuple_value < number_of_teams_conf_select:
                number_of_teams_conf_del_value_list.append(this_choice_tuple)

        form.fields['number_of_teams_conf_select'].widget.choices = [this_tuple for this_tuple in form.fields['number_of_teams_conf_select'].widget.choices if this_tuple not in number_of_teams_conf_del_value_list]

        context['source_page_title'] = 'Edit League Settings'
        welcome_message = "League Settings: " + league_name

    elif source == 'cnl':
        context['source_page_title'] = 'Create New League'
        context['league_id'] = -1
        welcome_message = "Create New League"

    context['form'] = form
    context['source'] = source
    context['season_active'] = is_league_season_active

    context['welcome_message'] = welcome_message

    return render(request, 'jpartyfb/show_league_form_1.html', context)

@ensure_csrf_cookie
def start_new_season(request):
    context = {}

    welcome_message = "Start New Season"
    context['welcome_message'] = welcome_message

    return render(request, 'jpartyfb/start_new_season.html', context)

@ensure_csrf_cookie
def edit_league_settings(request):

    #use session variable to pass along parameter in HttpResponseRedirect
    request.session['source_page'] = 'edit_league_settings'

    #redirect to choose league page
    return HttpResponseRedirect('/jpartyfb/choose_league/')

@ensure_csrf_cookie
def start_new_season(request):

    #use session variable to pass along parameter in HttpResponseRedirect
    request.session['source_page'] = 'start_new_season'

    #redirect to choose league page
    return HttpResponseRedirect('/jpartyfb/choose_league/')

@ensure_csrf_cookie
def draft_options(request):

    context = {}

    welcome_message = "Draft Options"
    context['welcome_message'] = welcome_message
    league_id = request.session['league_id']

    #create a session variable to store the latest season_id for this league
    try:
        season_obj = Season.objects.using("xactly_dev").filter(league_id=league_id).order_by("-id")
    except Exception:
        season_obj = None

    if season_obj is not None:
        request.session['season_id'] = season_obj[0].id

    return render(request, 'jpartyfb/draft_options.html', context)

@ensure_csrf_cookie
def create_draft_list(request, source=None):

    context = {}

    welcome_message = "Draft Options"
    context['welcome_message'] = welcome_message

    league_id = int(request.session['league_id'])
    season_id = int(request.session['season_id'])

    #if the draft list has not been created, then create it now.
    #the draft list is officially created when a row for this season's draft in the league exists

    try:
        draft_obj = Draft.objects.using("xactly_dev").filter(season_id=season_id, league_id=league_id)
    except Exception:
        draft_obj = None

    if draft_obj is not None:
        #we already have created the draft player list
        #depending on source, we will either watch the draft or fast forward the draft
        #....
        pass
    else:

        # we need to create the draft player list for this coming season in the league
        status_code = create_draft_players(league_id)

        if status_code == -1:
            context['error_msg'] = "Failed to create draft player list."

    return render(request, 'jpartyfb/draft_options.html', context)


@ensure_csrf_cookie
def choose_league(request):

    context = {}

    #get session variable
    source_page = request.session['source_page']
    context['source_page'] = request.session['source_page']

    welcome_message = "Choose League"
    context['welcome_message'] = welcome_message

    league_select_list = []

    if source_page == 'edit_league_settings':

        # load all league ids and names
        try:
            league_obj_list = League.objects.using("xactly_dev").all().order_by("-id")
        except Exception:
            league_obj_list = []

        for this_league_obj in league_obj_list:
            league_id = this_league_obj.id
            league_name = this_league_obj.name

            league_select_list.append([league_id, league_name])

    elif source_page == 'start_new_season':

        # load only leagues that do not currently have an active season. This will require submitting a
        # raw SQL query so that I can use GROUP BY

        try:
            league_obj_list = League.objects.using("xactly_dev").raw("SELECT 1 as id, l.id as league_id, l.name as league_name, max(s.id) as most_recent_season_id FROM season s INNER JOIN league l ON l.id = s.league_id GROUP BY l.id")
        except Exception:
            league_obj_list = []

        for this_league_obj in league_obj_list:
            league_id = this_league_obj.league_id
            league_name = this_league_obj.league_name
            most_recent_season_id = this_league_obj.most_recent_season_id

            #query Season to determine if most_recent_season_id is active or not
            try:
                this_season_obj = Season.objects.using("xactly_dev").filter(id=most_recent_season_id)
            except Exception:
                this_season_obj = None

            if this_season_obj[0].start_time is None:
                league_select_list.append([league_id, league_name])

    context['league_list'] = league_select_list

    return render(request, 'jpartyfb/choose_league.html', context)


@csrf_exempt
def league_redirect(request):

    league_id = request.POST['choose_league_select']
    source_page = request.POST['source_page_hidden']

    # pass league_id in a session variable
    request.session['league_id'] = league_id

    #depending on how we got to the choose league page, we will redirect to the proper location
    if source_page == 'edit_league_settings':
        return HttpResponseRedirect('/jpartyfb/show_league_form_1/els/')
    elif source_page == 'start_new_season':
        return HttpResponseRedirect('/jpartyfb/draft_options/')


@csrf_exempt
def process_create_league_form_1(request, edit_from_breadcrumb=None):

    if edit_from_breadcrumb != 'True':

        league_name = request.POST['league_name']
        source_page = request.POST['source_page_hidden']
        season_active = request.POST['season_active_hidden']
        league_id = int(request.POST['league_id_hidden'])
        submit_button_clicked = request.POST['clicked_submit_button_hidden']

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

        try:
            neutral_site_checkbox = request.POST['neutral_site_checkbox']
        except Exception:
            neutral_site_checkbox = 'off'

        number_of_playoff_teams_select = int(request.POST['number_of_playoff_teams_select'])
        number_of_weeks_select = int(request.POST['number_of_weeks_select'])
        number_of_teams_conf_select = int(request.POST['number_of_teams_conf_select'])
        number_of_divisions_select = int(request.POST['number_of_divisions_select'])

        if submit_button_clicked == "save_and_leave_button":

            #save checkbox settings associated with League in db
            injury_setting = True if injury_checkbox == 'on' else False
            weather_setting = True if weather_checkbox == 'on' else False
            female_setting = True if female_checkbox == 'on' else False
            neutral_site_setting = True if neutral_site_checkbox == 'on' else False

            league_obj = League.objects.using("xactly_dev").get(id=league_id)
            league_obj.name = league_name

            #create new abbreviation
            league_name_parts_list = league_name.split()
            league_name_abbrev_letter_list = []
            league_name_abbrev_str = ""

            if len(league_name_parts_list) >= 2:

                for one_part in league_name_parts_list:
                    league_name_abbrev_letter_list.append(one_part[0])

                league_name_abbrev_str = ''.join(league_name_abbrev_letter_list)

            else:

                league_name_abbrev_str = league_name[:3]

            league_name_abbrev_str = league_name_abbrev_str.upper()
            league_obj.abbreviation = league_name_abbrev_str

            #get checkbox settings
            league_obj.weather_setting = weather_setting
            league_obj.injury_setting = injury_setting
            league_obj.female_setting = female_setting
            league_obj.neutral_site_setting = neutral_site_setting

            league_obj.save()

            return HttpResponseRedirect('/jpartyfb/')


    if edit_from_breadcrumb == 'True':

        league_id = request.GET['league_id']

        #the league has already been created, so query for the information
        try:
            league_obj = League.objects.using("xactly_dev").filter(id=league_id)
        except Exception:
            league_obj = None

        league_name = league_obj[0].name
        injury_checkbox = league_obj[0].injury_setting
        weather_checkbox = league_obj[0].weather_setting
        female_checkbox = league_obj[0].female_setting
        neutral_site_checkbox = league_obj[0].neutral_site_setting
        number_of_playoff_teams_select = league_obj[0].num_playoff_teams_per_conference
        number_of_weeks_select = league_obj[0].num_weeks_regular_season
        number_of_teams_conf_select = league_obj[0].num_teams_per_conference
        number_of_divisions_select = league_obj[0].num_divisions_per_conference
        source_page = 'els'

        #determine if the season is active or not
        try:
            season_obj = Season.objects.using("xactly_dev").filter(league_id=league_id).order_by("-id")

            if season_obj[0].start_time is None:
                season_active = False
            else:
                season_active = True

        except Exception:
           pass


    number_of_teams_per_division = number_of_teams_conf_select / number_of_divisions_select

    team_html_str, city_nickname_to_city_id_dict, conference_name_list, tdid_to_team_id_dict = build_choose_teams_html(number_of_divisions_select, number_of_teams_conf_select, number_of_teams_per_division, source_page, league_id)

    context = {}

    welcome_message = "Choose Your Teams"
    context['league_id'] = league_id
    context['league_name'] = league_name
    context['eastern_conference_name'] = conference_name_list[0]
    context['western_conference_name'] = conference_name_list[1]
    context['injury_mode'] = injury_checkbox
    context['weather_mode'] = weather_checkbox
    context['female_mode'] = female_checkbox
    context['neutral_site_mode'] = neutral_site_checkbox
    context['welcome_message'] = welcome_message
    context['source_page'] = source_page
    context['season_active'] = season_active
    context['number_of_playoff_teams'] = number_of_playoff_teams_select
    context['number_of_weeks'] = number_of_weeks_select
    context['number_of_teams_conf'] = number_of_teams_conf_select
    context['number_of_divisions_conf'] = number_of_divisions_select
    context['number_of_teams_per_division'] = number_of_teams_per_division
    context['city_nickname_to_city_id_dict'] = city_nickname_to_city_id_dict
    context['tdid_to_team_id_dict'] = tdid_to_team_id_dict
    context['team_html_str'] = team_html_str

    return render(request, 'jpartyfb/choose_teams.html', context)


@csrf_exempt
def process_create_league_form_final(request):

    #extract form information and pass it into the choose_teams page
    league_name = request.POST['league_name_hidden']

    #checkboxes still have 'on' and 'off' values at this point - need to convert to booleans
    injury_setting_raw = request.POST['injury_hidden']
    injury_setting = True if injury_setting_raw == 'on' else False

    weather_setting_raw = request.POST['weather_hidden']
    weather_setting = True if weather_setting_raw == 'on' else False

    female_setting_raw = request.POST['female_hidden']
    female_setting = True if female_setting_raw == 'on' else False

    neutral_site_setting_raw = request.POST['neutral_site_hidden']
    neutral_site_setting = True if neutral_site_setting_raw == 'on' else False

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

    source_page_hidden = request.POST['source_page_hidden']
    league_id_hidden = int(request.POST['league_id_hidden'])

    #these are data structures used to update Team rows with the new division and conference id values
    team_id_to_conference_name_dict_str = request.POST['team_id_to_conference_dict']
    team_id_to_conference_name_dict = json.loads(team_id_to_conference_name_dict_str)

    team_id_to_division_name_dict_str = request.POST['team_id_to_division_dict']
    team_id_to_division_name_dict = json.loads(team_id_to_division_name_dict_str)

    team_id_to_team_name_dict_str = request.POST['team_id_to_team_name_dict']
    team_id_to_team_name_dict = json.loads(team_id_to_team_name_dict_str)

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

    #this is a dict that will keep track of which db insertions have taken place, and the starting id of the commit
    #I will use this to retract prior db commits if an error occurs at some point

    db_commit_to_delete_id_dict = {}

    #start inserting form data into database tables
    #get latest League row
    try:
        league_id = int(League.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        league_id = 1

    try:
        League.objects.using("xactly_dev").create(id=league_id, name=league_name, abbreviation=league_name_abbrev_str,
                                                  weather_setting=weather_setting, injury_setting=injury_setting,
                                                  female_setting=female_setting, neutral_site_setting=neutral_site_setting,
                                                  num_playoff_teams_per_conference=number_of_playoff_teams_setting, num_weeks_regular_season=number_of_weeks_setting,
                                                  num_teams_per_conference=number_of_teams_conf_setting, num_divisions_per_conference=number_of_divisions_conf_setting)
        db_commit_to_delete_id_dict['League'] = league_id
    except Exception:
        return HttpResponse(-1)

    #next, insert conference rows for this league
    try:
        conference_id = int(
            Conference.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        conference_id = 1

    first_conference_id = conference_id

    #we need this for proper insertions into the Division table
    conference_name_to_id_dict = {}

    for conference_idx, this_conference_name in enumerate(conference_name_list):

        conference_name_to_id_dict[this_conference_name] = conference_id

        try:
            Conference.objects.using("xactly_dev").create(id=conference_id, conference_name=this_conference_name,
                                                          league_id=league_id)
            db_commit_to_delete_id_dict['Conference'] = first_conference_id
        except Exception:

            retract_prior_db_commits(db_commit_to_delete_id_dict)
            return HttpResponse(-2)

        conference_id += 1

    #now insert division rows for this league
    try:
        division_id = int(
            Division.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        division_id = 1

    first_division_id = division_id

    #we need this for proper insertions into the Team table
    division_name_to_id_dict = {}

    for division_idx, this_division_name in enumerate(division_name_list):

        this_conference_name = division_to_conference_dict[this_division_name]
        this_conference_id = conference_name_to_id_dict[this_conference_name]
        division_name_to_id_dict[this_division_name] = division_id

        try:
            Division.objects.using("xactly_dev").create(id=division_id, division_name=this_division_name,
                                                          conference_id=this_conference_id, first_season_id=-1, league_id=league_id)

            db_commit_to_delete_id_dict['Division'] = first_division_id
        except Exception:
            retract_prior_db_commits(db_commit_to_delete_id_dict)
            return HttpResponse(-3)

        division_id += 1

    # declare variables for player creation associated with any new teams added to the league
    team_name_els_list = []
    team_name_to_team_id_els_dict = {}

    #we will only create new rows for Team, TeamCity, and Season when creating a new league, otherwise we update rows
    if source_page_hidden == 'cnl':

        try:
            team_id = int(
                Team.objects.using('xactly_dev').latest('id').id) + 1
        except Exception:
            team_id = 1

        first_team_id = team_id

        #also insert team_city rows for this league
        try:
            team_city_id = int(
                TeamCity.objects.using('xactly_dev').latest('team_city_id').team_city_id) + 1
        except Exception:
            team_city_id = 1

        first_team_city_id = team_city_id

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

                db_commit_to_delete_id_dict['Team'] = first_team_id
            except Exception:
                retract_prior_db_commits(db_commit_to_delete_id_dict)
                return HttpResponse(-4)

            try:
                TeamCity.objects.using("xactly_dev").create(team_city_id=team_city_id, team_id=team_id,
                                                        city_id=this_team_city_id,
                                                        first_season_id=-1,stadium_id=this_team_stadium_id, league_id=league_id)

                db_commit_to_delete_id_dict['TeamCity'] = first_team_city_id
            except Exception:

                retract_prior_db_commits(db_commit_to_delete_id_dict)
                return HttpResponse(-5)

            team_id += 1
            team_city_id += 1

        #before creating players, I want to create the db row for season 1 of the new league. However, note that
        #the season will be inactive until the draft occurs
        #we will only do this when creating a new league - we will update the season if editing the league

        try:
            season_id = int(Season.objects.using('xactly_dev').latest('id').id) + 1
        except Exception:
            season_id = 1

        try:
            Season.objects.using("xactly_dev").create(id=season_id, start_time=None,
                                                        end_time=None,
                                                        season_year=1, league_id=league_id, created_draft_list=False)

            db_commit_to_delete_id_dict['Season'] = season_id

        except Exception:
            return HttpResponse(-9)

    #some rows will be deleted, others will be updated to support the new league id value
    if source_page_hidden == 'els':

        try:
            Season.objects.using("xactly_dev").filter(league_id=league_id_hidden).update(league_id=league_id)
        except Exception:
            pass

        try:

            #get latest team_id in case we have new teams
            try:
                insert_team_id = int(Team.objects.using('xactly_dev').latest('id').id) + 1
            except Exception:
                insert_team_id = 1

            #also get latest team_city_id for same reason
            try:
                insert_team_city_id = int(TeamCity.objects.using('xactly_dev').latest('team_city_id').team_city_id) + 1
            except Exception:
                insert_team_city_id = 1

            #for Team, we have to update the division_id, conference_id and league_id.
            for this_team_id, this_conference_name in team_id_to_conference_name_dict.items():

                this_team_id_int = int(this_team_id)

                try:
                    this_team_new_conference_id = conference_name_to_id_dict[this_conference_name]

                    this_team_division_name = team_id_to_division_name_dict[this_team_id]
                    this_team_new_division_id = division_name_to_id_dict[this_team_division_name]

                    #get new team nickname if any
                    this_team_new_name = team_id_to_team_name_dict[this_team_id]
                    this_team_name_parts_list = this_team_new_name.split()
                except Exception as e:
                    #return HttpResponse(s[this_team_new_conference_id, this_team_division_name]))
                    return HttpResponse(str(this_team_new_conference_id) + " " + str(this_team_id) + " " + str(team_id_to_division_name_dict) + " " + repr(e))

                if this_team_name_parts_list[0] == "Dallas":
                    this_team_nickname = this_team_name_parts_list[1] + " " + this_team_name_parts_list[2]
                else:
                    this_team_nickname = this_team_name_parts_list[-1]

                if this_team_id_int > 0:

                    #this is a team we already created

                    try:
                        Team.objects.using("xactly_dev").filter(id=this_team_id).update(nickname=this_team_nickname, conference_id=this_team_new_conference_id, division_id=this_team_new_division_id, league_id=league_id)
                    except Exception as e:
                        return HttpResponse("Team filter id > 0 : " + str(e))

                    this_team_city_id = city_nickname_to_city_id_dict[this_team_nickname]

                    #get the stadium associated with this_team_city_id
                    try:
                        stadium_obj = Stadium.objects.using("xactly_dev").filter(city_id=this_team_city_id)
                    except Exception:
                        pass

                    this_team_stadium_id = stadium_obj[0].stadium_id

                    #Update TeamCity object associated with this team with the new league_id and city, if the team
                    #has been switched in the standings
                    try:
                        TeamCity.objects.using("xactly_dev").filter(league_id=league_id_hidden, team_id=this_team_id).update(league_id=league_id, city_id=this_team_city_id, stadium_id=this_team_stadium_id)
                    except Exception:
                        pass

                else:

                    #if this is a new team, its city_id value in city_nickname_to_city_id_dict will be -1
                    #we will then query City using city_name to get city_id

                    try:
                        this_team_city_id = city_nickname_to_city_id_dict[this_team_nickname]
                    except Exception as e:
                        return HttpResponse(str(city_nickname_to_city_id_dict))

                    if this_team_city_id == -1:
                        try:
                            this_city_name = " ".join(this_team_name_parts_list[0:-1])
                            city_obj = City.objects.using("xactly_dev").filter(city_name=this_city_name)
                            this_team_city_id = city_obj[0].city_id
                        except Exception:
                            pass


                    # get the stadium associated with this_team_city_id
                    try:
                        stadium_obj = Stadium.objects.using("xactly_dev").filter(city_id=this_team_city_id)
                    except Exception:
                        pass

                    try:
                        this_team_stadium_id = stadium_obj[0].stadium_id
                    except Exception:
                        return HttpResponse("Getting stadium id..." + str(this_team_city_id) + " " + str(this_team_nickname) + str(this_city_name))

                    #create new Team and TeamCity objects for the new team
                    try:
                        Team.objects.using("xactly_dev").create(id=insert_team_id, nickname=this_team_nickname, first_season_id=-1, current_season_wins=0, current_season_losses=0,
                                                        stadium_id=this_team_stadium_id, conference_id=this_team_new_conference_id,
                                                        division_id=this_team_new_division_id,league_id=league_id)
                    except Exception as e:
                        return HttpResponse("error: " + str(e))

                    try:
                        TeamCity.objects.using("xactly_dev").create(team_city_id=insert_team_city_id, team_id=insert_team_id,
                                                                    city_id=this_team_city_id,
                                                                    first_season_id=-1, stadium_id=this_team_stadium_id,
                                                                    league_id=league_id)
                    except Exception as e:
                        return HttpResponse("error: " + str(e))

                    # add team name to team name list
                    whole_team_name = " ".join(this_team_name_parts_list)
                    team_name_els_list.append(whole_team_name)

                    team_name_to_team_id_els_dict[whole_team_name] = insert_team_id

                    insert_team_id += 1
                    insert_team_city_id += 1

        except Exception as d:
            return HttpResponse(str([this_team_new_conference_id, this_team_division_name, this_team_new_division_id, this_team_new_name, this_team_name_parts_list, this_team_id, this_conference_name]))

        #we need to update Player with the new league_id value
        try:
            Player.objects.using("xactly_dev").filter(league_id=league_id_hidden).update(league_id=league_id)
        except Exception:
            pass

        #we will go backwards from how these rows were originally committed into the db to avoid fk conflicts
        #these are the old league, division and conference rows
        try:
            Division.objects.using("xactly_dev").filter(league_id=league_id_hidden).delete()
        except Exception:
            pass

        try:
            Conference.objects.using("xactly_dev").filter(league_id=league_id_hidden).delete()
        except Exception:
            pass

        try:
            League.objects.using("xactly_dev").filter(league_id=league_id_hidden).delete()
        except Exception:
            pass


    #create all player info, including career arcs
    if source_page_hidden == 'cnl':
        status_code, exception_str, db_commit_to_delete_id_dict = create_players(team_name_list, team_name_to_team_id_dict, league_id, female_setting, db_commit_to_delete_id_dict, "league")

        if exception_str != "":
            retract_prior_db_commits(db_commit_to_delete_id_dict)
    elif len(team_name_els_list) > 0:

        #we have edited the league and added new teams. Now we need to add players to those teams
        status_code, exception_str, db_commit_to_delete_id_dict = create_players(team_name_els_list, team_name_to_team_id_els_dict, league_id, female_setting, db_commit_to_delete_id_dict, "league")

    else:
        status_code = 1

    return HttpResponse(status_code)


def watch_draft(request):
    pass

def fast_forward_draft(request):
    pass

def view_draft_list(request):

    #get league_id session variable and refresh it
    league_id = request.session['league_id']

    error_msg = ""
    context = {}

    player_filter = None

    #get filter, if user clicked on one already
    if 'player_filter' in request.GET:
        player_filter = request.GET['player_filter']

    #if the current season of this league_id has a created_draft_list value of True, then return an error message back to the draft
    #options page

    try:
        current_season_obj = Season.objects.using("xactly_dev").filter(id=league_id).order_by("-id")
    except Exception:
        context['error_msg'] = "Failed to load current season."
        context['welcome_message'] = "Draft Options"
        return render(request, 'jpartyfb/draft_options.html', context)

    created_draft_list = current_season_obj[0].created_draft_list
    league_id = current_season_obj[0].league_id

    if current_season_obj[0].created_draft_list == False:

        #create draft player list
        status_code = create_draft_players(league_id)

        if status_code == -1:
            context['error_msg'] = "Failed to create draft player list."
            context['welcome_message'] = "Draft Options"
            return render(request, 'jpartyfb/draft_options.html', context)

        #if we just created the draft list, then we'll have to calculate player draft ranks
        # query for all the players in the draft list
        try:
            player_obj_list = Player.objects.using("xactly_dev").filter(league_id=league_id, playing_status=0)
        except Exception:
            context['error_msg'] = "Failed to load draft player list."
            context['welcome_message'] = "Draft Options"
            return render(request, 'jpartyfb/draft_options.html', context)

        # indicate that draft player list has been created by updating the Season obj's created_draft_list property
        try:
            Season.objects.using("xactly_dev").filter(id=league_id).update(created_draft_list=True)
        except Exception:
            context['error_msg'] = "Failed to mark player list as created in Season db table"
            context['welcome_message'] = "Draft Options"
            return render(request, 'jpartyfb/draft_options.html', context)
    else:

        player_query_dict = {'league_id': league_id, 'playing_status': 0}

        if player_filter is not None:
            player_query_dict['primary_position'] = player_filter

        try:
            player_obj_list = Player.objects.using("xactly_dev").filter(**player_query_dict)
        except Exception:
            context['error_msg'] = "Failed to load draft player list."
            context['welcome_message'] = "Draft Options"
            return render(request, 'jpartyfb/draft_options.html', context)

    player_info_lol = []

    for this_player_obj in player_obj_list:

        this_player_id = this_player_obj.id
        this_player_first_name = this_player_obj.first_name.strip()
        this_player_last_name = this_player_obj.last_name.strip()
        this_player_middle_initial = this_player_obj.middle_initial.strip()

        if this_player_middle_initial == "":
            this_player_middle_initial = " "
        else:
            this_player_middle_initial = " " + this_player_middle_initial + " "

        this_player_full_name = this_player_first_name + this_player_middle_initial + this_player_last_name

        this_player_alma_mater = this_player_obj.alma_mater
        this_player_primary_position = this_player_obj.primary_position

        this_player_height = this_player_obj.height
        this_player_weight = this_player_obj.weight

        if created_draft_list == False:
            this_player_draft_value = calculate_player_draft_value(this_player_id, this_player_primary_position)

            # finally, insert this_player_draft_value into the Player table
            try:
                Player.objects.using("xactly_dev").filter(id=this_player_id).update(draft_value=this_player_draft_value)
            except Exception:
                context['error_msg'] = "Failed to update player draft value"
                context['welcome_message'] = "Draft Options"
                return render(request, 'jpartyfb/draft_options.html', context)

        else:
            this_player_draft_value = this_player_obj.draft_value

        player_info_lol.append([this_player_full_name, this_player_primary_position, this_player_alma_mater, this_player_height, this_player_weight, this_player_draft_value])

    # sort lists in player_info_lol by this_player_draft_value
    player_info_lol.sort(key=itemgetter(5), reverse=True)

    context['welcome_message'] = "Draft List"
    context['player_info_lol'] = player_info_lol
    return render(request, 'jpartyfb/draft_list.html', context)

