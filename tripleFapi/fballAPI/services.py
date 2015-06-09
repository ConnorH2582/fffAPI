from django.utils.text import slugify
import nflgame

def get_player_season_stats(year,name_slug):
    games_list = []
    for x in range(1,18):
        games = nflgame.games(year, x)
        players = nflgame.combine(games)
        for p in players:
            if slugify(p.player.full_name.replace(' ','_')) == name_slug:
                games_list.append(p)
    return games_list

def get_full_team_name(scoreboard_team_name):
    teams_dict = {'NYG':'New York Giants','PHI':'Philadelphia Eagles','DAL':'Dallas Cowboys','WAS':'Washington Redskins', 'NYJ':'New York Jets', 'NE': 'New England Patriots', 'MIA':'Miami Dolphins','BUF':'Buffalo Bills', 'TEN':'Tennessee Titans', 'HOU': 'Houston Texans', 'IND':'Indianapolis Colts','JAC':'Jacksonville Jaguars', 'OAK':'Oakland Raiders', 'DEN':'Denver Broncos','KC':'Kansas City Chiefs', 'SD':'San Diego Chargers','ATL':'Atlanta Falcons','CAR':'Carolina Panthers','NO':'New Orleans Saints','TB':'Tampa Bay Buccaneers','CHI':'Chicago Bears','MIN':'Minnesota Vikings','GB':'Green Bay Packers','DET':'Detroit Lions','ARI':'Arizona Cardinals','STL':'St. Louis Rams','SF':'San Francisco 49ers','SEA':'Seattle Seahawks','PIT':'Pittsburgh Steelers','BAL':'Baltimore Ravens', 'CLE':'Cleveland Browns','CIN':'Cincinnati Bengals'}
    return teams_dict[scoreboard_team_name]

def get_scheduled_home_teams(year, week):
    home_teams_list = []
    games = nflgame.games(year, week)
    for g in games:
        home_teams_list.append(get_full_team_name(g.home))
    return home_teams_list

def get_scheduled_away_teams(year, week):
    away_teams_list = []
    games = nflgame.games(year, week)
    for g in games:
        away_teams_list.append(get_full_team_name(g.away))
    return away_teams_list

def get_home_scores(year,week):
    home_teams_list = []
    home_team_scores = []
    games = nflgame.games(year, week)
    for g in games:
        home_teams_list.append(get_full_team_name(g.home))
        home_team_scores.append(g.score_home)
    home_score_list = zip(home_teams_list, home_team_scores)
    return home_score_list


def get_away_scores(year,week):
    away_teams_list = []
    away_team_scores = []
    games = nflgame.games(year, week)
    for g in games:
        away_teams_list.append(get_full_team_name(g.away))
        away_team_scores.append(g.score_away)
    away_score_list = zip(away_teams_list, away_team_scores)
    return away_score_list

def get_winners(year,week):
    winning_teams_list = []
    games = nflgame.games(year, week)
    for g in games:
        winning_teams_list.append(get_full_team_name(g.winner))
    return winning_teams_list

def get_losers(year,week):
    losing_teams_list = []
    games = nflgame.games(year, week)
    for g in games:
        losing_teams_list.append(get_full_team_name(g.loser))
    return losing_teams_list

# def get_team_record(year,team):
