from Singly_Linked_List import *

# code for delete
# def delete(self,data):
#     currNode = self.head
#     prevNode = self.head
#     nextNode = None
#     if (currNode != None):
#         nextNode = currNode.next
#     while(currNode != None):
#         if(currNode.data == data):
#             if(prevNode == self.head):
#                 self.head = nextNode
#                 prevNode = self.head
#             else:
#                 prevNode.next = nextNode
#         else:
#             prevNode = currNode
#         currNode = nextNode
#         if(currNode != None):
#             nextNode = currNode.next

print('\nDelete in Singly Linked List \n')

test_list0 = (1,2,3,4,5)
print("deleting 3")
test_list0.delete(3)
print("output list after delete: ",test_list0)

print('')

test_list1 = ('org','com','her','him','blah')
print("deleting 'org'")
test_list1.delete('org')
print("output list after delete: ",test_list1)

print('')

test_list4 = ('B')
print("deleting 'B'")
test_list4.delete('B')
print("output list after delete: ",test_list4)

print('')

test_list5 = ('B','B','B','B')
print("deleting 'B'")
test_list5.delete('B')
print("output list after delete: ",test_list5)

print('')
