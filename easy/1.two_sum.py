#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:junxu
@email: xujunrt@163.com
@time: 2019-03-08 13:08
"""

"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

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