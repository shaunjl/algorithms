# Bottom Up
# Dynamic Programming (tabluation) implementation of Coin Change problem 
def count(denominations, n): 

    # table[i] will be storing the number of solutions for 
    # value i. We need n+1 rows as the table is constructed 
    # in bottom up manner using the base case (n = 0) 
    # Initialize all table values as 0 
    table = [0 for k in range(n+1)] 

    # Base case (If given value is 0) 
    table[0] = 1

    # Pick all coins one by one and update the table[] values 
    # after the index greater than or equal to the value of the 
    # picked coin 
    for denomination in denominations: 
        print(denomination)
        for j in range(denomination,n+1): 
            table[j] += table[j-denomination] 
        print(table)

    return table[n]

# Driver program to test above function 
denoms = [1, 5, 10, 25] 
n = 49
x = count(denoms, n) 
print (x) 
