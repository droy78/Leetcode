class Solution:
    #The array will have values starting from 1. So index 0 will have the value 1, index 1 
    #will have the value 2 => index i will have the value i+1. Conversely, every value d should
    #be present in the index d-1. As a lazy manager, I just need to focus on index i and ensure 
    #the value there is i+1. Instead, if the value there is d, then I'll swap d with the number 
    #present in index d-1. This will ensure d goes to it's rightful index. I'll keep on swapping
    #until my index gets the value i+1
    def findDuplicate(self, nums: List[int]) -> int:
        
        #We iterate over the entire nums array
        for i in range(len(nums)):
            
            #If the lazy manager's index i doesn't have the value i+1, we start a while loop
            while nums[i] != i+1:
                
                #Lazy manager's index has the value d, d needs to go to index d-1
                d = nums[i]
                
                #But sending d to index d-1, we need to ensure that it already shouldn't have d.
                #If that happens, we will get into an infite loop
                if nums[d-1] != nums[i]:
                    nums[d-1], nums[i] = nums[i], nums[d-1]
                else:
                    #if d is already present in index d-1, we break this while loop and let the
                    #other lazy managers do their jobs
                    break
        
        #We then iterate over the entire array again to check which index still doesn't have
        #the right element. That element will be a duplicate element
        for i in range(len(nums)):
            if nums[i] != i+1:
                return nums[i]
        
        
        
