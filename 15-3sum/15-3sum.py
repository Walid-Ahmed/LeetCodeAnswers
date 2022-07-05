
class Solution(object):


    def twoSum(self,s, target,num):
        #print(num)
        answer=[]
        lo, hi = 0, len(s)-1
        while hi>lo:
            #print(lo,hi)
            sums = s[lo] + s[hi]
            if sums < target:
                lo += 1
            elif sums > target:
                hi -= 1
            else:
                answer.append( [num,s[lo], s[hi]])
                #print("appending {}".format([num,s[lo], s[hi]]))
                while (hi>lo) and s[lo]==s[lo+1]:
                  lo+=1
                while (hi>lo) and s[hi]==s[hi-1]:
                  hi-=1
                lo+=1
                hi-=1
        return answer
    def threeSum(self, nums):
      answer=[]
      nums.sort()
      #print(nums)
      #print(nums)
      for i,num in enumerate(nums):
        if(i>0):
          if(nums[i]==nums[i-1]):  #to avoid repetition
            continue
        target=0-num
        subList=self.twoSum(nums[i+1:],target,num)
        if(len(subList)!=0):
          answer=answer+subList
          #print(answer)
          #exit()
      return answer
