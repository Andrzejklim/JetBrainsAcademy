import random
tuple_of_words = ('python', 'java', 'swift', 'javascript')
_random = random.randint(0, len(tuple_of_words) - 1)
word = tuple_of_words[_random]


def main():
    print('H A N G M A N')
    guess = input('Guess the word: ')

    if guess == word:
        print('You survived!')
    else:
        print('You lost!')


if __name__ == "__main__":
    main()