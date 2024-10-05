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
'''setUp - метод, где создаются 3 объекта -  пары значений имени и скорости'''

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.values():
            print(key, ':', value)
'''tearDownClass - метод выполняеться в конце, печать словарая  all_results по очереди в столбец'''

    def usein_vs_nick(self):

        tournament = runner_and_tournament.Tournament(90, self.usein, self.nick)
        result = tournament.start()
        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()