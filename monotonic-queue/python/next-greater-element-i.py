class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """LC 496. Next Greater Element I
        """
        m = len(nums1)
        n = len(nums2)
        
        result = [-1] * m
        mapping = {}
        stack = []
        
        for i in range(n)[::-1]:
            while len(stack) > 0 and nums2[i] > stack[-1]:
                stack.pop()
            mapping[nums2[i]] = -1 if len(stack) == 0 else stack[-1]
            stack.append(nums2[i])
        
        for i in range(m):
            result[i] = mapping[nums1[i]]
        
        return result