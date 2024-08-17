immutable_var = 'zero', 0, 'seven', 7
print('immutable_ver:', immutable_var)
# значения элементов кортежа нельзя изменить т.к. кортежи это неизменяемый тип данных,
# и является упорядоченной коллекцией
# однако это всё же возможно путем преобразования кортежа в изменяемый тип (например list) и обратно
# либо если имеются изменяемые объекты внутри
mutable_list = ['zero', 0, 'seven', 7]
mutable_list[0] = 'ten'
mutable_list[1] = 10
mutable_list[2] = 'two'
mutable_list[3] = 2
print('mutable_list:',mutable_list)
