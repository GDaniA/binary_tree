class Node:
    def _init_(self, value: int):
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None

    def _str_(self): #En lugar de dar la direccion de memoria da el valor
        return str(self.value)

    def is_leaf(self): #veirficamos que no sea una hoja
        return self.left is None and self.right is None