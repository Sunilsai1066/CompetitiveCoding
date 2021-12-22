"""
Find Node Value By Using The Given Index 
Time Complexity - O(n)
Space Complexity - O(1)
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def FindValueByIndexInLL(head,Index):
    Count = 0
    while(head != None):
        if(Count == Index): return head.val
        head = head.next
        Count += 1
    return "Index Is Larger Than LinkedList Length"

Link1 = Node(2)
Link2 = Node(5)
Link3 = Node(7)
Link4 = Node(9)

Link1.next = Link2
Link2.next = Link3
Link3.next = Link4

Index = 3
print(FindValueByIndexInLL(Link1,Index))
