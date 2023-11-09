class QueueList:
    def __init__(self):
        self.data = []
        self.priority = []

    def enqueue(self, value, priority):
        self.data.append(value)
        self.priority.append(priority)

    def dequeue(self):
        index = 0
        min_priority = 9999
        for i in range(0, len(self.priority)):
            if self.priority[i] < min_priority:
                index = i
                min_priority = self.priority[i]
        value = self.data[index]
        del self.data[index]
        del self.priority[index]
        return value

    def front(self):
        index = 0
        min_priority = 9999
        for i in range(0, len(self.priority)):
            if self.priority[i] < min_priority:
                index = i
                min_priority = self.priority[i]
        value = self.data[index]
        return value

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

    def delete(self):
        if self.size == 1:
            hapus = self.head
            value = self.head.data
            self.head = None
            self.tail = None
        else:
            helper = self.head
            hapus = self.head
            while helper.next != None:
                if helper.priority < hapus.priority:
                    hapus = helper
                helper = helper.next

            value = hapus.data
            if hapus == self.head:
                self.head = self.head.next
            elif hapus == self.tail:
                helper = self.head
                while helper.next != self.tail:
                    helper = helper.next
                helper.next = None
                self.tail = helper
            else:
                helper = self.head
                while helper.next != hapus:
                    helper = helper.next
                helper.next = hapus.next
        self.size -= 1
        del hapus
        return value

    def front(self):
        if self.size == 1:
            hapus = self.head
            value = self.head.data
        else:
            helper = self.head
            hapus = self.head
            while helper.next != None:
                if helper.priority < hapus.priority:
                    hapus = helper
                helper = helper.next
            value = hapus.data
        self.size -= 1
        return value

    def insert_tail(self, value, priority):
        new_node = Node(value, priority)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1


class QueueLinkedList:
    def __init__(self):
        self.queue_data = SLNC()

    def enqueue(self, value, priority):
        self.queue_data.insert_tail(value, priority)

    def dequeue(self):
        return self.queue_data.delete()

    def front(self):
        return self.queue_data.front()

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
queue.enqueue(40, 1)  # 40 50 10 30
queue.enqueue(70, 5)  # 40 50 10 30 70
print(queue.dequeue())  # 40
print(queue.dequeue())  # 50
print(queue.dequeue())  # 10
print(queue.dequeue())  # 30
print(queue.dequeue())  # 70
