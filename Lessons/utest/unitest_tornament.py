import runner_and_tournament
import unittest

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
        for key, value in cls.all_results.values():
            print(key, ':', value)


    def test_usein_vs_nick(self):
        a = self.usein
        b = self.nick
        tournament = runner_and_tournament.Tournament(90, a, b)
        print(tournament)
        print(a)
        print(b)

        result = tournament.start()
        print(result)
        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()