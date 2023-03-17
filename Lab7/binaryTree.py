class node:
    '''Node for use with binary tree'''

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
        self.counter = 0


class binaryTree:
    def __init__(self):
        self.capacity = 15
        self.size = 0
        self.root = node(None)

    def add_Node(self, value):
        if self.size == self.capacity:
            raise IndexError("Binary Tree Is Full!")
        else:
            leafFound = False
            new_Node = node(value)
            self.size += 1
            if self.root.item == None:
                self.root = new_Node
            else:
                current_Node = self.root
                while leafFound == False:
                    if current_Node.left is None or current_Node.right is None:
                        leafFound = True
                        if new_Node.item < current_Node.item:
                            current_Node.left = new_Node
                        elif new_Node.item > current_Node.item:
                            current_Node.right = new_Node
                    elif new_Node.item < current_Node.item:
                        current_Node = current_Node.left
                    elif new_Node.item > current_Node.item:
                        current_Node = current_Node.right
        return True


def preorder_recursive(currentTreeRoot, intList):
    if currentTreeRoot:
        # print root of current tree being passed
        # print(currentTreeRoot.item)
        intList.append(currentTreeRoot.item)
        # Pass left and right subtree roots to print out the roots of each tree
        preorder_recursive(currentTreeRoot.left, intList)
        preorder_recursive(currentTreeRoot.right, intList)
    return intList


def inorder_recursive(currentTreeRoot, intList):
    if currentTreeRoot:
        # Pass left and right subtree roots to print out the roots of each tree
        inorder_recursive(currentTreeRoot.left, intList)
        intList.append(currentTreeRoot.item)
        inorder_recursive(currentTreeRoot.right, intList)
        # print root of current tree being passed
    return intList


def postorder_recursive(currentTreeRoot, intList):
    if currentTreeRoot:
        # Pass left and right subtree roots to print out the roots of each tree
        postorder_recursive(currentTreeRoot.left, intList)
        postorder_recursive(currentTreeRoot.right, intList)
        # print root of current tree being passed
        intList.append(currentTreeRoot.item)
    return intList


def preorder_iteration(currentTreeRoot, intList):
    numStack = []
    numStack.append(currentTreeRoot)
    #Check that numstack is not empty
    while numStack:
        currentTreeRoot = numStack.pop()
        intList.append(currentTreeRoot.item)
        if currentTreeRoot.right:
            numStack.append(currentTreeRoot.right)
        if currentTreeRoot.left:
            numStack.append(currentTreeRoot.left)
    return intList


def inorder_iteration(currentTreeRoot, intList):
    nodeStack = []
    while True:
        if currentTreeRoot:
            nodeStack.append(currentTreeRoot)
            currentTreeRoot = currentTreeRoot.left
        elif currentTreeRoot is None and nodeStack:
            currentTreeRoot = nodeStack.pop()
            intList.append(currentTreeRoot.item)
            currentTreeRoot = currentTreeRoot.right
        #If there are no more nodes in the stack
        else:
            break
    return intList


def postorder_iteration(currentTreeRoot, intList):
    nodeStack = []
    nodeStack.append(currentTreeRoot)
    while nodeStack:
        currentTreeRoot = nodeStack.pop()
        intList.append(currentTreeRoot.item)
        if currentTreeRoot.left:
            nodeStack.append(currentTreeRoot.left)
        if currentTreeRoot.right:
            nodeStack.append(currentTreeRoot.right)
    return intList[::-1]

