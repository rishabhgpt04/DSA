class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # brute for would be to generate all substring and then compare if it is palindrome 
        start,end= 0,0
        lenOfStr=len(s)
        def expand(ptr_l,ptr_r):
            while(ptr_l>=0 and ptr_r< lenOfStr and s[ptr_l] == s[ptr_r]):
                ptr_l-=1
                ptr_r+=1
            return ptr_l+1 , ptr_r-1
        
        for i in range(lenOfStr):
            # for odd length palindrome  abbba
            ptr_l_odd, ptr_r_odd=expand(i,i)
            # for even lenght palindorme ab ba 
            ptr_l_even, ptr_r_even = expand(i,i+1)
            if (ptr_r_odd-ptr_l_odd) > (end-start):
                end = ptr_r_odd
                start=ptr_l_odd
            if (ptr_r_even-ptr_l_even) > (end-start):
                end = ptr_r_even
                start=ptr_l_even
        return s[start:end+1]
