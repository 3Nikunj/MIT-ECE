# '''
# Linked List:
# '''

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Operations:
#     def traversing (self, head):
#         cur = head 
#         while cur != None:
#             print(cur.data, end=" ")
#             cur = cur.next

#     def inserting(self, head, val):
#         new_node = Node(val)
#         cur = head 
#         while cur.next != None:
#             cur = cur.next
#         cur.next = new_node
    
#     def insertAfter(self, head, after, val):
#        new_node = Node(val)
#        cur = head 
#        while cur.next != None:
#         if cur.data == after:
#             break 
#         cur = cur.next
#         new_node.next = cur.next
#         cur.next = new_node

#     def deleteLast(self, head):
#         cur = head 
#         while cur.next.next != None:
#             cur = cur.next
#         cur.next = None

#         # i = None 
#         # j = head
#         # while j.next != None:
#         #     i = j
#         #     j = j.next
#         # i.next = None

#     def deleteAfter(self, head, after):
#         cur = head
#         while cur.next != None:
#             if cur.data == after:
#                 temp = cur.next
#                 cur.next = cur.next.next
#                 break 
#         temp.next = None
            


# node1 = Node(1) 
# node2 = Node(2)
# node3 = Node(3)
# node1.next = node2
# node2.next = node3
# head = node1

# op = Operations()
# op.traversing(head)
# print()
# op.inserting(head, 4)
# op.traversing(head)
# print()
# op.insertAfter(head, 2, 6)
# op.traversing(head)
# print()
# op.deleteLast(head)
# op.traversing(head)


'''
Stack: Last In First Out
Implementation : List and Class&Object

OPeration:
1. Push
2. Pop
3. Peek
4. isEmpty
'''

# stack = []

# def push(stack, val):
#     stack.append(val) 

# def pop(stack):
#     return stack.pop()

# def isEmpty() :
#     if len(stack) == 0:
#         return True
#     return False 

# def Peak():
#     return stack[-1]

'''
Queue : First In First Out
Implementation : List and Class&Object

OPeration:
1. Enqueue
2. Dequeue
3. Peek
4. isEmpty
'''

# queue = []
# def enqure(ele):
#     queue.append(ele)

# def deque():
#     return queue.pop(0)

# def Peak():
#     return queue[0]

# def isEmpty():
#     if len(queue) == 0:/
#         return True
#     return False 
