# Avery Shepherd
# Project Euler problem 2
# 07/20/2020

# By considering the terms in the Fibonacci sequence whose values do
# not exceed four million, find the sum of the even-valued terms.

def fib_generator(limit):
    fst, scnd = 0, 1
    while fst < limit:
        yield fst
        fst, scnd = scnd, fst + scnd

def sum_even_fib(limit):
    return sum([i for i in fib_generator(limit) if i % 2 == 0])


def main():
    print(sum_even_fib(4000000))

if __name__ == '__main__':
    main()
