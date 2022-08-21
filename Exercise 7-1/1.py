import math


def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x


def test_square_root():
    i = 1
    print('a' + ' ' * 2, 'mysqrt(a)' + ' ' * 11, 'math.sqrt(a)' + ' ' * 8, 'diff')
    print('-' + ' ' * 2, '---------' + ' ' * 11, '------------' + ' ' * 8, '----')
    while i < 10:
        print(str(i) + ' ' * 2, str(mysqrt(i)) + ' ' * (20 - len(str(mysqrt(i)))), str(math.sqrt(i)) + ' ' *
              (20 - len(str(math.sqrt(i)))), mysqrt(i) - math.sqrt(i))
        i = i + 1


test_square_root()
