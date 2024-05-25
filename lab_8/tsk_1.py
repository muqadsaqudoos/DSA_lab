class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def set_value(self, value):
        self.value = value
    def set_left(self, left):
        self.left = left
    def set_right(self, right):
        self.right = right
    def get_value(self):
        return self.value
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_element_root(self, value):
        self.root = Node(value)

    def insert_left_child(self, parent, value):
        if parent is None:
            return "Parent node does not exist"
        parent.left = Node(value)

    def insert_right_child(self, parent, value):
        if parent is None:
            return "Parent node does not exist"
        parent.right = Node(value)
    
    def delete_element(self, value):
        def delete_node(root, key):
            if root is None:
                return root

            if key < root.value:
                root.left = delete_node(root.left, key)
            elif key > root.val:
                root.right = delete_node(root.right, key)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left

                root.value = self.min_value(root.right)
                root.right = delete_node(root.right, root.value)

            return root

        self.root = delete_node(self.root, value)

    def display_pre_order(self, node): 
        if node:
            print(node.value, end=" ")
            self.display_pre_order(node.left)
            self.display_pre_order(node.right)

    def display_in_order(self, node):
        if node:
            self.display_in_order(node.left)
            print(node.value, end=" ")
            self.display_in_order(node.right)

    def display_post_order(self, node): 
        if node:
            self.display_post_order(node.left)
            self.display_post_order(node.right)
            print(node.value, end=" ")

    def count_nodes(self, node): 
        if node is None:
            return 0 
        left = self.count_nodes(node.left)
        right = self.count_nodes(node.right)
        return 1 + left + right
        
    def min_value(self, node):
        if node is None:
            return None
        left_min = self.min_value(node.left)
        right_min = self.min_value(node.right)
        if left_min is None and right_min is None:
            return node.value
        min_val = node.value
        if left_min is not None:
            min_val = min(min_val, left_min)
        if right_min is not None:
            min_val = min(min_val, right_min)
        return min_val
        
    def count_leaf_nodes(self, node): 
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)
        
    def non_rec_pre_order(self):
        if self.root is None:
            return 
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.value, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def non_rec_post_order(self):
        if self.root is None:
            return 
        root = self.root
        stack = []
        result = []
        while root or stack:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            root = stack.pop()
            if stack and stack[-1] == root.right:
                stack.pop()
                stack.append(root)
                root = root.right
            else:
                result.append(root.value)
                root = None
        return result

    def non_rec_in_order(self): 
        stack = []
        current = self.root
        while True:
            while current:
                stack.append(current)
                current = current.left
            if not stack:
                break
            current = stack.pop()
            print(current.value, end=" ")
            current = current.right

    def find_balance_factor(self, node):
        if node is None:
            return 0

        def calculate_height(node):
            if node is None:
                return 0
            return 1 + max(calculate_height(node.left), calculate_height(node.right))

        left_height = calculate_height(node.left)
        right_height = calculate_height(node.right)
        balance_factor = left_height - right_height
        return balance_factor
    
    def display_ancestors(self, node_data):
        def find_ancestors(root, target, ancestors):
            if root is None:
                return False
            if root.value == target:
                return True
            if find_ancestors(root.left, target, ancestors) or find_ancestors(root.right, target, ancestors):
                ancestors.append(root.value)
                return True
            return False
        
        ancestors = []
        find_ancestors(self.root, node_data, ancestors)

        if ancestors:
            for ancestor in ancestors:
                print(ancestor, end=" ")

    def display_descendants(self, node_data): 
        def helper_descendants(node, target):
            if node is None:
                return []
            if node.value == target:
                return [node.value]  
            left_descendants = helper_descendants(node.left, target)
            right_descendants = helper_descendants(node.right, target)
            if left_descendants or right_descendants:
                return [node.value] + left_descendants + right_descendants
            return []

        descendants = helper_descendants(self.root, node_data)

        if descendants:
            for descendant in descendants:
                print(descendant, end=" ")

    def height_of_tree(self):
        def helper_height(node):
            if node is None:
                return 0
            left_height = helper_height(node.left)
            right_height = helper_height(node.right)
            return max(left_height, right_height) + 1
        return helper_height(self.root)