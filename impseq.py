""" Generate unit sample sequence page 23 """

from numpy import arange, int16


def impseq(n0, n1, n2):
    """ Generates x(n) = delta(n-n0); n1 <= n <= n2
        -------------------------------------------
        (x, n) = impseq(n0, n1, n2)
    """
    n = arange(n1, n2 + 1)
    x = (n0 == n).astype(int16)
    return x, n
