# Patryk Tomaszewski, 302930

import random
from timeit import timeit
import sys
sys.setrecursionlimit(1500)
from typing import Tuple, List


def quicksort_used_in_quicksort(lista: list, start: int, koniec: int) -> None:

    pivot = lista[koniec-1]
    i = start
    j = koniec
    while i < j:
        if lista[i] < pivot:
            i += 1
        if lista[j] > pivot:
            j -= 1
        if lista[i] >= pivot and lista[j] <= pivot:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
            j -= 1
    if start < j:
        quicksort_used_in_quicksort(lista, start, j)
    if i < koniec:
        quicksort_used_in_quicksort(lista, i, koniec)

def quicksort(lista: list) -> list:
    c_list = lista[:]
    quicksort_used_in_quicksort(c_list, 0, len(c_list) - 1)

    return c_list



def bubblesort(lst) -> tuple:
    c_list = lst[:]
    n = len(c_list)
    counter = 0

    while n > 1:
        ending = True


        for k in range(1,n):
            counter += 1
            if c_list[k] < c_list[k-1]:
                temp = c_list[k]
                c_list[k] = c_list[k-1]
                c_list[k-1] = temp
                ending = False

        if ending:
            return (c_list,counter)

        n -= 1
    return (c_list, counter)

