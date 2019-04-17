class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None
  
    # Function to reverse the linked list 
    def reverse(self): 
		curr_node = self.head
    	prev_node = None
    	while curr_node:
    		next_node = curr.next
    		curr_node.next = prev_node
    		prev_node = curr_node
    		curr_node = next_node
    	self.head = prev_node
    	

          
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
    	new_node = Node(new_data)
    	new_node.next = self.head
    	self.head = new_node
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while temp: 
            print(temp.data, end ="->") 
            temp = temp.next