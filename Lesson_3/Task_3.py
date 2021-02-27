def thesaurus():
    """Sort of names by first letter."""
    lst = ("Иван", "Мария", "Петр", "Илья", "Маргарита", "Павел")
    my_dict = {}
    for el in lst:
        my_dict[el[0]] = list(filter(lambda x: x.startswith(el[0]), lst))
    return my_dict


print(thesaurus())
