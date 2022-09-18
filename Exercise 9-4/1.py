def uses_only(word, string_of_letters):
    i = 0
    correct = 0
    while i < len(word):
        for letter in word:
            for character in string_of_letters:
                if letter == character:
                    correct = correct + 1
                    if correct == len(word):
                        return True
                else:
                    i = i + 1
    return False


user_word = input('What is your word? \n')
user_string_of_letters = input('What is your list of letters? \n')
if uses_only(user_word, user_string_of_letters):
    print('This word contains only letters in the list')
else:
    print('This word contains other letters')
