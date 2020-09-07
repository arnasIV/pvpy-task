import time
import datetime
import numpy as np

class ResultField:
    def __init__(self, name, power, duration):
        self.name = name
        self.power = power
        self.duration = duration

def log(text):
    time = str(datetime.datetime.now())
    print("["+time+"]: " + text)

def element_power_ratio(mat, i, j):
    i_ind1 = i - 1
    res = 1
    # North
    while i_ind1 >= 0:
        if mat[i_ind1][j]:
            res *= 1.1
        else:
            break
        i_ind1 -= 1
    i_ind2 = i + 1
    #  South
    while i_ind2 < len(mat):
        if mat[i_ind2][j]:
            res *= 1.15
        else:
            break
        i_ind2 += 1
    j_ind1 = j - 1
    # West
    while j_ind1 >= 0:
        if mat[i][j_ind1]:
            res *= 1.12
        else:
            break
        j_ind1 -= 1
    j_ind2 = j + 1
    # East
    while j_ind2 < len(mat[i]):
        if mat[i][j_ind2]:
            res *= 1.08
        else:
            break
        j_ind2 += 1
    return res

def calculate_total_power(mat, e_init):
    print("**********************")
    print("row | col | ratio")
    sum = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]:
                res = element_power_ratio(mat, i, j)
                sum += res
                print("{} | {} | {:.4f}".format(i, j, res))
    print("**********************")
    return e_init * sum

def calculate_power_task(name, binary, power, grid_input):
    log("Starting task with: {}, {}, {}, {}".format(name, binary, power, grid_input))
    power = float(power)
    start = time.time()
    split  = grid_input.split()

    mat = []
    if binary:
        for i in range(len(split)):
            arr = list(split[i])
            mat.append([])
            for x in arr:
                mat[i].append(int(x))
    else:
        cols = []
        for i in range(len(split)):
            cols.append(int(split[i]))
        mat = np.zeros(shape=(len(cols), max(cols)))
        for i in range(len(cols)):
            for j in range(cols[i]):
                mat[i][j] = 1

    print("**********************")
    print("Mat:")
    print(mat)
    print("**********************")

    total_power = calculate_total_power(mat, power)

    duration = time.time() - start
    duration = "{:.4f}".format(duration)
    total_power = "{:.4f}".format(total_power)
    log("Finished task. Total power: " + total_power + ", time: " + duration)
    res = ResultField(name, total_power, duration)
    return res
