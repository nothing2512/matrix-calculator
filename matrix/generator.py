import random
import math


def generate_data(row=3, col=3, min_val=0, max_val=None):
    if max_val is None:
        max_val = (row * col) + min_val
    value = list(range(min_val, max_val))
    random.shuffle(value)

    result = []

    for x in range(len(value)):
        i_row = math.ceil((x + 1) / col) - 1
        i_col = x % col
        if i_col == 0:
            result.append([])
        result[i_row].append(value[x])

    return result
