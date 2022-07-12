# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from perceptron import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    weights = [-0.5, 0, 0.5, 0, -0.5]
    examples = [
        [True, [1, 1, 1, 1, 0]],
        [False, [1, 1, 1, 1, 1]],
        [False, [0, 0, 0, 0, 0]],
        [False, [0, 0, 1, 1, 0]],
        [False, [1, 0, 1, 0, 1]],
        [False, [1, 0, 1, 0, 0]],
        [False, [0, 1, 0, 1, 1]],
        [False, [0, 1, 0, 1, 0]],
        [False, [0, 0, 1, 0, 0]],
        [False, [0, 0, 0, 1, 0]],
    ]

    result = perceptron(0.5, 0.1, weights, examples, 4)
    printOutput(result, 4)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
