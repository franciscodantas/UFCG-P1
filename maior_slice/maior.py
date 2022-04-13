def maior_slice(lista):
    slice_ = []
    maior_slice = []
    for index in range(len(lista)):
        if lista[index] < lista[index + 1]:
            slice_.append(lista[index])
        else:
            slice_.append(lista[index])
            maior_slice.append(slice_)
            slice_ = []

    for index in range(len(maior_slice) - 1, -1, -1):
        if len(maior_slice[index]) == len(maior_slice[index - 1]) and len(maior_slice) > 1:
            maior_slice.pop(index - 1)
        elif maior_slice[index] < maior_slice[index - 1]:
            maior_slice.pop()

    return maior_slice[0]
