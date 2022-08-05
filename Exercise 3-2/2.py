def do_twice(f, v):
    f(v)
    f(v)


def print_spam(a):
    print(a)


do_twice(print_spam, 'spam')
