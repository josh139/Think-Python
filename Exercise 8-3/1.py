def is_palindrome(word):
    if word == word[::-1]:
        return True


result = is_palindrome('radar')
print(result)
