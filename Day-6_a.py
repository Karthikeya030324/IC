class Solution(object):
  def maxSubArray(self, nums):
      c = 0
      m = float('-inf')
      for i in nums:
          c = c + i 
          m = max(c, m)
          if c < 0:
              c = 0
      return m  


if __name__ == "__main__":
  nums = list(map(int,input("Enter the elements of the array: ").split()))
  solution = Solution()
  print(solution.maxSubArray(nums))
