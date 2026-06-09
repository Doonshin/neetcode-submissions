class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        res = 1
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue  # 重複は無視
            elif nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                res = max(res, curr)
                curr = 1

        return max(res, curr)
