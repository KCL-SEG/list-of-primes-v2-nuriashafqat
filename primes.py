"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def primes(number_of_primes):
    list = []
    number = 2

    if(number_of_primes <= 0):
        raise ValueError()
    else:
        while len(list) < number_of_primes:
            if is_prime(number):
                list.append(number)
            number += 1
        return list
