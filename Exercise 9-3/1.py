def avoids(word, forbidden_letters):
    for character in forbidden_letters:
        for letter in word:
            if character == letter:
                return False
    return True


user_word = input('What is your word? \n')
user_letters = input('What are the forbidden letters? \n')

if avoids(user_word, user_letters):
    print("This word doesn't use any forbidden letters")
else:
    print("This word does use forbidden letters")
