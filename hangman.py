word = 'python'


def main():
    print('H A N G M A N')
    guess = input('Guess the word: ')

    if guess == word:
        print('You survived!')
    else:
        print('You lost!')


if __name__ == "__main__":
    main()