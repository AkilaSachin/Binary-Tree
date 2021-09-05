# Creating the Binary node class
class binaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Adding new child to node
    def addChild(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = binaryNode(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = binaryNode(data)

    # In-Order Traversal method / Left, Root, Right Traversal (Remember "In-Order" means root is in between Left and Right)
    def inOrderTraversal(self):
        nodes = []

        if self.left:
            nodes += self.left.inOrderTraversal()

        nodes.append(self.data)

        if self.right:
            nodes += self.right.inOrderTraversal()

        return nodes

    # Pre-Order Traversal method / Root, Left, Right Traversal (Remember "Pre-Order" means root is in before the Left and Right)
    def preOrderTraversal(self):
        nodes = []

        nodes.append(self.data)

        if self.left:
            nodes += self.left.preOrderTraversal()

        if self.right:
            nodes += self.right.preOrderTraversal()

        return nodes

    # Post-Order Traversal method / Left, Right, Root Traversal (Remember "Post-Order" means root is in after the Left and Right)
    def postOrderTraversal(self):
        nodes = []

        if self.left:
            nodes += self.left.postOrderTraversal()

        if self.right:
            nodes += self.right.postOrderTraversal()

        nodes.append(self.data)

        return nodes

    #Searching a value in the Tree
    def search(self, val):
        if self.data == val:
            return True

        if self.data > val:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if self.data < val:
            if self.right:
                return self.right.search(val)
            else:
                return False

    # Finding the minimum value in the tree
    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self.data

    # Finding the Maximum value in the tree
    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self.data

    # Calculating the Sum of all nodes in the tree
    def sum(self):
        sum = 0

        if self.left:
            sum += self.left.sum()

        if self.right:
            sum += self.right.sum()

        sum += self.data
        return sum

    # Deleting a node in the tree
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            minVal = self.right.min()
            self.data = minVal
            self.right = self.right.delete(minVal)

        return self

# Building the tree
def buildTree(values):
    root = binaryNode(values[0])

    for i in range(1, len(values)):
        root.addChild(values[i])

    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    tree = buildTree(numbers)

    print(tree.inOrderTraversal())
    print(tree.preOrderTraversal())
    print(tree.postOrderTraversal())

    print(tree.search(17))
    print(tree.search(1000))

    print(tree.min())
    print(tree.max())
    print(tree.sum())

    tree.delete(20)
    print(tree.inOrderTraversal())

    tree.delete(9)
    print(tree.inOrderTraversal())
