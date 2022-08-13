def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+5)


recurse(-1, 0)
