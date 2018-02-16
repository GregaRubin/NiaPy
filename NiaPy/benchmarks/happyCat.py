# encoding=utf8
# pylint: disable=anomalous-backslash-in-string
"""Implementation of Happy cat function.

Date: 2018

Author: Lucija Brezočnik

License: MIT

Function: Happy cat function

Input domain:
    The function can be defined on any input domain but it is usually
    evaluated on the hypercube x_i ∈ [-100, 100], for all i = 1, 2,..., D.

LaTeX formats:
    Inline: $ f(\mathbf{x}) = {\left |\sum_{i = 1}^D {x_i}^2 -
            D \right|}^{1/4} + (0.5 \sum_{i = 1}^D {x_i}^2 +
            \sum_{i = 1}^D x_i) / D + 0.5$
    Equation:  \begin{equation} f(\mathbf{x}) = {\left |\sum_{i = 1}^D {x_i}^2 - 
            D \right|}^{1/4} + (0.5 \sum_{i = 1}^D {x_i}^2 +
            \sum_{i = 1}^D x_i) / D + 0.5 \end{equation}
    Domain: $-100 \leq x_i \leq 100$

Reference: http://bee22.com/manual/tf_images/Liang%20CEC2014.pdf
"""

import math

__all__ = ['HappyCat']


class HappyCat(object):

    def __init__(self, Lower=-100, Upper=100):
        self.Lower = Lower
        self.Upper = Upper

    @classmethod
    def function(cls):
        def evaluate(D, sol):

            val = 0.0
            val1 = 0.0
            val2 = 0.0

            for i in range(D):
                val1 += math.pow(abs(math.pow(sol[i], 2) - D), 0.25)
                val2 += (0.5 * math.pow(sol[i], 2) + sol[i]) / D

            val = val1 + val2 + 0.5

            return val

        return evaluate
