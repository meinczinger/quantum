from cgitb import reset
from typing import List
import cirq
from cirq.circuits.circuit import Circuit
from cirq.devices.line_qubit import LineQubit

from algorithms.common.src.boolean_function import BooleanFunction
from algorithms.circuits.src.oracle import Oracle
from cirq import H, X, CNOT, measure

class DeutschJozsaCircuit:
  def __init__(self, hidden_function:BooleanFunction) -> None:
      self.function_dim = hidden_function.dim()
      self.hidden_function = hidden_function
      self.circuit = self.create_circuit()
    
  def create_circuit(self):
    # The Deutsch circuit has two input qubits
    inputs = LineQubit.range(self.function_dim + 1)
    
    # Create the oracle, which represents the hidden function as a unitary operator
    oracle = self.create_oracle()
    
    # Create the circuit, which is using the just created oracle
    return self.create_deutsch_circuit(inputs, oracle)
  
  def get_circuit(self) -> Circuit:
    return self.circuit
  
  def create_oracle(self: LineQubit) -> cirq.Gate:
    return Oracle(self.hidden_function)

  def create_deutsch_circuit(self, inputs, oracle: cirq.Gate) -> Circuit:
      circuit = cirq.Circuit()

      # Initialize qubits
      # The first qubit needs to be in state |0> and the second in state |1>, as qbits are by default
      # in state |0>, for the second qubit we need a not (Pauli X) first to make it a |1>
      circuit.append([X(inputs[-1]), H(inputs[-1])])

      # Apply Hadamard on the first n qubits      
      circuit.append(H.on_each(inputs[:-1]))

      # Add the oracle, which implements the hidden function
      circuit.append([oracle.on(*inputs)])

      # After the oracle was applied, apply the Hadamard on the first n qubit
      circuit.append([H.on_each(inputs[:-1])])
  
      # Measurment part
      # At this stage, if the function is constant, all n qubits are in |0> state, if not, 
      # the function is balanced
      # Insteda of measuring each qubit, the following steps are done
    
      # Apply a NOT on each of the n qubits
      circuit.append([X.on_each(inputs[:-1])])

      # Apply the Hadmard on the auxiliary bit, it will become |1>         
      circuit.append(H(inputs[-1]))

      # Apply an N-Toffoli now, if the function is constant, then all n qubits are in zero and
      # after the previous NOT, all are 1, the N-Toffoli will have result 0. For 
      # balanced, it will have result 1      
      cnx = X.controlled(self.function_dim).on(*inputs[:-1], inputs[-1])
      circuit.append(cnx)
                 
      # Append the measurment of the result of the N-Toffoli gate                   
      circuit.append([measure(inputs[-1], key='result')])     
      
      return circuit
