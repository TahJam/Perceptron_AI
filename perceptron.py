"""
A program that will implement a perceptron.

Written by Taher Jamali
"""
from typing import List
from copy import deepcopy

"""
The main function that will be called to implement the perceptron. After 

@:param threshold: a float value representing the threshold of the perceptron
@:param adjust: a float value representing the adjustment factor of the weights 
@:param weights: a list of of float values that are the weights of the inputs
@:param train: a list of of examples to train the perceptron
@:param passes: an integer value that represents how many passes the perceptron model should go through 

@:return:
    A Python dictionary that contains the initial weights and the results of the passes.
"""


def perceptron(threshold: float, adjust: float, weights: List[float], train: List,
               passes: int) -> dict:
    # create the dictionary to return
    out = dict()
    init = {'weights': deepcopy(weights), 'threshold': threshold, 'adjustment': adjust}
    out['init'] = init

    # counter to go through the passes
    for i in range(1, passes + 1):
        # create a list that will be the value of the current pass
        curr_pass = [None for _ in range(len(train))]
        # go through the examples
        for j, ex in enumerate(train):
            inputs = ex[1]
            total = 0
            # multiply the weights with the inputs
            for weight, input in zip(weights, inputs):
                total += (weight * input)
            pred = True if total > threshold else False
            if pred != ex[0]:
                # change the weights based on adjustment
                newWeights(weights, inputs, adjust, ex[0])
            # create the dictionary
            add = {'inputs': inputs, 'prediction': pred, 'answer': ex[0], 'adjusted_weights': deepcopy(weights)}
            curr_pass[j] = add
        # add the list to the dict
        out[i] = curr_pass

    return out


"""
This function will take old weights and change them to the adjusted weights based on whether the answer is False or 
True

@:param weights: A list of float values that represent the old weights
@:param inputs: A list of integer values that represent the inputs
@:param adjust: A float value that will be the adjustment value
@:param answer: A boolean value that represents the correct value (to increase if True or decrease if False)

@:return:
    None, replaces the weights in-place
"""


def newWeights(weights: List[float], inputs: List[int], adjust: float, answer: bool) -> None:
    # if answer == True, increase all the weights with input == 1
    if answer:
        for i in range(len(weights)):
            if inputs[i] == 1:
                weights[i] += adjust
    else:  # answer == False, decrease all the weights with input == 1
        for i in range(len(weights)):
            if inputs[i] == 1:
                weights[i] -= adjust


"""
Function to print the output of the perception function
Used for debugging purposes
"""


def printOutput(result: dict, passes: int):
    print(f'init=\t{result["init"]}\n')
    for i in range(1, passes + 1):
        print(f'{i}:')
        curr = result[i]
        for dic in curr:
            print(f'\t{dic}')

