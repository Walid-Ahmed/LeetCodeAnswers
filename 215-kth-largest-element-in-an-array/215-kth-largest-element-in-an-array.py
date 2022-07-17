class Solution(object):

  #function which returns the index of minimum value in the list




  def findKthLargest(self, nums, k):
      """
      :type nums: List[int]
      :type k: int
      :rtype: int
      """
      
      nums.sort()
      print(nums)
      return(nums[-k])     

