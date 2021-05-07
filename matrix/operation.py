import math
from fractions import Fraction


SARRUS = 0
EXPANSION_COFACTOR = 1
GAUSS = 2
ESELON = 3


def __determinant2x2(data):
    if type(data).__name__ == 'dict':
        name, data = data['name'], data['matrix']
    else:
        name = "Matrix"

    a = data[0][0] * data[1][1]
    b = data[1][0] * data[0][1]

    result = a - b

    return [
        [
            "Determinant => ",
            f"|{name}| = " + str(a) + " - " + str(b),
            f"|{name}| = " + str(result)
        ],
        result
    ]


def __determinant3x3_sarrus(data):
    if type(data).__name__ == 'dict':
        name, data = data['name'], data['matrix']
    else:
        name = "Matrix"

    a1 = data[0][0] * data[1][1] * data[2][2]
    a2 = data[0][1] * data[1][2] * data[2][0]
    a3 = data[0][2] * data[1][0] * data[2][1]
    b1 = data[2][0] * data[1][1] * data[0][2]
    b2 = data[2][1] * data[1][2] * data[0][0]
    b3 = data[2][2] * data[1][0] * data[0][1]

    result = a1 + a2 + a3 - (b1 + b2 + b3)

    return [
        [
            "Determinant => ",
            f"|{name}| = " + str(a1) + " + " + str(a2) + " + " + str(a3) + " - ( " + str(b1) + " + " + str(b2) + " + " + str(
                b3) + " )",
            f"|{name}| = " + str(a1 + a2 + a3) + " - " + str(b1 + b2 + b3),
            f"|{name}| = " + str(result)
        ],
        result
    ]


def __determinant4x4_sarrus(data):
    if type(data).__name__ == 'dict':
        name, data = data['name'], data['matrix']
    else:
        name = "Matrix"

    def gi_multiple(matrix, chars):
        result = 1
        for char in chars:
            index = ord(char) - 96
            row = math.ceil(index / 4) - 1
            col = index - (row * 4) - 1
            result *= matrix[row][col]
        return result

    def generate_a1(matrix):
        afkp = gi_multiple(matrix, "afkp")
        bglm = gi_multiple(matrix, "bglm")
        chin = gi_multiple(matrix, "chin")
        dejo = gi_multiple(matrix, "dejo")
        ahkn = gi_multiple(matrix, "ahkn")
        belo = gi_multiple(matrix, "belo")
        cfip = gi_multiple(matrix, "cfip")
        dgjm = gi_multiple(matrix, "dgjm")

        a1 = afkp - bglm + chin - dejo - ahkn + belo - cfip + dgjm
        flow = [
            f"{name}1 = " + str(afkp) + " - " + str(bglm) + " + " + str(chin) + " - " + str(dejo) + " - " + str(
                ahkn) + " + " + str(belo) + " - " + str(cfip) + " + " + str(dgjm),
            f"{name}1 = " + str(a1),
            ""
        ]
        return flow, a1

    def generate_a2(matrix):
        aflo = gi_multiple(matrix, "aflo") * -1
        bgip = gi_multiple(matrix, "bgip")
        chjm = gi_multiple(matrix, "chjm")
        dekn = gi_multiple(matrix, "dekn")
        ahjo = gi_multiple(matrix, "ahjo")
        bekp = gi_multiple(matrix, "bekp")
        cflm = gi_multiple(matrix, "cflm")
        dgin = gi_multiple(matrix, "dgin")

        a2 = aflo + bgip - chjm + dekn + ahjo - bekp + cflm - dgin
        flow = [
            f"{name}2 = " + str(aflo) + " + " + str(bgip) + " - " + str(chjm) + " + " + str(dekn) + " + " + str(
                ahjo) + " - " + str(bekp) + " + " + str(cflm) + " - " + str(dgin),
            f"{name}2 = " + str(a2),
            ""
        ]
        return flow, a2

    def generate_a3(matrix):
        agln = gi_multiple(matrix, "agln")
        bhio = gi_multiple(matrix, "bhio")
        cejp = gi_multiple(matrix, "cejp")
        dfkm = gi_multiple(matrix, "dfkm")
        agjp = gi_multiple(matrix, "agjp")
        bhkm = gi_multiple(matrix, "bhkm")
        celn = gi_multiple(matrix, "celn")
        dfio = gi_multiple(matrix, "dfio")

        a3 = agln - bhio + cejp - dfkm - agjp + bhkm - celn + dfio
        flow = [
            f"{name}3 = " + str(agln) + " - " + str(bhio) + " + " + str(cejp) + " - " + str(dfkm) + " - " + str(
                agjp) + " + " + str(bhkm) + " - " + str(celn) + " + " + str(dfio),
            f"{name}3 = " + str(a3)
        ]
        return flow, a3

    f1, a1 = generate_a1(data)

    f2, a2 = generate_a2(data)

    f3, a3 = generate_a3(data)

    return f1 + f2 + f3 + ["Determinant => ", f"|{name}| = " + str(a1) + " + " + str(a2) + " + " + str(a3)], a1 + a2 + a3


def __determinant_expansion_cofactor(data):
    if type(data).__name__ == 'dict':
        name, data = data['name'], data['matrix']
    else:
        name = "Matrix"

    flow = ["Determinant => ", f'|{name}| => ']
    flow2 = [f'|{name}| => ']
    result = 0
    for i in range(len(data[0])):
        mnr = minor(data, 0, i)
        _, det = determinant(mnr)
        mnr = tuple(mnr)
        k = data[0][i]
        if i % 2 == 0:
            result += k * det
            if len(data[0]) - 1 > i:
                flow.append(f"{k} * Matrix{mnr} +")
                flow2.append(f'{k} ({det}) +')
            else:
                flow.append(f"{k} * Matrix{mnr}")
                flow2.append(f'{k} ({det})')
        else:
            result -= k * det
            if len(data[0]) - 1 > i:
                flow.append(f"{k} * Matrix{mnr} -")
                flow2.append(f'{k} ({det}) -')
            else:
                flow.append(f"{k} * Matrix{mnr}")
                flow2.append(f'{k} ({det})')
    flow += [""] + flow2
    return flow, result


def determinant(data, method=SARRUS):
    if type(data).__name__ == 'dict':
        data_type = len(data['matrix'])
    else:
        data_type = len(data)

    if method == SARRUS:
        if data_type == 2:
            return __determinant2x2(data)
        elif data_type == 3:
            return __determinant3x3_sarrus(data)
        elif data_type == 4:
            return __determinant4x4_sarrus(data)
        else:
            raise Exception("Invalid Type")
    else:
        if data_type == 2:
            return __determinant2x2(data)
        else:
            return __determinant_expansion_cofactor(data)


def transpose(data):
    if type(data).__name__ == 'dict':
        data = data['matrix']
    print(data)
    return [[data[j][i] for j in range(len(data[i]))] for i in range(len(data))]


def minor(data, i_row, i_col):
    result = [[] for _ in range(len(data) - 1)]
    index = 0

    for row in range(len(data)):
        for col in range(len(data[row])):
            if i_col != col and i_row != row:
                result[index].append(data[row][col])
        if i_row != row:
            index += 1
    return result


def cofactor(data, i_row, i_col):
    mnr = minor(data, i_row, i_col)
    _, result = determinant(mnr)
    return mnr, result * (-1 if (i_row + i_col) % 2 == 1 else 1)


def adjoint(data):
    data = data['matrix']
    result = []
    flow = ["Adjoint => "]
    for i_row in range(len(data)):
        result.append([])
        temp_flow = []
        for i_col in range(len(data[i_row])):
            mnr, cof = cofactor(data, i_row, i_col)
            result[i_row].append(cof)
            for x in range(len(mnr)):
                if i_col == 0:
                    temp_flow.append("")
                    temp_flow[x] += f'|{mnr[x]}' + "\t"
                elif i_col + 1 < len(data[i_row]):
                    temp_flow[x] += f'{mnr[x]}' + "\t"
                else:
                    temp_flow[x] += f'{mnr[x]}|'
        flow += temp_flow
        flow.append("")
    return flow, result


def multiply(x, y):
    if type(x).__name__ == 'int' and type(y).__name__ == 'int':
        print("Two above are not matrix")

    if type(x).__name__ == 'int':
        x, y = y, x

    if type(y).__name__ == 'int':
        return None, [[i * y for i in row] for row in x]
    else:
        if len(x) != len(y[0]):
            raise Exception("Row Matrix 1 != Col Matrix 2")
        else:
            flow = []
            result = []
            for i in range(len(x)):
                result.append([])
                flow.append([])
                for k in range(len(x)):
                    temp_result = 0
                    temp_flow = ""
                    for j in range(len(x[i])):
                        temp_result += x[i][j] * y[j][k]
                        if j == 0:
                            temp_flow += "|"
                        if len(x[i]) - 1 > j:
                            temp_flow += f'{x[i][j]}*{y[j][k]} + '
                        else:
                            temp_flow += f'{x[i][j]}*{y[j][k]}|'
                    flow[i].append(temp_flow)
                    result[i].append(temp_result)
            return flow, result


def subtract(x, y):
    result = []
    x, y = x, y
    for i in range(len(x)):
        result.append([])
        for j in range(len(x[i])):
            result[i].append(x[i][j] - y[i][j])
    return result


def addition(x, y):
    result = []
    x, y = x['matrix'], y['matrix']
    for i in range(len(x)):
        result.append([])
        for j in range(len(x[i])):
            result[i].append(x[i][j] + y[i][j])
    return result


def inverse(data):
    flow_det, det = determinant(data)
    flow_adj, adj = adjoint(data)
    flow = flow_det + [""] + flow_adj + ["Inverse =>"]
    result = []

    for i in range(len(adj)):
        result.append([])
        temp_flow = ""
        for j in range(len(adj[i])):
            if det == 0:
                result[i].append(0)
            else:
                f = Fraction(adj[i][j], det)
                result[i].append(f'{f.numerator}/{f.denominator}')
            temp_flow += f'({adj[i][j]}/{det})' + "\t"
        flow.append(temp_flow)

    return flow, result
