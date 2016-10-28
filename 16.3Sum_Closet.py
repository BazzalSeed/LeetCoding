"""

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Subscribe to see which companies asked this question
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        res = []
        for i in range(0, length - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            new_target = nums[i] * (-1) + target
            left, right = i + 1, length - 1
            first, second = nums[left], nums[right]
            dist = abs(new_target - (first + second))
            # print "each iteration => %s" % (i)
            while left < right:
                # print "       target is %s" % new_target
                if abs(new_target - (nums[left] + nums[right])) < dist:
                    first, second = nums[left], nums[right]
                    dist = abs(new_target - (first + second))
                    # print "     updating first and second %s, %s" % (first, second)
                    # print left, right, nums
                    # while left < right and nums[left] == nums[left - 1]:
                    #     left += 1
                    # while left < right and nums[right] == nums[right + 1]:
                    #     right -= 1
                if nums[left] + nums[right] > new_target:
                    # print "      approaching from right"
                    right -= 1
                else:
                    # print "      approaching from left"
                    left += 1

            res.append([nums[i], first, second])
        # print res,min(res, key = lambda x : abs(target- sum(x)))
        return sum(min(res, key = lambda x : abs(target- sum(x))))

        
