import random

num_list = []
odd_num_list = []
summ = 0

def sum_of_odd(input_list):
    # num = 0
    # num in range(100)
    num_list.append(random.randint(1, 101))
    for item in input_list:
        if item % 2 != 0:
            odd_num_list.append(item)
    summ = sum(odd_num_list)
    return summ

print(sum_of_odd(num_list))

sum_of_odd(num_list)





