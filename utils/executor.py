import os
import json
from fractions import Fraction

from utils import Matrix


class Executor:

    def __init__(self):
        self.data = {}

    @staticmethod
    def intro():
        print("Welcome to matrix calculator")
        print()
        print("Available Command: ")
        print("- add         : Count Add 2 Matrix")
        print("- adjoint     : Count Adjoint Matrix")
        print("- cancel      : Back To Homepage")
        print("- create      : Create New Matrix")
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

    def cls(self):
        if os.name == 'posix':
            os.system("clear")
        else:
            os.system("cls")
        self.intro()

    @staticmethod
    def not_found():
        print("Matrix has been not declared")

    def input_matrix(self, name, matrix=None):
        if matrix is None:
            while True:
                matrix = input(f'Input Matrix {name}: ')
                self.data[name] = Matrix(name, json.loads(matrix))
                try:
                    if name.lower() == "cancel":
                        return name.lower()
                except Exception as _:
                    print("Invalid Matrix format")
        else:
            self.data[name] = Matrix(name, json.loads(matrix))

    def get_matrix(self, name, accept_num=False):
        while True:
            name = input(name)
            if name.lower() == "cancel":
                return name.lower()
            elif name in self.data:
                return self.data[name]
            elif accept_num:
                try:
                    if name.isnumeric():
                        return int(name)
                    else:
                        if "/" in name or "." in name or "," in name:
                            return Fraction(name.replace(" ", ""))
                        else:
                            self.not_found()
                except Exception as _:
                    self.not_found()
            else:
                self.not_found()

    def save_result(self, matrix):
        is_save = input("Save result? [y|n]").lower() == "y"
        if is_save:
            name = input("Matrix Name: ")
            if name.lower() != "cancel":
                self.data[name] = Matrix(name, matrix)

    def add(self, matrix1=None, matrix2=None):
        if matrix1 is None or matrix2 is None:
            matrix1 = self.get_matrix("Input Matrix Name 1: ")
            if matrix1 == "cancel":
                self.cls()
                return
            else:
                matrix2 = self.get_matrix("Input Matrix Name 2: ")
                if matrix2 == "cancel":
                    self.cls()
                    return
        else:
            if matrix1 in self.data:
                matrix1 = self.data[matrix1]
            else:
                return

            if matrix2 in self.data:
                matrix2 = self.data[matrix2]
            else:
                return

        addition = matrix1 + matrix2
        self.save_result(addition)

    def subtract(self, matrix1=None, matrix2=None):
        if matrix1 is None or matrix2 is None:
            matrix1 = self.get_matrix("Input Matrix Name 1: ")
            if matrix1 == "cancel":
                self.cls()
                return
            else:
                matrix2 = self.get_matrix("Input Matrix Name 2: ")
                if matrix2 == "cancel":
                    self.cls()
                    return
        else:
            if matrix1 in self.data:
                matrix1 = self.data[matrix1]
            else:
                return

            if matrix2 in self.data:
                matrix2 = self.data[matrix2]
            else:
                return

        subtract = matrix1 - matrix2
        self.save_result(subtract)

    def adjoint(self, matrix=None):
        if matrix is None:
            matrix = self.get_matrix("Input Matrix Name: ")
            if matrix == "cancel":
                self.cls()
                return
        elif matrix in self.data:
            matrix = self.data[matrix]
        else:
            return
        adjoint = matrix.adjoint()
        self.save_result(adjoint)

    def determinant(self, matrix=None):
        if matrix is None:
            matrix = self.get_matrix("Input Matrix Name: ")
            if matrix == "cancel":
                self.cls()
                return
        elif matrix in self.data:
            matrix = self.data[matrix]
        else:
            return

        print("List Type:")
        print("1. Sarrus")
        print("2. Cofactor")
        print("3. Gauss")
        types = input("Input Type:")

        if types.lower() in ["2", "cofactor"]:
            matrix.determinant(Matrix.EXPANSION_COFACTOR)
        elif types.lower() in ["3", "gauss"]:
            matrix.determinant(Matrix.GAUSS)
        else:
            matrix.determinant(Matrix.SARRUS)

    def generate(self, name=None, row=None, col=None, min_val=None):
        if name is None:
            name = input("Matrix Name: ")
            if name.lower() == "cancel":
                self.cls()
                return

        while row is None:
            value = input("Row count [numeric]: ")
            if value.lower() == "cancel":
                self.cls()
                return
            elif not value.isnumeric():
                print("Invalid row count")
            else:
                row = int(value)

        while col is None:
            value = input("Col count [numeric]: ")
            if value.lower() == "cancel":
                self.cls()
                return
            elif not value.isnumeric():
                print("Invalid col count")
            else:
                col = int(value)

        while min_val is None:
            value = input("Min Value [numeric|none]: ")
            if value.lower() == "cancel":
                self.cls()
                return
            elif value.lower() == "none" or value.lower() == "":
                min_val = 0
            elif not value.isnumeric():
                print("Invalid min value")
            else:
                min_val = int(value)

        self.data[name] = Matrix.generate(name, row, col, min_val)

    def inverse(self, matrix=None):
        if matrix is None:
            matrix = self.get_matrix("Input Matrix Name: ")
            if matrix == "cancel":
                self.cls()
        elif matrix in self.data:
            matrix = self.data[matrix]
        else:
            return
        inverse = matrix.inverse()
        self.save_result(inverse)

    def multiply(self, matrix1=None, matrix2=None):
        if matrix1 is None or matrix2 is None:
            matrix1 = self.get_matrix("Input Matrix 1 or num 1: ", True)
            if matrix1 == "cancel":
                self.cls()
                return

            matrix2 = self.get_matrix("Input Matrix 2 or num 2: ", True)
            if matrix2 == "cancel":
                self.cls()
                return
        else:
            if matrix1 in self.data:
                matrix1 = self.data[matrix1]
            else:
                return

            if matrix2 in self.data:
                matrix2 = self.data[matrix2]
            else:
                return

        try:
            multiply = matrix1 * matrix2
            self.save_result(multiply)
        except Exception as e:
            print("Error: ", e)

    def transpose(self, matrix=None):
        if matrix is None:
            matrix = self.get_matrix("Input Matrix Name: ")
            if matrix == "cancel":
                self.cls()
        elif matrix in self.data:
            matrix = self.data[matrix]
        else:
            return
        transpose = matrix.transpose()
        self.save_result(transpose)

    def parse_command(self, command=None):
        if command is None:
            original_command = input("Command: ")
            command = original_command.lower()
            if command == "create":
                name = input("Matrix Name: ")
                if name.lower() == "cancel":
                    self.cls()
                else:
                    g_data = self.input_matrix(name)
                    if g_data == "cancel":
                        self.cls()
            elif command == "add":
                self.add()
            elif command == "adjoint":
                self.adjoint()
            elif command == "clear":
                self.data = {}
                self.cls()
            elif command in ["done", "exit"]:
                exit(0)
            elif command == "determinant":
                self.determinant()
            elif command == "generate":
                self.generate()
            elif command == "inverse":
                self.inverse()
            elif command == "multiply":
                self.multiply()
            elif command == "show":
                for x in self.data:
                    self.data[x].prints(data_only=True)
            elif command == "subtract":
                self.subtract()
            elif command == "transpose":
                self.transpose()
            else:
                self.parse_command(original_command)
        else:
            command = command.replace(" ", "").split(":")
            args = command[1:]
            command = command[0]

            if command == "create":
                self.input_matrix(args[0], args[1])
            elif command == "add":
                self.add(args[0], args[1])
            elif command == "adjoint":
                self.adjoint(args[0])
            elif command == "clear":
                self.data = {}
                self.cls()
            elif command in ["done", "exit"]:
                exit(0)
            elif command == "determinant":
                self.determinant(args[0])
            elif command == "generate":
                if len(args) - 1 == 3:
                    min_val = args[3]
                else:
                    min_val = 0
                self.generate(args[0], int(args[1]), int(args[2]), int(min_val))
            elif command == "inverse":
                self.inverse(args[0])
            elif command == "multiply":
                self.multiply(args[0], args[1])
            elif command == "show":
                for x in self.data:
                    self.data[x].prints(data_only=True)
            elif command == "subtract":
                self.subtract(args[0], args[1])
            elif command == "transpose":
                self.transpose(args[0])
            else:
                print("Command not found")

    def start(self):
        self.intro()
        while True:
            self.parse_command()
