import math
from fractions import Fraction
import random


class Matrix:

    SARRUS = 0
    EXPANSION_COFACTOR = 1
    GAUSS = 2
    ESELON = 3

    def __init__(self, name, data):
        self.data = data
        self.name = name
        self.flow = []
        self.result = None

    def __add__(self, other):
        result = []
        x, y = self.data, other.data
        for i in range(len(x)):
            result.append([])
            for j in range(len(x[i])):
                result[i].append(x[i][j] + y[i][j])
        self.result = None
        self.prints(data=result)
        return result

    def __sub__(self, other):
        result = []
        x, y = self.data, other.data
        for i in range(len(x)):
            result.append([])
            for j in range(len(x[i])):
                result[i].append(x[i][j] - y[i][j])

        self.result = None
        self.prints(data=result)
        return result

    def __mul__(self, other):
        x, y = self, other
        if type(x).__name__ == 'int' and type(y).__name__ == 'int':
            print("Two above are not matrix")

        if type(x).__name__ == 'int':
            x, y = y, x

        x = x.data

        if type(y).__name__ == 'int':
            result = [[i * y for i in row] for row in x]
            self.result = None
            self.prints(data=result)
            return None, result
        else:
            y = y.data
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
                self.prints()
                return flow, result

    @staticmethod
    def generate(name, row=3, col=3, min_val=0, max_val=None):
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

        matrix = Matrix(name, result)
        matrix.prints()

        return matrix

    def __determinant2x2(self, show=True):
        data = self.data
        name = self.name

        a = data[0][0] * data[1][1]
        b = data[1][0] * data[0][1]

        self.result = a - b
        self.flow = [
                "Determinant => ",
                f"|{name}| = " + str(a) + " - " + str(b),
                f"|{name}| = " + str(self.result)
            ]

        if show:
            self.prints()

        return [
            self.flow,
            self.result
        ]

    def __determinant3x3_sarrus(self, show=True):
        data = self.data
        name = self.name

        a1 = data[0][0] * data[1][1] * data[2][2]
        a2 = data[0][1] * data[1][2] * data[2][0]
        a3 = data[0][2] * data[1][0] * data[2][1]
        b1 = data[2][0] * data[1][1] * data[0][2]
        b2 = data[2][1] * data[1][2] * data[0][0]
        b3 = data[2][2] * data[1][0] * data[0][1]

        result = a1 + a2 + a3 - (b1 + b2 + b3)
        self.result = result

        self.flow = [
                "Determinant => ",
                f"|{name}| = " + str(a1) + " + " + str(a2) + " + " + str(a3) + " - ( " + str(b1) + " + " + str(
                    b2) + " + " + str(
                    b3) + " )",
                f"|{name}| = " + str(a1 + a2 + a3) + " - " + str(b1 + b2 + b3),
                f"|{name}| = " + str(result)
            ]

        if show:
            self.prints()

        return [
            self.flow,
            self.result
        ]

    def __determinant4x4_sarrus(self, show=True):
        data = self.data
        name = self.name

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

        self.flow = f1 + f2 + f3 + ["Determinant => ", f"|{name}| = " + str(a1) + " + " + str(a2) + " + " + str(a3)]
        self.result = a1 + a2 + a3

        if show:
            self.prints()

        return self.flow, self.result

    def __determinant_expansion_cofactor(self, show=True):
        data = self.data
        name = self.name

        flow = ["Determinant => ", f'|{name}| => ']
        flow2 = f'|{name}| => '
        result = 0
        for i in range(len(data[0])):
            mnr = self.minor(0, i, False)
            _, det = self.determinant(data=mnr, show=False)
            mnr = tuple(mnr)
            k = data[0][i]
            if i % 2 == 0:
                result += k * det
                if len(data[0]) - 1 > i:
                    flow.append(f"{k} * Matrix{mnr} +")
                    flow2 += f'{k} ({det}) +'
                else:
                    flow.append(f"{k} * Matrix{mnr}")
                    flow2 += f'{k} ({det})'
            else:
                result -= k * det
                if len(data[0]) - 1 > i:
                    flow.append(f"{k} * Matrix{mnr} -")
                    flow2 += f'{k} ({det}) -'
                else:
                    flow.append(f"{k} * Matrix{mnr}")
                    flow2 += f'{k} ({det})'
        self.flow = flow + ["", flow2]
        self.result = result

        if show:
            self.prints()

        return self.flow, self.result

    def determinant(self, method=SARRUS, data=None, show=True):
        if data is None:
            data = self.data

        if type(data).__name__ == 'dict':
            data_type = len(data['matrix'])
        else:
            data_type = len(data)

        if method == Matrix.SARRUS:
            if data_type == 2:
                return self.__determinant2x2(show)
            elif data_type == 3:
                return self.__determinant3x3_sarrus(show)
            elif data_type == 4:
                return self.__determinant4x4_sarrus(show)
            else:
                raise Exception("Invalid Type")
        else:
            if data_type == 2:
                return self.__determinant2x2(show)
            else:
                return self.__determinant_expansion_cofactor(show)

    def transpose(self):
        data = self.data
        if type(data).__name__ == 'dict':
            data = data['matrix']
        self.result = [[data[j][i] for j in range(len(data[i]))] for i in range(len(data))]
        self.prints()
        return self.result

    def minor(self, i_row, i_col, show=True):
        data = self.data

        result = [[] for _ in range(len(data) - 1)]
        index = 0

        for row in range(len(data)):
            for col in range(len(data[row])):
                if i_col != col and i_row != row:
                    result[index].append(data[row][col])
            if i_row != row:
                index += 1
        self.result = result

        if show:
            self.prints()

        return result

    def cofactor(self, i_row, i_col, show=True):
        mnr = self.minor(i_row, i_col, False)
        _, result = self.determinant(data=mnr, show=False)
        self.result = result * (-1 if (i_row + i_col) % 2 == 1 else 1)
        self.flow = mnr

        if show:
            self.prints()

        return mnr, self.result

    def adjoint(self):
        data = self.data
        result = []
        flow = ["Adjoint => "]
        for i_row in range(len(data)):
            result.append([])
            temp_flow = []
            for i_col in range(len(data[i_row])):
                mnr, cof = self.cofactor(i_row, i_col, False)
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

        self.flow = flow
        self.result = result

        self.prints()

        return flow, result

    def inverse(self):
        flow_det, det = self.determinant(show=False)
        flow_adj, adj = self.adjoint()
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

        self.flow = flow
        self.result = result

        self.prints()

        return flow, result

    def prints(self, result=None, data=None, data_only=False):
        if data_only:
            self.flow = []
            self.result = None

        if data is None:
            data = self.data
        flow = self.flow

        self.flow = []

        if data is not None:
            print(f"Matrix {self.name} =>")

            for x in data:
                row = "\t".join(
                    [str(y) if type(y).__name__ == 'int' else f"{Fraction(y).numerator}/{Fraction(y).denominator}" for
                     y in x])
                print(f"[{row}]")
            print()

        if flow:
            if type(flow[0]).__name__ == 'list':
                for x in flow:
                    print(x)
            else:
                print("\n".join(flow))
            print()

        if result is not None:
            if type(result).__name__ == 'int' or type(result).__name__ == 'float':
                print("Result = ", result)
            else:
                print("Result =>")
                for x in result:
                    row = "\t".join(
                        [str(y) if type(y).__name__ == 'int' else f"{Fraction(y).numerator}/{Fraction(y).denominator}"
                         for
                         y in x])
                    print(f"[{row}]")