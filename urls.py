from django.urls import path, include
from . import views 
from jpartyfb import urls

app_name = 'jpartyfb'  # This is where you define the namespace

urlpatterns = [
    path('', views.index, name='index'),
    path('play_football/', views.play_football, name='play_football'),
    path('manage_leagues/', views.manage_leagues, name='manage_leagues'),
    path('view_stats/', views.view_stats, name='view_stats'),
    
    #path('^show_league_form_1/(?P<source>\w+)/$', views.show_league_form_1, name='show_league_form_1'),
    path('show_league_form_1/<str:source>/', views.show_league_form_1, name='show_league_form_1'),
    
    path('start_new_season/', views.start_new_season, name='start_new_season'),
    path('edit_league_settings/', views.edit_league_settings, name='edit_league_settings'),
    
    #path('^process_create_league_form_1/(?P<edit_from_breadcrumb>\w+)/$', views.process_create_league_form_1, name='process_create_league_form_1'),
    path('process_create_league_form_1/<str:edit_from_breadcrumb>/', views.process_create_league_form_1, name='process_create_league_form_1'),
    
    
    path('process_create_league_form_final/', views.process_create_league_form_final, name='process_create_league_form_final'),
    path('choose_league/', views.choose_league, name='choose_league'),
    path('league_redirect/', views.league_redirect, name='league_redirect'),
    path('watch_draft/', views.watch_draft, name='watch_draft'),
    path('view_draft_list/', views.view_draft_list, name='view_draft_list'),
    path('start_new_season/', views.start_new_season, name='start_new_season'),
    path('draft_options/', views.draft_options, name='draft_options'),
    
    #path('^create_draft_list/(?P<source>\w+)$', views.create_draft_list, name='create_draft_list'),
    path('create_draft_list/<str:source>/', views.create_draft_list, name='create_draft_list'),
    
    path('watch_draft/', views.watch_draft, name='watch_draft'),
    path('view_draft_results/', views.view_draft_results, name='view_draft_results'),
    path('view_league_schedule/', views.view_league_schedule, name='view_league_schedule'),
    path('view_preseason_power_rankings/', views.view_preseason_power_rankings, name='view_preseason_power_rankings'),

]