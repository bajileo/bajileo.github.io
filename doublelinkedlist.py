class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)


            

    def print_forward(self):
        if self.head == None:
            print("DoubleLinkedList is empty")
            return
        dll = " "
        itr = self.head
        while itr:
            dll += str(itr.data) + "-->"
            itr = itr.next
        print(dll)
    
    def print_backward(self):
        itr = self.head
        dllb = " "
        while itr.next:
            itr = itr.next
        while itr:
            dllb += str(itr.data) + "<--"
            itr = itr.prev
        print(dllb)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count
    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_begining(data)

    def insert_at(self, index, data):
        if index<0 or index>self.get_lenght():
            raise Exception("Invalid Index")
        if index==0:
            self.insert_at_begining()
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next =  node
                break
            itr = itr.next
            count += 1


if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.insert_at_begining("4")
    dll.insert_at_begining("3")
    dll.insert_at_begining("2")
    dll.insert_at_begining("1")
    dll.insert_at_end("5")
    dll.insert_at_end("6")
    dll.insert_at_end("7")
    dll.insert_at_end("8")
    dll.insert_values(["A", "B", "C", "D", "E", "F"])
    dll.insert_at(14, "bajo")
    dll.print_forward()
    dll.print_backward()
    print(dll.get_last_node())
    dll.get_lenght()
