from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

# Initializing 9 qubits - 1 signal and 8 ancillary bits
qreg_q = QuantumRegister(9, 'q')
creg_c = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

# Error Correction Encoding
circuit.cx(qreg_q[0], qreg_q[3])
circuit.cx(qreg_q[0], qreg_q[6])
circuit.h(qreg_q[0])
circuit.h(qreg_q[3])
circuit.h(qreg_q[6])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.cx(qreg_q[6], qreg_q[7])
circuit.cx(qreg_q[3], qreg_q[4])
circuit.cx(qreg_q[0], qreg_q[2])
circuit.cx(qreg_q[6], qreg_q[8])
circuit.cx(qreg_q[3], qreg_q[5])


# Noisy Channel
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2], qreg_q[3], qreg_q[4], qreg_q[5], qreg_q[6], qreg_q[7], qreg_q[8])
circuit.x(qreg_q[0])
circuit.z(qreg_q[0])
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2], qreg_q[3], qreg_q[4], qreg_q[5], qreg_q[6], qreg_q[7], qreg_q[8])

# Error Correction Decoding
circuit.cx(qreg_q[0], qreg_q[1])
circuit.cx(qreg_q[6], qreg_q[7])
circuit.cx(qreg_q[3], qreg_q[4])
circuit.cx(qreg_q[0], qreg_q[2])
circuit.cx(qreg_q[6], qreg_q[8])
circuit.cx(qreg_q[3], qreg_q[5])
circuit.ccx(qreg_q[1], qreg_q[2], qreg_q[0])
circuit.ccx(qreg_q[4], qreg_q[5], qreg_q[3])
circuit.ccx(qreg_q[7], qreg_q[8], qreg_q[6])
circuit.h(qreg_q[0])
circuit.h(qreg_q[3])
circuit.h(qreg_q[6])
circuit.cx(qreg_q[0], qreg_q[3])
circuit.cx(qreg_q[0], qreg_q[6])
circuit.ccx(qreg_q[3], qreg_q[6], qreg_q[0])

# Signal Qubit Readout
circuit.measure(qreg_q[0], creg_c[0])