def print_tree(p):
    if not p:
        return
    print('[', end='')
    print_tree(p.left)
    print(" %s " % p.value, end='')
    print_tree(p.right)
    print(']', end='')


def push(l, v):
    l.append(v)
    return l


def pop(l):
    return l.pop()


def peak(l):
    return l[len(l) - 1]
