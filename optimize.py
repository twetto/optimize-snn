import iqif
import numpy as np

net = iqif.lifnet("neuron.txt", "table.txt")
with open("current.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split(" ")
        net.set_biascurrent(int(line[0]), float(line[1]))

#for i in range(4):
#    net.set_vmin(i, -1)

files = []
for i in range(net.num_neurons()):
    files.append(open("potential_{:d}.txt".format(i), 'w'))

steps = 500
for i in range(steps):
    net.send_synapse()
    for j in range(net.num_neurons()):
        files[j].write('{:f}\n'.format(net.potential(j)))

for i in range(net.num_neurons()):
    files[i].close()

rate = np.zeros(net.num_neurons())
for i in range(net.num_neurons()):
    count = net.spike_count(i)
    #rate[i] = count / (steps)          # my SNN simulator can only
    rate[i] = count / (steps - count)   # fire every other timestep
                                        

print('Firing rate:{}'.format(rate))
