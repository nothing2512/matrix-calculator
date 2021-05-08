from fractions import Fraction

# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# data = [[0, 2, 1], [6, 4, 3], [8, 5, 7]]
data = [[1, 1, 3], [1, 3, -3], [-2, -4, -4]]
result = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
flows = []


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

# flows = create_flows(data, result)
for x in flows:
    print(x)

# for x in result:
#     row = "\t".join(
#         [str(y) if type(y).__name__ == 'int' else f"{Fraction(y).numerator}/{Fraction(y).denominator}"
#             if Fraction(y).numerator % Fraction(y).denominator != 0
#             else f"{int(Fraction(y).numerator / Fraction(y).denominator)}"
#             for y in x])
#     print(f"[{row}]")