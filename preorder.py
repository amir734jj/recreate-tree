from node import Node


def pre_order_calc(l):
    st = list()

    root = Node()
    root.value = l[0]
    st.append(root)

    for i in range(1, len(l)):
        temp = None

        while len(st) > 0 and l[i] > st[len(st) - 1].value:
            temp = st.pop()

        if temp is not None:
            temp.right = Node()
            temp.right.value = l[i]
            st.append(temp.right)
        else:
            temp = st[len(st) - 1]
            temp.left = Node()
            temp.left.value = l[i]

            st.append(temp.left)

    return root