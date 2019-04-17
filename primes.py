import datetime

def primes_naive(n):
    nums = []
    now = datetime.datetime.now()
    for p in range(2, n+1):
        for i in range(2, p):
            if p % i == 0:  # p is a factor of something lower than it
                break
        else:
            nums.append(p)
    later = datetime.datetime.now()
    delta = later - now
    print('primes naive took {} seconds'.format(delta.total_seconds()))
    return nums

# the naive implementation is actually slightly faster for large numbers
def primes(n):
    nums = []
    now = datetime.datetime.now()
    if n >= 2:
        nums.append(2)
    for p in range(3, n+1, 2):
        for i in range(2, p):
            if p % i == 0:  # p is a factor of something lower than it
                break
        else:
            nums.append(p)
    later = datetime.datetime.now()
    delta = later - now
    print('primes took {} seconds'.format(delta.total_seconds()))
    return nums

# using the sieve of eratosthenes
def sieve_primes(n):
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    pass


def nth_prime(n):
    curr_prime = 2
    curr_prime_idx = 1
    maybe_prime = 3
    while curr_prime_idx < n:
        for i in range(3, maybe_prime, 2):
            if maybe_prime % i == 0:  # maybe_prime is a factor of something lower than it
                break
        else:  # not a factor of anything below so it is a prime
            curr_prime = maybe_prime
            curr_prime_idx += 1
        maybe_prime += 2
    return curr_prime
