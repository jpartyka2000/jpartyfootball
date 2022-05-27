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
#from jpartyfb.models import FitGenUploads

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

    number_of_playoff_teams_select = request.POST['number_of_playoff_teams_select']
    number_of_weeks_select = request.POST['number_of_weeks_select']
    number_of_teams_conf_select = request.POST['number_of_teams_conf_select']
    number_of_divisions_select = request.POST['number_of_divisions_select']

    context = {}

    welcome_message = "Choose Your Teams"
    context['welcome_message'] = welcome_message

    return render(request, 'jpartyfb/choose_teams.html', context)