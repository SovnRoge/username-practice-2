my_dict = {'apple': 90, 'orange': 150, 'watermelon': 40}
print(my_dict)
print(my_dict['orange'])
print(my_dict.get('pine-apple'))
my_dict.update({'potato': 20,
                'tomato': 80})
deleted_value = my_dict.pop('apple')
print(deleted_value)
print(my_dict)


my_set = {'dot', 10, 'dash', 20, 'comma', 30, 20, 'dash', 'comma', 'dot', 10, 30}
print(my_set)
my_set.update({40, 40, 50, 50, 50, 40})
my_set.discard('comma')
print(my_set)
