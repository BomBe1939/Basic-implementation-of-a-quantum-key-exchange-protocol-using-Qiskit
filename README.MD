# Basic-implementation-of-a-quantum-key-exchange-protocol-using-Qiskit

This simulation, does the following:

1) Generate a pair of entangled qubits in the Bell state. Bell states are typical examples of entangled states.

2) Simulate measurements in different bases on the qubits to demonstrate the correlation between them.

3) Visualize the correlation using a Bloch sphere or bar graphs to show how measurements in different bases are correlated.


Using the bell state
![Texto alternativo](https://github.com/BomBe1939/Basic-implementation-of-a-quantum-key-exchange-protocol-using-Qiskit/blob/main/bell-state.PNG)

# Instalation

This code uses qiskit to simulate quantum entanglement and qubit measurement in different bases. If you don't have qiskit installed yet, you can install it with:

```pip install qiskit```

# Procedure

 A circuit with two qubits is created. The Hadamard gate H is applied to the first qubit, followed by a CNOT gate to entangle the qubits, forming the Bell state. Therefore, they are measured in the standard basis and the distribution of results is visualized. Given the entanglement, you should see a strong correlation between the qubits. Lastly the Hadamard gate is applied to both qubits to measure on a different basis. This shows how entanglement persists even on different bases.

# Expected Results

- Measurement at the Computational Base: You should see that only the states appear, reflecting entanglement.
- Measurement in the Hadamard Basis: Again, you should see that only correlated states appear, showing that the qubits are entangled.

You can expand or modify it to explore other quantum properties.

# Change Bell Status

```qc.h(0)
qc.cx(0, 1)
qc.x(1)  # Invertir el segundo qubit para cambiar a |Ψ+⟩
```

```qc.h(0)
qc.cx(0, 1)
qc.z(0)  # Aplicar una puerta Z en el primer qubit para cambiar a |Φ−⟩
```

```qc.h(0)
qc.cx(0, 1)
qc.x(1)  # Invertir el segundo qubit para |Ψ+⟩
qc.z(0)  # Aplicar una puerta Z en el primer qubit para cambiar a |Ψ−⟩
```

# Add more Qubits

You can extend the code to entangle more than two qubits. Here's how to entangle three qubits in a GHZ state:
```qc = QuantumCircuit(3, 3)  # Tres qubits
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)  # Aplicar CNOT en el tercer qubit
qc.measure([0, 1, 2], [0, 1, 2])
```

# Measurements at Different Bases

You can measure on different bases by combining doors before measurement:
```qc.sdg(0)  # Aplicar puerta S† en el primer qubit (cambio a base Y)
qc.h(0)    # Aplicar Hadamard
qc.sdg(1)  # Aplicar puerta S† en el segundo qubit (cambio a base Y)
qc.h(1)    # Aplicar Hadamard
```

# Change the Number of Shots
You can modify the number of times you run the simulation to see how the statistical results change: 

```result = execute(qc, simulator, shots=4096).result()  # Cambiar a 4096 tiros```

# Display in Different Formats
Instead of using a bar chart, you can try other visualizations. For example, using qiskit to represent the Bloch sphere:
```from qiskit.visualization import plot_bloch_multivector
statevector = execute(qc, Aer.get_backend('statevector_simulator')).result().get_statevector()
plot_bloch_multivector(statevector)
plt.show()
```
If you try these modifications, you will gain a deeper understanding of how entanglement works and how measurements on different bases affect the results.


# The protocol BB84 (AliceBob)

Alice prepares qubits on a random basis (computational or Hadamard) then Alice sends the qubits to Bob, who also measures on a random basis. Alice and Bob publicly compare the bases they used for each qubit. If the bases match, the results of their measurements should match, and these bits are used to form a key. If an eavesdropper (Eve) tries to intercept the key, the interference introduced will be detectable, since it will alter the measurement results.

# Explanation of the Code

Alice creates a random sequence of bits and bases (0 for computational basis, 1 for Hadamard basis), depending on the bits and bases, Alice prepares a qubit in the state ∣0⟩,∣1⟩,∣+⟩ or 
∣−⟩. Bob also randomly chooses bases and measures the qubits he received, so A and B compare their bases, and only those qubits that were measured in the same bases are used to form the shared key.

This code is a first step towards quantum cryptography. You can build on it to simulate a noisy channel or include an eavesdropper that tries to intercept the qubits.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project uses [Qiskit](https://qiskit.org/), which is licensed under the Apache License 2.0.

```bibtex
@misc{qiskit2024,
  title={Quantum computing with {Q}iskit},
  author={Javadi-Abhari, Ali and Treinish, Matthew and Krsulich, Kevin and Wood, Christopher J. and Lishman, Jake and Gacon, Julien and Martiel, Simon and Nation, Paul D. and Bishop, Lev S. and Cross, Andrew W. and Johnson, Blake R. and Gambetta, Jay M.},
  year={2024},
  doi={10.48550/arXiv.2405.08810},
  eprint={2405.08810},
  archivePrefix={arXiv},
  primaryClass={quant-ph}
}
