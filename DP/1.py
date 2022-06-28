# 0-1 KNAPSACK
t = [[-1 for i in range(0,101)] for j in  range(0,1001) ]

def knapSack(wt,val,W,n):
    if(n==0 or W==0):
        return 0
    if(t[n][W] != -1):
        return t[n][W]
    if(wt[n-1]<= W):
        t[n][W] = max(val[n-1] + knapSack(wt,val,W - wt[n-1],n-1), knapSack(wt,val,W,n-1))
        return t[n][W]
    elif(wt[n-1] > W):
        t[n][W] = knapSack(wt,val,W,n-1)
        return [n][W]
    
    
print(knapSack([1,1,1],[10,20,30],2,3))

# input weights , input values , total weight , n = size of array 
# O(2 ** n)
# to optimize we will use DP and memoize it 
