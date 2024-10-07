import runner_and_tournament as rat
import unittest
from unittest import TestCase
class TournamentTest(TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.usein = rat.Runner("Усэйн", 10)
        self.andrey = rat.Runner("Андрей", 9)
        self.nick = rat.Runner("Ник", 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usein_vs_nick(self):
        tournament = rat.Tournament(90, self.usein, self.nick)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_vs_nick(self):
        tournament = rat.Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_all_vs_all(self):
        tournament = rat.Tournament(90, self.usein, self.andrey, self.nick)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(f'{i + 1}. {elem}')


if __name__ == "__main__":
    unittest.main()