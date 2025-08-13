class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            poss = target - nums[i]
            if poss in table:
                return [table[poss], i]
            table[nums[i]] = i
        return []

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = []
#         for i in range (len(nums)):
#             need = target - nums[i]
#             if need in seen:
#                 return [seen.index(need), i]
#             seen.append(nums[i])
