# w7 56. Merge Intervals


# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the 
# non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

class Solution(object):
    def merge(self, intervals_list):
        stack = []
        
        for start_current, end_current in sorted(intervals_list):
            if stack and stack[-1][1] >= start_current:
                last_start, last_end = stack.pop()
                print("last_start :",last_start,"last_end",last_end)
                merged_interval = (min(last_start, start_current), max(last_end, end_current))
                print("merged_interval",merged_interval)
                stack.append(merged_interval)
            else:
                stack.append((start_current, end_current))
        print("final stack:", stack)
        return stack
    
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[1,4],[4,5]]
sol = Solution()
sol.merge(intervals2)
