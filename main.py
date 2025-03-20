from binary_tree import BinaryTree
from node import Node

def main():
    numbers = BinaryTree()
    root = numbers.append(13,None, None)
    node_19 = numbers.append(19, root, 'left')
    node_33= numbers.append(33, root,'right')
    node_15= numbers.append(15, node_33, 'left')
    node_8 = numbers.append(8, node_33,'right')


    print(numbers.preorder())
    print(numbers.postorder())
    print(numbers.inorder())


main()