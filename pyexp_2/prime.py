from math import sqrt
import time


def count_time(func):
    def wrapper(*args, **kwargs):
        stat_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - stat_time} second.")
        return result

    return wrapper


@count_time
def is_prime(n):
    count = 0
    prime_sum = 0
    for i in range(2, n):
        Is_Prime = True
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                Is_Prime = False
                break

        if Is_Prime:
            count += 1
            prime_sum += i

    return count, prime_sum


@count_time
def is_prime_slow(n):
    count = 0
    prime_sum = 0
    for i in range(2, n):
        Is_Prime = True
        for j in range(2, i):
            if i % j == 0:
                Is_Prime = False
                break

        if Is_Prime:
            count += 1
            prime_sum += i

    return count, prime_sum


print(is_prime(1000))
print(is_prime_slow(1000))
