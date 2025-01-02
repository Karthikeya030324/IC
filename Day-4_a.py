class Solution(object):
  def moveZeroes(self, nums):
      """
      Do not return anything, modify nums in-place instead.
      """
      non_zero_index = 0

      for i in range(len(nums)):
          if nums[i] != 0:
              nums[non_zero_index] = nums[i]
              non_zero_index += 1
      for i in range(non_zero_index, len(nums)):
          nums[i] = 0