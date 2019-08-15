#creating linked list with different methods
#for manipulation

# to do: reverse list,

class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head = None
        
    def append_front(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
        '''        
        if self.head is None:
            self.head = node(data)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node(data)
        '''
    def append_back(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        '''
        curr = self.head
        new_node = node(data)
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        '''
        
    def length(self):
        curr = self.head
        total = 0
        while curr is not None:
            total +=1
            curr = curr.next
        return total
    
    def display(self):
        list = []
        curr = self.head
        if self.head is None:
            return
        while curr is not None:
            list.append(curr.data)
            curr = curr.next
        print(list)
        
    def get(self,index):
        curr = self.head
        indx = 0
        if self.head is None:
            return
        while curr is not None:
            if index == indx:
                return curr.data
            indx +=1
            curr = curr.next
            
    
    def erase(self, key): 
          
        # Store head node 
        curr = self.head 
  
        # If head node itself holds the key to be deleted 
        if (curr is not None): 
            if (curr.data == key): 
                self.head = curr.next
                curr = None
                return
  
        # Search for the key to be deleted, keep track of the 
        # previous node as we need to change 'prev.next' 
        while(curr is not None): 
            if curr.data == key: 
                break 
            prev = curr 
            curr = curr.next 
  
        # if key was not present in linked list 
        if curr is None: 
            return 
  
        # Unlink the node from linked list 
        prev.next = curr.next 
        curr = None 

    def erase_index(self, indx):
        curr = self.head
        
        if indx is 0:
            self.head = curr.next
            curr = None
            return
        
        count = 1 # since we already checked for head
        while curr is not None:
            if count is not indx:
                prev = curr
                curr = curr.next
                count +=1
        
        if curr is None: 
            return
        
        prev.next = curr.next 
        curr = None
        



my_list = linked_list()
my_list.append_back('A')
my_list.append_back('B')
my_list.append_back('C')
my_list.append_back('D')
my_list.append_back('E')
my_list.append_back('F')
my_list.append_back('G')
my_list.append_back('H')
my_list.display()
print("list length: %d" % my_list.length())
my_list.append_front('Z')
my_list.display()
print("list length after append: %d" % my_list.length())
my_list.display()
print(my_list.get(1))
my_list.append_back('I')
my_list.display()
print("list length after append: %d" % my_list.length())
print(my_list.get(0))
my_list.append_back('J')
my_list.display()
print("list length after append: %d" % my_list.length())
print(my_list.get(10))
my_list.erase('A')
my_list.erase_index(0)
my_list.display()