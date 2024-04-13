# Узел связанного списка
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Функция обнаружения цикла в связанном списке с использованием
# Алгоритм определения цикла Флойда
def detectCycle(head):
    # принимает две ссылки — `slow` и `fast`.
    slow = fast = head

    while fast and fast.next:

        # двигаться медленнее на один
        slow = slow.next

        # двигаться быстрее на два
        fast = fast.next.next

        # , если они встречаются с любым узлом, связанный список содержит цикл
        if slow == fast:
            return True

    # мы достигаем здесь, если медленное и быстрое не встречаются
    return False


if __name__ == '__main__':

    head = None
    for i in reversed(range(5)):
        head = Node(i + 1, head)

    # Цикл вставки
    head.next.next.next.next.next = head.next.next

    if detectCycle(head):
        print('Cycle Found')
    else:
        print('No Cycle Found')
