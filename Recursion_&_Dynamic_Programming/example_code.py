#The Fibonacci Sequence
#computing the nth finonacci number
#
def fibonacci_regularrecursive(i):
    if i==0:
        return 0
    if i==1:
        return 1
    return fibonacci_regularrecursive(i-1) + fibonacci_regularrecursive(i-2)


#With memoization
def fibonacci_memoization(i):
    return fibonacci_memoization(i, arr[i+1])
def fibonacci_memoization(i, memo[]):
    if i == 0 or i==1:
        return i
    if (memo[i]==0):
        memo[i] = fibonacci_memoization(i-1, memo) + fibonacci_memoization(i-2, memo)
    return memo[i]
