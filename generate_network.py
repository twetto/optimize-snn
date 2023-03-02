import numpy as np
import scipy

A = np.array([[-0.4, 0.3],
              [ 0.4, 0.3]])

b = np.array([[-0.4*0.002 + 0.3*-0.006],
              [ 0.4*0.002 + 0.3*-0.006]])

# rate limit multiplier. If multiply by d, the final firing rates also need to multiply by d.
#A *= 4

A_augmented = np.hstack((A, -A))
C = A_augmented.T @ A_augmented
I = A_augmented.T @ b

ci_max = np.amax(np.hstack((C, I)))
C /= ci_max
I /= ci_max

x_np, residuals_np, rank, singular = np.linalg.lstsq(A, b, rcond=None)
x_sp, residuals_sp = scipy.optimize.nnls(C, I.flatten())

print("A:\n{}".format(A))
print("b:\n{}".format(b))
print("C = [A, -A].T @ [A, -A]:\n{}".format(C))
print("I = [A, -A].T @ b\n{}".format(I))
print("Solve Ax = b using NumPy lstsq:\n{}".format(x_np))
print("Solve Cx = I using SciPy NNLS:\n{}".format(x_sp))

with open('neuron.txt', 'w') as f:
    for i, current in enumerate(I):
        f.write('{:d} 0 0.5 1 1 0\n'.format(i))

table = 1 * -C.T
#print("SNN weight matrix = -C.T:\n{}".format(table))
num_row, num_col = table.shape
with open('table.txt', 'w') as f:
    for i in range(num_row):
        for j in range(num_col):
            f.write('{:d} {:d} {:f} 1\n'.format(i, j, table[i, j]))

with open('current.txt', 'w') as f:
    for i, current in enumerate(I):
        current = current[0]
        f.write("{:d} {:f}\n".format(i, current))
