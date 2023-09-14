#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
---------------------------------------------------------------
 authors: A. Ramirez-Morales (andres.ramirez.morales@cern.ch)
---------------------------------------------------------------
'''

import numpy as np


class MatrixMultiplication:
    """
    Class to compute matrix multiplication in different ways 
    """
    def __init__(self, A, B):
        self.A = A
        self.B = B
        print("Matrix multiplication starts!")

    
    def multiply_matrix_native(self):
        global C
        if  self.A.shape[1] == self.B.shape[0]:
            C = np.zeros((self.A.shape[0], self.B.shape[1]), dtype = int)
            for row in range(rows):
                for col in range(cols):
                    for elt in range(len(self.B)):
                        C[row, col] += self.A[row, elt] * self.B[elt, col]
            return C
        else:
            return "Invalid inputs, try again. Bye!."
