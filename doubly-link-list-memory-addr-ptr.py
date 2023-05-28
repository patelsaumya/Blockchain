class Node:
    def __init__(self, content):
        self.prev = None
        self.next = None
        self.content = content

def add_new_node(new_node, head):
    if not head:
        head = Node(new_node.content)
        return head
    else:
        tmp = head
        while True:
            if tmp.next == None:
                tmp.next = new_node
                new_node.prev = tmp
                break
            else:
                tmp = tmp.next
        return head


def print_link_list(head):
    tmp = head
    while True:
        if tmp != None:
            print(tmp.content, end=' ')
            tmp = tmp.next
        else:
            return

head = None
while True:
    content = int(input('\nEnter the number: '))
    new_node = Node(content)
    head = add_new_node(new_node, head)
    print('List:', end=' ')
    print_link_list(head)
    is_continue = int(input('\n\nDo you want to continue? (1(Y)/0(N))'))
    if not is_continue:
        print('\nProgram Ended!!!')
        break