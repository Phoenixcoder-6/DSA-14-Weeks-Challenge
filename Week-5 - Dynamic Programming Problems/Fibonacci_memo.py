def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    
    memo[n]= fibonacci(n-1,memo)+ fibonacci(n-2,memo)

    return memo[n]
num=5
for i in range(num):
    res= fibonacci(i)
    print(res)

