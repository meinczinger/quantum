import cirq
import numpy as np
from algorithms.common.src.boolean_function import BooleanFunction


class Oracle(cirq.Gate):
  def __init__(self, f: BooleanFunction) -> None:
      super(Oracle, self)
      self.f = f
      
  def _num_qubits_(self) -> int:
      return 2
    
  def _unitary_(self) -> np.array:
     return np.array([
            [0.0,  1.0, 0.0,  0.0],
            [1.0,  0.0, 0.0,  0.0],
            [0.0,  0.0, 0.0,  1.0],
            [0.0,  0.0, 1.0,  0.0]
        ]) / np.sqrt(2)

  def _circuit_diagram_(self, args):
    return "G"