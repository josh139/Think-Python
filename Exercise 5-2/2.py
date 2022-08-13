def check_format(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work")


number_1 = input('Number 1 = ')
number_2 = input('Number 2 = ')
number_3 = input('Number 3 = ')
power = input('Power = ')

check_format(int(number_1), int(number_2), int(number_3), int(power))
