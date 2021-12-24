"""
Program To Find Maximum Width Of Binary Tree 
Time Complexity - O(n)
Space Complexity - O(n)
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
        
def WidthOfBt(root):
    Stack = [(root,0)]
    Res = []
    Max = float("-inf")
    while(Stack):
        StackLen = len(Stack)
        SubRes = []
        for i in range(StackLen):
            CurrNode,CurrVal = Stack.pop(0)
            SubRes.append(CurrVal)
            if(CurrNode.left):Stack.append((CurrNode.left,(2*CurrVal)+1))
            if(CurrNode.right):Stack.append((CurrNode.right,(2*CurrVal)+2))
        MaxVal = SubRes[-1]-SubRes[0]+1
        if(MaxVal > Max):
            Max = MaxVal
    return Max
    
NumTree = Node(1)
NumTree.right = Node(2)
NumTree.right.right = Node(9)
NumTree.left = Node(3)
NumTree.left.left = Node(5)
NumTree.left.right = Node(3)

print(WidthOfBt(NumTree))
