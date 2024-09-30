def is_prime(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        prime_or_not = 'Составное' if any(result % d == 0 for d in range(2, result // 2) ) else 'Простое'
        return prime_or_not, result  # Вместо печати интереснее возвратить результат исследования числа на простое/составное
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

prim, result = sum_three(2, 3, 6)
print(prim + '\n', result)