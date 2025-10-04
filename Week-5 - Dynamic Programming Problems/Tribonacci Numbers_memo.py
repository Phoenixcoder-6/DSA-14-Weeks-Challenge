def tribo(n,memo={}):
    if n in memo:
        return memo[n]
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    
    memo[n]= tribo(n-1,memo) + tribo(n-2,memo) + tribo(n-3,memo)
    return memo[n]

res= [tribo(i) for i in range(6)]
print(res)