import unittest
from algorithms.common.src.boolean_function import BooleanFunction
from algorithms.deutsch.src.deutsch import AlgorithmDeutsch

class TestDeutschAlgorithm(unittest.TestCase):
    def test_if_function_is_constant(self):
      # create a constant function
      f = BooleanFunction(1, [1, 1])
      # Ensure the function is really constant
      self.assertTrue(f.is_constant())
      # create Deutsch algorithm
      alg = AlgorithmDeutsch(f)
      output = alg.run()
      # For constant functions, the algorithm returns 0
      self.assertEqual(0, output)

    def test_if_function_is_balanced(self):
      # create a balanced function
      f = BooleanFunction(1, [1, 0])
      # Ensure the function is really balanced
      self.assertTrue(f.is_balanced())
      # create Deutsch algorithm
      alg = AlgorithmDeutsch(f)
      output = alg.run()
      # For balanced functions, the algorithm returns 1
      self.assertEqual(1, output)

if __name__ == '__main__':
    unittest.main()