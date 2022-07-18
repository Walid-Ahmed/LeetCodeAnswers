class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s)!=len(t)):
            return False
        wordDict1={}
        wordDict2={}
        for char in s:
          wordDict1[char]=wordDict1.get(char,0)+1
        for char in t:
          wordDict2[char]=wordDict2.get(char,0)+1  
        for key in   wordDict1:
          if key not in wordDict2:
            return False
          if(wordDict1[key]!=wordDict2[key]): 
            return False 
        return True 
