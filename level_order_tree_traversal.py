from collections import deque

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_level_order(root):
    if not root:
        return

    queue = deque()
    queue.append(root)

    while queue:
        print(queue[0].data, end=" ")
        node = queue.popleft()

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

#Driver Program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.right.right = Node(5) 
root.right.right.left = Node(4) 
root.right.right.right = Node(7) 
  
print("Level Order Traversal of binary tree is -")
print_level_order(root)
print()