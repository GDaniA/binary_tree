from node import Node

class BinaryTree:
    def __init__(self):
        self.root: Node | None = None

    def append(self, value: int, ref: Node | None, side: str | None):
        new_node = Node(value)

        if ref is None:
            self.root =  new_node

        else:
            if side == 'left':
                ref.left = new_node

            elif side == 'right':
                ref.right = new_node

        return new_node

    def inorder(self) -> str:
        return f"({self.__inorder(self.root)})"

    def __inorder(self, ref: Node | None) -> str:
        if ref is None:
            return 'NULL'
        elif ref.is_leaf():
            return str(ref)

        left = self.__inorder(ref.left)
        root = str(ref)
        right = self.__inorder(ref.right)

        return f"({left}({root}){right})"



    def preorder(self) -> str:
        return self.__preorder(self.root)

    def __preorder(self, ref: Node | None)-> str:
        if ref is None:
            return 'NULL'

        result = str(ref)

        if ref.is_leaf():
            return result

        result = '('
        result += str(ref)
        result += '('
        result += self.__preorder(ref.right)
        result += ','
        result += self.__preorder(ref.left)
        result += ')'

        return result

    def postorder(self) -> str:
        return f"({self._postorder(self.root)})"

    def _postorder(self, ref: Node | None ) -> str:
        if ref is None:
            return 'NULL'

        if ref.is_leaf():
            return str(ref)

        result = '('
        result += self._postorder(ref.left)
        result += ','
        result += self._postorder(ref.right)
        result += ')'
        result += str(ref)

        return result

    def search(self, value : int) -> Node | None:
        ref = self.__search(value, self.root)
        if ref is None:
            raise Exception('EL valor no existe')

        return ref

    def __search(self, value: int, ref: Node | None) -> Node | None:
        if ref is None:
            return None

        if ref.value == value:
            return ref

        left = self.__inorder(value, ref.left)

        if left is None:
            return left

        right = self.__search(value, ref.right)
        return right