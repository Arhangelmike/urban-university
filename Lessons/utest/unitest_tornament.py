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
        # self.runners = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}



    @classmethod
    def tearDownClass(cls):
        # for key, value in TournamentTest.all_results.items():
        #     print(key, '-:-', value)
        for key, value in TournamentTest.all_results.items():
            # Преобразуем объект Runner в строку, вызывая метод str()
            result_str = {place: str(runner) for place, runner in value.items()}
            print(key, '-:-', result_str)


    def test_usein_vs_nick(self):
        a = self.usein
        b = self.nick
        tournament = runner_and_tournament.Tournament(90, a, b)
        result = tournament.start()
        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = result.values()
        self.assertTrue(result[max(result.keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()