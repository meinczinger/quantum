import unittest
from algorithms.common.src.boolean_function import BooleanFunction
from algorithms.deutsch.src.deutsch_jozsa import AlgorithmDeutschJozsa

class TestDeutschJozsaAlgorithm(unittest.TestCase):
    def test_if_function_is_constant(self):
      # create a constant function
      f = BooleanFunction(2, [1, 1, 1, 1])
      self.assertTrue(f.is_constant())
      # create Deutsch algorithm
      alg = AlgorithmDeutschJozsa(2, f)
      output = alg.run()
      # For constant functions, the algorithm returns 0
      self.assertEqual(0, output)

    # def test_if_function_is_balanced(self):
    #   # create a constant function
    #   f = BooleanFunction(1, [1, 0])
    #   self.assertTrue(f.is_balanced())
    #   # create Deutsch algorithm
    #   alg = AlgorithmDeutschJozsa(2, f)
    #   output = alg.run()
    #   # For constant functions, the algorithm returns 0
    #   self.assertEqual(1, output)

if __name__ == '__main__':
    unittest.main()