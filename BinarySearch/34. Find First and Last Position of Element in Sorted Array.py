class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target):
            lb, ub = 0, len(nums) - 1
            while lb <= ub:
                mid = (lb + ub) // 2
                if nums[mid] >= target:
                    ub = mid - 1
                else:
                    lb = mid + 1
            return lb if lb < len(nums) and nums[lb] == target else -1

        def find_last(nums, target):
            lb, ub = 0, len(nums) - 1
            while lb <= ub:
                mid = (lb + ub) // 2
                if nums[mid] <= target:
                    lb = mid + 1
                else:
                    ub = mid - 1
            return ub if ub >= 0 and nums[ub] == target else -1

        first = find_first(nums, target)
        last = find_last(nums, target)
        return [first, last] if first != -1 else [-1, -1]
