def lucasnum(n):
    if n==0:
        return 2
    if n== 1:
        return 1
    dp= [0]*(n+1)
    dp[0],dp[1] = 2,1

    for i in range(2,n+1):
        dp[i]= dp[i-1]+ dp[i-2]
    return dp[n]

res=[ lucasnum(i) for i in range(4)]
print(res)
