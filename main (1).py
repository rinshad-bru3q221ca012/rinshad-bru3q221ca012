def fact(n):
    if n == 1:
        # base case, when to discontinue recursion
        return 1
    else:
        return n*fact(n-1)
        # recursive call

print(fact(5))
# initial call