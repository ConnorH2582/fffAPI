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
