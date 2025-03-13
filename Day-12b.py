class Solution(object):
  def removeDuplicateLetters(self, s):
      last_occ = {}  # Stores the last occurrence index of each character
      stack = []      # Stack to store the result in lexicographical order
      visited = set() # Set to track visited characters

      # Store the last occurrence index of each character
      for i in range(len(s)):
          last_occ[s[i]] = i

      # Iterate over the string
      for i in range(len(s)):
          if s[i] not in visited:
              # Remove characters from the stack if:
              # - They are lexicographically greater than the current character
              # - They appear later in the string
              while stack and stack[-1] > s[i] and last_occ[stack[-1]] > i:
                  visited.remove(stack.pop())

              stack.append(s[i])
              visited.add(s[i])

      return ''.join(stack)

# Driver code for Replit
if __name__ == "__main__":
  s = input("Enter a string: ")  # Take user input
  solution = Solution()
  result = solution.removeDuplicateLetters(s)
  print("Result after removing duplicate letters:", result)
