# https://www.youtube.com/watch?v=vHKzIPwWQkg&t=150s&ab_channel=Cl%C3%A9mentMihailescu


def reverseLinkedList(head):
    # new_head = LinkedList(head.value)
    # a -> b -> c -> d -> None
    # d -> c -> b -> a -> None

    if head.next is None:
        return head
    else:
        preious_node = head.next  # b
        tmp_node = head.next.next  # c
        head.next = None  # a -> None
        preious_node.next = head  # b -> a
        next_node = tmp_node  # cur = c

    while True:
        temp_node = next_node.next  # d
        next_node.next = preious_node  # c -> b
        preious_node = next_node  # prev = c
        if not temp_node:
            break
        next_node = temp_node

    return next_node


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print_linking(self):
        node = self
        while node is not None:
            print(f"{node.value} -> ", end="")
            node = node.next
        print("None")


if __name__ == "__main__":
    a = LinkedList("a")
    b = LinkedList("b")
    c = LinkedList("c")
    d = LinkedList("d")
    e = LinkedList("e")
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    reversed_head = reverseLinkedList(a)
    reversed_head.print_linking()
