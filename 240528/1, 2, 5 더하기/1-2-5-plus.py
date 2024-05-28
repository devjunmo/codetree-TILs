"""
1은 1
2는 1+1, 2    2
3은 1+1+1,2+1,1+2     3
4는 1 1 1 1, 2 1 1,2 2   5
5는 9
"""

n=int(input())
dp=[1]*10000
dp[1]=1
dp[2]=2
dp[3]=3
dp[4]=5

for i in range(5,n+1):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-5]
    dp[i]=dp[i]%10007

print(dp[n])