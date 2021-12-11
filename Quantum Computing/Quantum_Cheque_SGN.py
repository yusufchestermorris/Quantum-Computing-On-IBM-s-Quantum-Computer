## Signature Of Quantum Cheque

## Importing Packages
from qiskit import *
from qiskit.providers import backend
import qrng
from qiskit.tools.visualization import *
from qiskit.tools.monitor import job_monitor
from math import *
import numpy as np

## Genterating random number
provider_rn = qrng.set_provider_as_IBMQ('ibm-q')
backend_rn = qrng.set_backend('b')
rn = qrng.get_random_float(0,1)

print(rn)

qr = QuantumRegister(5) # assigning number of quibits in circuit
cr = ClassicalRegister(5) # assigning number of classical bits for circuit
qc = QuantumCircuit(qr,cr) # constructing quantum circuit

## Alices ID 
qc.h(qr[0])
qc.t(qr[0])
qc.h(qr[0])
qc.s(qr[0])

## Wave function ffrfom GEN algorithm + Psi Alice
qc.u3(0.15*pi, 0.16796875*pi, 0, qr[1]) # programing u3 with calculated Euler angles
qc.barrier()

# random number (correesponing to ammount M)
qc.u1(rn*pi, qr[0]) # programing u1 with rn
qc.cx(qr[0],qr[1])

# entangling Bank and Alices wavefunctions
qc.cx(qr[1], qr[4])

#Forming GHZ gates using protocol to allow entanglement both ways
qc.h(qr[2])
qc.h(qr[4])
qc.cx(qr[4], qr[2])
qc.h(qr[2])
qc.h(qr[2])

# changing the phase of the qubit so its in a superpositon between |+> and |->
qc.s(qr[2])
qc.s(qr[4])

# measure alices wavefunction
qc.measure(qr[2], cr[2])

%matplotlib inline
qc.draw(output='mpl') # circuit diagram

## Load account to find available providers
IBMQ.load_account()
provider = IBMQ.get_provider(group='open')
provider.backends()

## calling backends for simulaton
simulator_2 = Aer.get_backend('qasm_simulator')
sim_send_2 = execute(qc, backend = simulator_2, shots = 8192).result()
result_sim_2 = sim_send_2.get_counts(qc)

## calling backends for real quantum computer
backend = provider.get_backend('ibmq_burlington')
job_2 = execute(qc, backend = backend, shots = 8192)

## print status of job
job_monitor(job_2)

## plot results to compare real vs simulated
result_2 = job_2.result()
QCcount_2 = result_2.get_counts(qc)
plot_histogram([QCcount_2, result_sim_2], legend = ['Quantum Computer', 'Simulator'])




