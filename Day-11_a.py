from typing import List

class Solution:
          def combinationSum3(self, k: int, n: int) -> List[List[int]]:
              results = []

              def backtrack(remain, comb, next_start):
                  if remain == 0 and len(comb) == k:
                      results.append(list(comb))
                      return
                  elif remain < 0 or len(comb) == k:
                      return
                  for i in range(next_start, 9):
                      comb.append(i + 1)
                      backtrack(remain - i - 1, comb, i + 1)
                      comb.pop()

              backtrack(n, [], 0)
              return results
def main():
          k = int(input("Enter the number of elements in each combination (k): "))
          n = int(input("Enter the target sum (n): "))

          solution = Solution()
          result = solution.combinationSum3(k, n)

          print("Combinations of", k, "numbers that sum to", n, ":", result)

if __name__ == "__main__":
          main()
