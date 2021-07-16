class Solution:
    #Index 0 should contain 1, index 1 should contain 2, index i should contain i+1
    #Conversely, d should be present in index d-1
    
    #As a lazy manager, I just focus on index i and try to get i+1 there. If I find
    #d at my index then I swap it with the value at index d-1. This will ensure d goes
    #to its correct spot. I keep on swapping till I get i+1 at my index. 
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        #We iterate over the entire nums array
        for i in range(len(nums)):
            
            #If the number at lazy manager's index i is not i+1, we start a while loop
            while nums[i] != i+1:
                
                #The lazy manager has d at his index, d rightful place is at index d-1
                d = nums[i]
                
                #But before swapping values with index d-1, we need to ensure that index
                #d-1 doesn't alreay contain d. Else we will enter into an infinite loop
                if nums[d-1] != nums[i]:
                    nums[i], nums[d-1] = nums[d-1], nums[i]
                else:
                    #If the index d-1 aleady contains d, the we break the while loop and 
                    #let the other lazy managers continue with their tasks
                    break
                    
        result = []
        
        #We iterate over the nums array again to check which indexes still don't have
        #the appropriate value. THose will be the duplicate values. We collect them
        #in the results array
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(nums[i])
                
        return result
    
    
        
