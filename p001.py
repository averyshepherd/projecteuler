# Avery Shepherd
# Project Euler problem 1
# 07/20/2020

# Find the sum of all the multiples of 3 or 5 below 1000


def sum_multiples():
    total = 0
    for i in range(1000):
        if i % 5 == 0 or i % 3 == 0:
            total += i

    return total

def main():
    print(sum_multiples())

if __name__ == '__main__':
    main()
