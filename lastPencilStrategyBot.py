import random
bot_win_strategy = False
names = ['John', 'Jack']
numbers = [1, 2, 3]

while True:
    number_of_pencils = input("How many pencils would you like to use: ")
    limit = number_of_pencils

    if number_of_pencils.isdigit():
        number_of_pencils = int(number_of_pencils)
        if number_of_pencils == 0:
            print('The number of pencils should be positive')
            continue
    else:
        print('The number of pencils should be numeric')
        continue

    print("Who will be the first (John, Jack): ")

    while True:
        name = input()
        if name not in names:
            print("Choose between 'John' and 'Jack'")
            continue
        else:
            _index = names.index(name)
            print("|" * number_of_pencils)
            break

    while True:
        print(f"{names[_index]}'s turn: ")

        if names[_index] == names[1]:
            if number_of_pencils == int(limit):
                number = 1

            if number_of_pencils % 4 == 0:
                number = 3
            elif number_of_pencils % 2 == 0:
                number = 1
            elif number_of_pencils % 2 == 1 and number_of_pencils != 1:
                number = 2
            else:
                if number_of_pencils == 1:
                    number = random.randint(1, 1)
                else:
                    number = random.randint(1, 3)
            if number_of_pencils - number < 0:
                print('Too many pencils were taken')
                continue
        else:
            number = input()

            if number.isdigit():
                number = int(number)
                if number != numbers[0] and number != numbers[1] and number != numbers[2]:
                    print("Possible values: '1', '2' or '3'")
                    continue
                if number_of_pencils - number < 0:
                    print('Too many pencils were taken')
                    continue
            else:
                print("Possible values: '1', '2' or '3'")
                continue

        number_of_pencils -= number
        if names[_index] == names[1]:
            print(number)
        print('|' * number_of_pencils)
        _index = (_index + 1) % len(names)

        if number_of_pencils <= 0:
            print(f'{names[_index]} won!')
            quit()