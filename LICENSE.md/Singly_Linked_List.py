class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Singly_Linked_List:
    def __init__(self):
        self.head = None

    def add(self,data): # push_back # pushing at the end of Singly_Linked_List
        node_elem = Node(data)
        if(self.head == None):
            self.head = node_elem
        else:
            currNode = self.head
            while(currNode.next != None):
                currNode = currNode.next
                # print(currNode.data)
            currNode.next = node_elem
            # print(currNode.data)
            node_elem.next = None
            # print(currNode.next.data)
            # print(node_elem.next)

    def delete(self,data):
        currNode = self.head
        prevNode = self.head
        nextNode = None
        if (currNode != None):
            nextNode = currNode.next
        while(currNode != None):
            if(currNode.data == data):
                print(currNode.data);
                # if(prevNode ==self.head)
                # break
                if(prevNode == self.head):
                    self.head = nextNode
                    prevNode = self.head
                    #print(prevNode.data,"pooo")
                else:
                    #print(prevNode.data,"kooo")
                    prevNode.next = nextNode
            else:
                prevNode = currNode
            currNode = nextNode
            if(currNode != None):
                nextNode = currNode.next
            # if(currNode.data == 1):
            #     print(prevNode.data)
            #     print(currNode.data)
            #     print(nextNode.next)
            #     break

    def __str__(self):
        currNode = self.head
        s = ''
        # if(currNode.next != None):
        while(currNode != None):
            # print(currNode.data)
            s += str(currNode.data)
            # if(currNode.next != None):
            s+= '=>'
            currNode = currNode.next
        s += str(currNode)
        return s
    def print(list):
        currNode = list.head
        s = ''
        # if(currNode.next != None):
        while(currNode != None):
            # print(currNode.data)
            s += str(currNode.data)
            # if(currNode.next != None):
            s+= '=>'
            currNode = currNode.next
        s += str(currNode)
        return s 
