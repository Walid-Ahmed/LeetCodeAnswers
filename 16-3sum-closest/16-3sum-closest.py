import copy
import math

class Solution(object):

    def twoSum(self,s, target,num,leastDiff):
        #print(num,s)
        answer=[]
        #leastDiff=float('inf')
        lo, hi = 0, len(s)-1
        while hi>lo:
            #print(lo,hi)
            sums = s[lo] + s[hi]
            #print("sums={},target={}".format(sums,target))
            if sums < target:
                diff=abs(sums-target)
                if(diff<leastDiff):
                  answer=( [num,s[lo], s[hi]])
                  leastDiff=diff
                lo += 1  
            elif sums > target:
                diff=abs(sums-target)
                if(diff<leastDiff):
                  answer=( [num,s[lo], s[hi]])
                  leastDiff=diff
                hi -= 1
            elif(sums == target):
                #print("[INFO] Found exact target")
                answer=( [num,s[lo], s[hi]])
                return answer,0
            elif (leastDiff==1) or (leastDiff==-1):   
                      break
            while (hi>lo) and s[lo]==s[lo+1]:
                  lo+=1
            while (hi>lo) and s[hi]==s[hi-1]:
                  hi-=1  
     
        return  answer,leastDiff

    def threeSumClosest(self, nums, target):
      nums.sort()
      #print(nums)
      #print(nums)
      leastDiff=float('inf')
      for i,num in enumerate(nums):
        if(i>0):
          if(nums[i]==nums[i-1]):  #to avoid repetition
            continue
        new_target=target-num
        answer,diff=self.twoSum(nums[i+1:],new_target,num,leastDiff)
        #print("current answer {} with dif {}".format(answer,diff))
        if(diff<leastDiff):
          best_answer=answer
          leastDiff=diff
        if (leastDiff==0):   
                      break  
        

      return sum(best_answer)