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

    def len(self):
        '''
            Returns length of the queue
        '''
        return len(self._queue)

    def show(self):
        '''
            Returns list representation of the
            items in queue
        '''
        return list(self._queue)


myQueue = Queue()

myQueue.enqueue('Rex')
myQueue.enqueue('Fives')
myQueue.enqueue('Echo')
myQueue.enqueue('Hevy')
myQueue.enqueue('Cody')

print(myQueue.show())

print(myQueue.dequeue()) # Rex
print(myQueue.dequeue()) # Fives
print(myQueue.dequeue()) # Echo
print(myQueue.dequeue()) # Hevy

