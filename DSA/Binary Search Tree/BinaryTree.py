class BST:
    def __init__(self,element):
        self.left = None
        self.right = None
        self.value = element

    def insert(self,data):
        if data < self.value:
            if self.left is None:
                self.left = BST(data)
            else:
                self.left.insert(data)

        else:
            if self.right is None:
                self.right = BST(data)
            else:
                self.right.insert(data) 

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.inorder_traversal()
        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        if self.right:
            self.right.inorder_traversal()
        print(self.value)

bst = BST(10)
bst.insert(2)
bst.insert(5)

print(bst.left.right.value)