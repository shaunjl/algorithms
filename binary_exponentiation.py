"""

https://www.hackerearth.com/practice/notes/mod-integer-exponentiation-useful-in-competetive-programming/

This is a recursive top-down approach where we use the fact that x^n = x^(2*n/2) and to use integers with odd numbers x^n = x * x^(2*(n-1)/2)

  Function exp_by_squaring(x, n)
    if n < 0  then return exp_by_squaring(1 / x, -n);
    else if n = 0  then return  1;
    else if n = 1  then return  x ;
    else if n is even  then return exp_by_squaring(x * x,  n / 2);
    else if n is odd  then return x * exp_by_squaring(x * x, (n - 1) / 2);

"""

def exp_by_squaring(x, n):
	"""
	compute x^n
	"""
	# base cases 
	if n < 0:
		return exp_by_squaring(1/x, -n)
	elif n == 0:
		return 1
	elif n == 1:
		return x
	
	elif n % 2 == 0:
		return exp_by_squaring(x * x,  n / 2)
	else:
		return x * exp_by_squaring(x * x,  (n - 1) / 2)

if __name__ == '__main__':
	print(exp_by_squaring(2,32))
