from utility import print_tree
from preorder import pre_order_calc


#       10
#     /   \
#   5      40
#  /  \   /  \
# 1    7 35   50
def main():
    l = [10, 5, 1, 7, 40, 35, 50]
    print_tree(pre_order_calc(l))


if __name__ == "__main__":
    main()
