from typing import List
import cirq
from cirq.circuits.circuit import Circuit
from cirq.devices.line_qubit import LineQubit

from algorithms.common.src.boolean_function import BooleanFunction
from algorithms.circuits.src.oracle import Oracle
from cirq import H, X, CNOT, measure

class DeutschJozsaCircuit:
  def __init__(self, function_dim:int, hidden_function:BooleanFunction) -> None:
      self.function_dim = function_dim
      self.hidden_function = hidden_function
      self.circuit = self.create_circuit()
    
  def create_circuit(self):
    # The Deutsch circuit has two input qubits
    q0 = cirq.LineQubit.range(self.function_dim)
    q1 = cirq.NamedQubit('q1')
    
    # Create the oracle, which represents the hidden function as a unitary operator
    oracle = self.create_oracle(q0, q1)
    
    # Create the circuit, which is using the just created oracle
    return self.create_deutsch_circuit(q0, q1, oracle)
  
  def get_circuit(self) -> Circuit:
    return self.circuit
  
  def create_oracle(self, q0, q1: LineQubit) -> cirq.Gate:
    return Oracle(self.hidden_function)

  def create_deutsch_circuit(self, q0, q1: LineQubit, oracle: cirq.Gate) -> Circuit:
      circuit = cirq.Circuit()

      # Initialize qubits
      # The first qubit needs to be in state |0> and the second in state |1>, as qbits are by default
      # in state |0>, for the second qubit we need a not (Pauli X) first to make it a |1>
      circuit.append([X(q1), H(q1), H.on_each(*q0)])

      # Add the oracle, which implements the hidden function
      circuit.append(oracle.on(*q0))

      # Measure the first qubit in standard basis
      # 0 as the result means the function is constant, 1 as the result means the function is balanced
      circuit.append([H.on_each(*q0), measure(*q0, key='result')])
      
      return circuit
