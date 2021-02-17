duration = int(input('Enter seconds '))
d = duration // 86400
h = duration % 86400 // 3600
m = duration % 3600 // 60
s = duration % 3600 % 60
print(f'{d} days {h} hours {m} minutes {s} seconds')
