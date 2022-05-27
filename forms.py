from django import forms
from django.forms.widgets import Input

#define tuples for select values
NUM_PLAYOFF_TEAMS = (
    ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')
)

NUM_WEEKS_REG_SEASON = (
    ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18')
)

NUM_TEAMS_PER_CONFERENCE = (
    ('8', '8'), ('9', '9'), ('10', '10'), ('12', '12'), ('14', '14'), ('15', '15'), ('16', '16')
)

NUM_DIVISIONS_PER_CONFERENCE = (
    ('2', '2'), ('3', '3'), ('4', '4')
)

class JPartyFBInputForm(forms.Form):
    candidate_csv_file = forms.FileField(label='Load a new candidate spreadsheet:',widget=forms.ClearableFileInput(attrs={'multiple': True}))

class CreateLeagueForm1(forms.Form):
    number_of_playoff_teams_select = forms.CharField(label='Number of Playoff Teams Per Conference', widget=forms.Select(choices=NUM_PLAYOFF_TEAMS))
    number_of_weeks_select = forms.CharField(label='Number of Weeks in Regular Season', widget=forms.Select(choices=NUM_WEEKS_REG_SEASON))
    number_of_teams_conf_select = forms.CharField(label='Number of Teams Per Conference', widget=forms.Select(choices=NUM_TEAMS_PER_CONFERENCE))
    number_of_divisions_select = forms.CharField(label='Number of Divisions Per Conference',
                                                     widget=forms.Select(choices=NUM_DIVISIONS_PER_CONFERENCE))


    
