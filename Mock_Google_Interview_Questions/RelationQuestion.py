# https://www.youtube.com/watch?v=V0xjK_6ZoEY&t=612s&ab_channel=KeepOnCoding
def dfs(node, level, map_to_children):
    print(f"{level}:" + "  " * level + node)

    if node in map_to_children:
        children_nodes = map_to_children[node]
        for child in children_nodes:
            dfs(child, level + 1, map_to_children)

def printTree(relation_list):
    map_to_children = dict()
    non_child_node = set()

    for parent, child in relation_list:
        if parent not in map_to_children:
            map_to_children[parent] = []

        map_to_children[parent].append(child)

    non_child_node = set(map_to_children.keys())

    for _, child in relation_list:
        if child in non_child_node:
            non_child_node.remove(child)

    dfs(non_child_node.pop(), 1, map_to_children)


def main():
    relation_list = []
    relation_list.append(["animal", "mamal"])
    relation_list.append(["animal", "bird"])
    relation_list.append(["lifeform", "animal"])
    relation_list.append(["cat", "lion"])
    relation_list.append(["mamal", "cat"])
    relation_list.append(["animal", "fish"])

    printTree(relation_list)


if __name__ == "__main__":
    main()
