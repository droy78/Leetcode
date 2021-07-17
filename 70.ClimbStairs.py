class Solution(object):
    #As a lazy manager, I just want to focus on the number of ways a person can reach
    #my level i. There are actually just 2 possible ways someone can reach at level i : By
    #taking 1 step from level i-1 or by taking 2 steps from level i-2. I am assuming that
    #the no. of ways of reaching level i-1 would have been calculated by my predecessor and
    #the no. of ways of reaching level i-2 would have been calculated by his predecessor. I just
    #need to take the 2 values and add them up. 
    
    #We just need 3 spaces : One to store the solution solved by manager at level i-1, one to store 
    #the solution solved by the manager at level i-2 and one to be used by the current lazy manager
    #at level i who is going to add his predecessor's numbers
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #We initialize a table array with 3 indexes representing level 0, 1 and 2
        #You already start with level 0. So 0 ways of reaching there
        #Level 1 can be reached only one way by taking a single step from level 0
        #Level 2 can be reached 2 ways : 
        #Way1 - 1 step from level 0 + 1 step from level 1 
        #Way2 - 2 steps from level 0
        table = [0, 1, 2]
        
        #We iterate over all the levels starting with level 3
        for i in range(3, n+1):
            #The lazy manager computes his solution for level i by adding the solutions
            #calculated by his predecessor's at level i-1 and i-2
            #The first lazy manager, therefore, will fill up the solution for level 3 and
            #store it at index 3%3 => index 0
            table[i%3] = table[(i-1)%3] + table[(i-2)%3]
                
        return table[n%3]
    
    
