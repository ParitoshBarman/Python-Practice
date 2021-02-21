def factorial_iter(n):
    prodect = 1
    for i in range(n):
        prodect = prodect * (i+1)
    return prodect

print(factorial_iter(5))


def factorial_recurcive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recurcive(n-1)

print(factorial_recurcive(5))