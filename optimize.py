import iqif
import numpy as np

net = iqif.lifnet("neuron.txt", "table.txt")
net.set_biascurrent(0, -0.08)
net.set_biascurrent(1, 0.09)
net.set_biascurrent(2, 0.08)
net.set_biascurrent(3, -0.09)
#for i in range(4):
#    net.set_vmin(i, -1)

fp0 = open("potential_0.txt", "w")
fp1 = open("potential_1.txt", "w")
fp2 = open("potential_2.txt", "w")
fp3 = open("potential_3.txt", "w")

for i in range(500):
    net.send_synapse()
    fp0.write('{:f}\n'.format(net.potential(0)))
    fp1.write('{:f}\n'.format(net.potential(1)))
    fp2.write('{:f}\n'.format(net.potential(2)))
    fp3.write('{:f}\n'.format(net.potential(3)))
fp0.close()
fp1.close()
fp2.close()
fp3.close()
print('Firing rate:{:f}, {:f}, {:f}, {:f}'.format(net.spike_rate(0), net.spike_rate(1), net.spike_rate(2), net.spike_rate(3)))
#print('Firing rate:{:f}, {:f}'.format(net.spike_rate(0), net.spike_rate(1)))
