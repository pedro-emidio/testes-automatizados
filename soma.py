def soma(x, y):
    """
    Soma x e y
    >>> soma(12, 50)
    62

    >>> soma(-16, 20)
    4

    >>> soma(12.5, -11.5)
    1.0

    >>> soma('10', '15')
    Traceback (most recent call last):
    ...
    AssertionError: Os parametros devem ser do tipo int ou float.
    """
    assert isinstance(x, (int, float)), 'Os parametros devem ser do tipo int ou float.'
    assert isinstance(y, (int, float)), 'Os parametros devem ser do tipo int ou float.'
    return x + y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
