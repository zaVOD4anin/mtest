def hello():
    print('hello world')


def metro_init(flag):
    if num < 10:
        return 'Выезжаем'
    else:
        return 'Остаемся'


source = ['C:\\Code', 'aboba']
print(type(' '.join(source)))
hello()
num1 = num2 = [5, 4, 3, 2, 7]
print(num1 + num2, 'абоба')
print(f'{num1 + num2} aboba')
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, num1))))
num = 5
print(str(lambda b: (lambda a, b: a(a, b))(lambda a, b: b * a(a, b - 1) if b > 0 else 1, b)(num)))
assert metro_init(3) == 'Выезжаем'
assert metro_init(11) == 'Остаемся'
