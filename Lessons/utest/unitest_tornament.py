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
        for result in cls.all_results.values():
            print(result)
'''tearDownClass - метод, где выводятся all_results по очереди в столбец.выполняеться в конце'''

    def tournament_usein_vs_nick(self):
        Tournament = runner_and_tournament.Tournament(90, self.usein, self.nick)
        result = Tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")
