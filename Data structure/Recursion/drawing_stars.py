def print_stars(n):
    if n == 1:
        print("*")
    else:
        print("*", end="")
        print_stars(n-1)

print_stars(6)


def ourSum(lower, upper, margin=0):
    # Returns the sum of the numbers from lower through upper.
    blanks = "#" * margin
    print(blanks, lower, upper)
    if lower > upper:
       print(blanks, 0)
       return 0
    else:
       result = lower + ourSum(lower + 1, upper, margin + 4)
       print(blanks, result)
       return result

print(ourSum(1, 3))