from qiskit import QuantumCircuit
from qiskit.circuit import Gate
from qiskit_aer import Aer
from qiskit.circuit.library import HGate, MCXGate
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram

mcx4 = MCXGate(4)
mcx3 = MCXGate(3)

Ggate_circut = QuantumCircuit(4, name='Ggate')
Oracle_circut = QuantumCircuit(5, name='Oracle')

Ggate_circut.h([0, 1, 2, 3])
Ggate_circut.x([0, 1, 2, 3])
Ggate_circut.h(3)
Ggate_circut.append(mcx3, [0, 1, 2, 3])
Ggate_circut.h(3)
Ggate_circut.x([0, 1, 2, 3])
Ggate_circut.h([0, 1, 2, 3])

Ggate = Ggate_circut.to_gate()

Oracle_circut.x([0,1])
Oracle_circut.append(mcx4, [0, 1, 2, 3, 4])   
Oracle_circut.x([0,1])

Oracle = Oracle_circut.to_gate()


qc = QuantumCircuit(5, 4)

qc.h([0, 1, 2, 3])

qc.x(4)
qc.h(4)

for i in range(3):
    qc.append(Oracle, [0, 1, 2, 3, 4])
    qc.append(Ggate, [0, 1, 2, 3])


qc.measure(0, 0)
qc.measure(1, 1)
qc.measure(2, 2)
qc.measure(3, 3)

schemat = qc.draw("mpl")
schemat.savefig("schemat_111.png")


simulator = Aer.get_backend('aer_simulator')
qc = qc.decompose()
result = simulator.run(qc, shots=10000).result()
counts = result.get_counts()

histogram = plot_histogram(counts)
histogram.savefig("histogram_111.png")
print(counts)
