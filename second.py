import random

def get_numbers_ticket(min, max, quantity):
    """
    Generates a set of unique random numbers.

    Parameters:
    min (int): The minimum possible number in the set (at least 1).
    max (int): The maximum possible number in the set (at most 1000).
    quantity (int): The number of unique numbers to generate (between min and max).

    Returns:
    list: A sorted list of unique random numbers. 

    Raises:
    ValueError: If the input parameters do not meet the constraints.
    """
     
    if min < 1:
        raise ValueError("Parameter 'min' must be at least 1")
    if max > 1000:
        raise ValueError("Parameter 'max' must be at most 1000")
    if quantity < 1:
        raise ValueError("Parameter 'quantity' must be at least 1")
    if quantity > (max - min + 1):
        raise ValueError("Parameter 'quantity' must not be greater than the range of numbers between 'min' and 'max'")
 
    numbers = random.sample(range(min, max + 1), quantity)

    numbers.sort()

    return numbers


try:
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Your lottery numbers:", lottery_numbers)
except ValueError as e:
    print(e)