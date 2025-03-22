import time

#everything has it`s own comments

def action_1():
    number1 = float(input("Первое число: ")) # number selection
    number2 = float(input("Второе число: ")) # number selection
    result = number1 + number2
    print(result)

def action_2():
    number1 = float(input("Первое число: ")) # number selection
    number2 = float(input("Второе число: ")) # number selection
    result = number1 - number2
    print(result)

def action_3():
    number1 = float(input("Первое число: ")) # number selection
    number2 = float(input("Второе число: ")) # number selection
    result = number1 * number2
    print(result)

def action_4():
    number1 = float(input("Первое число: ")) # number selection
    number2 = float(input("Второе число: ")) # number selection
    if number2 != 0:
        result = number1 / number2
        print(result)
    else:
        print("Нельзя делить на 0!")

def action_5():
    time.sleep(2)
    print("Terminating process...")
    time.sleep(1)
    print("Logging out...")
    time.sleep(0.5)
    print("Please, wait...")
    time.sleep(5)
    print("Shutting down...")
    time.sleep(6)
    exit()
