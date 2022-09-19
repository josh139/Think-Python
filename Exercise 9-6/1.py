import os

path = os.getcwd()
parent_directory = (os.path.abspath(os.path.join(path, os.pardir)))
file = '\\words.txt'
path = parent_directory + file
fin = open(path)


def is_abecedarian(word):
    old_letter = ''
    for new_letter in word:
        if new_letter < old_letter:
            return False
        old_letter = new_letter
    return True

abecedarian = 0

for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        abecedarian = abecedarian + 1

print(abecedarian)
