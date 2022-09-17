import os

path = os.getcwd()
parent_directory = (os.path.abspath(os.path.join(path, os.pardir)))
file = '\\words.txt'
path = parent_directory + file
fin = open(path)

for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)
