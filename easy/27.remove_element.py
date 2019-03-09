#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:junxu
@email: xujunrt@163.com
@time: 2019-03-08 21:16
"""

"""

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

Subscribe to see which companies asked this question.

"""

class Solution(object):
    def remove_element(self,nums,target):
        """
        :param nums: List[int]
        :param target: int
        :return: int
        """
        if not nums :
            return 0

        no_target_num = 0
        current_target_index = 0
        for index,value in enumerate(nums):
            if value != target :
                tmp = nums[current_target_index]
                nums[current_target_index] = nums[index]
                nums[index] = tmp
                current_target_index = current_target_index + 1
                no_target_num = no_target_num + 1
        return no_target_num

if __name__ == '__main__':
    nums = [2,3,3,2,1]
    target = 3
    solution = Solution()
    result = solution.remove_element(nums,target)
    print(result)