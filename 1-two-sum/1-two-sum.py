class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data={}
        for index1,num in enumerate(nums):
          subTarget=target-num
          if((data.get(subTarget, -1))!=-1) and target==2*num:    # the element existed
            return(data.get(subTarget),index1)    
          data[num]=index1
          index2 = data.get(subTarget, -1)
          if(index2!=-1) and index2!=index1:
              return index1,index2
