import json
import os
from fractions import Fraction

import matrix


def intro():
    print("Welcome to matrix calculator")
    print()
    print("Available Command: ")
    print("- add         : Add New Matrix")
    print("- addition    : Count Add 2 Matrix")
    print("- adjoint     : Count Adjoint Matrix")
    print("- cancel      : Back To Homepage")
    print("- clear       : Clear Stored Matrix Data")
    print("- determinant : Count Determinant")
    print("- done        : Exit Application")
    print("- exit        : Exit Application")
    print("- generate    : Generate Random matrix")
    print("- inverse     : Inverse Matrix")
    print("- multiply    : Count Multiply matrix with matrix or matrix with numeric")
    print("- show        : Showing stored matrix")
    print("- subtract    : Count Subtract 2 Matrix")
    print("- transpose   : Transposing Matrix")
    print()
    print("Example Add Matrix")
    print("Matrix A => ")
    print("|1   2   3|")
    print("|4   5   6|")
    print("|7   8   9|")
    print("Matrix Name: A")
    print("Input Matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
    print()


def cls():
    if os.name == 'posix':
        os.system("clear")
    else:
        os.system("cls")
    intro()


def not_found():
    print("Matrix has been not declared")


def get_matrix(m_name, stored=None, accept_num=False):
    while True:
        if stored is not None:
            m_name = input(m_name)
            if m_name.lower() == "cancel":
                return m_name.lower()
            elif m_name in stored:
                return {
                    "name": m_name,
                    "matrix": stored[m_name]
                }
            elif accept_num:
                try:
                    if m_name.isnumeric():
                        return {
                            "name": m_name,
                            "matrix": int(m_name)
                        }
                    else:
                        if "/" in m_name or "." in m_name or "," in m_name:
                            return {
                                "name": m_name,
                                "matrix": Fraction(m_name.replace(" ", ""))
                            }
                        else:
                            not_found()
                except Exception as _:
                    not_found()
            else:
                print(name)
                print(stored)
                not_found()
        else:
            try:
                m_data = input(f'Input Matrix {m_name}: ')
                if m_data.lower() == "cancel":
                    return m_data.lower()
                return json.loads(m_data)
            except Exception as _:
                print("Invalid Matrix format")


if __name__ == '__main__':
    intro()
    data = {}


    def save_result(m):
        is_save = input("Save result? [y|n]").lower() == "y"
        if is_save:
            n = input("Matrix Name: ")
            if n.lower() != "cancel":
                data[n] = m


    while True:
        command = input("Command: ").lower()
        if command == "add":
            name = input("Matrix Name: ")
            if name.lower() == "cancel":
                cls()
            else:
                g_data = get_matrix(name)
                if g_data == "cancel":
                    cls()
                else:
                    data[name] = g_data
        elif command == "addition":
            matrix1 = get_matrix("Input Matrix Name 1: ", data)
            if matrix1 == "cancel":
                cls()
            else:
                matrix2 = get_matrix("Input Matrix Name 2: ", data)
                if matrix2 == "cancel":
                    cls()
                else:
                    addition = matrix.addition(matrix1, matrix2)
                    matrix.prints(addition)
                    save_result(addition)
        elif command == "adjoint":
            matrix1 = get_matrix("Input Matrix Name: ", data)
            if matrix1 == "cancel":
                cls()
            else:
                flow, adjoint = matrix.adjoint(matrix1)
                matrix.prints(matrix1, adjoint, flow)
                save_result(adjoint)
        elif command == "clear":
            data = {}
            cls()
        elif command in ["done", "exit"]:
            exit(0)
        elif command == "determinant":
            matrix1 = get_matrix("Input Matrix Name: ", data)
            if matrix1 == "cancel":
                cls()
            else:
                print("List Type:")
                print("1. Sarrus")
                print("2. Cofactor")
                types = input("Input Type:")

                if types.lower() in ["2", "cofactor"]:
                    flow, determinant = matrix.determinant(matrix1, matrix.EXPANSION_COFACTOR)
                else:
                    flow, determinant = matrix.determinant(matrix1)
                matrix.prints(matrix1, determinant, flow)
        elif command == "generate":
            name = input("Matrix Name: ")
            if name.lower() == "cancel":
                cls()
            else:
                row = None
                col = None
                min_val = None
                g_data = None

                while row is None:
                    value = input("Row count [numeric]: ")
                    if value.lower() == "cancel":
                        row = 0
                        cls()
                    elif not value.isnumeric():
                        print("Invalid row count")
                    else:
                        row = int(value)
                        while col is None:
                            value = input("Col count [numeric]: ")
                            if value.lower() == "cancel":
                                col = 0
                                cls()
                            elif not value.isnumeric():
                                print("Invalid col count")
                            else:
                                col = int(value)
                                while min_val is None:
                                    value = input("Min Value [numeric|none]: ")
                                    if value.lower() == "cancel":
                                        min_val = 0
                                        cls()
                                    elif value.lower() == "none":
                                        min_val = 0
                                        g_data = matrix.generate_data(row, col)
                                        data[name] = g_data
                                        matrix.prints(g_data)
                                    elif not value.isnumeric():
                                        print("Invalid min value")
                                    else:
                                        min_val = int(value)
                                        g_data = matrix.generate_data(row, col, min_val)
                                        data[name] = g_data
                                        matrix.prints(g_data)
        elif command == "inverse":
            matrix1 = get_matrix("Input Matrix Name: ", data)
            if matrix1 == "cancel":
                cls()
            else:
                flow, inverse = matrix.inverse(matrix1)
                matrix.prints(matrix1, inverse, flow)
                save_result(inverse)
        elif command == "multiply":
            matrix1 = get_matrix("Input Matrix 1 or num 1: ", data, True)
            if matrix1 == "cancel":
                cls()
            else:
                matrix2 = get_matrix("Input Matrix 2 or num 2: ", data, True)
                if matrix2 == "cancel":
                    cls()
                else:
                    try:
                        flow, multiply = matrix.multiply(matrix1['matrix'], matrix2['matrix'])
                        matrix.prints(None, multiply, flow)
                        save_result(multiply)
                    except Exception as e:
                        print("Error: ", e)
        elif command == "show":
            for x in data:
                matrix.prints({
                    "name": x,
                    "matrix": data[x]
                })
        elif command == "subtract":
            matrix1 = get_matrix("Input Matrix 1: ", data)
            if matrix1 == "cancel":
                cls()
            else:
                matrix2 = get_matrix("Input Matrix 2: ", data)
                if matrix2 == "cancel":
                    cls()
                else:
                    subtract = matrix.subtract(matrix1['matrix'], matrix2['matrix'])
                    matrix.prints(subtract)
                    save_result(subtract)
        elif command == "transpose":
            matrix1 = get_matrix("Input Matrix Name: ", data)
            if matrix1 == "cancel":
                cls()
            else:
                transpose = matrix.transpose(matrix1)
                matrix.prints(transpose)
                save_result(transpose)
        else:
            print("Command not found")
