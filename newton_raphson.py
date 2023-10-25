## Name : Shah Ahmed Raad ; ID : 20 03 042
## Newton-Raphson Method 

def func(x):
	return (x**3 - 2*x - 5)

def derivFunc(x):
	return (3*x**2 - 2)

def newton_raphson(x,tol):
	d = func(x) / derivFunc(x)
	while abs(d) >= tol:
		d = func(x)/derivFunc(x)
		x = x - d
	
	return x 


x0 = 2 
tol = 1e-6
root_value = newton_raphson(x0,tol) 
print(f"The value of the root is: {root_value:.4f}")
