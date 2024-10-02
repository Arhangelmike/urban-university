import runner, unittest
class RunnerTest(TestCase):

    def test_walk(self):
        walk_test1 = Runner.walk
        for wt in range(1, 10):
            wt = walk_test1
            print(wt)
        self.assertEqual(wt.distance, 50)
    def test_run(self):
        pass
    def test_challenge(self):
        pass
