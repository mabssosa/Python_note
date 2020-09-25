# First definition
def factorial(n):
    #base case
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


# Second definition
def factorial2(n):
    # Returns the factorial of n.
    def recurse(n, product):
    # Helper function to compute factorial.
        if n == 1:
            return product
        else:
            return recurse(n - 1, n * product)
    return recurse(n, 1)

print(factorial2(5))


# Third definition
def factorial3(n, product = 1):
    #Returns the factorial of n.
    if n == 1:
        return product
    else:
        return factorial3(n - 1, n * product)

print(factorial3(5))