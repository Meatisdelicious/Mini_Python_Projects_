# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()  # Dummy node to simplify the merging process
        current = dummy  # Pointer to build the merged list

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Move pointer forward

        # Attach the remaining nodes (if any)
        current.next = list1 if list1 else list2

        return dummy.next  # Return the head of the merged list

    
list1 = [1,2,4]
list2 = [1,3,4]
# Output: [1,1,2,3,4,4]


list11 = []
list22 = []
# Output: []

list13 = []
list23 = [0]
# Output: [0]

sol = Solution()
print(sol.mergeTwoLists(list1,list2))