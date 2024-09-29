from random import choice

# Задание 1 - написать lambda-функцию для посимвольного сравнения двух строк
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y , first, second)))


# Задание 2

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w') as file:
            for d in data_set:
                file.writelines (str(d) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Задание 3

class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self, *args, **kwargs):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
