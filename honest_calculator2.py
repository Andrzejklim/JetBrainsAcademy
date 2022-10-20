msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
list_operators = ['+', '-', '*', '/']

while True:
    try:
        print(msg_0)
        calc = input().split()
        x = float(calc[0])
        oper = (calc[1])
        y = float(calc[2])

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

    except ValueError:
        print(msg_1)
    else:
        print(result)

