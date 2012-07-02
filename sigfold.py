""" Folding """


def sigfold(x, n):
    """ implements y(n) = x(-n)
        -----------------------
        y, n = sigfold(x, n)
    notes: only supports 1-d
    """
    y = x[::-1]
    n = -n[::-1]

    return y, n
