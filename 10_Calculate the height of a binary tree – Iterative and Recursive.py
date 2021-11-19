from collections import deque
 
 
# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.key = data
        self.left = left
        self.right = right
 
 
# Iterative function to calculate the height of a given binary tree
# by doing level order traversal on the tree
def height(root):
 
    # empty tree has a height of 0
    if root is None:
        return 0
 
    # create an empty queue and enqueue the root node
    queue = deque()
    queue.append(root)
    height = -1
    # print(queue[0].key)
    # loop till queue is empty
    while queue:
 
        # calculate the total number of nodes at the current level
        size = len(queue)
        #print("size",size)
        # process each node of the current level and enqueue their
        # non-empty left and right child
        while size > 0:
            front = queue.popleft()
            #print("front",front.key)
            if front.left:
                #print("left_key",front.left.key)
                queue.append(front.left)
 
            if front.right:
                #print("right_key",front.right.key)
                queue.append(front.right)
 
            size = size - 1
 
        # increment height by 1 for each level
        height = height + 1
 
    return height

root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
 
print("The height of the binary tree is", height(root)) 