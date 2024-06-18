class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def createQST(keys):
    counter = 0
    root = None
    for key in keys:
        if root:
            counter = insert(root,key,counter)
        else:
            root = Node(key)
        print(counter)
    return root

def insert(root, val, counter):
    counter += 1
    if not root:
        root = Node(val)
    else:
        if root.val > val:
            insert(root.left, val, counter)
        else:
            insert(root.right, val, counter)
    return counter

def in_order_print(root):
    if not root:
        return
    in_order_print(root.left)
    print (root.val)
    in_order_print(root.right)

def pre_order_print(root):
    if not root:
        return        
    print (root.val)
    pre_order_print(root.left)
    pre_order_print(root.right)    

