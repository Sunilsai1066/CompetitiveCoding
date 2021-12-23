"""
Reverse Given Linked List

To Just Return Reverse Node
Time Complexity - O(n)
Space Complexity - O(1)

To Return Reverse Values In List 
Time Complexity - O(n)
Time Complexity - O(n)
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
def ReverseLinkedList(head):
    # 2 --> 5 --> 7 --> 9 --> None
    Prev = None
    Curr = head
    while(Curr != None):
        NextV = Curr.next
        Curr.next = Prev
        Prev = Curr
        Curr = NextV
    Lis = []
    while(Prev != None):
        Lis.append(Prev.val)
        Prev = Prev.next
    return Lis
        

Link1 = Node(2)
Link2 = Node(5)
Link3 = Node(7)
Link4 = Node(9)

Link1.next = Link2
Link2.next = Link3
Link3.next = Link4

print(ReverseLinkedList(Link1))
