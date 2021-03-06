# """Task_5. Part A, B."""

catalog = [57.8, 98, 46.51, 102.67, 174.6, 135.7, 102, 196.63, 201.79, 19.75, 359.98, 146.79]
print(id(catalog))
catalog.sort()
print(id(catalog))
for el in catalog:
    string = str(el).split('.')
    if len(string) == 1:
        print(f'{str(string[0])} руб 00 коп', end=', ')
    elif len(string[1]) == 1:
        print(f'{str(string[0])} руб 0{str(string[1])} коп', end=', ')
    else:
        print(f'{str(string[0])} руб {str(string[1])} коп', end=', ')

# """Task_5. Part. Part C."""

catalog_2 = [57.8, 98, 46.51, 102.67, 174.6, 135.7, 102, 196.63, 201.79, 19.75, 359.98, 146.79]
print(id(catalog_2))
catalog_2.sort(reverse=True)
print(id(catalog_2))
for el in catalog_2:
    string = str(el).split('.')
    if len(string) == 1:
        print(f'{str(string[0])} руб 00 коп', end=', ')
    elif len(string[1]) == 1:
        print(f'{str(string[0])} руб 0{str(string[1])} коп', end=', ')
    else:
        print(f'{str(string[0])} руб {str(string[1])} коп', end=', ')

# """Task_5. Part. Part D."""

catalog = [57.8, 98, 46.51, 102.67, 174.6, 135.7, 102, 196.63, 201.79, 19.75, 359.98, 146.79]
print(id(catalog))
catalog.sort()
print(id(catalog))
for el in catalog[-5:]:
    string = str(el).split('.')
    if len(string) == 1:
        print(f'{str(string[0])} руб 00 коп', end=', ')
    elif len(string[1]) == 1:
        print(f'{str(string[0])} руб 0{str(string[1])} коп', end=', ')
    else:
        print(f'{str(string[0])} руб {str(string[1])} коп', end=', ')
