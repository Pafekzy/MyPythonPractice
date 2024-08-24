def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

n = int(input("Enter the upper limit to find primes: "))
print("Prime numbers up to", n, ":", sieve_of_eratosthenes(n))

#Sieve of Eratosthenes for Prime Numbers