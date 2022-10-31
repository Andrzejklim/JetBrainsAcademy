msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
list_operators = ['+', '-', '*', '/']
memory = 0.0
con_store_result = True


def read_operation(memory2):

    continue_type = True
    while continue_type:
        print(msg_0)
        x, oper, y = input().split()

        try:
            x, y = variables_value(x, y, memory2, oper)

        except ValueError:
            print(msg_1)
            continue

        if y == 0 and oper == "/":
            print(msg_3)
            continue

        if oper not in list_operators:
            print(msg_2)
            continue
        else:
            continue_type = False

    return x, y, oper


def check_operator(x, y, oper):
    if oper == "+":
        check(x, y, oper)
        result = y + x
    elif oper == "-":
        check(x, y, oper)
        result = x - y
    elif oper == "*":
        check(x, y, oper)
        result = x * y
    elif oper == "/" and y != 0:
        check(x, y, oper)
        result = x / y
    return result


def variables_value(x, y, memory3, oper1):
    if x == "M":
        x = memory3
        y = float(y)
    elif y == "M":
        y = memory3
        x = float(x)
        if y == 0.0 and oper1 == "/":
            check(x, y, "/")
    else:
        x = float(x)
        y = float(y)
    return x, y


def store_result(memory2, result1, con_store_result3):

    while con_store_result3:
        print(msg_4)
        answer = input()

        if answer == "y":  # want to store result
            memory2 = result1
            con_store_result3 = continue_calculations(con_store_result3)

        elif answer == "n":  # don't want to store result
            con_store_result3 = continue_calculations(con_store_result3)
    return memory2


def continue_calculations(con_store_result4):

    while True:
        print(msg_5)
        answer = input()

        if answer == "y":  # to continue
            con_store_result4 = False
            break
        elif answer == "n":  # to leave
            quit()
        else:
            continue
    return con_store_result4


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output

def main(memory1, con_store_result1):

    continue_calc = True
    while continue_calc:
        x, y, oper = read_operation(memory1)
        result = check_operator(x, y, oper)
        print(result)
        memory1 = store_result(memory1, result, con_store_result1)


if __name__ == "__main__":
    main(memory, con_store_result)
