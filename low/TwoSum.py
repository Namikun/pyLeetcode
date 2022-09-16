class Solution(object):

    @staticmethod
    def two_sum(nums, target):
        d = {}
        for index, value in enumerate(nums):
            if target - value in d:
                return [d[target - value], index]
            d[value] = index
        return []


param = [1, 3, 3, 7]
result = Solution.two_sum(param, 6)
print(result)
