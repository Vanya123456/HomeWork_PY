def odd_nums_gen(n):
    """The generator generate odd numbers from 1 to 'n'-number. The function with 'yield'"""
    for el in range(1, n + 1, 2):
        yield el


odd_numbers = odd_nums_gen(15)
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))


def odd_nums_gen(n):
    """The generator generate odd numbers from 1 to 'n'-number. The function without 'yield'"""
    odd_nums = (el for el in range(1, n + 1, 2))
    return odd_nums


odd = odd_nums_gen(15)
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
