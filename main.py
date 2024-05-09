import re


previous = 0
run = True


def perform_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation.lower() in ['quit', 'exit']:
        run = False
    elif equation.lower() in ['c', 'clear']:
        previous = 0
    else:
        equation = re.sub('[a-zA-Z,.:() ]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


print("Basic Python Calculator")
print("Type 'C' to clear or 'quit' to exit\n")

while run:
    perform_math()
