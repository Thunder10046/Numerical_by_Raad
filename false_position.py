## Name : Shah Ahmed Raad ; ID : 20 03 042
## False_Position 


Max_iter = 100

def false_pos(a,b):

    if func(a)*func(b)>=0 : 
        print("You've Entered Wrong Assumption")
        return -1
    
    c = a 

    iter_count = 0

    for i in range(Max_iter):

        c = ((a*func(b)-b*func(a))/(func(b)-func(a)))

        if func(c)==0 :
            return c, iter_count 

        elif (func(c)*func(a))<0 :
            b = c 
            iter_count +=1
        else :
            a = c
            iter_count +=1
    
    return c,iter_count


def func(x) : 
    return (x**3 - 2*x - 5)
 

root, iteration = false_pos(2,3)

print(root,iteration)







    



             
    

