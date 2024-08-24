def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
primes = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", primes)


#Filter Prime Numbers with Lambda