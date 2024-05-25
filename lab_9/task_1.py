import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def insert(self, root, value):
        #implement the following method
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        return self.rotation(root,value)


    def rotation(self,root,value):
         #implement the following method
        

        balance = self.balance_factor(root)


        if balance > 1 and value < root.left.value:
            return self.rotation_ll(root)
        if balance < -1 and value > root.right.value:
            return self.rotation_rr(root)
        if balance > 1 and value > root.left.value:
            return self.rotation_lr(root)
        if balance < -1 and value < root.right.value:
            return self.rotation_rl(root)

        return root

    def balance_factor(self, node):
         #implement the following method
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotation_ll(self, z):
         #implement the following method
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def rotation_rr(self, z):
         #implement the following method
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def rotation_lr(self, z):
         #implement the following method
        z.left = self.rotation_rr(z.left)
        return self.rotation_ll(z)

    def rotation_rl(self, z):
         #implement the following method
        z.right = self.rotation_ll(z.right)
        return self.rotation_rr(z)

    def inorder(self, p):
        if p.left:
            self.inorder(p.left)
        print(p.value, end=" ")
        if p.right:
            self.inorder(p.right)

    def inorder_traversal(self):
        if self.root:
            self.inorder(self.root)

    def getHeight(self):
        return self.calculateHeight(self.root)

    def calculateHeight(self, root):
        if root is None:
            return 0
        lh = self.calculateHeight(root.left)
        rh = self.calculateHeight(root.right)
        return max(lh, rh) + 1

# Test your code using the following driver code
# Creating AVL and inserting random values
tree = AVL()
for _ in range(500):
    val = random.randint(10, 2000)
    tree.insert_value(val)

print("Height:", tree.getHeight())
print("\nIn Order:\t", end="")
tree.inorder_traversal()