# w2 8 876. Middle of the Linked List

# Given the head of a singly linked list,
# return the middle node of the linked list.
# If there are two middle nodes,
# return the second middle node.


# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        middle_list = []
        index_middle_of_head = int(len(head)/2)
        for i in head[index_middle_of_head:]:
            middle_list.append(i)
        return middle_list

# good solution, the fist one wasn't for liked lists...
# Just regular lists, my mistake


class Solution1(object):
    def middleNode(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


sol = Solution()
head = [1, 2, 3, 4, 5]
head1 = [1, 2, 3, 4, 5, 6]

print(sol.middleNode(head))
print(sol.middleNode(head1))
