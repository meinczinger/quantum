import unittest
from algorithms.common.src.boolean_function import BooleanFunction

class TestBooleanFunction(unittest.TestCase):
  def test_access_function_value(self):
    bf = BooleanFunction(2, [1, 1, 1, 1])
    self.assertEqual(1, bf[[0, 1]])
  
  def test_if_one_dim_function_is_constant(self):
    bf = BooleanFunction(1, [1, 1])
    self.assertTrue(bf.is_constant())
    
  def test_if_two_dim_function_is_constant(self):
    bf1 = BooleanFunction(2, [1, 1, 1, 1])
    bf0 = BooleanFunction(2, [0, 0, 0, 0])
    self.assertTrue(bf0.is_constant() and bf1.is_constant())

  def test_if_one_dim_function_is_balanced(self):
    bf = BooleanFunction(1, [1, 0])
    self.assertTrue(bf.is_balanced())

if __name__ == '__main__':
    unittest.main()