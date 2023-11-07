class BinarySearchTree:
    # initializes a new node in the binary search tree (BST) with the specified value (val).
    # It also initializes the left and right child nodes as None.
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

    # nodes with values less than the current node are placed in the left subtree, 
    # and nodes with values greater than the current node are placed in the right subtree. 
    # The method recursively inserts the node in the appropriate subtree.
    def insert_node(self, data):
        if data < self.value:
            if self.left is None:
                self.left = BinarySearchTree(data)
            else:
                self.left.insert_node(data)
        else:
            if self.right is None:
                self.right = BinarySearchTree(data)
            else:
                self.right.insert_node(data) 

    # the nodes of the tree are visited in ascending order. 
    # It recursively traverses the left subtree, then visits the current node, 
    # and finally, recursively traverses the right subtree.
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    # to find the node with the minimum value in the current BST. 
    def find_min_node(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
    
    # If the node to be deleted has no children, it is simply removed.
    # If the node has one child, the node is replaced by its child.
    # If the node has two children, it is replaced by the node with the minimum value in its right subtree.
    # After deleting the node, the method returns the modified BST.
    def delete_node(self, key):
        if self is None:
            return self

        if key < self.value:
            self.left = self.left.delete_node(key)
        elif key > self.value:
            self.right = self.right.delete_node(key)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            temp = self.right.find_min_node()
            self.value = temp.value
            self.right = self.right.delete_node(temp.value)
        return self
    
    # for deleting a node with the specified value (item).
    # It calls the delete_node method to perform the deletion.
    def delete_element(self, item):
        self.delete_node(item)

    # delete the node with the maximum value in the BST and return the deleted value. 
    # It iteratively traverses the right subtree until it reaches the rightmost node,
    # which has the maximum value, and then deletes that node.
    def delete_max_value(self):
        if self.right is None:
            max_val = self.value
            if self.left:
                return self.left, max_val
            return None, max_val
        else:
            self.right, max_val = self.right.delete_max_value()
            return self, max_val
        
    # delete the node with the minimum value in the BST and return the deleted value.
    # It uses the find_min_node method to locate the leftmost node in the BST and then deletes that node.
    def delete_min_value(self):
        if self.left is None:
            min_val = self.value
            if self.right:
                return self.right, min_val
            return None, min_val
        else:
            self.left, min_val = self.left.delete_min_value()
            return self, min_val

    # recursively search the left or right subtrees, depending on the value being searched for.
    # If the value is found, the method returns True; otherwise, it returns False.
    def search_element(self, item):
        if item == self.value:
            return True
        elif item < self.value and self.left:
            return self.left.search_element(item)
        elif item > self.value and self.right:
            return self.right.search_element(item)
        return False

    # It recursively searches the BST for the node with the target value and 
    # keeps track of the parent node while traversing. If the value is found, 
    # it returns the parent node; otherwise, it returns None.
    def get_parent(self, item, parent=None):
        if item == self.value:
            return parent
        elif item < self.value and self.left:
            return self.left.get_parent(item, self)
        elif item > self.value and self.right:
            return self.right.get_parent(item, self)
        return None

# Create a modified BST
root = BinarySearchTree(10)
root.insert_node(5)
root.insert_node(15)
root.insert_node(3)
root.insert_node(8)
root.insert_node(12)
root.insert_node(18)

# Display the initial tree using inorder traversal
print("Initial Tree (Inorder Traversal):")
root.inorder_traversal()
print()

# Delete a specific item from the tree
print("Deleting Specific Item")
root.delete_element(5)
print("After deleting 5 (Inorder Traversal):")
root.inorder_traversal()
print()

# Delete the maximum value and get the deleted item
print("Deleting Maximum Item")
root, deleted_max = root.delete_max_value()
print(f"Deleted Maximum Value: {deleted_max}")
print("After deleting the maximum (Inorder Traversal):")
root.inorder_traversal()
print()

# Delete the minimum value and get the deleted item
print("Deleting Minimum Item")
root, deleted_min = root.delete_min_value()
print(f"Deleted Minimum Value: {deleted_min}")
print("After deleting the minimum (Inorder Traversal):")
root.inorder_traversal()
print()

# Search for a specific item
print("Searching for an Item")
item_to_search = 12
found = root.search_element(item_to_search)
if found:
    print(f"{item_to_search} found in the tree.")
else:
    print(f"{item_to_search} not found in the tree.")
print()

# Get the parent of a specific item
print("Getting Parent of an Item")
item_to_find_parent = 12
parent = root.get_parent(item_to_find_parent)
if parent:
    print(f"Parent of {item_to_find_parent}: {parent.value}")
else:
    print(f"{item_to_find_parent} has no parent in the tree.")
