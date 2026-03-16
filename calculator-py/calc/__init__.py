math_sign = None
num_num = 0
a, b = 0, 0


def add(a, b):
    return float(a) + float(b)


def remove(a, b):
    return float(a) - float(b)


def multiplication(a, b):
    return float(a) * float(b)


def division(a, b):
    return float(a) / float(b)


def set_math_sign(sign_num):  # 0 - `+`; 1 - `-`, 2 - `*`, 3 - `/`
    global math_sign, num_num
    math_sign = sign_num
    if num_num == 0:
        num_num = 1
    else:
        num_num = 0


def add_to_num(num):
    global a, b, num_num
    if num_num == 0:
        a = float(str(int(a)) + str(int(num)))
    else:
        b = float(str(int(b)) + str(int(num)))


def get_num():
    global a, b, num_num
    if num_num == 0:
        return a
    else:
        return b


def get_sign():
    if math_sign == 0:
        result = '+'
    elif math_sign == 1:
        result = '-'
    elif math_sign == 2:
        result = '*'
    elif math_sign == 3:
        result = '/'
    return result


def calculate():
    global math_sign, result, a, b
    result = "Set math sign!"
    if math_sign == 0:
        result = str(add(a, b))
    elif math_sign == 1:
        result = str(remove(a, b))
    elif math_sign == 2:
        result = str(multiplication(a, b))
    elif math_sign == 3:
        result = str(division(a, b))
    return result


def c():
    global math_sign, result, a, b
    math_sign = None
    num_num = 0
    a, b = 0, 0
