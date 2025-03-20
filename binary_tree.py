from node import Node

class BinaryTree:
    def _init_(self):
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
    def preorder(self) -> str:
        return self._preorder(self.root)

    def _preorder(self, ref: Node | None)-> str:
        if ref is None:
            return 'NULL'

        result = str(ref)

        if ref.is_leaf():
            return result

        result = '('
        result += str(ref)
        result += '('
        result += self._preorder(ref.right)
        result += ','
        result += self._preorder(ref.left)
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

    def inorder(self) -> str:
        return f"({self._inorder(self.root)})"

    def _inorder(self, ref: Node | None ) -> str:
        if ref is None:
            return 'NULL'

        if ref.is_leaf():
            return str(ref)

        result = self._inorder(ref.left)
        result += '('
        result += str(ref)
        result += '('
        result += self._inorder(ref.right)
        result += ')'
        result += ')'

        return result
