class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[1]*len(nums)
        #print(answer)
        productBefore=[1]*len(nums)
        i=1
        for num in nums:
          #print(num)
          if(i)==len(nums):
            break
          #print(productBefore[i-1],num)  
          productBefore[i]=productBefore[i-1]*num
          i+=1
        #print(productBefore)

        productAfter=[1]*len(nums)
        i=1
        for num in list(reversed(nums)):
          #print(num)
          if(i)==len(nums):
            break
          #print(productAfter[i-1],num)  
          productAfter[i]=productAfter[i-1]*num
          i+=1
        productAfter= list(reversed(productAfter))
        #print(productAfter)
        #print(productBefore)
        
        i=0
        for a,b in zip(productBefore,productAfter):
          answer[i]=a*b
          #print(answer)
          i=i+1
        return answer 