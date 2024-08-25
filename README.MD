# Basic-implementation-of-a-quantum-key-exchange-protocol-using-Qiskit

This simulation, does the following:

1) Generate a pair of entangled qubits in the Bell state. Bell states are typical examples of entangled states.

2) Simulate measurements in different bases on the qubits to demonstrate the correlation between them.

3) Visualize the correlation using a Bloch sphere or bar graphs to show how measurements in different bases are correlated.


Using the bell state
![image alt][https://github.com/BomBe1939/Basic-implementation-of-a-quantum-key-exchange-protocol-using-Qiskit/blob/main/bell-state.PNG]

#Instalation

This code uses qiskit to simulate quantum entanglement and qubit measurement in different bases. If you don't have qiskit installed yet, you can install it with:

```pip install qiskit```

# Procedure

 A circuit with two qubits is created. The Hadamard gate H is applied to the first qubit, followed by a CNOT gate to entangle the qubits, forming the Bell state. Therefore, they are measured in the standard basis and the distribution of results is visualized. Given the entanglement, you should see a strong correlation between the qubits. Lastly the Hadamard gate is applied to both qubits to measure on a different basis. This shows how entanglement persists even on different bases.

# Expected Results

- Measurement at the Computational Base: You should see that only the states appear, reflecting entanglement.
- Measurement in the Hadamard Basis: Again, you should see that only correlated states appear, showing that the qubits are entangled.

You can expand or modify it to explore other quantum properties, such as:

# Change Bell Status






