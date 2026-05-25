class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        for index in range(len(nums) * 2):
            element = nums[index % len(nums)]
            result.append(element)
        return result