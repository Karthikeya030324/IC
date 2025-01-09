class Solution(object):
  def singleNumber(self, nums):
      nums1 = []
      for i in nums:
          if i not in nums1:
              nums1.append(i)
          else:
              nums1.remove(i)
      return nums1[0]

if __name__ == "__main__":
  nums =list(map(int,input("Enter the elements of the array: ").split()))
  solution = Solution()
  print(solution.singleNumber(nums))
