import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
          sign=1
        else: 
          sign=-1
        x*=sign  
        nums=[]
        while True:
          num=x%10
          nums.append(num)
          x=x//10
          if(x==0):
            break
          print(x,num)

        #print(nums) 
        s=""
        for num in nums:
          s+=str(num)
        s=int(s)*sign  
        if s >(math.pow(2,31)-1) or s <-1*math.pow(2,31):
          s=0
        return(s)  