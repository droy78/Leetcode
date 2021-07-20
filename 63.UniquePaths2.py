class Solution(object):
    #You can reach any cell either from the cell above it and to its left. However, if the cell has
    #a value 1 that is a blocked cell. Similar to problem no. 62-Unique paths, we create another grid
    #called table where each cell will hold the no. of ways of reaching it. If the obstablegrid has a
    #1 in its cell, we add a 0 to the corresponding cell in our table array indicating that no. of ways
    #of reaching that cell is 0
    
    #As a lazy manager, I'll just focus on my own cell and calculate the no. of ways of reaching it.
    #This will be equal to the no. of ways of reaching the cell above me and one to my left. 
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        numrows = len(obstacleGrid)
        numcols = len(obstacleGrid[0])
        
        #We define a table array with the same dimensions as the obstacleGrid
        table = [[0 for j in range(numcols)] for i in range(numrows)]
        
        #First fill in the base cases i,e, the cell (0,0). If the obstacleGrid has a value of 1
        #there, we put a value 0 indicating there is no way of reaching that cell
        if obstacleGrid[0][0] == 1:
            table[0][0] = 0
        else:
            table[0][0] = 1
            
        #For all the cells in row0, there's only 1 way of reaching there (from the cell to the left of it), 
        #so we initialize those cells with the same value as the cell to the left if it has, unless the obstacleGrid 
        #has a 1 there in which case we put a 0
        for col in range(1, numcols):
            if obstacleGrid[0][col] == 1:
                table[0][col] = 0
            else:
                table[0][col] = table[0][col-1]
                
        #For all the cells in col0, there's only 1 way of reaching there (from the cell above it), so we
        #initialize those cells with the same value as the cell above it has, unless the obstacleGrid had 
        #a 1 there in which case we put a 0
        for row in range(1, numrows):
            if obstacleGrid[row][0] == 1:
                table[row][0] = 0
            else:
                table[row][0] = table[row-1][0]
           
        
        #Now do the main traversal, where every lazy manager, fills up his cell by adding the value computed
        #by his predecessor above it (row-1) and to the left of it (col-1), unless there's a 1 in the corresponding
        #cell in the obstacleGrid in which case we put a 0
        for row in range(1,numrows):
            for col in range(1, numcols):
                if obstacleGrid[row][col] == 1:
                    table[row][col] = 0
                else:
                    table[row][col] = table[row-1][col] + table[row][col-1]
        
        #We return the value of the last cell in the table grid
        return table[numrows-1][numcols-1]
    
    
    
