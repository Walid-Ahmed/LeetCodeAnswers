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
            runingSum.append(sum)
            
        return (runingSum)