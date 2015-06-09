from django.test import TestCase,Client
import unittest
import json
# Create your tests here.

class TestMyModule(unittest.TestCase): #must inherit
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_matchup_requests(self):
        res = self.client.get('/fballAPI/2014/week-10/matchups/')
        self.assertEqual(res.status_code,200)
        string_dict = res.content
        matchup_dict = json.loads(string_dict)
        self.assertEqual(len(matchup_dict['week_10_schedule']), matchup_dict['game_count'])

    def test_scores_requests(self):
        res = self.client.get('/fballAPI/2014/week-10/scores/')
        self.assertEqual(res.status_code,200)
        string_dict = res.content
        scores_dict = json.loads(string_dict)
        print(scores_dict['week_10_scores'])
        print(len(scores_dict['week_10_scores']))
        self.assertEqual(len(scores_dict['week_10_scores']), scores_dict['game_count'])
        scores_list = []
        for game in scores_dict['week_10_scores']:
            scores_list.append(game['away']['score'])
            scores_list.append(game['home']['score'])
        for score in scores_list:
            self.assertIsInstance(score, int)

    def test_winners(self):
        res = self.client.get('/fballAPI/2014/week-10/winners/')
        self.assertEqual(res.status_code,200)
        string_dict = res.content
        winners_dict = json.loads(string_dict)
        self.assertEqual(len(winners_dict['winning_teams']), winners_dict['game_count'])

    def test_losers(self):
        res = self.client.get('/fballAPI/2014/week-10/losers/')
        self.assertEqual(res.status_code,200)
        string_dict = res.content
        losers_dict = json.loads(string_dict)
        self.assertEqual(len(losers_dict[
        'losing_teams']), losers_dict['game_count'])

if __name__ == '__main__':
    unittest.main()
