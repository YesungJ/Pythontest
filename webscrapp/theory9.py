'''
plus +
minus -
times *
division /
negation -
power **
remainder %
'''
#create calculation system
'''
def init_int(input_keyboard_num1):
    input_number = int(input_keyboard)


def cal(input_keyboard_num1, input_keyboard_cal, input_keyboard_num2):
    num1 = int(input_keyboard_num1)
    num2 = int(input_keyboard_num2)

    if input_keyboard_cal == "+":
        result = num1 + num2
        return result
    elif input_keyboard_cal == "-":
        result = num1 - num2
        return result
    elif input_keyboard_cal == "*":
        result = num1 * num2
        return result
    elif input_keyboard_cal == "/":
        result = num1 / num2
        return result
    elif input_keyboard_cal == "**":
        result = num1 ** num2
        return result
    elif input_keyboard_cal == "%":
        result = num1 % num2
        return result


input_keyboard_num1 = input("please input number and want calculator:  ")
input_keyboard_cal = input("please input cal:  ")
input_keyboard_num2 = input("please input second number:  ")

print(input_keyboard_num1)
print(input_keyboard_cal)
print(input_keyboard_num2)

result_cal = cal(input_keyboard_num1, input_keyboard_cal, input_keyboard_num2)
'''

def plus(a,b):
    return(int(a) + int(b))

def minus(a,b):
    return(int(a) - int(b))

def times(a,b):
    return(int(a) * int(b))

def division(a,b):
    return(int(a) / int(b))

def negation(a):
    return(-int(a))

def power(a,b):
    return(int(a) ** int(b))

def remainder(a,b):
    return(int(a) % int(b))

print(plus(3,"7"))
print(minus("9",1))
print(times("10",2))
print(division("9","3"))
print(negation("-3"))
print(power("10",2))
print(remainder("9","3"))