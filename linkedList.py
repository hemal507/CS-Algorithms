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

    def get_element_at_index(self, position):
        if position >= self.length():
            print('Linked list length is less than the requested position; No action is taken')
            return None
        curr_node = self.head
        i = 0
        while i <= position:
            curr_node = curr_node.next
            i += 1
        return curr_node.data

    def delete_at_index(self, position):
        if position >= self.length():
            print('Linked likst length is less than the requested position; No action is taken')
            return None
        curr_node = self.head
        i = 0
        while i < position:
            curr_node = curr_node.next
            i += 1
        print('element to be deleted is ', curr_node.data)
        curr_node.next = curr_node.next.next


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
    print(ll.get_element_at_index(5))
    ll.delete_at_index(4)
    ll.print_elements()
