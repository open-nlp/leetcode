#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:junxu
@email: xujunrt@163.com
@time: 2019-03-09 21:23
"""

"""

Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

"""

class Solution(object):
    def search_insert_position(self,nums,target):
        """
        :param nums: List[int]
        :param target: int
        :return: int
        """
        if not nums:
            return 0
        low = 0
        high = len(nums) - 1
        while low <= high :
            mid = (low + high) // 2
            if nums[mid] == target :
                return mid
            elif nums[mid] > target :
                high = mid - 1
            else:
                low = mid + 1
        return low

if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 0
    solution = Solution()
    result = solution.search_insert_position(nums,target)
    print(result)