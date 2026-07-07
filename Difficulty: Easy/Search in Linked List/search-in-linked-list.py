'''
class head:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        #Code here
        def helper(head):
            if head==None:
                return False
            # print(head.data)
            if head.next == None :
                if head.data==key:
                    return True
                else:
                    return False
            chk=helper(head.next)
            if head.data==key:
                chk=True
            return chk
        return helper(head)