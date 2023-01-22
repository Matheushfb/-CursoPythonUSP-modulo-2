import time

def factorial1(number):
    if number <= 1:
        return 1
    else:
        return number*factorial1(number-1)

print(factorial1(900))


def factorial2(number):
    product = 1
    for i in range(number):
        product = product * (i+1)
    return product

print(factorial2(900))