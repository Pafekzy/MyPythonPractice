def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

number = int(input("Enter a number: "))
print("Divisors:", divisors(number))
