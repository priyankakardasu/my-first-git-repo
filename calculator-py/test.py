import calc as c
from sys import exit
import random


def generate():
    global a, b
    a = random.randint(0, 1000)
    b = random.randint(0, 1000)


generate()
c.set_math_sign(0)
c.a = a
c.b = b
print('\n\n' + str(a) + '+' + str(b) + '=' + str(c.calculate()))
if str(float(a + b)) == str(c.calculate()):
    print('Add successful\n')
else:
    print('\n\nBuild unsuccessful\n' + str(float(a + b)))
    exit(1)

generate()
c.set_math_sign(1)
c.a = a
c.b = b
print(str(a) + '-' + str(b) + '=' + c.calculate())
if str(float(a - b)) == str(c.calculate()):
    print('Remove successful\n')
else:
    print('\n\nBuild unsuccessful')
    exit(1)

generate()
c.set_math_sign(2)
c.a = a
c.b = b
print(str(a) + '*' + str(b) + '=' + c.calculate())
if str(float(a * b)) == str(c.calculate()):
    print('Myltiply successful\n')
else:
    print('\n\nBuild unsuccessful')
    exit(1)

generate()
c.set_math_sign(0)
c.a = a
c.b = b
print(str(a) + '/' + str(b) + '=' + c.calculate())
if str(float(a + b)) == str(c.calculate()):
    print('Division successful\n')
else:
    print('\n\nBuild unsuccessful')
    exit(1)



print('\n\nBuild successful')
exit(0)
