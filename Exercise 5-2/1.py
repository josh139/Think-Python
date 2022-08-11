def check_format(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work")


check_format(3987, 4365, 4472, 12)
