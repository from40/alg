import random
import string
from matplotlib import pyplot as plt


def gnr_dict(dict_len):
    dict = {}
    list_abc = string.ascii_uppercase
    for i in range(dict_len):
        gnr_key = list_abc[random.randint(0, len(list_abc) - 1)]
        while gnr_key in dict.keys():
            gnr_key = list_abc[random.randint(0, len(list_abc) - 1)]
        dict[gnr_key] = random.randint(0, 500)
    return dict


def find_key(dict):
    biggest_value = 0
    chosen_key = ""
    run_time = 1
    for key, value in dict.items():
        run_time += 1
        if value >= biggest_value:
            biggest_value = value
            chosen_key = key
    return chosen_key, run_time


def selectionSortDict(dict):
    new_dict = {}
    run_time = 0
    for i in range(len(dict)):
        chosen_key, find_key_run_time = find_key(dict)
        new_dict[chosen_key] = dict.pop(chosen_key)
        run_time += find_key_run_time
    print(new_dict)
    return run_time


def useSSDict():
    dict_len = int(input("Какая будет длина словаря? "))
    rounds = int(input("Сколько итераций? "))
    total_run_time = 0
    run_time_list = []
    for i in range(rounds):
        ss_run_time = selectionSortDict(gnr_dict(dict_len))
        total_run_time += ss_run_time
        run_time_list.append(ss_run_time)
    print(total_run_time/rounds)
    plt.hist(run_time_list, bins=12, edgecolor="black")
    plt.show()


useSSDict()

