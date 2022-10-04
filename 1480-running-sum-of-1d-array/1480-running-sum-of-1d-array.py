class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runingSum=[]
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            if(i>0):
                runingSum.append(runingSum[i-1]+nums[i])
            else:
                runingSum.append(nums[0])
                
            
        return (runingSum)