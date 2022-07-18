class Solution(object):
  def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=[]
        bestResult=[]
        if (len(s)==1):
            return 1
        for char in s:
          if char not in  result:
            result.append(char)
            if(len(result))>len(bestResult):
              bestResult = list(result)
          else:
            index = result.index(char)  
            result=result[index+1::]
            result.append(char)
            #print(result)

        #print(tmp)    
        return(len(bestResult)) 