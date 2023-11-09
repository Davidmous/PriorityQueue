class QueueList:
    def __init__(self):
        self.data = []
        self.priority = []

    def enqueue(self, value, priority):
        index = 0
        for i in range(0, len(self.priority)):
            if priority < self.priority[i]:
                break
            index += 1
        self.data.insert(index, value)
        self.priority.insert(index, priority)

    def dequeue(self):
        return self.data.pop(0)

    def front(self):
        return self.data[0]

    def clear(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __str__(self):
        output = ""
        for item in self.data:
            output = output + str(item) + " "
        return output


class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None


class SLNC:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def delete_head(self):
        hapus = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        del hapus

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            if new_node.priority < self.head.priority:
                new_node.next = self.head
                self.head = new_node
            elif new_node.priority >= self.tail.priority:
                self.tail.next = new_node
                self.tail = new_node
            else:
                helper = self.head
                while helper.priority < new_node.priority:
                    helper = helper.next
                helper2 = self.head
                while helper2.next != helper:
                    helper2 = helper2.next
                new_node.next = helper2.next
                helper2.next = new_node
        self.size += 1


class QueueLinkedList:
    def __init__(self):
        self.queue_data = SLNC()

    def enqueue(self, value, priority):
        self.queue_data.insert(value, priority)

    def dequeue(self):
        value = self.queue_data.head.data
        self.queue_data.delete_head()
        return value

    def front(self):
        return self.queue_data.head.data

    def clear(self):
        self.queue_data = SLNC()

    def __len__(self):
        return len(self.queue_data.size)

    def __str__(self):
        output = ""
        helper = self.queue_data.head
        while helper != None:
            output = output + str(helper.data) + " "
            helper = helper.next
        return output


queue = QueueLinkedList()
queue.enqueue(30, 5)  # 30
queue.enqueue(50, 3)  # 50 30
queue.enqueue(10, 4)  # 50 10 30
queue.enqueue(40, 1)
queue.enqueue(70, 5)
print(queue)  # 40 50 10 30 70
