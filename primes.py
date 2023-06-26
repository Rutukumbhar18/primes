def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Test the function
n = int(input("Enter a number: "))
prime_numbers = generate_primes(n)
print("Prime numbers up to", n, "are:")
print(prime_numbers)
