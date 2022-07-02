class Solution(object):
  def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=[]
        tmp=[]
        if (len(s)==1):
            return 1
        for char in s:
          if char not in  result:
            result.append(char)
          else:
            if(len(result))>len(tmp):
              tmp = list(result)
            index = result.index(char)  
            result=result[index+1::]
            result.append(char)
            
          if(len(result))>len(tmp):
              tmp = list(result)
        print(tmp)    
        return(len(tmp)) 