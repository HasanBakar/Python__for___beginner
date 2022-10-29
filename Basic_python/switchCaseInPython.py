def getInput():
    f_num = int(input("Enter first number: "))
    s_num = int(input("Enter second number: "))
    return f_num,s_num

def add():
    x, y = getInput()
    return x + y

def sub():
    x, y = getInput()
    return x - y

def div():
    x, y = getInput()
    return x // y

def mul():
    x, y = getInput()
    return x * y

print('''
    1. Add
    2. Sub
    3. Div
    4. Mul
''')

choice = int(input("Enter your choice: "))

operations = [add, sub, div, mul]

output = operations[choice - 1]()

print(output)