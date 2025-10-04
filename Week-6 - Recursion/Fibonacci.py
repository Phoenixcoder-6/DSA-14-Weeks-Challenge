
# Iterative approach
'''
def fibonacci(n):
    first=0
    second= 1
    res= [first,second]
    for i in range(n-2):
        third= second + first
        res.append(third)
        first,second= second,third
    return res
'''

# Recursive approach
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = 5
res = [fibonacci(i) for i in range(n)]
print(res)   

