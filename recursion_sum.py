def sum_rec(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_rec(lst[1:])


input_file = open("list_numbers.txt", "r")
lst = [int(x) for x in input_file.read().split()]
print(sum_rec(lst))
