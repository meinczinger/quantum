from cirq.study import resolver
from algorithms.common.src.boolean_function import BooleanFunction
from algorithms.circuits.src.deutsch_circuit import DeutschCircuit
import cirq
from cirq import H, X, CNOT, measure

class AlgorithmDeutsch:
  def __init__(self, hidden_function: BooleanFunction) -> None:
    """
    """
    self.circuit = DeutschCircuit(hidden_function).get_circuit()

  def run(self) -> int:
    # simulate
    simulator = cirq.Simulator()
    result = simulator.run(self.circuit)
    return result.data.iloc[0][0]
        
