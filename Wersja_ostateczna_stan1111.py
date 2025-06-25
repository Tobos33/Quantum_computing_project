from qiskit import QuantumCircuit
from qiskit.circuit import Gate
from qiskit_aer import Aer
from qiskit.circuit.library import HGate, MCXGate
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram

mcx5 = MCXGate(5)
mcx4 = MCXGate(4)

Ggate_circut = QuantumCircuit(5, name='Ggate')
Oracle_circut = QuantumCircuit(6, name='Oracle')

Ggate_circut.h([0, 1, 2, 3, 4])
Ggate_circut.x([0, 1, 2, 3, 4])
Ggate_circut.h(4)
Ggate_circut.append(mcx4, [0, 1, 2, 3, 4])
Ggate_circut.h(4)
Ggate_circut.x([0, 1, 2, 3, 4])
Ggate_circut.h([0, 1, 2, 3, 4])

Ggate = Ggate_circut.to_gate()

Oracle_circut.x([0,1])
Oracle_circut.append(mcx5, [0, 1, 2, 3, 4, 5])   
Oracle_circut.x([0,1])

Oracle = Oracle_circut.to_gate()


qc = QuantumCircuit(6, 5)

qc.h([0, 1, 2, 3, 4])

qc.x(5)
qc.h(5)

for i in range(4):
    qc.append(Oracle, [0, 1, 2, 3, 4, 5])
    qc.append(Ggate, [0, 1, 2, 3, 4])


qc.measure(0, 0)
qc.measure(1, 1)
qc.measure(2, 2)
qc.measure(3, 3)
qc.measure(4, 4)

schemat = qc.draw("mpl")
schemat.savefig("schemat_1111.png")

Ggate_schemat = Ggate_circut.draw("mpl")
Ggate_schemat.savefig("Ggate_schemat.png")

Oracle_schemat = Oracle_circut.draw("mpl")
Oracle_schemat.savefig("Oracle_schemat.png")

simulator = Aer.get_backend('aer_simulator')
qc = qc.decompose()
result = simulator.run(qc, shots=10000).result()
counts = result.get_counts()

histogram = plot_histogram(counts)
histogram.savefig("histogram_1111.png")
print(counts)
