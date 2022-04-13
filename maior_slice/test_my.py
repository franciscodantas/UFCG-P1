from undertst import maior_slice

def test_exemplo_1():
    lista = [1, 2, 3, 4, 2, 0, 1]
    assert maior_slice(lista) == [1, 2, 3, 4]

def test_exemplo_2():
    assert maior_slice([7, 6, 2, 9, 10]) == [2, 9, 10]

def test_03():
    assert maior_slice([7, 8, 9, 1, 2, 3, 0]) == [1, 2, 3]
