class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem={}
        def dfs(amount):
            if amount==0:
                return 0
            if amount in mem:
                return mem[amount]
            ans=float('inf')
            for coin in coins:
                if coin<=amount:
                    ans=min(ans,1+dfs(amount-coin))
            mem[amount]=ans
            return ans
        res=dfs(amount)
        return -1 if res == float('inf') else res

        