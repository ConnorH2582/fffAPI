from django.views.generic import View
from django.http import JsonResponse,Http404
from django.utils.text import slugify
from fballAPI.services import get_matchups,get_scores,get_winners,get_losers
import requests
import json
import nflgame

class WeeklyMatchupView(View):
    def get(self,request,year,week):
        # year = int(year)
        week = week.strip('week-')
        games = get_matchups(year,week)
        game_count = games.__len__()
        return JsonResponse({'week_{}_schedule'.format(week): games, 'game_count':game_count})

class WeeklyScoresView(View):
    def get(self,request,year,week):
        year = int(year)
        week = int(week.strip('week-'))
        games = get_scores(year,week)
        game_count = games.__len__()
        return JsonResponse({'week_{}_scores'.format(week): games, 'game_count':game_count})

class WeeklyWinnersView(View):
    def get(self, request, year, week):
        year = int(year)
        week = int(week.strip('week-'))
        winners = get_winners(year,week)
        game_count = winners.__len__()
        return JsonResponse({'winning_teams':winners, 'game_count':game_count})

class WeeklyLosersView(View):
    def get(self, request, year, week):
        year = int(year)
        week = int(week.strip('week-'))
        losers = get_losers(year,week)
        game_count = losers.__len__()
        return JsonResponse({'losing_teams':losers,'game_count':game_count})
