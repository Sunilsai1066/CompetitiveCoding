"""
Simple Program To Find If Value Present In Linked List Or Not
Time Complexity - O(n)
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def FindValueInLL(head,ValCheck):
    while(head != None):
        if(ValCheck == head.val): return True
        head = head.next
    return False

Link1 = Node(2)
Link2 = Node(5)
Link3 = Node(7)
Link4 = Node(9)

Link1.next = Link2
Link2.next = Link3
Link3.next = Link4

ValCheck = 9
print(FindValueInLL(Link1,ValCheck))
