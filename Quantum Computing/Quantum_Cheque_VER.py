## Verification Of Quantum Cheque

## Importing Packages
from qiskit import *
from qiskit.tools.visualization import *
from qiskit.tools.monitor import job_monitor
from math import *
import numpy as np

qr = QuantumRegister(5) # assigning number of quibits in circuit
cr = ClassicalRegister(5) # assigning number of classical bits for circuit
qc = QuantumCircuit(qr,cr) # constructing quantum circuit

## building circuit with gate operations
qc.h(range(3))
qc.cx(qr[1], qr[2])
qc.h(qr[1])
qc.cx(qr[1], qr[2])
qc.tdg(qr[2])
qc.cx(qr[0], qr[2])
qc.t(qr[0])
qc.cx(qr[1], qr[2])
qc.tdg(qr[2])
qc.barrier()
qc.cx(qr[0], qr[2])
qc.t(qr[1])
qc.t(qr[2])
qc.h(qr[2])
qc.cx(qr[1], qr[2])

qc.h(qr[1])
qc.h(qr[2])
qc.cx(qr[1], qr[2])
qc.h(qr[1])
qc.h(qr[2])
qc.cx(qr[1], qr[2])
qc.cx(qr[0], qr[2])
qc.t(qr[0])
qc.tdg(qr[2])
qc.cx(qr[0], qr[2])
qc.h(qr[0])
qc.cx(qr[1], qr[2])

qc.h(qr[1])
qc.h(qr[2])
qc.cx(qr[1], qr[2])

qc.h(qr[1])
qc.h(qr[2])
qc.cx(qr[1], qr[2])

qc.h(qr[1])
qc.h(qr[2])
qc.cx(qr[1], qr[2])

qc.h(qr[1])
qc.h(qr[2])

qc.barrier()
qc.measure(qr[0], cr[0]) ## measure of quantum states

%matplotlib inline
qc.draw(output='mpl') # circuit diagram

## Load account to find available providers
IBMQ.load_account()
provider = IBMQ.get_provider(group='open')
provider.backends()

## calling backends for simulaton
simulator_3 = Aer.get_backend('qasm_simulator')
sim_send_3 = execute(qc, backend = simulator_3, shots = 8192).result()
result_sim_3 = sim_send_3.get_counts(qc)

## calling backends for real quantum computer
backend = provider.get_backend('ibmq_burlington')
job_3 = execute(qc, backend = backend, shots = 8192)

## print status of job
job_monitor(job_3)

## plot results to compare real vs simulated
result_3 = job_3.result()
QCcount_3 = result_3.get_counts(qc)
plot_histogram([QCcount_3, result_sim_3], legend = ['Quantum Computer', 'Simulator'])