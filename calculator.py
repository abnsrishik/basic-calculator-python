def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print('Simple Calculator')
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
op = input('Enter Operation (+,-,*,/): ')
if op=='+':
    print('Result: ', add(a,b))
elif op == '-':
    print('Result: ', sub(a,b))
elif op == '*':
    print('Result: ', mul(a,b))
elif op == '/':
    if b!=0:
        print('Result: ', div(a,b))
    else:
        print('Invalid operation')
else:
    print('Invalid operation')
