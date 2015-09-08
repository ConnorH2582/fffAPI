from django.utils.text import slugify
import nflgame


def get_full_team_name(scoreboard_team_name):
    teams_dict = {'NYG':'New York Giants','PHI':'Philadelphia Eagles','DAL':'Dallas Cowboys','WAS':'Washington Redskins', 'NYJ':'New York Jets', 'NE': 'New England Patriots', 'MIA':'Miami Dolphins','BUF':'Buffalo Bills', 'TEN':'Tennessee Titans', 'HOU': 'Houston Texans', 'IND':'Indianapolis Colts','JAC':'Jacksonville Jaguars', 'OAK':'Oakland Raiders', 'DEN':'Denver Broncos','KC':'Kansas City Chiefs', 'SD':'San Diego Chargers','ATL':'Atlanta Falcons','CAR':'Carolina Panthers','NO':'New Orleans Saints','TB':'Tampa Bay Buccaneers','CHI':'Chicago Bears','MIN':'Minnesota Vikings','GB':'Green Bay Packers','DET':'Detroit Lions','ARI':'Arizona Cardinals','STL':'St. Louis Rams','SF':'San Francisco 49ers','SEA':'Seattle Seahawks','PIT':'Pittsburgh Steelers','BAL':'Baltimore Ravens', 'CLE':'Cleveland Browns','CIN':'Cincinnati Bengals'}
    return teams_dict.get(scoreboard_team_name)

def convert_month(month_int):
    months_dict = {9:'September', 10:'October', 11:'November',12:'December'}
    return months_dict.get(month_int)

def convert_weekday(wday):
    wday_dict = {'Mon':'Monday','Thu':'Thursday','Sat':'Saturday','Sun':'Sunday'}
    return wday_dict.get(wday)

def get_matchups(year, week):
    away_teams_dict = {}
    home_teams_dict = {}
    matchups_list = []
    next_year = str(int(year)+1)
    games = nflgame.sched.games
    for key, value in games.items():
        if key[0:4] == year or key[0:4] == next_year:
            if value.get('week') == int(week):
                if value.get('season_type') == 'REG':
                    game = {'home':get_full_team_name(value.get('home')),
                            'away':get_full_team_name(value.get('away')),
                            'month': convert_month(value.get('month')),
                            'day': value.get('day'),
                            'weekday': convert_weekday(value.get('wday')),
                            'time': value.get('time')}
                    matchups_list.append(game)
    print(matchups_list)
    return matchups_list

def get_scores(year,week):
    games = nflgame.games(year, week)
    home_scores_dict = {}
    away_scores_dict = {}
    scores_list = []
    for g in games:
        if get_full_team_name(g.winner):
            game = {'home':
                        {'teamname':get_full_team_name(g.home),
                        'score':g.score_home},
                    'away':
                        {'teamname':get_full_team_name(g.away),
                        'score':g.score_away},
                    'winner':
                        {'teamname':get_full_team_name(g.winner)}
                    }
        else:
            game = {'home':
                        {'teamname':get_full_team_name(g.home),
                        'score':g.score_home},
                    'away':
                        {'teamname':get_full_team_name(g.away),
                        'score':g.score_away},
                    'winner':
                        {'teamname':"TIE"}
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
