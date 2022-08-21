def any_lowercase1(s):
    """ This function doesn't check the whole String and therefore returns False if the first letter is not lowercase
    and True if it is """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """ This function incorrectly uses dot notation and checks to see if 'c' is lowercase and not the String passed as
    an argument """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """ This function assigns the result of whether the first letter in the String argument is lowercase or not to the
    local variable 'flag' and then returns this value """
    for c in s:
        flag = c.islower()
        return flag


def any_lowercase4(s):
    """ This function determines whether the local variable 'flag' which is always False or the first letter of the
    String argument is True or False and then returns this value. Therefore, it is only able to check the first letter
    of the String argument """
    flag = False
    for c in s:
        flag = flag or c.islower()
        return flag


def any_lowercase5(s):
    """ Instead of checking if any of the letters in the String passed are lowercase the function returns False is any
    are not. Therefore, this function simply checks if all letters in the String are lowercase """
    for c in s:
        if not c.islower():
            return False
    return True
