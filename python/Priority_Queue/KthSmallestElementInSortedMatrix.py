'''
378. Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        matrix_list = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix_list.append(matrix[row][col])
                
        heapq.heapify(matrix_list)
        smallest = heapq.nsmallest(k, matrix_list)
        return smallest[-1]
        