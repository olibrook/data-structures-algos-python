class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = dict()
        i = 0
        for num in nums:
            complement = target - num
            if complement in indices and not i == indices.get(num, None):
                return [indices[complement], i]
            indices[num] = i
            i += 1
        raise Exception()
