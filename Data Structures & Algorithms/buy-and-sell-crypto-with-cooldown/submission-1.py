class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo=[[-1]*2 for _ in range(len(prices))]
        def dfs(i,buying):
            if i>=len(prices):
                return 0
            if memo[i][buying]!=-1:
                return memo[i][buying]
            cooldown=dfs(i+1,buying)
            if buying:
                buy=dfs(i+1,not buying)-prices[i]
                memo[i][buying]=max(cooldown,buy)
                return memo[i][buying]
            else:
                sell=dfs(i+2,not buying)+prices[i]
                memo[i][buying]=max(cooldown,sell)
                return memo[i][buying]
        return dfs(0,True)
            
            
                
            

        
        