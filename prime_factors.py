import math

def prime_factors(n):
     
    # Print the number of two's that divide n. - takes care of even numbers
    while n % 2 == 0:
        print(2)
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    # the condition to stop at int(math.sqrt(n))+1 is okay because 
    # every composite number has at least one prime factor less than or equal to square root of itself.
    for i in range(3,int(math.sqrt(n))+1,2):
        # while i divides n , print i and divide n
        # The condition below is sufficient because the factors of composite odd numbers are smaller odd numbers.
        # So if any number i is a composite, it's factors will already have been handled and this condition won't 
        # yeild true.
        while n % i == 0:
            print(int(i))
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(int(n))

n = int(input("Factors of what number? "))
prime_factors(n)