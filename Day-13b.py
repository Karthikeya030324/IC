# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      m, n = len(text1), len(text2)
      dp = [[0] * (n + 1) for _ in range(m + 1)]

      for i in range(1, m + 1):
          for j in range(1, n + 1):
              if text1[i - 1] == text2[j - 1]:
                  dp[i][j] = dp[i - 1][j - 1] + 1
              else:
                  dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

      return dp[m][n]

def main():
  text1 = input("Enter first string: ")
  text2 = input("Enter second string: ")
  solution = Solution()
  result = solution.longestCommonSubsequence(text1, text2)
  print("Length of Longest Common Subsequence:", result)

if __name__ == "_main_":
  main()