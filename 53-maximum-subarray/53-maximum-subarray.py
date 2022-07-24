class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        allZeroFlag=True
        for num1 in nums:
            if(num1>0):
                allZeroFlag=False
                break
        if(allZeroFlag):
            #print("[INFO] Finding the large of max number")
            return(max(nums))

        maximumSubArray=float("-inf")
        sum=0
        for num in nums:
            sum=sum+num

            if(sum<0): 
                sum=0

            if(sum>maximumSubArray):  #maybe a single number is better
                        maximumSubArray=sum  

           
        return(maximumSubArray)
        