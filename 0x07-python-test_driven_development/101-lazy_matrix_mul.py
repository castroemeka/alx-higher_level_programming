#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
=======

# This funtion multiplies 2 matrices by using the module 'NumPy'

import numpy as nmp

def lazy_matrix_mul(m_a, m_b):
    return (nmp.matmul(m_a, m_b))

print("\nCode developed by CASTRO")
>>>>>>> 3a2eaf8046d8ffb5d83c112dbc4ecb8cd4b3b32b
