from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # 如果当前固定的数字和前一个一样，跳过，避免重复答案
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # 移动 left 和 right
                    left += 1
                    right -= 1

                    # 跳过重复的 left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # 跳过重复的 right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    # sum 太小，需要更大的数
                    left += 1

                else:
                    # sum 太大，需要更小的数
                    right -= 1

        return result