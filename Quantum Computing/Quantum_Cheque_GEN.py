## Generation Of Quantum Cheque

## Importing Packages
from qiskit import *
import qrng
from qiskit.tools.visualization import *
from qiskit.tools.monitor import job_monitor
from math import *
import numpy as np

qr = QuantumRegister(5) # assigning number of quibits in circuit
cr = ClassicalRegister(5) # assigning number of classical bits for circuit
qc = QuantumCircuit(qr,cr) # constructing quantum circuit

## building circuit with gate operations
qc.h(qr[0])
qc.h(qr[2])
qc.h(qr[4])
qc.t(qr[0])
qc.cx(qr[1], qr[2])
qc.h(range(3)) # applying a Hadamard operation from qubit 0 to 3
qc.s(qr[0])
qc.cx(qr[1], qr[2])
qc.h(qr[2])
qc.cx(qr[4], qr[2])
qc.h(qr[2])
qc.h(qr[4])

qc.cx(qr[1], qr[2])
qc.h(qr[1])
qc.h(qr[2])
qc.cx(qr[1], qr[2])
qc.h(qr[1])
qc.h(qr[2])
qc.cx(qr[0], qr[1])
qc.cx(qr[0], qr[2])
qc.h(qr[0])
qc.h(qr[2])
qc.cx(qr[0], qr[2])
qc.h(qr[2])
qc.measure(qr[2], cr[2]) ## measure of quantum states

%matplotlib inline
qc.draw(output='mpl') # circuit diagram

## Load account to find available providers
IBMQ.load_account()
provider = IBMQ.get_provider(group='open')
provider.backends()

## calling backends for simulaton
simulator_1 = Aer.get_backend('qasm_simulator')
sim_send_1 = execute(qc, backend = simulator_1, shots = 8192).result()
result_sim_1 = sim_send_1.get_counts(qc)

## calling backends for real quantum computer
backend = provider.get_backend('ibmq_vigo')
job_1 = execute(qc, backend = backend, shots = 8192)

## print status of job
job_monitor(job_1)

## plot results to compare real vs simulated
result_1 = job_1.result()
QCcount_1 = result_1.get_counts(qc)
plot_histogram([QCcount_1, result_sim_1], legend = ['Quantum Computer', 'Simulator'])
