class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runingSum=[]
        runingSum.append(nums[0])
        for i in range(1,len(nums)):
            runingSum.append(runingSum[i-1]+nums[i])

               
                
            
        return (runingSum)