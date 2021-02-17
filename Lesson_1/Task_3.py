while True:
    user_answer = int(input('Enter a number from 1 to 20. '))
    if user_answer == 1:
        print(str(user_answer) + ' процент')
        break
    elif 1 < user_answer < 5:
        print(str(user_answer) + ' процента')
        break
    elif 4 < user_answer <= 20:
        print(str(user_answer) + ' процентов')
        break
    else:
        print('Incorrect number.')
