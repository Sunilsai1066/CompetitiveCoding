"""
Sum Of Left Leaves In A Binary Tree
Time Complexity - O(n)
Space Complexity - O(n)
"""
class Node: 
    def __init__(self,val): 
        self.val = val 
        self.right = None 
        self.left = None 

def LeftLeavesSum(root):
    Sum = 0
    Stack = [(root,False)]
    while(Stack):
        Curr,State = Stack.pop()
        if(Curr.left == None and Curr.right == None and State == True): Sum += Curr.val
        if(Curr.left): Stack.append((Curr.left,True))
        if(Curr.right): Stack.append((Curr.right,False))
    return Sum

NumTree = Node(3)  
NumTree.left = Node(9)  
NumTree.right = Node(20)  
NumTree.right.left = Node(15)  
NumTree.right.right = Node(7)
NumTree.right.right.left = Node(6)

print(LeftLeavesSum(NumTree))
