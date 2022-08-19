def is_power(a, b):
    if a % b == 0:
        if a == b:
            return True
        else:
            return is_power(a / b, b)
    return False


print(is_power(3, 3))
