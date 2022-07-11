import random
import string

lst = []
item = 0


def binary_search(bs_lst, bs_item):
    low = 0
    high = len(bs_lst) - 1

    count = 0

    while low <= high:
        count += 1
        mid = (low + high) // 2
        guess = bs_lst[mid]
        if guess == bs_item:
            return mid, count
        elif guess < bs_item:
            low = mid + 1
        elif guess > bs_item:
            high = mid - 1
    print(bs_lst)
    return f"Number {bs_item} is not found", count


def bs_file():
    input_file = open("list_numbers.txt", "r")
    lst = [int(x) for x in input_file.read().split()]
    item = int(input())
    print(lst)
    print(binary_search(lst, item))
    input_file.close()


def bs_rnd():
    dict = {}
    list_abc = string.ascii_uppercase
    for i in range(16):
        dict[list_abc[random.randint(0, len(list_abc) - 1)]] = random.randint(0, 500)
    item = int(input())
    print(binary_search(sorted(dict.values()), item))


bs_file()
