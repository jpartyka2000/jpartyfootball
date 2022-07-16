from django.conf.urls import patterns, url, include

from jpartyfb import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^play_football/$', views.play_football, name='play_football'),
    url(r'^manage_leagues/$', views.manage_leagues, name='manage_leagues'),
    url(r'^view_stats/$', views.view_stats, name='view_stats'),
    url(r'^show_league_form_1/(?P<source>\w+)/$', views.show_league_form_1, name='show_league_form_1'),
    url(r'^start_new_season/$', views.start_new_season, name='start_new_season'),
    url(r'^edit_league_settings/$', views.edit_league_settings, name='edit_league_settings'),
    url(r'^process_create_league_form_1/(?P<edit_from_breadcrumb>\w+)/$', views.process_create_league_form_1, name='process_create_league_form_1'),
    url(r'^process_create_league_form_final/$', views.process_create_league_form_final, name='process_create_league_form_final'),
    url(r'^choose_league/$', views.choose_league, name='choose_league'),
    url(r'^league_redirect/$', views.league_redirect, name='league_redirect'),
    url(r'^watch_draft/$', views.watch_draft, name='watch_draft'),
    url(r'^fast_forward_draft/$', views.fast_forward_draft, name='fast_forward_draft'),
    url(r'^view_draft_list/$', views.view_draft_list, name='view_draft_list'),
    url(r'^start_new_season/$', views.start_new_season, name='start_new_season'),
    url(r'^draft_options/$', views.draft_options, name='draft_options'),
    url(r'^create_draft_list/(?P<source>\w+)$', views.create_draft_list, name='create_draft_list'),
    url(r'^watch_draft/$', views.watch_draft, name='watch_draft'),
    url(r'^fast_forward_draft/$', views.fast_forward_draft, name='fast_forward_draft'),
    url(r'^view_draft_list/$', views.view_draft_list, name='view_draft_list'),


)

