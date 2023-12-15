#!usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
import matplotlib.pyplot as plt
import random
import sympy as sp


def heapify(list_of_num, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list_of_num[i] < list_of_num[left]:
        largest = left

    if right < n and list_of_num[largest] < list_of_num[right]:
        largest = right

    if largest != i:
        list_of_num[i], list_of_num[largest] = list_of_num[largest], list_of_num[i]
        heapify(list_of_num, n, largest)


def heapsort(list_of_num):
    n = len(list_of_num)

    for i in range(n // 2 - 1, -1, -1):
        heapify(list_of_num, n, i)

    for i in range(n - 1, 0, -1):
        list_of_num[i], list_of_num[0] = list_of_num[0], list_of_num[i]
        heapify(list_of_num, i, 0)


def min_grh(x, y):
    sum_x = sum(x)
    sum_y = sum(y)

    sum_x2 = sum(i ** 2 for i in x)
    sum_xy = sum([i * j for i, j in zip(x, y)])

    n = len(x) + 1

    a, b = sp.symbols('a b')

    eq1 = sp.Eq(sum_x2 * a + sum_x * b, sum_xy)
    eq2 = sp.Eq(sum_x * a + (n) * b, sum_y)

    solution = sp.solve((eq1, eq2), (a, b))

    x1 = x
    x2 = [solution[a] * i + solution[b] for i in x1]
    return x1, x2


def ever_sort(x, y):
    for i in range(1000, 50001, 1000):
        x.append(i)
        list_of_num = [j for j in range(i)]
        execution_time = timeit.timeit(
            lambda: heapsort(list_of_num), number=1
        )
        y.append(execution_time)

    x1, y1 = min_grh(x, y)

    create_grf(
        x,
        y,
        x1,
        y1,
        "Отсортированный список",
        "Размер списка",
        "Время работы"
    )


def worst_sort(x, y):
    for i in range(1000, 50001, 1000):
        x.append(i)
        list_of_num = [j for j in range(i, 0, -1)]
        execution_time = timeit.timeit(
            lambda: heapsort(list_of_num), number=1
        )
        y.append(execution_time)

    x1, y1 = min_grh(x, y)

    create_grf(
        x,
        y,
        x1,
        y1,
        "Неотсортированный список",
        "Размер списка",
        "Время работы"
    )


def gen_list(n):
    nums = []
    for _ in range(n):
        nums.append(random.randint(1, 100))
    return nums


def sr_sort(x, y):
    for i in range(1000, 50001, 1000):
        x.append(i)
        list_of_num = gen_list(i)
        execution_time = timeit.timeit(
            lambda: heapsort(list_of_num), number=1
        )
        y.append(execution_time)

    x1, y1 = min_grh(x, y)

    create_grf(
        x,
        y,
        x1,
        y1,
        "Cписок с радомными значениями",
        "Размер списка",
        "Время работы"
    )


def create_grf(x, y, x1, y1, name_of_graph, name_x, name_y):
    plt.plot(x, y, 'o', color='red')
    plt.plot(x1, y1, 'o-', color='blue')

    plt.xlabel(name_x)
    plt.ylabel(name_y)

    plt.title(name_of_graph)
    plt.show()


def main():

    ever_sort(x=[], y=[])
    worst_sort(x=[], y=[])
    sr_sort(x=[], y=[])


if __name__ == "__main__":
    main()
