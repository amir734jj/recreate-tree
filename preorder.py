from node import Node
from utility import peak, push, pop


def pre_order_calc(l):
    st = list()

    root = Node()
    root.value = l[0]
    push(st, root)

    for i in range(1, len(l)):
        temp = None

        while len(st) > 0 and l[i] > peak(st).value:
            temp = pop(st)

        if temp is not None:
            temp.right = Node()
            temp.right.value = l[i]

            push(st, temp.right)
        else:
            temp = peak(st)
            temp.left = Node()
            temp.left.value = l[i]

            push(st, temp.left)

    return root