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

def convert_month(month_int):
    months_dict = {9:'September', 10:'October', 11:'November',12:'December',1:'January'}
    return months_dict[month_int]

def convert_weekday(wday):
    wday_dict = {'Mon':'Monday','Thu':'Thursday','Sat':'Saturday','Sun':'Sunday'}
    return wday_dict[wday]

def get_matchups(year, week):
    pass
    away_teams_dict = {}
    home_teams_dict = {}
    matchups_list = []
    games = nflgame.games(year, week)
    for g in games:
        game = {'home':get_full_team_name(g.home),
                'away':get_full_team_name(g.away),
                'month': convert_month(g.schedule['month']),
                'day': g.schedule['day'],
                'weekday': convert_weekday(g.schedule['wday']),
                'time': g.schedule['time']}
        matchups_list.append(game)
    return matchups_list

def get_scores(year,week):
    games = nflgame.games(year, week)
    home_scores_dict = {}
    away_scores_dict = {}
    scores_list = []
    for g in games:
        game = {'home':
                    {'teamname':get_full_team_name(g.home),
                    'score':g.score_home},
                'away':
                    {'teamname':get_full_team_name(g.away),
                    'score':g.score_away},
                'winner':
                    {'teamname':get_full_team_name(g.winner)}
                }
        scores_list.append(game)
    return scores_list

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
