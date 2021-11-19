class Node:
    def __init__(self,parent):
        self.parent = parent
        self.left = None
        self.right = None

def Insert(node,Data):
    if node is None:
            return Node(Data)
        
    elif Data<node.parent:
        node.left = Insert(node.left,Data)

    else:
        node.right = Insert(node.right,Data)
        
    return node
 
            
def Inorder(data):
    if data:
        Inorder(data.left)
        print(data.parent,"->",end=' ')
        Inorder(data.right)
 
root = None
root = Insert(root, 8)
root = Insert(root, 3)
root = Insert(root, 1)
root = Insert(root, 6)
root = Insert(root, 7)

Inorder(root)