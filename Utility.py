import random as rand

def generate_random_numbers(count):
    """
    Generate a list of random numbers within a specified range.

    Parameters:
    - start (int): The starting value of the range.
    - end (int): The ending value of the range.
    - count (int): The number of random numbers to generate.

    Returns:
    - list: A list of random numbers.
    """
    return [rand.randint(0, 10000) for _ in range(count)]

# the input count must be equivalent to k-1 for Shamir
n = 3
numlist = generate_random_numbers(n)