class Node:
    def __init__(self, x):
        self.key = x
        self.left = None  # lewy syn
        self.right = None  # prawy syn
        self.p = None  # ojciec


class BST:
    def __init__(self):
        self.root = None

    def print(self):
        height = self.height(self.root)
        max_len = 8
        width = 140
        last_children = []
        children = [self.root]
        for level in range(1, height + 1):
            blank_space = round(
                (width - ((max_len) * 2 ** (level - 1))) / (2 ** (level - 1) + 2)
            )
            if level == 1:
                blank_space = round((width - max_len) / 2)
            blank_space *= " "

            for i, child in enumerate(children, 1):
                print(blank_space, end="")
                if (i == (len(children) / 2 + 1)) and (level != 1):
                    print(blank_space, end="")

                if child is None:
                    print(" " * max_len, end="")
                else:
                    text = str(child.key)
                    if len(text) > max_len:
                        text = text[:max_len]
                    elif len(text) < max_len:
                        text = text + " " * (max_len - len(text))
                    print(f"{text}", end="")

            print()

            children, last_children = [], children
            for child in last_children:
                if child is not None:
                    children.extend((child.left, child.right))
                else:
                    children.extend((None, None))

    def wstaw(self, z):
        if self.szukaj(z.key) is not None:
            return

        x = self.root
        y = None  # y jest ojcem x
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:  # drzewo puste
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def szukaj(self, k):
        x = self.root
        while x is not None and x.key != k:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def bstMinimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def Transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def bstDeleteC(self, z):
        if z.left is None:
            self.Transplant(z, z.right)
        elif z.right is None:
            self.Transplant(z, z.left)
        else:
            y = self.bstMinimum(z.right)
            if y.p != z:
                self.Transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.Transplant(z, y)
            y.left = z.left
            y.left.p = y

    def BSTinOrder(self, x):
        if x is None:
            return
        self.BSTinOrder(x.left)
        print(x.key)
        self.BSTinOrder(x.right)

    def height(self, x):
        if x is None:
            return 0
        else:
            return 1 + max(self.height(x.left), self.height(x.right))


with open("less.txt", "r") as f:
    text = f.read().split(" ")

    words = []

    for word in text:
        if word.isalpha():
            words.append(word.lower())

for size in [500, 1000, 2000]:
    bst = BST()
    for i in range(size):
        bst.wstaw(Node(words[i]))

    print("Size: ", size)
    print("Height: ", bst.height(bst.root))


size = 10
bst = BST()
for i in range(size):
    bst.wstaw(Node(words[20 + i]))

print("Size: ", size)
print("Height: ", bst.height(bst.root))
bst.print()
