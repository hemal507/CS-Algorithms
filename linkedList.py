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

    def length(self):
        l = 0
        curr_node = self.head
        while curr_node.next != None:
            l += 1
            curr_node = curr_node.next
        return l

    def insert_at_index(self, data, position):
        """ considering linked list elements start position # 0 """
        new_node = node(data)
        curr_node = self.head
        i = 0
        while i < position:
            curr_node = curr_node.next
            i += 1
        new_node.next = curr_node.next
        curr_node.next = new_node

    def insert_at_index(self, data, position):
        """ considering linked list elements start position # 0 """
        new_node = node(data)
        curr_node = self.head
        i = 0
        while i < position:
            curr_node = curr_node.next
            i += 1
        new_node.next = curr_node.next
        curr_node.next = new_node


if __name__ == '__main__':
    ll = linked_list()
    ll.print_elements()
    ll.append(10)
    ll.print_elements()
    ll.append(20)
    ll.append(90)
    ll.append(5)
    ll.print_elements()
    print(ll.length())
    ll.insert_at_index(89, 3)
    ll.print_elements()
    ll.append(12)
    ll.append(14)
    ll.print_elements()
