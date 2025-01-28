from typing import List

def find_prime_factors(number: int) -> List[int]:
    result: List[int] = []
    primes: List[int] = [2]
    for i in range(3, int(number ** 0.5) + 1):
        for prime in primes:
            if i % prime == 0:
                break
        else:
            primes.append(i)
    for prime in primes:
        while number % prime == 0:
            result.append(prime)
            number = number // prime
    if number != 1:
        result.append(number)
    return result

if __name__ == "__main__":
    assert find_prime_factors(630) == [2, 3, 3, 5, 7]
    assert find_prime_factors(13) == [13]
