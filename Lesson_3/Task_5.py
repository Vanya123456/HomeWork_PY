import random


def get_jokes(num):
    """Generation of random jokes. Num - the desired number of jokes"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    my_jokes = []
    for _ in zip(nouns, adverbs, adjectives):
        my_joke = f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'
        my_jokes.append(my_joke)
    return random.sample(my_jokes, num)


print(get_jokes(4))
