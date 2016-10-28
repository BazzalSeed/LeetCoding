 class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp_str = ""
        max = 0
        if s == None:
            return max
        for i in s:
            if i not in temp_str:
                temp_str += i
                if(len(temp_str) > max):
                    max = len(temp_str)
            else:
                temp_str = temp_str[temp_str.index(i)+1:] + i
        return max
