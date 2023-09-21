class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  
        
def list_to_listnode(array):
    if len(array) == 0:
        return None
    root = ListNode(val=array[0])
    parent_node = root
    for i in array[1:]:
        cur_node = ListNode(val=i)
        parent_node.next = cur_node
        parent_node = cur_node
    return root
    
def display_listnode(root):
    result = []
    while root is not None:
        result.append(root.val)
        root = root.next
    print(result)
