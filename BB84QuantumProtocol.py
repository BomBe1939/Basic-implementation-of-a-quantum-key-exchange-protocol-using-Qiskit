import numpy as np
from qiskit import QuantumCircuit, Aer, execute

# Mensaje que queremos encriptar
message = np.array([1, 1, 0, 1, 1])  # El mensaje "11011"
num_bits = len(message)  # El tamaño de la clave debe ser igual al del mensaje

# Paso 1: Alice genera una secuencia de bits y bases aleatorios
alice_bits = np.random.randint(2, size=num_bits)
alice_bases = np.random.randint(2, size=num_bits)

# Paso 2: Alice crea un circuito cuántico y prepara los qubits
qc = QuantumCircuit(num_bits, num_bits)

for i in range(num_bits):
    if alice_bits[i] == 1:
        qc.x(i)
    if alice_bases[i] == 1:
        qc.h(i)

# Bob elige aleatoriamente sus bases
bob_bases = np.random.randint(2, size=num_bits)

# Paso 3: Bob mide los qubits en sus bases
for i in range(num_bits):
    if bob_bases[i] == 1:
        qc.h(i)

qc.measure(range(num_bits), range(num_bits))

# Simulación de la medición
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1).result()
counts = result.get_counts()

# Convertir el resultado de la medición a un array de bits
# Puede haber más de un resultado, tomaremos el primero
measured_bits = list(counts.keys())[0]
bob_results = np.array([int(bit) for bit in measured_bits.zfill(num_bits)])

# Paso 4: Alice y Bob comparan las bases para obtener la clave compartida
matching_bases = alice_bases == bob_bases
# Usar los bits medidos de Bob para construir la clave compartida
shared_key = bob_results[matching_bases]

# Asegurarse de que la clave compartida tiene la longitud adecuada
shared_key = shared_key[:len(message)]

# Paso 5: Encriptar el mensaje usando XOR
encrypted_message = np.bitwise_xor(message, shared_key)

# Paso 6: Bob desencripta el mensaje usando la misma clave compartida
decrypted_message = np.bitwise_xor(encrypted_message, shared_key)

# Mostrar resultados
print("Mensaje original:      ", message)
print("Bits de Alice:         ", alice_bits)
print("Bases de Alice:        ", alice_bases)
print("Bases de Bob:          ", bob_bases)
print("Resultados de Bob:     ", bob_results)
print("Bases que coinciden:   ", matching_bases)
print("Clave compartida:      ", shared_key)
print("Mensaje encriptado:    ", encrypted_message)
print("Mensaje desencriptado: ", decrypted_message)
