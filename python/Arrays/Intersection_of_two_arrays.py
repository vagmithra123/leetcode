class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set()
        for i in range(0, len(nums1)):
            if nums1[i] in nums2:
                intersection.add(nums1[i])
            else:
                continue
                
        return intersection
        