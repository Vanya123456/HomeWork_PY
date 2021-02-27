def num_translate_adv(number):
    """Translating numbers from English to Russian. Number - the number for translate in the format 'one' or 'One'.
    Translation is available from one to ten.
    """
    translate_dict = {'one': 'один',
                      'two': 'два',
                      'three': 'три',
                      'four': 'четыре',
                      'five': 'пять',
                      'six': 'шесть',
                      'seven': 'семь',
                      'eight': 'восемь',
                      'nine': 'девять',
                      'ten': 'десять',
                      }
    for key, val in translate_dict.items():
        if number == key:
            return val
        elif number == key.capitalize():
            return val.capitalize()


print(num_translate_adv('Six'))
