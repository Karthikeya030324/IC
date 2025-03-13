class Solution(object):
    def strWithout3x3y(self, x, y):
        result = []

        while x > 0 or y > 0:
            if len(result) >= 2 and result[-1] == result[-2]:  # Check last two letters
                if result[-1] == 'x':  # Avoid "xxx", so add 'y'
                    result.append('y')
                    y -= 1
                else:  # Avoid "yyy", so add 'x'
                    result.append('x')
                    x -= 1
            else:
                if x >= y:  # If more 'x' left, add 'x'
                    result.append('x')
                    x -= 1
                else:  # Otherwise, add 'y'
                    result.append('y')
                    y -= 1

        return "".join(result)

# Driver code for Replit
if __name__ == "__main__":
    x = int(input("Enter the number of 'x': "))
    y = int(input("Enter the number of 'y': "))

    solution = Solution()
    result = solution.strWithout3x3y(x, y)

    print("Generated string:", result)
