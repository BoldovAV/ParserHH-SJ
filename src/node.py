class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.tail = Node(None, None)
        self.head = Node(None, self.tail)

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с
         этими данными в начало связанного списка"""
        self.head = Node(data, self.head)
        if self.tail.data is None:
            self.tail = self.head

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел
         с этими данными в конец связанного списка"""
        new_data = Node(data, None)
        self.tail.next_node = new_data
        self.tail = new_data
        if self.head.data is None:
            self.head = self.tail

    def __str__(self) -> str:

        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node.data is None:
            return str(None)

        ll_string = ''
        while node:
            if not node.data:
                break
            ll_string += f'{str(node.data)}\n'
            node = node.next_node

        ll_string += 'None'
        return ll_string
