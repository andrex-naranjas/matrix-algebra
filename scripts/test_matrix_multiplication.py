#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
---------------------------------------------------------------
 authors: A. Ramirez-Morales (andres.ramirez.morales@cern.ch)
---------------------------------------------------------------
'''

import numpy as np
# framework includes
from matrix_algebra.matrix_product import MatrixMultiplication 

np.random.seed(27)
A = np.random.randint(1,10,size = (3,3))
B = np.random.randint(1,10,size = (3,2))

prod_matrices = MatrixMultiplication(A, B)
producto_nativo = prod_matrices.multiply_matrix_native()

print(producto_nativo, "Matrix Producto de A y B")
