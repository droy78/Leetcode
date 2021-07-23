class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        #f(n,d) = Number of distinct n-digit numbers which end at digit d
        
        #We create a table array with 0..n rows with 10 columns each. The cell (i,j) will hold
        #the no. of ways of dialing a number of i digits whose last number is j. 
        table = [ [0 for _ in range(10)] for _ in range(n+1)]
        
        #Obviously, there is no way for the knight to dial a number of 0 digits whose last number ends 
        #in 0..n. That's way all cells in row0 have a value 0.
        #We initialized the table with all cells to value 0. So let those values remain 0 for row0
        
        #Any cell in row1 e.g. (1, j) stores number of ways of dialing a 1 digit number whose last digit is j.
        #For example (1, 4) cell will contain number of ways of dialing a 1 digit number whose last digit is
        #4. The assumption is that the knight is sitting outside the dial in the beginning. So the only way
        #for the knight to dial a 4 is jumping straignt on the 4 button => 1 way. That's way all cells in row1 
        #have a value 1.
        for digit in range(10):
            table[1][digit] = 1        
        
        
        #Any cell in row2 e.g. (2, j) stores no. of ways of dialing a 2-digit number that ends whose last number ends in j. 
        #For example, cell (2, 4) will store the number of ways of dialing a 2 digit number that ends in 4. 
        #This can be done in 3 ways : 
        #WAY1 : The knight's first jump is from outside to number 0 and then it jumps to number 4. So it dials 04
        #WAY2 : The knight's first jump is from outside to number 3 and then it jumps to number 4. So it dials 34
        #WAY3 : The knight's first jump is from outside to number 9 and then it jumps to number 4. So it dials 94
        
        #We start iterating over the numbers starting from 2 till n.
        #Each lazy manager in this case, would focus on a single row and fill up all the cells for that row.         
        for i in range(2, n+1):
            
            #The knight can reach 0 only from 4 and 6. So the total ways of reaching 0 and dialing a number of i digits
            # = total no. of ways of reaching 4 by dialing a number of i-1 digits + total no. of ways of reaching 6 by dialing
            # a number of i-1 digits
            table[i][0] = table[i-1][4] + table[i-1][6]
            
            
            table[i][1] = table[i-1][8] + table[i-1][6]
            table[i][2] = table[i-1][7] + table[i-1][9]
            table[i][3] = table[i-1][4] + table[i-1][8]
            
            #The knight can reach 4 only from 3, 9 and 0. So the total ways of reaching 4 and dialing a number of i digits
            # = total no. of ways of reaching 3 by dialing a number of i-1 digits + total no. of ways of reaching 9 by dialing
            # a number of i-1 digits + total no. of ways of reaching 0 by dialing a number of i-1 digits
            table[i][4] = table[i-1][3] + table[i-1][9] + table[i-1][0]
            
            #The knight cannot reach 5 from any other numbers on the dial
            table[i][5] = 0
            table[i][6] = table[i-1][0] + table[i-1][7] + table[i-1][1]
            table[i][7] = table[i-1][2] + table[i-1][6]
            table[i][8] = table[i-1][1] + table[i-1][3]
            table[i][9] = table[i-1][4] + table[i-1][2]
        
        #The answer will reside in the last row and will be the sum of all the cells in the last row
        return sum(table[-1]) % (10**9 + 7)
