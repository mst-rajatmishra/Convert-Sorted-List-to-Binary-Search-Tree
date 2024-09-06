# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Convert linked list to array
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        # Helper function to convert sorted array to BST
        def sortedArrayToBST(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(values[mid])
            root.left = sortedArrayToBST(left, mid - 1)
            root.right = sortedArrayToBST(mid + 1, right)
            return root
        
        # Create BST from the entire array
        return sortedArrayToBST(0, len(values) - 1)
   
