import random


def gnr_arr(arr_len):
    arr = []
    for i in range(arr_len):
        arr.append(random.randint(0, 500))
    return arr


def find_biggest(arr):
    if len(arr) == 1:
        print(arr[0])
    else:
        if arr[0] > arr[1]:
            del arr[1]
        else:
            del arr[0]
        find_biggest(arr)


def use_selection_sort():
    arr_len = int(input("Какая будет длина массива? "))
    arr = gnr_arr(arr_len)
    find_biggest(arr)


use_selection_sort()

