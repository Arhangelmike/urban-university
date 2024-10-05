import runner_and_tournament
import unittest
from collections import OrderedDict

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''setUpClass - метод, где создаётся атрибут класса all_results. Это словарь
         в который будут сохраняться результаты всех тестов.'''
        cls.all_results = {}

    def setUp(self):
        self.usein = runner_and_tournament.Runner("Усэйн", 10)
        self.andrey = runner_and_tournament.Runner("Андрей", 9)
        self.nick = runner_and_tournament.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in TournamentTest.all_results.items():
            # Преобразуем объект Runner в строку, вызывая метод str()
            result_str = {place: str(runner) for place, runner in value.items()}
            print(result_str)
            # res = dict(reversed(list(result_str.items())))
            # print(res)


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

# result_str = {}
# for place, runner in value.items():
#     result_str[place] = str(runner)