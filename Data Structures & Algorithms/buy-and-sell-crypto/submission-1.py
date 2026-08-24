class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        res=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                res=max(res,profit)
            else:
                l=r
            r+=1
        return res
        '''
        maxP=0
        minBuy=prices[0]
        
        for sell in prices:
            maxP=max(maxP,sell-minBuy)
            minBuy=min(minBuy,sell)
        return maxP
        '''
        
        

        