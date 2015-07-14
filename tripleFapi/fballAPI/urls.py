from django.conf.urls import patterns, include, url
from django.contrib import admin
from fballAPI.views import WeeklyMatchupView,WeeklyScoresView, WeeklyWinnersView,WeeklyLosersView
from django.views.generic import View

urlpatterns = patterns('',

    #weekly pickem views

    #weekly scheduled matchups
    url(r'^(?P<year>20[0-2][0-9])/(?P<week>week-[1-9][0-7]?)/matchups/$', WeeklyMatchupView.as_view()),

    #weekly scores
    url(r'^(?P<year>20[0-2][0-9])/(?P<week>week-[1-9][0-7]?)/scores/$', WeeklyScoresView.as_view()),

    #winning teams
    url(r'^(?P<year>20[0-2][0-9])/(?P<week>week-[1-9][0-7]?)/winners/$', WeeklyWinnersView.as_view()),

    #losing teams
    url(r'^(?P<year>20[0-2][0-9])/(?P<week>week-[1-9][0-7]?)/losers/$', WeeklyLosersView.as_view()),
)
