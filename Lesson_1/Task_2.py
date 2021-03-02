"""Task 1. Part 'a' """

lst = [pow(el, 3) for el in range(1, 1001, 2)]
lst_2 = []
for i in lst:
    s = 0
    while i > 0:
        digit = i % 10
        s += digit
        i //= 10
    if s % 7 == 0:
        lst_2.append(s)
print(sum(lst_2))

"""Task 1. Part 'b' """

lst = [pow(el, 3) + 17 for el in range(1, 1001, 2)]
lst_2 = []
for i in lst:
    s = 0
    while i > 0:
        digit = i % 10
        s += digit
        i //= 10
    if s % 7 == 0:
        lst_2.append(s)
print(sum(lst_2))

"""Task 1. Part 'c' """

lst = []
for i in range(1, 1001, 2):
    s = 0
    result = pow(i, 3) + 17
    while result > 0:
        digit = result % 10
        s += digit
        result //= 10
    if s % 7 == 0:
        lst.append(s)
print(sum(lst))
