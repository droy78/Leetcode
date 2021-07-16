class Solution:
    #Index 0 should contain 1, index 1 should contain 2, index i should contain i+1
    #Conversely, 1 should go to index 0, d should go to index d-1
    #As a lazy manager, I focus on my index i and ensure that i+1 is there. Instead,
    #if there is d, then I swap d with the value at index d-1. That way, d will 
    #be at its right position. I keep on doing it till i+1 comes to i. 
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        #We iterate over the array
        for i in range(len(nums)):
            
            #The lazy manager checks if index i contains i+1. If not, start a while loop
            while nums[i] != i+1:
                
                #Index i contains d, d should go to index d-1
                d = nums[i]
                
                #We swap only if index d-1 doesn't already contain d
                if nums[d-1] != nums[i]:
                    nums[i], nums[d-1] = nums[d-1], nums[i]
                else:
                    #If index d-1 already contains d then we break the while loop
                    #and let the other lazy managers do their jobs
                    break
        
        #We iterate over the entire loop again to see which index i doesn't have i+1
        #The number present at that index is the repeated number and the number that
        #should have present there is the missing number
        for i in range(len(nums)):
            if nums[i] != i+1:
                return [nums[i], i+1]
                
        
