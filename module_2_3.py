my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = -1

while number + 1 != len(my_list) and my_list[number] >= 0:
    number = number + 1

    if my_list[number] >= 1:
        print("Положительное число: ", my_list[number])
    elif my_list[number] == 0:
        continue
    else:
       break