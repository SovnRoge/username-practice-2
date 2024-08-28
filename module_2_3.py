my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
start_list = 0
while start_list < len(my_list):
    a = (my_list[start_list])
    start_list = start_list + 1
    if a == 0:
        continue
    elif a < 0:
        break
    else:
        print(a)
