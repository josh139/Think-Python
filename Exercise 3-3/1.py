def do_four(f, v):
    f(v)
    f(v)
    f(v)
    f(v)


def draw_grid():
    row = '+ - - - - + - - - - +'
    column = '|         |         |'

    do_one(row)
    do_four(do_one, column)
    do_one(row)
    do_four(do_one, column)
    do_one(row)


def do_one(v):
    print(v)


draw_grid()
