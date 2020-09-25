# complexity : O(2^n)
def fibo(n):
    return fibo(n-1) + fibo(n-2) if n >= 2 else n

print(fibo(10))


# complexity : O(n)
def fibo2(n):
    if n < 2:
        return n

    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b

    return b

for n in range(1, 11):
    print(n, fibo2(n))


# Memorization
memo = {1: 1, 2: 1}
def fibo3(n):

    if n in memo:
        return memo[n]
    else:
        output = fibo3(n-1) + fibo3(n-2)
        memo[n] = output
        return output

print(fibo3(10))