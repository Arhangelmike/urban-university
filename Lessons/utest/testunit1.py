import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usein = runner_and_tournament.Runner("Усэйн", 10)
        self.andrey = runner_and_tournament.Runner("Андрей", 9)
        self.nick = runner_and_tournament.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        res = dict(reversed(list(TournamentTest.all_results.items())))
        for key, value in res.items():
            result_str = {place: str(runner) for place, runner in value.items()}
            print(result_str)

    def test_usein_vs_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.usein, self.nick)
        result = tournament.start()
        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_andrey_vs_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_all_vs_all(self):
        tournament = runner_and_tournament.Tournament(90, self.usein, self.andrey, self.nick)
        result = tournament.start()
        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")


if __name__ == "__main__":
    unittest.main()
