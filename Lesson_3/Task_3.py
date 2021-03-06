def thesaurus(*names):
    """Sort of names by first letter. Arguments are names in the format 'Name', 'Name'"""
    lst_names = [*names]
    my_dict = {}
    for el in lst_names:
        my_dict[el[0]] = list(filter(lambda x: x.startswith(el[0]), lst_names))
    return my_dict


print(thesaurus('Иван', 'Мария', 'Илья', 'Петр'))
