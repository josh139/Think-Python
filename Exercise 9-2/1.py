import os

path = os.getcwd()
parent_directory = (os.path.abspath(os.path.join(path, os.pardir)))
file = '\\words.txt'
path = parent_directory + file
fin = open(path)


def has_no_e(test):
    x = len(test)
    i = 0
    while x != i:
        if test[i] == 'e':
            return False
        else:
            i = i + 1
    return True


all_word_amount = 0
has_no_e_amount = 0

for line in fin:
    all_word_amount = all_word_amount + 1
    word = line.strip()

    if has_no_e(word):
        print(word)
        has_no_e_amount = has_no_e_amount + 1

has_e_percent = has_no_e_amount / all_word_amount * 100
has_no_e_percent = 100 - has_e_percent

print('\n')
print(f"{has_no_e_percent:.2f}% of words contain an 'e'")
