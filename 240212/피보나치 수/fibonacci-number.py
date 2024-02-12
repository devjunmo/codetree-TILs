n = int(input())

fib = [-1] * 100

fib[1] = 1
fib[2] = 1

def dp(n):
    for i in range(3, n+1):
        fib[i] = fib[i-1] + fib[i-2]

dp(n)

print(fib[n])