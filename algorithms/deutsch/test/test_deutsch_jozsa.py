import unittest
from algorithms.common.src.boolean_function import BooleanFunction
from algorithms.deutsch.src.deutsch_jozsa import AlgorithmDeutschJozsa

class TestDeutschJozsaAlgorithm(unittest.TestCase):
    def test_if_function_is_constant_dim1(self):
      # create a constant function
      f = BooleanFunction(1, [0, 0])
      self.assertTrue(f.is_constant())
      # create Deutsch algorithm
      alg = AlgorithmDeutschJozsa(f)
      output = alg.run()
      # For constant functions, the algorithm returns 0
      self.assertEqual(0, output)

    def test_if_function_is_balanced_dim1(self):
      # create a balanced function
      f = BooleanFunction(1, [1, 0])
      self.assertTrue(f.is_balanced())
      # create Deutsch algorithm
      alg = AlgorithmDeutschJozsa(f)
      output = alg.run()
      # For balanced functions, the algorithm returns 1
      self.assertEqual(1, output)

    def test_if_function_is_constant_dim2(self):
      # create a constant function
      f = BooleanFunction(2, [0, 0, 0, 0])
      self.assertTrue(f.is_constant())
      # create Deutsch algorithm
      alg = AlgorithmDeutschJozsa(f)
      output = alg.run()
      # For constant functions, the algorithm returns 0
      self.assertEqual(0, output)

    def test_if_function_is_balanced_dim2(self):
      # create a balanced function
      f = BooleanFunction(2, [0, 0, 1, 1])
      self.assertTrue(f.is_balanced())
      # create Deutsch algorithm
      alg = AlgorithmDeutschJozsa(f)
      output = alg.run()
      # For balanced functions, the algorithm returns 1
      self.assertEqual(1, output)

    def test_if_function_is_constant_dim3(self):
      # create a constant function
      f = BooleanFunction(3, [1, 1, 1, 1, 1, 1, 1, 1])
      self.assertTrue(f.is_constant())
      # create Deutsch algorithm
      alg = AlgorithmDeutschJozsa(f)
      output = alg.run()
      # For constant functions, the algorithm returns 0
      self.assertEqual(0, output)

    def test_if_function_is_balanced_dim3(self):
      # create a balanced function
      f = BooleanFunction(3, [0, 0, 1, 1, 1, 0, 1, 0])
      self.assertTrue(f.is_balanced())
      # create Deutsch algorithm
      alg = AlgorithmDeutschJozsa(f)
      output = alg.run()
      # For balanced functions, the algorithm returns 1
      self.assertEqual(1, output)

if __name__ == '__main__':
    unittest.main()