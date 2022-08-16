def recurse(n, s):
    """ This method takes two arguments n=int and s=int. The base case is when n is 0. Else one is taken away from n
    and s now equals the old value of n plus five"""
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+5)


recurse(8, 0)
