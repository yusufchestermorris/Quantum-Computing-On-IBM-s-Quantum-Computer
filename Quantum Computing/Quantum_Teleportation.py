## Quantum Teleportation Algorithm

## Importing Packages
from qiskit import *
from qiskit.tools.visualization import *
from qiskit.tools.monitor import job_monitor

qr = QuantumRegister(3) # assigning number of quibits in circuit
cr = ClassicalRegister(3) # assigning number of classical bits for circuit
qc = QuantumCircuit(qr,cr) # constructing quantum circuit

## building circuit with gate operations
qc.x(qr[0])
qc.barrier()
qc.h(qr[1])
qc.cx(qr[1], qr[2])
qc.cx(qr[0], qr[1])
qc.h(qr[0])
qc.barrier()
qc.measure([0,1], [0,1]) ## measure of quantum states
qc.cx(qr[1], qr[2])
qc.cz(qr[0], qr[2])

%matplotlib inline
qc.draw(output='mpl') # circuit diagram

## Load account to find available providers
IBMQ.load_account()
provider = IBMQ.get_provider(group='open')
provider.backends()



### First set of results at 1024 shots
## calling backends for simulaton
sim_t1 = Aer.get_backend('qasm_simulator')
sim_send_t1 = execute(qc, backend = sim_t1, shots = 1024).result()
result_sim_t1 = sim_send_t1.get_counts(qc)

## calling backends for real quantum computer
backend = provider.get_backend('ibmq_burlington')
job_t1 = execute(qc, backend = backend, shots = 1024)

## print status of the first job
job_monitor(job_t1)

## plot results to compare real vs simulated
result_t1 = job_t1.result()
QCcount_t1 = result_t1.get_counts(qc)
plot_histogram([QCcount_t1, result_sim_t1], legend = ['Quantum Computer', 'Simulator'])



### Second set of results at 4096 shots
## calling backends for simulaton
sim_t2 = Aer.get_backend('qasm_simulator')
sim_send_t2 = execute(qc, backend = sim_t2, shots = 4096).result()
result_sim_t2 = sim_send_t2.get_counts(qc)

## calling backends for real quantum computer
job_t2 = execute(qc, backend = backend, shots = 4096)

## print status of the first job
job_monitor(job_t2)

## plot results to compare real vs simulated
result_t2 = job_t2.result()
QCcount_t2 = result_t2.get_counts(qc)
plot_histogram([QCcount_t2, result_sim_t2], legend = ['Quantum Computer', 'Simulator'])



### Second set of results at 8192 shots
## calling backends for simulaton
sim_t3 = Aer.get_backend('qasm_simulator')
sim_send_t3 = execute(qc, backend = sim_t3, shots = 8192).result()
result_sim_t3 = sim_send_t3.get_counts(qc)

## calling backends for real quantum computer
job_t3 = execute(qc, backend = backend, shots = 8192)

## print status of the first job
job_monitor(job_t3)

## plot results to compare real vs simulated
result_t3 = job_t3.result()
QCcount_t3 = result_t3.get_counts(qc)
plot_histogram([QCcount_t3, result_sim_t3], legend = ['Quantum Computer', 'Simulator'])

