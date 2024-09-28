first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = list((abs(len(x[0]) - len(x[1])) for x in zip(first, second) if len(x[0]) != len(x[1])))
print(first_result)

second_result = list( (len(second[i]) == len(first[i]) for i in range(max(len(first), len(second))) ) )
print(second_result)