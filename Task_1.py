def main(string):
    word_one = string.lower()

    word_two = word_one[::-1]

    if word_one == word_two:
        print('True')
    else:
        print('False')


