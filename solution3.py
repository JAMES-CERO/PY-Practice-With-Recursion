# Write code for algorithm 3 below
#Write a function that returns the nth elements in the Fibonacci Sequence.

def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    elif num <= 0:
        return 0
    else:
        return fibonacci(num -1) + fibonacci(num -2)
    
print("2nd fib number:")
print(fibonacci(2))
print("4th fib number:")
print(fibonacci(4))
print("8th fib number:")
print(fibonacci(8))