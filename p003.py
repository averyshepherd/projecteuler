# Avery Shepherd
# Project Euler problem 3
# 07/20/2020

# What is the largest prime factor of the number 600851475143 ?

import math
from utilities import is_prime

def get_large(n):
    if is_prime(n):
        return n

    largest = -1
    while n % 2 == 0:
        largest = 2
        n /= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest = i
            n /= i

    if n > 2:
        return n
    return largest


def main():
    print(get_large(600851475143))

if __name__ == '__main__':
    main()
