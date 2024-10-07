from rt_with_exceptions import Runner
import unittest, logging

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            second = Runner('Илья', 5)
            logging.info(f'"test_walk" выполнен успешно')
            walk_test = Runner('Walker_one')
            for i in range(10):
                second.walk()
            self.assertEqual(walk_test.distance, 50)
        except:
            logging.warning(f"Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            first = Runner('sdfs', 10)
            logging.info(f'"test_run" выполнен успешно')
            run_test = Runner('Runner_two')
            for i in range(10):
                first.run()
            self.assertEqual(run_test.distance, 100)
        except:
            logging.warning(f"Неверный тип данных для объекта Runner", exc_info=True)



if __name__ == "__main__":
    unittest.main()


logging.basicConfig(level=logging.INFO, filename='mylog.log', filemode='w', encoding='utf-8',
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")


