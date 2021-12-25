"""
Pre In Post Order Traversal Of Binary Tree Using Single Stack

Time Complexity - O(n)
Space Complexity - O(n)[For Stack]
                 - O(3*n)[For Storing PreOrder InOrder PostOrder Traversal]

"""
class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

def PreInPostOrderTraversal(root):
    Stack = [[root,1]]
    PreOrder,InOrder,PostOrder = [],[],[]
    while(Stack):
        CurrNode = Stack[-1]
        if(CurrNode[1] == 1):
            PreOrder.append(CurrNode[0].val)
            CurrNode[1] += 1
            if(CurrNode[0].left): Stack.append([CurrNode[0].left,1])
        elif(CurrNode[1] == 2):
            InOrder.append(CurrNode[0].val)
            CurrNode[1] += 1
            if(CurrNode[0].right): Stack.append([CurrNode[0].right,1])
        else:
            PostOrder.append(CurrNode[0].val)
            Stack.pop()
    return "PreOrder :",PreOrder,"InOrder :",InOrder,"PostOrder : ",PostOrder
    
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

print(PreInPostOrderTraversal(NumTree))
