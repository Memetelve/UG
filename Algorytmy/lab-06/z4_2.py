class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head

    def wstaw(self, s):
        new_node = Node(s)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node

    def drukuj(self):
        temp = self.head.next
        print("[", end="")
        while temp != self.head:
            print(temp.key, end=", ")
            temp = temp.next

        print("]")

    def szukaj(self, s):
        temp = self.head.next
        while temp != self.head:
            if temp.key == s:
                return temp
            temp = temp.next
        return None

    def usun(self, s):
        temp = self.head.next
        while temp != self.head:
            if temp.key == s:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.next = None
                temp.prev = None
                return
            temp = temp.next

    def bezpowtorzen(self):
        seen = set()
        new_list = LinkedList()
        temp = self.head.next
        while temp != self.head:
            if temp.key not in seen:
                seen.add(temp.key)
                new_list.wstaw(temp.key)
            temp = temp.next
        return new_list

    @staticmethod
    def scal(l1, l2):
        l1.head.prev.next = l2.head.next
        l2.head.next.prev = l1.head.prev
        l1.head.prev = l2.head.prev
        l2.head.prev.next = l1.head
        return l1


# Tworzymy listę
lista = LinkedList()

# Wstawiamy słowa
lista.wstaw("ala")
lista.wstaw("kot")
lista.wstaw("ala")
lista.wstaw("pies")
lista.wstaw("ryba")

# Drukujemy listę
lista.drukuj()

# Szukamy słowa "kot"
kot = lista.szukaj("kot")
print(kot.key)

# Usuwamy słowo "ala"
lista.usun("ala")
lista.drukuj()

# Tworzymy nową listę bez powtórzeń
nowa_lista = lista.bezpowtorzen()
nowa_lista.drukuj()

# Scalamy dwie listy
lista2 = LinkedList()
lista2.wstaw("kot")
lista2.wstaw("pies")
lista3 = LinkedList.scal(lista, lista2)
lista3.drukuj()
