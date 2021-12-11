## Importing Packages
from qiskit import *
%matplotlib inline
from qiskit.tools.visualization import *
from math import *
import numpy as np

qr = QuantumRegister(2) # assigning number of quibits in circuit
cr = ClassicalRegister(2) # assigning number of classical bits for circuit
qc = QuantumCircuit(qr,cr)

## Building the circuit with gate operations 
qc.h(qr[0]) # applying Haradamard
qc.cx(qr[0], qr[1]) # applying controlled x gate

qc.draw(output='mpl') # drawing diagram of circuit

## call backends for simulation
sim = Aer.get_backend('statevector_simulator')
results = excecute(qc, backend=sim).results()
statevec = results.get_statevector()

plot_bloch_multivector(statevec) # plotting Bloch shpere vector


