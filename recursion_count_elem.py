def count_elem(lst):
    if len(lst) == 1:
        return 1
    else:
        return 1 + count_elem(lst[1:])


input_file = open("list_numbers.txt", "r")
lst = [int(x) for x in input_file.read().split()]
print(count_elem(lst))
