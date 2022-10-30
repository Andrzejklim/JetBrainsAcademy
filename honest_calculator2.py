msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
list_operators = ['+', '-', '*', '/']
memory = ""
while True:
    try:
        bool_leave = False  # to leave double loop
        print(msg_0)
        calc = input().split()

        if calc[0] == "M" and memory:
            x = memory
            y = float(calc[2])
        elif calc[2] == "M" and memory:
            y = memory
            x = float(calc[0])
        elif calc[2] == "M" and not memory:
            memory = 0
            x = float(calc[0])
            y = memory
        else:
            x = float(calc[0])
            y = float(calc[2])

        oper = (calc[1])

        if oper in list_operators:
            if oper == "+":
                result = y + x
            elif oper == "-":
                result = x - y
            elif oper == "*":
                result = x * y
            elif oper == "/" and y != 0:
                result = x / y
            else:
                print(msg_3)
                continue
        else:
            print(msg_2)
            continue

        print(result)

        while True:

            if bool_leave:
                break

            print(msg_4)
            answer = input()

            if answer == 'y':
                memory = result

                while True:
                    print(msg_5)
                    answer2 = input()

                    if answer2 == "y":
                        bool_leave = True
                        break
                    elif answer2 == "n":
                        quit()
                    else:
                        continue

            elif answer == "n":
                while True:
                    print(msg_5)
                    answer2 = input()

                    if answer2 == "y":
                        bool_leave = True
                        break
                    elif answer2 == "n":
                        quit()
                    else:
                        continue
            else:
                break

    except ValueError:
        print(msg_1)


