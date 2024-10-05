
def fibonacci(n):
    if n <= 2:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


sumfib = 0
for i in range(100):
    #print(fibonacci(i+1))
    fib = fibonacci(i+1)
    if fib%2 == 0 and fib < 4000000:
        #print(fib)
        sumfib += fib
    else:
        if fib >= 4000000:
            break

print(sumfib)