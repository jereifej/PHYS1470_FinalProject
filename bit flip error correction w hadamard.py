from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(qreg_q[0])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.cx(qreg_q[0], qreg_q[2])
circuit.barrier(qreg_q[1])
circuit.barrier(qreg_q[0])
circuit.barrier(qreg_q[2])
circuit.id(qreg_q[2])
circuit.id(qreg_q[1])
circuit.h(qreg_q[0])
circuit.barrier(qreg_q[0])
circuit.barrier(qreg_q[2])
circuit.barrier(qreg_q[1])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.cx(qreg_q[0], qreg_q[2])
circuit.ccx(qreg_q[2], qreg_q[1], qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])
