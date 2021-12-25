"""
Recursive And Iterative Approach For In Order Traversal Of Binary Tree

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

def InOrderRecursive(root):
    if(root == None): return []
    LeftVal = InOrderRecursive(root.left)
    RightVal = InOrderRecursive(root.right)
    return [*LeftVal,root.val,*RightVal]

def InOrderIterative(root): 
    Stack = [] 
    Res = [] 
    Curr = root 
    while True:
        if Curr is not None:
            Stack.append(Curr)
            Curr = Curr.left
        elif(Stack):
            Curr = Stack.pop()
            Res.append(Curr.val)
            Curr = Curr.right
        else:
            break
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

print(InOrderRecursive(NumTree))
print(InOrderIterative(NumTree))
