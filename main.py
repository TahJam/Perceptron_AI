from perceptron import *


if __name__ == '__main__':
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
