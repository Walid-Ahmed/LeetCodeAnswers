class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==1:
            return [[1]]
        allnums=[[1],[1,1]]
        for row in range(2,numRows):
            sublist=[-1]*(row+1)
            sublist[0]=1
            sublist[-1]=1
            prevSubList=allnums[row-1] #previous
            print("[INFO] prevSubList {}".format(prevSubList))
            for j in range(0,len(prevSubList)-1):  
                print("prevSubList[j] {} prevSubList[j+1 {}".format(prevSubList[j],prevSubList[j+1]))
                element=prevSubList[j]+prevSubList[j+1]
                sublist[j+1]=element
                           
            allnums.append(sublist)  
            print(allnums)
        return allnums
                           

                