"""
Recursive And Iterative Approach For Pre Order Traversal Of Binary Tree

Recursive 
Time Complexity - O(n)
Space Complexity - O(n)

Iterative 
Time Complexity - O(n)
Space Complexity - O(n)
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

def PreOrderRecursive(root):
    if(root == None): return []
    LeftVal = PreOrderRecursive(root.left)
    RightVal = PreOrderRecursive(root.right)
    return [root.val,*LeftVal,*RightVal]

def PreOrderIterative(root):
    Stack = [root]
    Res = []
    while(Stack):
        Curr = Stack.pop()
        Res.append(Curr.val)
        if(Curr.right): Stack.append(Curr.right)
        if(Curr.left): Stack.append(Curr.left)
    return Res
        
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

print(PreOrderRecursive(NumTree))
print(PreOrderIterative(NumTree))
