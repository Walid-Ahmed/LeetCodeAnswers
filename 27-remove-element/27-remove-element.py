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
        k=len(nums)
        if k==0: #empty list
            return 0
        if k==1 and nums[0]==val: #single element list with element is val
            return 0

        while(left<=right):
            if nums[left]==val:
                self.exchange(nums,left,right)
                right=right-1

            else:
                left=left+1
                
        print(nums,left,right)
        if(left==0) and nums[left]==val:
            return 0
        return(left)


                
            