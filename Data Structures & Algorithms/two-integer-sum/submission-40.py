class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indicies and i != indicies[diff]:
                return [indicies[diff], i]
            indicies[nums[i]] = i