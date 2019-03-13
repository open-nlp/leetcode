#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:junxu
@email: xujunrt@163.com
@time: 2019-03-08 13:08
"""

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""

class Solution(object):
    def twoSum(self,nums,target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        value_key_dict = dict()
        for index,value in enumerate(nums):
            sub = target - value
            if sub in value_key_dict:
                return [value_key_dict[sub],index]
            else:
                value_key_dict[value] = index


if __name__ == '__main__':
    nums = [2,3,4,5]
    target = 1
    solution = Solution()
    result = solution.twoSum(nums,target)
    print(result)