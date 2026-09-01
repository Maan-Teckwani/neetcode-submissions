class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo=[[-1 for _ in range(amount)] for _ in range(len(coins))]
        def dfs(i,amo):
            if amo==amount:
                return 1
            if amo>amount or i>=len(coins):
                return 0
            if memo[i][amo]!=-1:
                return memo[i][amo]

            take=dfs(i,amo+coins[i])
            skip=dfs(i+1,amo)

            memo[i][amo]=take+skip
            return memo[i][amo]
        return dfs(0,0)
        