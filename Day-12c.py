from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        # Count occurrences of each task
        task_counts = Counter(tasks)

        # Sort frequencies in descending order
        frequencies = sorted(task_counts.values(), reverse=True)

        # Most frequent task count
        max_freq = frequencies[0]

        # Maximum possible idle time
        idle_time = (max_freq - 1) * n

        # Fill idle slots with other tasks
        for freq in frequencies[1:]:
            idle_time -= min(max_freq - 1, freq)

        # Ensure idle time is not negative
        idle_time = max(0, idle_time)

        # Total execution time = tasks count + remaining idle slots
        return len(tasks) + idle_time

# Driver code for Replit
if __name__ == "__main__":
    tasks = input("Enter tasks as uppercase letters separated by spaces: ").split()
    n = int(input("Enter cooling time (n): "))

    solution = Solution()
    result = solution.leastInterval(tasks, n)

    print("Minimum CPU intervals required:", result)
