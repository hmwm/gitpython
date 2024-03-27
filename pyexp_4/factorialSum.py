def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)


def factorial_sum(n):
    return sum(factorial_recursive(i) for i in range(1, n+1))


print("1！+ 2！+ 3！+ 4！+ 5！=",factorial_sum(5))

