# Function to calculate nth Fibonacci number
def fib(n, lookup):
 
    # Base case
    if n == 0 or n == 1 :
        lookup[n] = n
 
    # If the value is not calculated previously then calculate it
    if lookup.get(n) is None:
        lookup[n] = fib(n-1 , lookup)  + fib(n-2 , lookup) 
 
    # return the value corresponding to that value of n
    return lookup[n]
# end of function
 
# Driver program to test the above function
def main():
    n = 348
    # Declaration of lookup table
    # Handles till n = 100 
    lookup = {}
    print("Fibonacci Number is {}".format(fib(n, lookup)))
 
if __name__=="__main__":
    main()