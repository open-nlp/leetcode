#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:junxu
@email: xujunrt@163.com
@time: 2019-03-08 18:50
"""


"""

Given a sorted array, remove the duplicates in place such that each element appear only once and return 
the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the new length.

Subscribe to see which companies asked this question.

"""

class Solution(object):
    def remove_duplicates(self,nums):
        """
        :param nums: List[int]
        :return: int
        """
        if not nums:
            return 0
        current_max_value = nums[0]
        no_repeat_num = 1
        for index,value in enumerate(nums):
            if value > current_max_value:
                tmp = nums[no_repeat_num]
                nums[no_repeat_num] = nums[index]
                nums[index] = tmp
                current_max_value = value
                no_repeat_num = no_repeat_num + 1
        return no_repeat_num

if __name__ == '__main__':
    nums = [1,1,2,3,3]
    solution = Solution()
    result = solution.remove_duplicates(nums)
    print(result)