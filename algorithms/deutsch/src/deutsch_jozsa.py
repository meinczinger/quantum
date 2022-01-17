from cirq.study import resolver
from algorithms.common.src.boolean_function import BooleanFunction
from algorithms.circuits.src.deutsch_jozsa_circuit import DeutschJozsaCircuit
import cirq

class AlgorithmDeutschJozsa:
  def __init__(self, hidden_function: BooleanFunction) -> None:
    """
    """
    self.circuit = DeutschJozsaCircuit(hidden_function).get_circuit()

  def run(self) -> int:
    # simulate
    simulator = cirq.Simulator()
    result = simulator.run(self.circuit)
    return result.data.iloc[0][0]
        
