"""
General Context:
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.
"""



"""
Problem 1

Return the total number of ways you can get to that amount of money
"""
# Bottom Up
# Dynamic Programming (tabluation) implementation
def count_total_ways(denominations: list[int], n: int) -> int:
    """
    params:
     - denominations: a list of denomination amounts
     - n: amount to reach

    """

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
        for j in range(denomination,n+1):
            table[j] += table[j-denomination]

    return table[n]

# Driver program to test above function
denoms = [1, 5, 10, 25]
n = 49
x = count_total_ways(denoms, n)
print(f'total_possible_ways for n={n}:', x)


"""
Problem 2

Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.
"""


# Bottom Up
# Dynamic Programming (tabluation) implementation
def fewest_coins(denominations: list[int], n: int) -> int:
    """
    find the fewest number of coins necessary to get to n

    params:
     - denominations: a list of denomination amounts
     - n: amount to reach

    """

    # table[i] will be storing the number of solutions for
    # value i. We need n+1 values as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize the first value as 0 because you need 0 coins to get to 0
    # Initialize all other values as None to indicate we have not gotten to that value, before
    table = [0] + [float('inf') for k in range(n)]

    # the minimum amount of coins it takes to get to i is the minimum of the ways to get to i-denomination + 1
    for amount_to_reach in range(1, len(table)):
        for denomination in denominations:
            if denomination <= amount_to_reach: # optimization: if the denomination is higher than i, it can't possibly be used to get to this number
                table[amount_to_reach] = min(table[amount_to_reach], table[amount_to_reach - denomination] + 1)

    if table[n] == float('inf'):
        return -1
    return table[n]

# Driver program to test above function 
denoms = [1, 5, 10, 25]
n = 49
x = fewest_coins(denoms, n)
print(f'fewest_coins for n={n}:', x)
