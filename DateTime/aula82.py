import datetime

print(datetime.datetime.now())

hoje = datetime.datetime.now()

print(hoje.year)
print(hoje.month)
print(hoje.day)
print(hoje.weekday())  # 0 = segunda, 6 = domingo
print(hoje.isoweekday())  # 1 = segunda, 7 = domingo