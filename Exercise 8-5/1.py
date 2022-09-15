def rotate_word(word, rotation):
    new_word = ''
    for letter in word.lower():
        numeric_code = ord(letter)
        # print(numeric_code)

        new_letter_numeric_code = numeric_code + rotation
        # print(new_word_numeric_code)

        if numeric_code == 97:
            new_letter_numeric_code = 122 + rotation + 1
        elif new_letter_numeric_code < 97:
            used_rotation = numeric_code - 97
            wrap = rotation + used_rotation + 1
            new_letter_numeric_code = 122 + wrap
        elif new_letter_numeric_code > 122:
            used_rotation = numeric_code - 122
            wrap = rotation + used_rotation - 1
            new_letter_numeric_code = 97 + wrap
        elif numeric_code == 122:
            new_letter_numeric_code = 97 - rotation - 1

        new_letter = chr(new_letter_numeric_code)
        # print(new_letter)

        new_word = new_word + new_letter

        if len(new_word) == len(word):
            print(new_word)


rotate_word('cheer', 7)
rotate_word('melon', -10)
rotate_word('ibm', -1)
