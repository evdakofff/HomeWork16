def print_params(a=1, b='Im_ingeneer', c=True):
    return print(a, b, c)


print_params("7.3")
print_params(7, 'Как хочется спать')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['Сон для слабаков', 1.5, False]
values_dict = {'a': 'А может все же поспать?', 'b': True, 'c': 1991}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
