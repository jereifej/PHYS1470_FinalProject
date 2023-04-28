from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

# Initialize 3 qubits - 1 signal and 2 ancillary
qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

# Error Correction Encode
circuit.cx(qreg_q[0], qreg_q[1])
circuit.cx(qreg_q[0], qreg_q[2])
circuit.h(qreg_q[0])
circuit.h(qreg_q[2])
circuit.h(qreg_q[1])

# Noisy Channel
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.id(qreg_q[1])
circuit.id(qreg_q[2])
circuit.z(qreg_q[0])
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])

# Error Correction Decode
circuit.h(qreg_q[0])
circuit.h(qreg_q[2])
circuit.h(qreg_q[1])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.cx(qreg_q[0], qreg_q[2])
circuit.ccx(qreg_q[1], qreg_q[2], qreg_q[0])

# Signal Qubit Readout
circuit.measure(qreg_q[0], creg_c[0])
