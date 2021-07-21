class Solution(object):
    #Comparing the problem #70 Climbing Stairs. As a lazy manager I just want to focus on the
    #what are the fewest number of coins that can be used to reach my amount i. In the Climbing 
    #Stairs problem it was given that level i can be reached by taking 2 steps from level i-1 or by
    #taking a single step from i-1. Here we have a list of coin denominations. So an amount i can be
    #reached using a denomincation of c1 from level i-c1, or using a denomination of c2 from level 
    #i-c2 etc. As a lazy manager I need to find out which path from my predecessors lead to the lowest
    #no. of coin denominations to me. 
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #We declare a table array of size amount + 1. All indexes are initialized to infinity. Each 
        #index i would store the fewest no. of coins that make up the amount in that index. For example, 
        #index 5 would contain the fewest no. of coins of the given denominations that can be used to 
        #make $5. The first cell will correspond to $0. This is the reason the table array is amount + 1
        table = [float('inf') for index in range(amount+1)]
        
        #We can always create an amount 0 if we use no coins
        table[0] = 0
        
        #We iterate over the table array starting from index 1
        for i in range(1, amount+1):
            mincoins = float('inf')
            
            #We iterate over the coins array. For every denomination c, we check if the solution to
            #min. no. of coins to generate the amount i-c has been calculated by a predecessor. That
            #value would be present in the location table[i-c]. We compare values in table[i-c] for 
            #all values of c to see which predecessor has the minimum value. To that value, we add
            #a 1 to it as we would be adding the coin with the same denomination to reach our amount
            #For example if i = 11 and denominations are 1, 2 and 5, then we compare the values in 
            #the indexes 11-1, 11-2 and 11-5 to see which has the lowest value. Let's say table[10] = 6,
            #table[9] = 5 and table[6] = 3. That means we can create an amount of $6 using just 3 coins
            #and to create the amount at the current index i.e, $11 , we just need to add another coin
            #of denomination 5 (hence +1)
            for c in coins:
                if i - c >= 0:
                    mincoins = min(mincoins, table[i-c]+1)
            table[i] = mincoins
        
        print(table)
        #We returning the value we check if the value is unchanged from infinity. This would mean no
        #solution exists. If so we return -1
        if table[amount] == float('inf'):
            return -1
        else:
            return table[amount]
