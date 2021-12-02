import random

class BooleanFunction:
  def __init__(self, dimension: int, values:tuple=()) -> None:
    # The number of parameters of the booelan function
    self.dimension = dimension
    # The function values, either provided here or generated randomly
    self.function_values = values
    
  def get_function_values(self) -> tuple:
    """ 
    Returns the function values 
    The list has 2^dimenion elements
    """
    # If the values were provided in the constructor, use those, otherwise create a random boolean function
    if self.function_values == []:
      self.function_values =(random.randint(0, 1) for _ in range(2**self.dimension))
    return self.function_values
  
  def __getitem__(self, key:tuple) -> int:
    """ 
    Gets an item by an list
    E.g., in three dimensions, a potential input is [0, 0, 1], the 
    return value is the function value f(0, 0, 1)
    """
    index_key = 0
    for i in range(self.dimension):
      index_key += (key[i] * 2**(self.dimension - i - 1))
    return self.function_values[index_key]
  
  def is_balanced(self) -> bool:
    """ 
    Checks if the function is balanced. 
    Definition of balanced: half of the possible elemts from the domain of the function map to 0 and the other half to 1
    """
    return sum(x ==1 for x in self.function_values) == 2**(self.dimension - 1)
  
  def is_constant(self) -> bool:
    """ Checks if the function is constant """
    return all(e == 1 for e in self.function_values) or all(e == 0 for e in self.function_values)
  
