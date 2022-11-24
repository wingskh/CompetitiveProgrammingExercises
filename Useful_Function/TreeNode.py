class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_treenode(elements):
    root_node = TreeNode(val=elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = i % 2 == 0
        node = TreeNode(val=x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node
