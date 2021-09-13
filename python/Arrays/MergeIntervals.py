'''
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
'''

def overlap(list1: List[int], list2: List[int]) -> bool:
    right = list1[1]
    left = list2[0]
    if right >= left:
        return True
    else:
        return False
    
def mergeIntervals(list1: List[int], list2: List[int]) -> List[int]:
    merged = [min(list1[0],list2[0]), max(list1[1],list2[1])]
    return merged

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        i, j = 0, 1
        while i < len(intervals)-1:
            print(intervals[i], intervals[j])
            if overlap(intervals[i], intervals[j]):
                list1 = mergeIntervals(intervals[i], intervals[j])
                intervals[i] = list1
                intervals.remove(intervals[j])
            else:
                i += 1
                j += 1
                
        return intervals
    
    
            
        
        