import sys
import numpy as np
from cell_power import calculate_total_power

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 task1.py initial_energy N [N ...]")
        exit()
    e_init = int(sys.argv[1])
    cols = []
    for i in range(2, len(sys.argv)):
       cols.append(int(sys.argv[i]))
    mat = np.zeros(shape=(len(cols), max(cols)))
    for i in range(len(cols)):
        for j in range(cols[i]):
            mat[i][j] = 1

    print("**********************")
    print(mat)
    print("**********************")
    sum = calculate_total_power(mat, e_init)
    print("Total power: {:.4f}".format(sum))
