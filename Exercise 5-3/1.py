def is_triangle(a, b, c):
    if a + b == c or b + c == a or c + a == b:
        print('Yes')
    else:
        print('No')


stick_1 = input("Stick 1's length is = ")
stick_2 = input("Stick 2's length is = ")
stick_3 = input("Stick 3's length is = ")

is_triangle(int(stick_1), int(stick_2), int(stick_3))
