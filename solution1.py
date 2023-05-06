# Write code for algorithm 1 below
# 1. Write a program that takes a positive number as an argument and prints the numbers from n to zero.

def countDown(num):
    if num <= 0:
        return 0
    else:
        print(num)
        return countDown(num-1)

print(countDown(5))