#!usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
import matplotlib.pyplot as plt
import random
import sympy as sp
import numpy as np


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def min_grh(x, y):
    sum_x = sum(x)
    sum_y = sum(y)

    sum_x2 = sum(i ** 2 for i in x)
    sum_xy = sum([i * j for i, j in zip(x, y)])

    n = len(x) + 1

    a, b = sp.symbols('a b')

    eq1 = sp.Eq(sum_x2 * a + sum_x * b, sum_xy)
    eq2 = sp.Eq(sum_x * a + n * b, sum_y)

    solution = sp.solve((eq1, eq2), (a, b))

    x1 = x
    x2 = [solution[a] * i + solution[b] for i in x1]
    return x1, x2


def ever_sort(x, y):
    for i in range(1000, 50001, 1000):
        x.append(i)
        arr = np.array([j for j in range(i)], int)
        execution_time = timeit.timeit(
            lambda: heapsort(arr), number=1
        )
        y.append(execution_time)

    x1, y1 = min_grh(x, y)

    create_grf(
        x,
        y,
        x1,
        y1,
        "Отсортированный массив",
        "Размер массива",
        "Время работы"
    )


def worst_sort(x, y):
    for i in range(1000, 50001, 1000):
        x.append(i)
        arr = np.array([j for j in range(i, 0, -1)], int)
        execution_time = timeit.timeit(
            lambda: heapsort(arr), number=1
        )
        y.append(execution_time)

    x1, y1 = min_grh(x, y)

    create_grf(
        x,
        y,
        x1,
        y1,
        "Неотсортированный массив",
        "Размер массива",
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
        arr = np.array(gen_list(i), int)
        execution_time = timeit.timeit(
            lambda: heapsort(arr), number=1
        )
        y.append(execution_time)

    x1, y1 = min_grh(x, y)

    create_grf(
        x,
        y,
        x1,
        y1,
        "Значения",
        "Размер массива",
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
