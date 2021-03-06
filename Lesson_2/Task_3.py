lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
string = ''
for idx, el in enumerate(lst, 1):
    if idx == 2:
        lst.pop(1)
        lst.insert(1, el.replace('5', '"05"'))
    elif idx == 9:
        lst.pop(8)
        lst.insert(8, el.replace('+5', '"+05"'))
    elif idx == 5:
        lst.pop(3)
        lst.insert(3, '"17"')
for el in lst:
    string += el + ' '
print(string)