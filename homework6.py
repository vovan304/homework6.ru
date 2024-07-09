my_dict = {'Vladimir': 1968, 'Katya': 1969, 'Vitaly': 1990, 'Valentina': 1950}
print('Dict:', my_dict)
print('Existing value:',my_dict['Vitaly'])
print('Not existing value:',my_dict.get('Stella'))
my_dict.update({'Sergey': 2017,
                'Alexandr': 1958})
a = my_dict.pop('Vladimir')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
print(' ')
my_set = {42, 35, 'load', 42, True, True, 'Urban', (4, 5, 6)}
print('Set:', my_set)
my_set.add(8)
my_set.add(9)
my_set.remove(42)
print('Modified set:',my_set)