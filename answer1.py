my_list = [42, 43]
my_dict = {
    "foo": {"a": 12, "b": (1, 2, 3, 4, my_list)},
    "bar": {"c": 12, "d": {5, 6, 7, 8}},
    "moo": {"e": 12, "f": {"Lol": ["L", "o", "l"]}}}

#Выведите на консоль значение ключа ‘foo’.
print(my_dict['foo'])
#Выведите на консоль значение ключа ‘b’.
print(my_dict['foo']['b'])
#Добавьте в my_list 44.
my_dict['foo']['b'][4].append(44)
print(my_dict['foo']['b'])
#Снова выведите на консоль значение ключа ‘b’.
#Выведите множество.
my_dict1 = set(my_dict)
print(my_dict1)

#Снова выведите множество.
#Удалите из списка элемент ‘o’.
my_dict['moo']['f']['Lol'].remove('o')
print(my_dict['moo']['f']['Lol'])
#Добавьте в словарь, который является значением ключа ‘f’ ключ ‘K’ со значением ['K', 'e', 'k'].
my_dict['moo']['K'] = ['K', 'e', 'k']
print(my_dict['moo'])
#Очистите словарь my_dict.
my_dict.clear()
print(my_dict)