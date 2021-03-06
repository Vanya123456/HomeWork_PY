from itertools import zip_longest


def some_tuple_gen():
    """The generator generate tuples from lists ''tutors' and 'klasses'"""
    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
    klases = ['9А', '7В', '9Б', '9В', '8Б', '10А', '11Б', '5В']
    if len(tutors) > len(klases):
        for tutor, klass in zip_longest(tutors, klases):
            yield tutor, klass
    elif len(tutors) < len(klases) or len(tutors) == len(klases):
        for tutor, klass in zip(tutors, klases):
            yield tutor, klass


my_tuple = some_tuple_gen()
print(next(my_tuple))
print(next(my_tuple))
print(next(my_tuple))
print(next(my_tuple))
print(next(my_tuple))
print(next(my_tuple))
print(next(my_tuple))
print(next(my_tuple))
