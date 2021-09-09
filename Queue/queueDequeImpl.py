# Queue implementation using collections.deque
from collections import deque


class Queue:
    '''
        Simple Queue implementation with deque
    '''

    def __init__(self) -> None:
        self._queue = deque()

    def enqueue(self, item):
        '''
            Enqueue item in queue
        '''
        if item:
            self._queue.append(item)
        return self

    def dequeue(self):
        '''
            Dequeue item from queue
        '''
        return self._queue.popleft()

    def contains(self, item):
        '''
            Checks if item exists in queue
        '''
        return item in self._queue

    def __len__(self):
        '''
            Returns length of the queue
        '''
        return len(self._queue)

    def __repr__(self):
        '''
            Returns list representation of the
            items in queue
        '''
        return ','.join(list(self._queue))


myQueue = Queue()

myQueue.enqueue('Rex')
myQueue.enqueue('Fives')
myQueue.enqueue('Echo')
myQueue.enqueue('Hevy')
myQueue.enqueue('Cody')

print(myQueue)  # Rex,Fives,Echo,Hevy,Cody

print(len(myQueue))  # 5

print(myQueue.contains('Hevy'))  # True
print(myQueue.contains('Wrecker'))  # False

print(myQueue.dequeue())  # Rex
print(myQueue.dequeue())  # Fives
print(myQueue.dequeue())  # Echo
print(myQueue.dequeue())  # Hevy

print(myQueue)  # Cody
