import sys
import numpy as np
import argparse
from cell_power import calculate_total_power

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My parser")
    parser.add_argument('--binary', dest='binary', action='store_true')
    args, leftovers = parser.parse_known_args()

    if len(leftovers) < 2:
        print("Usage: python3 task2.py initial_energy N [N ...] [--binary]")
        exit()

    e_init = None
    try:
        e_init = float(leftovers[0])
    except ValueError:
        raise Exception('Value provided for initial power is not a number.')

    mat = []
    if args.binary is not None and args.binary:
        cols = len(list(leftovers[1]))
        for i in range(1, len(leftovers)):
            if not leftovers[i].isnumeric():
                raise Exception('Value provided for an element describing a grid is not numeric.')
            arr = list(leftovers[i])
            if len(arr) != cols:
                raise Exception('Values provided for elements describing a grid do not have the same number of digits.')
            mat.append([])
            for x in arr:
                mat[i - 1].append(int(x))
    elif not args.binary:
        cols = []
        for i in range(1, len(leftovers)):
            if not leftovers[i].isnumeric():
                raise Exception('Value provided for an element describing a grid is not numeric.')
            cols.append(int(leftovers[i]))
        mat = np.zeros(shape=(len(cols), max(cols)))
        for i in range(len(cols)):
            for j in range(cols[i]):
                mat[i][j] = 1

    print("**********************")
    print("iniial energy:", e_init)
    print("Mat:")
    print(mat)
    print("**********************")
    sum = calculate_total_power(mat, e_init)
    print("Total power: {:.4f}".format(sum))
