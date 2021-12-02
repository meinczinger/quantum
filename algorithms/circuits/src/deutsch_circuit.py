import cirq
from cirq.circuits.circuit import Circuit
from cirq.devices.line_qubit import LineQubit

from algorithms.common.src.boolean_function import BooleanFunction
from cirq import H, X, CNOT, measure

class DeutschCircuit:
  def __init__(self, hidden_function:BooleanFunction) -> None:
      self.hidden_function = hidden_function
      self.circuit = self.create_circuit()
    
  def create_circuit(self):
    # The Deutsch circuit has two input qubits
    q0, q1 = cirq.LineQubit.range(2)
    
    # Create the oracle, which represents the hidden function as a unitary operator
    oracle = self.create_oracle(q0, q1)
    
    # Create the circuit, which is using the just created oracle
    return self.create_deutsch_circuit(q0, q1, oracle)
  
  def get_circuit(self) -> Circuit:
    return self.circuit
  
  def create_oracle(self, q0: LineQubit, q1: LineQubit) -> list:
    if self.hidden_function[[0]]:
        yield [CNOT(q0, q1), X(q1)]

    if self.hidden_function[[1]]:
        yield [CNOT(q0, q1)]

  def create_deutsch_circuit(self, q0: LineQubit, q1: LineQubit, oracle: list) -> Circuit:
      circuit = cirq.Circuit()

      # Initialize qubits
      circuit.append([X(q1), H(q1), H(q0)])

      # Add the oracle, which implements the hidden function
      circuit.append(oracle)

      # Measure the first qubit in standard basis
      # 0 as the result means the function is constant, 1 as the result means the function is balanced
      circuit.append([H(q0), measure(q0, key='result')])
      
      return circuit
