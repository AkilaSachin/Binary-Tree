class binaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

    def inOrderTravesal(self):
        nodes = []

        if self.left:
            nodes += self.left.inOrderTravesal()

        nodes.append(self.data)

        if self.right:
            nodes += self.right.inOrderTravesal()

        return nodes

    def preOrderTravesal(self):
        nodes = []

        nodes.append(self.data)

        if self.left:
            nodes += self.left.preOrderTravesal()

        if self.right:
            nodes += self.right.preOrderTravesal()

        return nodes

    def postOrderTravesal(self):
        nodes = []

        if self.left:
            nodes += self.left.postOrderTravesal()

        if self.right:
            nodes += self.right.postOrderTravesal()

        nodes.append(self.data)

        return nodes

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

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self.data

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self.data

    def sum(self):
        sum = 0

        if self.left:
            sum += self.left.sum()

        if self.right:
            sum += self.right.sum()

        sum += self.data
        return sum

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


def buildTree(values):
    root = binaryNode(values[0])

    for i in range(1, len(values)):
        root.addChild(values[i])

    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    tree = buildTree(numbers)

    print(tree.inOrderTravesal())
    print(tree.preOrderTravesal())
    print(tree.postOrderTravesal())

    print(tree.search(17))
    print(tree.search(1000))

    print(tree.min())
    print(tree.max())
    print(tree.sum())

    tree.delete(20)
    print(tree.inOrderTravesal())

    tree.delete(9)
    print(tree.inOrderTravesal())
