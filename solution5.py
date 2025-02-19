# Write code for algorithm 5 below
#  Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.

def palindrome_(str):
    if str == str[::-1]:
        return True
    else:
        return False
    
print(palindrome_('madam'))

# OR 

def palindrome2_(str):
    if len(str) == 1 or len(str) == 0:
        return True
    else:
        return (str[0] == str[-1]) and palindrome2_(str[1:-1])

    
print(palindrome2_('madam'))
print("is 'apple' a palindrome?")
print(palindrome2_('apple'))
print("is 'tacocat' a palindrome?")
print(palindrome2_('tacocat'))