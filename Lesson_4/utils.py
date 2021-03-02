from requests import get


def currency_rate(currency):
    res = get('http://www.cbr.ru/scripts/XML_daily.asp').text.split('<CharCode>')
    for el in res:
        some_lst = el.replace('</CharCode>', ' ').replace('<Value>', ' ').replace('</Value>', ' ').replace(',', '.').split()
        if currency in some_lst:
            for i in some_lst:
                try:
                    print(f'Курс рубля относительно Вашей валюты равен: {float(i)}')
                except ValueError:
                    continue
    if len(currency) < 3:
        print(f'Неверный код валюты {currency}! Проверьте код и попробуйте ещё раз')
