import iqif
import numpy as np

net = iqif.lifnet("neuron.txt", "table.txt")
net.set_biascurrent(0, 0.016)
net.set_biascurrent(1, -0.0126)
net.set_biascurrent(2, -0.016)
net.set_biascurrent(3, 0.0126)
#for i in range(4):
#    net.set_vmin(i, -1)

fp0 = open("potential_0.txt", "w")
fp1 = open("potential_1.txt", "w")
fp2 = open("potential_2.txt", "w")
fp3 = open("potential_3.txt", "w")

steps = 500
for i in range(steps):
    net.send_synapse()
    fp0.write('{:f}\n'.format(net.potential(0)))
    fp1.write('{:f}\n'.format(net.potential(1)))
    fp2.write('{:f}\n'.format(net.potential(2)))
    fp3.write('{:f}\n'.format(net.potential(3)))
fp0.close()
fp1.close()
fp2.close()
fp3.close()

rate = np.zeros(4)
for i in range(4):
    count = net.spike_count(i)
    #rate[i] = count / (steps)
    rate[i] = count / (steps - count)

print('Firing rate:{}'.format(rate))
#print('Firing rate:{:f}, {:f}'.format(net.spike_rate(0), net.spike_rate(1)))
