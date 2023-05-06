# Write code for algorithm 2 below
# 2. Write a function that prints the natural numbers from 1 to n.

def NaturalN(x, i=1):
   
    if i > x:
        return 0
    else:
        print(i)
        NaturalN(x, i+1)
    
print(NaturalN(5))