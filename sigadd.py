""" Signal addition """
from numpy import arange, zeros, nonzero


def sigadd(x1, n1, x2, n2):
    """ implements  y(n) = x1(n)+x2(n)
        ------------------------------
        [y,n] = siggadd(x1, n1, x2, n2)
          y = sum sequence over n, which include n1 and n2
          x1 = first sequence over n1
          x2 = second sequence over n2 (n2 can be different from n1)
    """
    n = arange(min(min(n1), min(n2)), max(max(n1), max(n2)) + 1)
    y1 = zeros(len(n))
    y2 = y1.copy()
    y1[nonzero((n >= min(n1)) & (n <= max(n1)))] = x1
    y2[nonzero((n >= min(n2)) & (n <= max(n2)))] = x2
    y = y1 + y2
    return y, n
