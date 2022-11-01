def option():
    print('''
        1. Add
        2. Sub
        3. Div
        4. Mul
        5. Quit
    ''')
    operations = [add, sub, div, mul,quit]
    choice = int(input("Enter your choice: "))

    output = operations[choice - 1]()
    print(output)
    return

def getInput():
    f_num = int(input("Enter first number: "))
    s_num = int(input("Enter second number: "))
    return f_num,s_num


def add():
    x, y = getInput()
    print(x + y)
    option()


def sub():
    x, y = getInput()
    print(x - y)
    option()


def div():
    x, y = getInput()
    print(x // y)
    option()


def mul():
    x, y = getInput()
    print(x * y)
    option()


def quit():
    exit()

option()
