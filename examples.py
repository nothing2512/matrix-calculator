from fractions import Fraction
from utils import Matrix


# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = [[0, 2, 1], [6, 4, 3], [8, 5, 7]]
m = Matrix("A", data)
m.determinant(Matrix.GAUSS)
# # data = [[0, 2, 1], [6, 4, 3], [8, 5, 7]]
# identifier = 1
#
# # Swapping
# for x in range(len(data)):
#     if data[x][0] == 0 and data[x][1] == 0 and x != 2:
#         data[x], data[2] = data[2], data[x]
#         identifier = -identifier
#         break
#
# for x in range(len(data)):
#     if data[x][0] == 0 and data[x][1] != 0 and x != 1:
#         data[x], data[1] = data[1], data[x]
#         identifier = -identifier
#         break
#
# # Start Elimination
# sub = Fraction(data[1][0], data[0][0])
# for x in range(len(data[1])):
#     data[1][x] -= data[0][x] * sub
#
# sub = Fraction(data[2][0], data[0][0])
# for x in range(len(data[2])):
#     data[2][x] -= data[0][x] * sub
#
# sub = Fraction(data[2][1], data[1][1])
# for x in range(1, len(data[2])):
#     data[2][x] -= data[1][x] * sub
#
# for row in data:
#     cols = []
#     for col in row:
#         if isinstance(col, Fraction):
#             if col.numerator % col.denominator == 0:
#                 cols.append(str(int(col.numerator / col.denominator)))
#             else:
#                 cols.append(f"{col.numerator}/{col.denominator}")
#         else:
#             cols.append(str(col))
#     cols = "\t".join(cols)
#     print(f"[{cols}]")
