import random
from matplotlib import pyplot as plt


def gnr_arr(arr_len):
    arr = []
    for i in range(arr_len):
        arr.append(random.randint(0, 500))
    return arr


def selection_sort_list(arr):
    count = 0
    for i in range(len(arr)-1):
        for k in range(i+1, len(arr)):
            count += 1
            if arr[k] < arr[i]:
                arr[i], arr[k] = arr[k], arr[i]
    print(arr)
    return count


def selection_sort_list_gen(arr):
    count = 0
    for i in range(len(arr)-1):
        min_idx = i
        for k in range(i+1, len(arr)):
            count += 1
            if arr[k] < arr[min_idx]:
                min_idx = k
        if min_idx != i:
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp
    print(arr)
    return count


def use_selection_sort():
    arr_len = int(input("Какая будет длина массива? "))
    rounds = int(input("Сколько итераций? "))
    total_run_time = 0
    run_time_list = []
    for i in range(rounds):
        arr = gnr_arr(arr_len)
        run_time = selection_sort_list_gen(arr)
        total_run_time += run_time
        run_time_list.append(run_time)
    print(total_run_time/rounds)
    plt.hist(run_time_list, bins=12, edgecolor="black")
    plt.show()


use_selection_sort()
