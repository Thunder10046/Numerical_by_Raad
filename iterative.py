## Name : Shah Ahmed Raad ; ID : 20 03 042
## False_Position 

import math

def f(x):
    return ((1+math.cos(x))/3)

def iterative(x1,Max_iter,tol):
    i = 1
    while i <= Max_iter:
        x = f(x1)
        if abs(x - x1) < tol:
            print(x)
            break
        print(f"Iteration {i}: x = {x}")
        i += 1
        x1 = x
        print(f"x = {x}")

    print(f"x = {x} after {i - 1}th iteration ")


iterative(1,100,1e-6)




    







