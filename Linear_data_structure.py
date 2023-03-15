class Node:

    def __init__(self, data=None):

        self.data = data

        self.next = None

def delete_zero_sum(head):

    prefix_sum = 0

    node_map = {}

    temp = head

    while temp:

        prefix_sum += temp.data

        if prefix_sum == 0 or prefix_sum in node_map:

            if prefix_sum == 0:

                head = temp.next

            else:

                node_map[prefix_sum].next = temp.next

            prefix_sum = 0

            node_map = {}

            temp = head

        else:

            node_map[prefix_sum] = temp

            temp = temp.next

    return head

