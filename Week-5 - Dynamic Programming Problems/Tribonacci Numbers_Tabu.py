def tribo(n):
    if n == 0:
        return 0
    if n==1 or n==2:
        return 1
    
    dp = [0] * (n+1)
    dp[0], dp[1],dp[2] =0, 1, 1

    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

res= [ tribo(i) for i in range(8)]
print(res)
