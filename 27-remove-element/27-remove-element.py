class Solution(object):
    
    def exchange(self,nums,i,j):
        nums[i],nums[j]=nums[j],nums[i]
        
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        left=0
        right=len(nums)-1
        if len(nums)==0: #empty list
            return 0


        while(left<=right):
            if nums[left]==val:
                self.exchange(nums,left,right)
                right=right-1

            else:
                left=left+1
                
        #print(nums,left,right)

        return(left)


                
            