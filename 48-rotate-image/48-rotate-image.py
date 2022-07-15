class Solution(object):
    def reverse(self,nums,start,stop):
      while(start<stop):
        nums[start], nums[stop]=nums[stop], nums[start]
        start=start+1
        stop=stop-1
      return nums 
    def rotate(self, matrix):
      #Transpose
      for row in range(len(matrix)):
                  for col in range(row,len(matrix)):
                      matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]
      #print(matrix)                
      for row in range(len(matrix)):
                      matrix[row]=self.reverse(matrix[row],0,len(matrix[row])-1)
      return (matrix)     
