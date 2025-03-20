# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2. You have the following three operations permitted on a word:Insert a character, Delete a character, Replace a character

class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
      m, n = len(word1), len(word2)
      dp = [[0] * (n + 1) for _ in range(m + 1)]

      for i in range(m + 1):
          dp[i][0] = i  
      for j in range(n + 1):
          dp[0][j] = j 

      for i in range(1, m + 1):
          for j in range(1, n + 1):
              if word1[i - 1] == word2[j - 1]:  
                  dp[i][j] = dp[i - 1][j - 1]
              else:
                  dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

      return dp[m][n]

def main():
  word1 = input("Enter first word: ")
  word2 = input("Enter second word: ")
  solution = Solution()
  result = solution.minDistance(word1, word2)
  print("Minimum edit distance:", result)

if __name__ == "_main_":
  main()