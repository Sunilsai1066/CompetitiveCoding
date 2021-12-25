"""
Height Of Binary Tree Using Recursive And Iterative

Recursive
Time Complexity - O(n)
Space Complexity - O(n)

Iterative
Time Complexity - O(n)
Space Complexity - O(1)
                 - O(n)[For Stack Space]
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
        
def HeightRecursive(root):
    if(root == None): return 0
    LeftVal = HeightRecursive(root.left)
    RightVal = HeightRecursive(root.right)
    return 1+max(LeftVal,RightVal)

def HeightIterative(root):
    Height = 0
    Stack = [root]
    while(Stack):
        StackLen = len(Stack)
        for i in range(StackLen):
            Curr = Stack.pop(0)
            if(Curr.left):Stack.append(Curr.left)
            if(Curr.right):Stack.append(Curr.right)
        Height += 1
    return Height

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

print(HeightRecursive(NumTree))
print(HeightIterative(NumTree))
