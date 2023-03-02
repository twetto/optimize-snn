# optimize-snn
Using spiking neural network (SNN) to solve Ax = b.

## Dependencies
NumPy
SciPy
[IQIF](https://github.com/twetto/iq-neuron)
[python-iqif](https://github.com/twetto/python-iqif)

## Usage
Set A and b in `generate_network.py`, and it will spit out `table.txt` as the SNN connection table, and `current.txt` as the input bias current.

Put corresponding number of neuron parameters in `neuron.txt`. For example, the x in Ax = b is a 4-element vector, then four neurons are required:

```
0 0 0 1 1 0
1 0 0 1 1 0
2 0 0 1 1 0
3 0 0 1 1 0
```

Here we use a typical LIF neuron. The corresponding parameters in each lines are neuron index, leaky term, rest potential, threshold potential, reset potential, noise strength.

For simplicity we set leaky term to 0 so LIF becomes simple IF, and reset potential being the same as threshold. The reset function will be handled by self-inhibitory connection during the generation of the weight matrix C.

After that, use `python optimize.py` and `python plot_potentials.py` to see the result.
