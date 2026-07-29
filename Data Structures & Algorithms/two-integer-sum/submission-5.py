class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if target % 2 == 0 and nums.count((target/2)) >= 2:
            ind1 = nums.index(target/2)
            nums.remove(target/2)
            ind2 = nums.index(target/2) + 1
            return [ind1, ind2]
        for i in range(len(nums)):
            second = target - nums[i]
            if second in nums and nums[i] != second:
                return [i, nums.index(second)]

