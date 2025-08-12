#This is a problem originally meant as greedy but now is not solvable using that, and we must use recursion or dp to solve this
class Solution:
    def MinimumCoins(self, coins, amount):
        coins.sort()
        n = len(coins)
        cnt = 0
        for i in range(n-1,-1,-1):
            if coins[i]<=amount:
                amount = amount - coins[i]
                cnt+=1
                while coins[i]<=amount: #keep checking if amount is still greater than the current coin we are on
                    amount = amount - coins[i]
                    cnt+=1
            else:
                continue
        if amount == 0:#if amount is zero then it is possible
            return cnt
        return -1
        #TC : O(N log N)
        #SDC : O(1)

    