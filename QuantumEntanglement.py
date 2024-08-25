from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Crear un circuito cuántico con 2 qubits
qc = QuantumCircuit(2, 2)

# Crear un estado de Bell |Φ+> = (|00> + |11>) / √2
qc.h(0)  # Aplicar Hadamard en el primer qubit
qc.cx(0, 1)  # Aplicar CNOT con el primer qubit como control y el segundo como objetivo

# Medir en la base computacional
qc.measure([0, 1], [0, 1])

# Simular el circuito cuántico
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
counts = result.get_counts()

# Mostrar los resultados de la medición
plot_histogram(counts)
plt.title("Medición en la base computacional (|0⟩, |1⟩)")
plt.show()

# Ahora, medir en la base de Hadamard (|+⟩, |−⟩)
qc = QuantumCircuit(2, 2)
qc.h(0)  # Crear estado de Bell
qc.cx(0, 1)

# Aplicar Hadamard en ambos qubits para cambiar la base
qc.h(0)
qc.h(1)

# Medir
qc.measure([0, 1], [0, 1])

# Simular
result = execute(qc, simulator, shots=1024).result()
counts = result.get_counts()

# Mostrar los resultados de la medición en la base de Hadamard
plot_histogram(counts)
plt.title("Medición en la base de Hadamard (|+⟩, |−⟩)")
plt.show()
