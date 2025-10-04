def count_ways(coins,target):
    n= len(coins)
    dp = [[0] * (target +1) for _ in range(n+1)]

    #base cases
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,n+1):
        for j in range(target+1):
        #exclude
            dp[i][j] = dp[i-1][j]
        #include
            if j-coins[i-1] >=0:
                dp[i][j] += dp[i][j-coins[i-1]]

    return dp[n][target]


arr=[1,2,5]
tar= 5
res= count_ways(arr,tar)
print(res)

