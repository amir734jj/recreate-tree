def print_tree(p):
    if not p:
        return
    print('[', end='')
    print_tree(p.left)
    print(" %s " % p.value, end='')
    print_tree(p.right)
    print(']', end='')
