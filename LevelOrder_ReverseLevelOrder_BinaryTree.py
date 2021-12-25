"""
Level Order Traversal And Reverse Level Order Traversal Of Binary Tree

Level Order Traversal
Time Complexity - O(n)
Space Complexity - O(n)

Reverse Level Order Traversal
Time Complexity - O(n)
Space Complexity - O(n)
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

def LevelOrderTraversal(root):
    Stack = [root]
    Res = []
    while(Stack):
        LevelRes = []
        StackLen = len(Stack)
        for i in range(StackLen):
            Curr = Stack.pop(0)
            LevelRes.append(Curr.val)
            if(Curr.left): Stack.append(Curr.left)
            if(Curr.right): Stack.append(Curr.right)
        Res.append(LevelRes)
    return Res
    
def ReverseLevelOrderTraversal(root):
    Stack = [root]
    Res = []
    while(Stack):
        LevelRes = []
        StackLen = len(Stack)
        for i in range(StackLen):
            Curr = Stack.pop(0)
            LevelRes.insert(0,Curr.val)
            if(Curr.left): Stack.append(Curr.left)
            if(Curr.right): Stack.append(Curr.right)
        Res.append(LevelRes)
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

print(LevelOrderTraversal(NumTree))
print(ReverseLevelOrderTraversal(NumTree))
