def rivien_summat(matriisi: list):
    for list in matriisi:
        list.append(sum(list))


if __name__ == '__main__':
    matriisi = [[1, 2], [3, 4]]
    rivien_summat(matriisi)
    print(matriisi)
