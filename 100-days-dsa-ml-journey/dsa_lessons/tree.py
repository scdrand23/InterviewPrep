from logging import RootLogger


class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 


"""
   0 
  / \
 1   2

"""
root = TreeNode(0)
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
root.left = one 
root.right = two 
one.left = three

def print_tree_dfs(node):

    if not node:
        return 

    print(f"===== Node: {node.val} =====")
    print_tree_dfs(node.left)
    print_tree_dfs(node.right)

print(" Tree InOrder Traversal")
print_tree_dfs(root)


def depth(node):
    if not node:
        return 0 

    return 1 + max(depth(node.left), depth(node.right))

print(" Depth ")
print(f" d = {depth(root)} " ) 



