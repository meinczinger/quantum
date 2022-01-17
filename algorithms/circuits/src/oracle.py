import cirq
import numpy as np
from algorithms.common.src.boolean_function import BooleanFunction


class Oracle(cirq.Gate):
  def __init__(self, f: BooleanFunction) -> None:
      super(Oracle, self)
      self.f = f
      
  def _num_qubits_(self) -> int:
      return self.f.dim() + 1
    
  def _unitary_(self) -> np.array:
    # the dimension of the domain of the function
    dim = self.f.dim()
    # Create a zero matrix with the proper size
    op = np.zeros(shape=(2**(dim + 1), 2**(dim + 1)), dtype=float)
    fvalues = self.f.get_function_values()
    # Populate this matrix
    for i in range(0, 2**(dim + 1), 2):
      # 1. case: |y> = 0
      col = i
      row =  col + fvalues[int(i/2)]
      op[row, col] = 1
      # 2. case: |y> = 1
      col = i + 1
      row = col - fvalues[int(i/2)]
      op[row, col] = 1
      
    return op / np.sqrt(2**dim)

  def _circuit_diagram_(self, args):
    return "G"