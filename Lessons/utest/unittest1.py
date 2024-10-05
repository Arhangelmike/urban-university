from unittest import TestCase
from runner_and_tournament import Runner
import unittest

class RunnerTest(TestCase):

    def test_walk(self):
        walk_test = Runner('Walker_one')
        for i in range(10):
            walk_test.walk()
        self.assertEqual(walk_test.distance, 50)

    def test_run(self):
        run_test = Runner('Runner_two')
        for i in range(10):
            run_test.run()
        self.assertEqual(run_test.distance, 100)

    def test_challenge(self):
        ch_test1 = Runner('challenger_three')
        ch_test2 = Runner('challenger_four')
        for i in range(10):
            ch_test1.walk()
            ch_test2.run()
        self.assertNotEqual(ch_test1.distance, ch_test2.distance)


if __name__ == "__main__":
    unittest.main()