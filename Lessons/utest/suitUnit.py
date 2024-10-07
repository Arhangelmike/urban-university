import unittest
import unittest1
import unitdrop

RunTest = unittest.TestSuite()
RunTest.addTest(unittest.TestLoader().loadTestsFromTestCase(unittest1.RunnerTest))
RunTest.addTest(unittest.TestLoader().loadTestsFromTestCase(unitdrop.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(RunTest)