# Есть 2 сортированных последовательности целых чисел.
# Хотим напечатать те элементы из первой последовательности, которых нет во второй последовательности(
# если число хоть раз встречается во второй последовательности, то удаляем все его экземпляры из первой).


def arr_minus_arr(a, b):
    pos_a = 0
    pos_b = 0
    result = []

    if len(b) == 0:
        return a

    while pos_a < len(a):
        if b[pos_b] == a[pos_a]:
            pos_a += 1
            continue
        if b[pos_b] < a[pos_a]:
            pos_b += 1
            if len(b) <= pos_b:
                result = result + a[pos_a:]
                break
            continue
        if b[pos_b] > a[pos_a]:
            result.append(a[pos_a])
            pos_a += 1
            continue

    print(result)
    return result


a = [1, 2, 2, 2, 10, 100]
b = [1, 2, 10, 500]
c = [100]
assert c == arr_minus_arr(a, b)

a = [5, 6]
b = [1, 6]
c = [5]
assert c == arr_minus_arr(a, b)

a = []
b = []
c = []
assert c == arr_minus_arr(a, b)

a = [2, 3, 4]
b = [1]
c = [2, 3, 4]
assert c == arr_minus_arr(a, b)

a = [3, 6, 7, 8]
b = [6]
c = [3, 7, 8]
assert c == arr_minus_arr(a, b)
