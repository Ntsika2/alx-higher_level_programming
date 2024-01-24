#!/usr/bin/python3
<<<<<<< HEAD
def square_matrix_simple(matrix = []):
=======
def square_matrix_simple(matrix=[]):
>>>>>>> 40bdaaf254618943c5b79377d5d723dabff34dd4
    squared = []
    for line in matrix:
        squared.append([c**2 for c in line])
        return squared
