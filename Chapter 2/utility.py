'''
This file contains utility function
'''
import random


def generate_random_sequence(n: int, start: int, end: int) -> list:
    '''
    Generates a list of n random integers between start and end (inclusive).

    Parameters:
    n (int): The number of random integers to generate.
    start (int): The lower bound for the random integers.
    end (int): The upper bound for the random integers.

    Returns:
    list: A list of n random integers between start and end.
    '''
    return [random.randint(start, end) for _ in range(n)]