# Avery Shepherd
# Project Euler problem 4
# 07/21/2020

# Find the largest palindrome made from the product of two 3-digit numbers.

def largest_pal():
    largest = -1
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            product_str = str(product)
            if product_str == product_str[::-1]:
                if largest < product:
                    largest = product
    return largest

def main():
    print(largest_pal())

if __name__ == '__main__':
    main()
