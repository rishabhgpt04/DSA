class Solution:
    def isPalindrome(self,x:int)->bool:
        if x<0:
            return False
        n=x
        c=0
        while n:
            n//=10
            c+=1
        div=10**(c-1) if c>0 else 1
        for i in range(c//2):
            if x%10!=(x//div):
                return False
            x//=10
            div//=10
            x=x%div
            div//=10
        return True