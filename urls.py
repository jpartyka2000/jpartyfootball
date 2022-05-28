from django.conf.urls import patterns, url, include

from jpartyfb import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^play_football/$', views.play_football, name='play_football'),
    url(r'^manage_leagues/$', views.manage_leagues, name='manage_leagues'),
    url(r'^view_stats/$', views.view_stats, name='view_stats'),
    url(r'^create_new_league/$', views.create_new_league, name='create_new_league'),
    url(r'^start_new_season/$', views.start_new_season, name='start_new_season'),
    url(r'^edit_league_settings/$', views.edit_league_settings, name='edit_league_settings'),
    url(r'^process_create_league_form_1/$', views.process_create_league_form_1, name='process_create_league_form_1'),
    url(r'^process_create_league_form_final/$', views.process_create_league_form_final, name='process_create_league_form_final'),



)

