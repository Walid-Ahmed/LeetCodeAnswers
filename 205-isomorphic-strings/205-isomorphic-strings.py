class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        rules=dict()

        s=list(s)
        t=list(t)
        #print(s)
        #print(t)
        for char1,char2 in zip(s,t):
            if char1 in rules :
             value=rules.get(char1)
             if(value==char2):  #old rule not violated
               continue
             else:
               return False  
            rules[char1]=char2
        #print(rules)
        
        rules=dict()

        for char1,char2 in zip(t,s):
            if char1 in rules :
             value=rules.get(char1)
             if(value==char2):  #old rule not violated
               continue
             else:
               return False  
            rules[char1]=char2
        #print(rules)
        return True