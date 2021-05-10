import math
import random
from fractions import Fraction


class Matrix:
    SARRUS = 0
    EXPANSION_COFACTOR = 1
    GAUSS = 2
    ADJOINT = 3

    def __init__(self, name, data):
        self.__data = data
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

    @property
    def data(self):
        data = []
        for x in range(len(self.__data)):
            data.append([])
            for col in self.__data[x]:
                data[x].append(col)
        return data

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

    def __determinant_gauss(self):
        data = self.data

        multiplier = 1
        flow = []

        # Swapping
        for x in range(len(data)):
            if data[x][0] == 0 and data[x][1] == 0 and x != 2:
                data[x], data[2] = data[2], data[x]
                multiplier = -multiplier
                if len(flow) > 0:
                    flow.append("")
                flow.append(f"Swap row {x + 1} with row 2, multiplier = {multiplier}")
                for row in data:
                    cols = []
                    for col in row:
                        if isinstance(col, Fraction):
                            if col.numerator % col.denominator == 0:
                                cols.append(str(int(col.numerator / col.denominator)))
                            else:
                                cols.append(f"{col.numerator}/{col.denominator}")
                        else:
                            cols.append(str(col))
                    cols = "\t".join(cols)
                    flow.append(f"[{cols}]")
                break

        for x in range(len(data)):
            if data[x][0] == 0 and data[x][1] != 0 and x != 1:
                data[x], data[1] = data[1], data[x]
                multiplier = -multiplier
                if len(flow) > 0:
                    flow.append("")
                flow.append(f"Swap row {x + 1} with row 2, multiplier = {multiplier}")
                for row in data:
                    cols = []
                    for col in row:
                        if isinstance(col, Fraction):
                            if col.numerator % col.denominator == 0:
                                cols.append(str(int(col.numerator / col.denominator)))
                            else:
                                cols.append(f"{col.numerator}/{col.denominator}")
                        else:
                            cols.append(str(col))
                    cols = "\t".join(cols)
                    flow.append(f"[{cols}]")
                break

        if len(flow) > 0:
            flow.append("")

        # Start Elimination
        sub = Fraction(data[1][0], data[0][0])
        for x in range(len(data[1])):
            data[1][x] -= data[0][x] * sub

        flow.append(f"Row 2 - (Row 1 * Row 2 Col 1 / Row 1 Col 1)")
        for row in data:
            cols = []
            for col in row:
                if isinstance(col, Fraction):
                    if col.numerator % col.denominator == 0:
                        cols.append(str(int(col.numerator / col.denominator)))
                    else:
                        cols.append(f"{col.numerator}/{col.denominator}")
                else:
                    cols.append(str(col))
            cols = "\t".join(cols)
            flow.append(f"[{cols}]")

        sub = Fraction(data[2][0], data[0][0])
        for x in range(len(data[2])):
            data[2][x] -= data[0][x] * sub

        flow.append("")
        flow.append(f"Row 3 - (Row 1 * Row 3 Col 1 / Row 1 Col 1)")
        for row in data:
            cols = []
            for col in row:
                if isinstance(col, Fraction):
                    if col.numerator % col.denominator == 0:
                        cols.append(str(int(col.numerator / col.denominator)))
                    else:
                        cols.append(f"{col.numerator}/{col.denominator}")
                else:
                    cols.append(str(col))
            cols = "\t".join(cols)
            flow.append(f"[{cols}]")

        sub = Fraction(data[2][1], data[1][1])
        for x in range(1, len(data[2])):
            data[2][x] -= data[1][x] * sub

        flow.append("")
        flow.append(f"Row 3 - (Row 2 * Row 3 Col 2 / Row 2 Col 2)")
        for row in data:
            cols = []
            for col in row:
                if isinstance(col, Fraction):
                    if col.numerator % col.denominator == 0:
                        cols.append(str(int(col.numerator / col.denominator)))
                    else:
                        cols.append(f"{col.numerator}/{col.denominator}")
                else:
                    cols.append(str(col))
            cols = "\t".join(cols)
            flow.append(f"[{cols}]")

        result = multiplier * data[0][0] * data[1][1] * data[2][2]
        flow.append("")
        flow.append(f"|{self.name}| = ({multiplier}) * {data[0][0]} * {data[1][1]} * {data[2][2]}")
        flow.append(f"|{self.name}| = {result}")

        self.flow = flow
        self.prints()

        return [
            self.flow,
            0
        ]

    def __determinant2x2(self, show=True, data=None):
        if data is None:
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

    def __determinant3x3_sarrus(self, show=True, data=None):
        if data is None:
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

    def __determinant4x4_sarrus(self, show=True, data=None):
        if data is None:
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

        self.result = a1 + a2 + a3
        self.flow = f1 + f2 + f3 + [
            "",
            f"|{name}| = " + str(a1) + " + " + str(a2) + " + " + str(a3),
            f"|{name}| = {self.result}"
        ]

        if show:
            self.prints()

        return self.flow, self.result

    def __determinant_expansion_cofactor(self, show=True):
        data = self.data
        name = self.name

        flow = ["Determinant => ", f'|{name}| = ']
        flow2 = f'|{name}| = '
        flow3 = f'|{name}| = '
        result = 0
        for i in range(len(data[0])):
            mnr = self.minor(0, i, data, False)
            _, det = self.determinant(data=mnr, show=False)
            mnr = tuple(mnr)
            k = data[0][i]
            kdet = k * det
            if i == 0:
                result += kdet
                flow.append("\t" + f"{k} * Matrix{mnr}")
                flow2 += f'{k} ({det})'
                flow3 += f'{kdet}'
            elif i % 2 == 0:
                result += kdet
                flow.append("\t" + f"- {k} * Matrix{mnr}")
                flow2 += f' - {k} ({det})'
                flow3 += f' - {kdet}' if kdet > 0 else f' + {-kdet}'
            else:
                result -= kdet
                flow.append("\t" + f"+ {k} * Matrix{mnr}")
                flow2 += f' + {k} ({det})'
                flow3 += f' + {kdet}' if kdet > 0 else f' - {-kdet}'
        self.flow = flow + [
            "",
            flow2,
            flow3,
            f'|{name}| = {result}'
        ]
        self.result = result

        if show:
            self.prints()

        return self.flow, self.result

    def __inverse_adjoint(self):
        flow_det, det = self.determinant(show=False)
        flow_adj, adj = self.adjoint(False)
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

    def __inverse_gauss(self):
        def get_val(fraction):
            return f"{int(fraction.numerator / fraction.denominator)}" \
                if fraction.numerator % fraction.denominator == 0 \
                else f"{fraction.numerator}/{fraction.denominator}"

        def create_flows(a, b):
            f = []
            for i in range(len(a)):
                tf = "[" + ",\t".join(get_val(a[i][j]) for j in range(len(a))) + "\t\t|\t" \
                     + ",\t".join(get_val(b[i][j]) for j in range(len(b))) + "]"
                f.append(tf)
            f.append("")
            return f

        result = []
        flows = []
        data = []

        # copying data
        for x in range(len(self.data)):
            data.append([])
            result.append([])
            for y in range(len(self.data[x])):
                result[x].append(Fraction(1 if x == y else 0))
                data[x].append(Fraction(self.data[x][y]))

        # Make Fractions
        for x in range(len(data)):
            for y in range(len(data)):
                data[x][y] = Fraction(data[x][y])
                result[x][y] = Fraction(result[x][y])

        # Applying Gauss Jordan Elimination
        for x in range(len(data)):
            for y in range(len(data)):
                if x != y:
                    ratio = data[y][x] / data[x][x]
                    for z in range(len(data)):
                        data[y][z] -= ratio * data[x][z]
                        result[y][z] -= ratio * result[x][z]
                    flows += create_flows(data, result)

        # Row operation to make principal diagonal element to 1
        for x in range(len(data)):
            divisor = data[x][x]
            for y in range(len(data)):
                data[x][y] = data[x][y] / divisor
                result[x][y] = result[x][y] / divisor
            flows += create_flows(data, result)

        self.flow = flows
        self.result = result
        self.prints()

        return flows, result

    def determinant(self, method=SARRUS, data=None, show=True):
        if data is None:
            data = self.data

        data_type = len(data)

        if method == Matrix.SARRUS:
            if data_type == 2:
                return self.__determinant2x2(show, data)
            elif data_type == 3:
                return self.__determinant3x3_sarrus(show, data)
            elif data_type == 4:
                return self.__determinant4x4_sarrus(show, data)
            else:
                raise Exception("Invalid Type")
        elif method == Matrix.EXPANSION_COFACTOR:
            if data_type == 2:
                return self.__determinant2x2(show)
            else:
                return self.__determinant_expansion_cofactor(show)
        elif method == Matrix.GAUSS:
            if data_type == 3:
                return self.__determinant_gauss()
            else:
                return self.determinant()

    def transpose(self, data=None, show=True):
        if data is None:
            data = self.data
        self.result = [[data[j][i] for j in range(len(data[i]))] for i in range(len(data))]
        if show:
            self.prints()
        return self.result

    def minor(self, i_row, i_col, data=None, show=True):
        if data is None:
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

    def cofactor(self, i_row, i_col, data=None, show=True):
        if data is None:
            data = self.data

        mnr = self.minor(i_row, i_col, data, False)
        _, result = self.determinant(data=mnr, show=False)
        self.result = result * (-1 if (i_row + i_col) % 2 == 1 else 1)
        self.flow = mnr

        if show:
            self.prints()

        return mnr, self.result

    def adjoint(self, show=True):
        data = self.transpose(self.data, False)
        result = []
        flow = ["Adjoint => "]
        for i_row in range(len(data)):
            result.append([])
            temp_flow = []
            for i_col in range(len(data[i_row])):
                mnr, cof = self.cofactor(i_row, i_col, data, False)
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

        if show:
            self.prints()

        return flow, result

    def inverse(self, method=ADJOINT):
        if method == Matrix.ADJOINT:
            return self.__inverse_adjoint()
        else:
            return self.__inverse_gauss()

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
                    [str(y) if type(y).__name__ == 'int' else f"{Fraction(y).numerator}/{Fraction(y).denominator}"
                    if Fraction(y).numerator % Fraction(y).denominator != 0
                    else f"{int(Fraction(y).numerator / Fraction(y).denominator)}"
                     for y in x])
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
                        if Fraction(y).numerator % Fraction(y).denominator != 0
                        else f"{int(Fraction(y).numerator / Fraction(y).denominator)}"
                         for y in x])
                    print(f"[{row}]")
