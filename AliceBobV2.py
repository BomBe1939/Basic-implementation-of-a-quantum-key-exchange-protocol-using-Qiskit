import numpy as np
from qiskit import QuantumCircuit, Aer, execute

# Solicitar al usuario una combinación de bits (código binario) para encriptar
user_input = input("Introduce una combinación de 1 y 0 (código binario) para encriptar: ")

# Convertir la entrada del usuario en un array de bits
try:
    message = np.array([int(bit) for bit in user_input])
except ValueError:
    print("Entrada no válida. Asegúrate de introducir solo 1s y 0s.")
    exit()

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

# Paso 6: Desencriptar el mensaje usando la misma clave compartida
decrypted_message = np.bitwise_xor(encrypted_message, shared_key)

# Mostrar resultados
print("\nMensaje original:      ", message)
print("Clave generada:        ", shared_key)
print("Mensaje encriptado:    ", encrypted_message)
print("Mensaje desencriptado: ", decrypted_message)
