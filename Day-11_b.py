from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(idx, comb):
            if idx == len(digits):
                res.append(''.join(comb)) 
                return

            for letter in digit_to_letters[digits[idx]]:
                comb.append(letter)        
                backtrack(idx + 1, comb)
                comb.pop()                  

        res = []
        backtrack(0, [])

        return res

def main():
    digits = input("Enter digits (2-9): ").strip()

    if not digits or any(d not in "23456789" for d in digits):
        print("Invalid input! Please enter digits between 2 and 9.")
        return

    
    solution = Solution()
    result = solution.letterCombinations(digits)

    print("Possible letter combinations:", result)

if __name__ == "__main__":
    main()
