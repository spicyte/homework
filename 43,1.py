class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if key < root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def deleteNode(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.minValueNode(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        return root

    def insertNode(self, key):
        self.root = self.insert(self.root, key)

    def delete(self, key):
        self.root = self.deleteNode(self.root, key)

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.val, end=' ')
            self.inorderTraversal(root.right)

if __name__ == "__main__":
    tree = BinaryTree()
    tree.insertNode(50)
    tree.insertNode(30)
    tree.insertNode(20)
    tree.insertNode(40)
    tree.insertNode(70)
    tree.insertNode(60)
    tree.insertNode(80)

    print("Binary tree inorder traversal:")
    tree.inorderTraversal(tree.root)
    print()

    print("Delete 20:")
    tree.delete(20)
    tree.inorderTraversal(tree.root)
    print()

    print("Delete 30:")
    tree.delete(30)
    tree.inorderTraversal(tree.root)
    print()

    print("Delete 50:")
    tree.delete(50)
    tree.inorderTraversal(tree.root)
    print()
