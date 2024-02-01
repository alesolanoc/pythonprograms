def generate_prime_numbers(limit):
    """
    Generate prime numbers up to the given limit using the Sieve of Eratosthenes algorithm.

    Args:
    limit (int): The upper limit for generating prime numbers.

    Returns:
    list: A list of prime numbers up to the given limit.
    """
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    for num in range(int(limit ** 0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)
    return primes

# Example usage
limit = 50
print(generate_prime_numbers(limit))
