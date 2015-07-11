from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import JsonResponse,Http404
from django.utils.text import slugify
from fballAPI.services import get_player_season_stats, get_matchups,get_scores,get_winners,get_losers
import requests
import json
import nflgame



class AllQuarterbacksView(View):
    def get(self, request, year):
        # year = int(year)
        games = nflgame.games(year)
        players = nflgame.combine(games)
        all_qb_list = []
        for p in players:
            if p.player.position == 'QB' and p.passing_att > 0:
                    name_slug = slugify(p.player.full_name.replace(' ', '_'))
                    all_qb_list.append({'fullname' : p.player.full_name,'shortname':p.name, 'name_slug':name_slug,'position': p.player.position, 'team':p.team, 'profile_url':p.player.profile_url, 'number': p.player.uniform_number, 'pass_attempts' : p.passing_att, 'pass_comps':p.passing_cmp, 'pass_yards' : p.passing_yds, 'pass_tds' : p.passing_tds, 'twoptconv_pass': p.passing_twoptm,'interceptions_thrown' : p.passing_ints, 'qb_rating': p.passer_rating(), 'rush_attempts' : p.rushing_att, 'rush_yards': p.rushing_yds, 'rush_tds' : p.rushing_tds, 'twoptconv_rush': p.rushing_twoptm,'fumbles_lost' : p.fumbles_lost})
        return JsonResponse({'all_qb_list': all_qb_list})

class AllRunningbacksView(View):
    pass
        # def get_rbs(year):
        #     games = nflgame.games(year)
        #     players = nflgame.combine(games)
        #     for p in players:
        #         if p.player.position == 'RB':
        #             print "Name: {}, Position: {}, Number: {}, Team:{}, Rush Attempts: {}, Rushing Yards: {}, Rushing TDs: {}, Receptions: {}, Receiving Yards: {}, Receiving TDs: {}, Fumbles Lost: {}, Profile URL: {}".format(p.player.full_name, p.player.position, p.team, p.rushing_att, p.rushing_yds, p.rushing_tds, p.receiving_rec, p.receiving_yds, p.receiving_tds, p.fumbles_lost, p.player.profile_url)

class AllReceiversView(View):
    pass
        # def get_wrs(year):
        #     games = nflgame.games(year)
        #     players = nflgame.combine(games)
        #     for p in players:
        #         if p.player.position == 'WR':
        #             print "Name: {}, Position: {}, Number: {}, Team:{}, Receptions: {}, Receiving Yards: {}, Receiving TDs: {}, Rush Attempts: {}, Rushing Yards: {}, Rushing TDs: {}, Fumbles Lost: {}, Profile URL: {}".format(p.player.full_name, p.player.position, p.team, p.receiving_rec, p.receiving_yds, p.receiving_tds, p.rushing_att, p.rushing_yds, p.rushing_tds, p.fumbles_lost, p.player.profile_url)

class AllTightEndsView(View):
    pass
    # OrderedDict([(u'receiving_tds', 0), (u'receiving_lng', 53), (u'receiving_rec', 2), (u'receiving_twopta', 0), (u'receiving_yds', 53), (u'receiving_lngtd', 0), (u'receiving_twoptm', 0)])
    # OrderedDict([(u'receiving_tds', 1), (u'receiving_lng', 89), (u'receiving_rec', 10), (u'receiving_twopta', 0), (u'receiving_yds', 121), (u'receiving_lngtd', 1), (u'receiving_twoptm', 0), (u'kickret_lng', 15), (u'kickret_lngtd', 0), (u'kickret_ret', 1), (u'kickret_avg', 15), (u'kickret_tds', 0)])
    # OrderedDict([(u'receiving_tds', 1), (u'receiving_lng', 128), (u'receiving_rec', 23), (u'receiving_twopta', 0), (u'receiving_yds', 258), (u'receiving_lngtd', 20), (u'receiving_twoptm', 0), (u'kickret_lng', 21), (u'kickret_lngtd', 0), (u'kickret_ret', 2), (u'kickret_avg', 21), (u'kickret_tds', 0)])

class AllKickersView(View):
    pass
    # 'kicking_xpmissed', 0), (u'kicking_totpfg', 87), (u'kicking_xptot', 27), (u'kicking_xpmade', 27), (u'kicking_fga', 33), (u'kicking_fgm', 29), (u'kicking_xpa', 27), (u'kicking_xpb', 0), (u'kicking_fgyds', 583)

class AllLinemenView(View):
    def get(self,request,year):
        year = int(year)
        games = nflgame.games(year)
        players = nflgame.combine(games)
        positions_list = ['NT','DT','DE']
        all_dline_list = []
        for p in players:
            if p.player.position in positions_list:
                name_slug = slugify(p.player.full_name.replace(' ', '_'))
                all_dline_list.append({'fullname' : p.player.full_name,'shortname':p.name, 'name_slug':name_slug,'position': p.player.position, 'team':p.team, 'profile_url':p.player.profile_url, 'number': p.player.uniform_number,'solo_tackles': p.defense_tkl, 'assisted_tackles': p.defense_ast, 'sacks':p.defense_sk, 'interceptions': p.defense_int, 'forced_fumbles':p.defense_ffum, 'recovered_fumbles':p.defense_ffum})
            return JsonResponse({'all_dline_list': all_dline_list})
        return HttpRep

class AllLinebackersView(View):
    def get(self,request,year):
        year = int(year)
        games = nflgame.games(year)
        players = nflgame.combine(games)
        positions_list = ['LB','OLB','MLB','ILB']
        all_lbers_list = []
        for p in players:
            if p.player.position in positions_list:
                name_slug = slugify(p.player.full_name.replace(' ', '_'))
                all_lbers_list.append({'fullname' : p.player.full_name,'shortname':p.name, 'name_slug':name_slug,'position': p.player.position, 'team':p.team, 'profile_url':p.player.profile_url, 'number': p.player.uniform_number,'solo_tackles': p.defense_tkl, 'assisted_tackles': p.defense_ast, 'sacks':p.defense_sk, 'interceptions': p.defense_int, 'forced_fumbles':p.defense_ffum, 'recovered_fumbles':p.defense_ffum})
        return JsonResponse({'all_lbers_list': all_lbers_list})


class AllDefensiveBacksView(View):
    def get(self,request,year):
        year = int(year)
        games = nflgame.games(year)
        players = nflgame.combine(games)
        positions_list = ['DB','CB','FS','SS']
        all_dbacks_list = []
        for p in players:
            if p.player.position in positions_list:
                name_slug = slugify(p.player.full_name.replace(' ', '_'))
                all_dbacks_list.append({'fullname' : p.player.full_name,'shortname':p.name, 'name_slug':name_slug,'position': p.player.position, 'team':p.team, 'profile_url':p.player.profile_url, 'number': p.player.uniform_number,'solo_tackles': p.defense_tkl, 'assisted_tackles': p.defense_ast, 'sacks':p.defense_sk, 'interceptions': p.defense_int, 'forced_fumbles':p.defense_ffum, 'recovered_fumbles':p.defense_ffum})
            return JsonResponse({'all_dbacks_list': all_dbacks_list})


class AllPuntersView(View):
    pass
    # u'punting_pts', 68), (u'punting_yds', 3138), (u'punting_i20', 29), (u'punting_lng', 899), (u'punting_avg', 633), (u'passing_att', 2), (u'passing_twoptm', 0), (u'passing_twopta', 0), (u'passing_yds', 27), (u'passing_cmp', 2), (u'passing_ints', 0), (u'passing_tds', 0)]

class QuarterbackView(View):
    def get(self,request,year,name_slug):
        game_stat_list = []
        year = int(year)
        p = get_player_season_stats(year, name_slug)
        if p.player.position == 'QB' and p[0].passing_att > 0:
            player_dict = {'fullname' : p[0].player.full_name, 'shortname':p[0].name, 'name_slug' : name_slug, 'position' : p[0].player.position, 'team':p[0].team, 'number': p[0].player.uniform_number, 'profile_url':p[0].player.profile_url}
            for x in range(len(p)):
                game_stat_list.append({'week':x+1, 'pass_attempts' : p[x].passing_att, 'pass_comps':p[x].passing_cmp, 'pass_yards' : p[x].passing_yds, 'pass_tds' : p[x].passing_tds, 'twoptconv_pass': p[x].passing_twoptm, 'interceptions_thrown' : p[x].passing_ints, 'qb_rating':p[x].passer_rating(), 'rush_attempts' : p[x].rushing_att, 'rush_yards': p[x].rushing_yds, 'rush_tds' : p[x].rushing_tds, 'twoptconv_rush': p[x].rushing_twoptm, 'fumbles_lost' : p[x].fumbles_lost})
            return JsonResponse({'player_dict':player_dict,'game_stat_list':game_stat_list})

class RunningbackView(View):
    pass
    # ['__add__', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattr__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__weakref__', '_add_stats', '_overwrite_stats', '_stats', 'formatted_stats', u'fumbles_lost', u'fumbles_rcv', u'fumbles_tot', u'fumbles_trcv', u'fumbles_yds', 'games', 'guess_position', 'has_cat', 'home', u'kickret_avg', u'kickret_lng', u'kickret_lngtd', u'kickret_ret', u'kickret_tds', 'name', 'passer_rating', 'player', 'playerid', u'receiving_lng', u'receiving_lngtd', u'receiving_rec', u'receiving_tds', u'receiving_twopta', u'receiving_twoptm', u'receiving_yds', u'rushing_att', u'rushing_lng', u'rushing_lngtd', u'rushing_tds', u'rushing_twopta', u'rushing_twoptm', u'rushing_yds', 'stats', 'tds', 'team', 'twopta', 'twoptm', 'twoptmissed']

class ReceiverView(View):
    pass
    # ['__add__', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattr__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__weakref__', '_add_stats', '_overwrite_stats', '_stats', 'formatted_stats', u'fumbles_lost', u'fumbles_rcv', u'fumbles_tot', u'fumbles_trcv', u'fumbles_yds', 'games', 'guess_position', 'has_cat', 'home', u'kickret_avg', u'kickret_lng', u'kickret_lngtd', u'kickret_ret', u'kickret_tds', 'name', 'passer_rating', 'player', 'playerid', u'receiving_lng', u'receiving_lngtd', u'receiving_rec', u'receiving_tds', u'receiving_twopta', u'receiving_twoptm', u'receiving_yds', u'rushing_att', u'rushing_lng', u'rushing_lngtd', u'rushing_tds', u'rushing_twopta', u'rushing_twoptm', u'rushing_yds', 'stats', 'tds', 'team', 'twopta', 'twoptm', 'twoptmissed']


class TightEndView(View):
    pass

class KickerView(View):
    pass

class LinemanView(View):
    def get(self,request,year,name_slug):
        game_stat_list = []
        year = int(year)
        positions_list = ['NT','DT','DE']
        p = get_player_season_stats(year,name_slug)
        if p.player.position in positions_list:
            player_dict = {'fullname' : p[0].player.full_name, 'shortname':p[0].name, 'name_slug' : name_slug, 'position' : p[0].player.position, 'team':p[0].team, 'number': p[0].player.uniform_number, 'profile_url':p[0].player.profile_url}
            for x in range(len(p)):
                game_stat_list.append({'solo_tackles': p[x].defense_tkl, 'assisted_tackles': p[x].defense_ast, 'sacks':p[x].defense_sk, 'interceptions': p[x].defense_int, 'forced_fumbles':p[x].defense_ffum, 'recovered_fumbles':p[x].defense_ffum})
            return JsonResponse({'player_dict':player_dict,'game_stat_list':game_stat_list})

class LinebackerView(View):
    def get(self,request,year,name_slug):
        game_stat_list = []
        year = int(year)
        positions_list = ['LB','OLB','MLB','ILB']
        p = get_player_season_stats(year,name_slug)
        if p.player.position in positions_list:
            player_dict = {'fullname' : p[0].player.full_name, 'shortname':p[0].name, 'name_slug' : name_slug, 'position' : p[0].player.position, 'team':p[0].team, 'number': p[0].player.uniform_number, 'profile_url':p[0].player.profile_url}
            for x in range(len(p)):
                game_stat_list.append({'solo_tackles': p[x].defense_tkl, 'assisted_tackles': p[x].defense_ast, 'sacks':p[x].defense_sk, 'interceptions': p[x].defense_int, 'forced_fumbles':p[x].defense_ffum, 'recovered_fumbles':p[x].defense_ffum})
            return JsonResponse({'player_dict':player_dict,'game_stat_list':game_stat_list})

class DefensiveBackView(View):
    def get(self,request,year,name_slug):
        game_stat_list = []
        year = int(year)
        positions_list = ['DB','CB','FS','SS']
        p = get_player_season_stats(year,name_slug)
        if p.player.position in positions_list:
            player_dict = {'fullname' : p[0].player.full_name, 'shortname':p[0].name, 'name_slug' : name_slug, 'position' : p[0].player.position, 'team':p[0].team, 'number': p[0].player.uniform_number, 'profile_url':p[0].player.profile_url}
            for x in range(len(p)):
                game_stat_list.append({'solo_tackles': p[x].defense_tkl, 'assisted_tackles': p[x].defense_ast, 'sacks':p[x].defense_sk, 'interceptions': p[x].defense_int, 'forced_fumbles':p[x].defense_ffum, 'recovered_fumbles':p[x].defense_ffum})
            return JsonResponse({'player_dict':player_dict,'game_stat_list':game_stat_list})

class PunterView(View):
    pass

class WeeklyMatchupView(View):
    def get(self,request,year,week):
        year = int(year)
        week = int(week.strip('week-'))
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
