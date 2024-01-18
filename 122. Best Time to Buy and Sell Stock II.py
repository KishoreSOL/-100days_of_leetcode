class Solution(object):
    def maxProfit(self, prices):
        l=0
        r=1
        total=0
        maxx=0
        while r<len(prices):
            if  prices[r]-prices[l] > maxx:
                maxx = prices[r]-prices[l]
            else:
                total+=maxx
                maxx=0
                l=r
            r+=1
        total+=maxx
        return total
            
            

        