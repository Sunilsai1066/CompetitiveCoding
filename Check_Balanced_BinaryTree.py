"""
Check If Binary Tree Is Balanced

Time Complexity - O(n)
Space Complexity - O(n)
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
        
def BalancedTree(root):
    def Height(root):
        if(root == None): return 0
        LeftVal = 1+Height(root.left)
        RightVal = 1+Height(root.right)
        if(RightVal == -1 or LeftVal == -1):return -1
        if(abs(LeftVal-RightVal) > 1): return -1
        return max(LeftVal,RightVal)
    return Height(root) != -1

NumTree = Node(0) 
NumTree.left = Node(2) 
NumTree.right = Node(4) 
NumTree.left.left = Node(1) 
NumTree.left.left.left = Node(5) 
NumTree.left.left.right = Node(1) 
NumTree.right.left = Node(3) 
NumTree.right.right = Node(-1) 
NumTree.right.left.right = Node(6) 
NumTree.right.right.right = Node(8)

print(BalancedTree(NumTree))
