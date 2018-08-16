# encoding=utf8
# pylint: disable=mixed-indentation, multiple-statements, old-style-class
"""Implementations of High Conditioned Elliptic functions."""

from NiaPy.benchmarks.benchmark import Benchmark

__all__ = ['Elliptic']

class Elliptic(Benchmark):
	r"""Implementations of High Conditioned Elliptic functions.

	Date: 2018

	Author: Klemen Berkovič

	License: MIT

	Function:
	**High Conditioned Elliptic Function**
	
		:math:`f(\textbf{x}) = \sum_{i=1}^D \left( 10^6 \right)^{ \frac{i - 1}{D - 1} } x_i^2`

		**Input domain:**
		The function can be defined on any input domain but it is usually
		evaluated on the hypercube :math:`x_i ∈ [-100, 100]`, for all :math:`i = 1, 2,..., D`.

		**Global minimum:**
		:math:`f(x^*) = 0`, at :math:`x^* = (420.968746,...,420.968746)`

	LaTeX formats:
		Inline:
				$f(\textbf{x}) = \sum_{i=1}^D \left( 10^6 \right)^{ \frac{i - 1}{D - 1} } x_i^2$

		Equation:
				\begin{equation} f(\textbf{x}) = \sum_{i=1}^D \left( 10^6 \right)^{ \frac{i - 1}{D - 1} } x_i^2 \end{equation}

		Domain:
				$-100 \leq x_i \leq 100$

	Reference:
	http://www5.zzu.edu.cn/__local/A/69/BC/D3B5DFE94CD2574B38AD7CD1D12_C802DAFE_BC0C0.pdf
	"""
	def __init__(self, Lower=-100.0, Upper=100.0): Benchmark.__init__(self, Lower, Upper)

	@classmethod
	def function(cls):
		def evaluate(D, sol):
			val = 0.0
			for i in range(D): val += (10 ** 6) ** (i / (D - 1)) * sol[i]
			return val
		return evaluate

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
