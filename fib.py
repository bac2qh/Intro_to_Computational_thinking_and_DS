def fib(n):
    if n == 0 or n == 1: 
        return 1 
    else: 
        return fib(n - 1) + fib(n - 2)

def fibMemo(n, memo={}):
    if n in memo: 
        return memo[n]
    elif n == 0 or n == 1: 
        memo[n] = 1
    else:
        memo[n] = fibMemo(n-1) + fibMemo(n-2)
    return memo[n]

print(fibMemo(40))
