"""
Recursive And Iterative Approach For Post Order Traversal Of Binary Tree

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

def PostOrderRecursive(root):
    if(root == None): return []
    LeftVal = PostOrderRecursive(root.left)
    RightVal = PostOrderRecursive(root.right)
    return [*LeftVal,*RightVal,root.val]
        
def PostOrderIterative(root):
    Stack = [root]
    Res = []
    while(Stack):
        Curr = Stack.pop()
        Res.insert(0,Curr.val)
        if(Curr.left): Stack.append(Curr.left)
        if(Curr.right): Stack.append(Curr.right)
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

print(PostOrderRecursive(NumTree))
print(PostOrderIterative(NumTree))
