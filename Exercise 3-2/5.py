def do_four(f, v):
    f(v)
    f(v)


def do_twice(f, v):
    f(v)
    f(v)


def print_twice(bruce):
    print(bruce)
    print(bruce)


do_four(print_twice, 'spam')
