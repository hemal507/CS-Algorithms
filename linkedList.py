class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list():
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def print_elements(self):
        items = []
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
            items.append(curr_node.data)
        print(items)


if __name__ == '__main__':
    ll = linked_list()
    ll.print_elements()
    ll.append(10)
    ll.print_elements()
    ll.append(20)
    ll.append(90)
    ll.append(5)
    ll.print_elements()