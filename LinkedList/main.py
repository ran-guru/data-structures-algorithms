class Node:
    def __init__(self, value) -> None:
        """Initialize a new node with a value"""
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        """Initializ e a new LinkedList with a value"""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1


    def pop(self):
        """Remove the last node from the list"""
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1 
        
        if self.length == 0:
            self.head = None
            self.tail = None
        
        return temp.value

    def prepend(self, value):
        """Create a new node and prepend it to the start of the list"""
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True
    
    def pop_first(self):
        """Remove the first node from the list"""
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp.value
    

    def get(self, index):
        """Get the value of the node at the given index"""
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp.value

    def insert(self, index, value):
        pass

    

my_linked_list = LinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
print(my_linked_list.get(2))