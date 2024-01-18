class Solution(object):
    def maxProfit(self, prices):
        maxx=0
        l=0
        r=1
        while r < len(prices):
            temp=prices[r]-prices[l]
            if prices[l] >= prices[r]:
                l=r
            else:
                maxx=max(maxx,temp)
            r+=1
        return maxx



        