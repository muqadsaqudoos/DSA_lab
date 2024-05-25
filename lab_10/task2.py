import math

class Student:
    def __init__(self, value):
        self.value = value

class StudentMaxHeap:
    def __init__(self, size):
        self.maxSize = size # Maximum number of students that can be stored in the heap
        self.currSize = 0 # Current number of students present in the heap
        self.student = [None] * size # Array of students which will be arranged like a Max Heap

    def isEmpty(self): # Checks whether the heap is empty or not
        return self.currSize == 0

    def isFull(self): # Checks whether the heap is full or not
        return self.currSize == self.maxSize

    def insert(self, student):
        if self.isFull():
            return False
        self.student[self.currSize] = student
        self._heapify_up(self.currSize)
        self.currSize += 1
        return True

    def removeBestStudent(self):
        if self.isEmpty():
            return None
        max_gcpa = self.student[0]
        self.student[0] = self.student[self.currSize - 1]
        self.student[self.currSize - 1] = None
        self.currSize -= 1
        self._heapify_down(0)
        return max_gcpa

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.student[index].value > self.student[parent].value:
                self.student[parent], self.student[index] = self.student[index], self.student[parent]
                index = parent
            else:
                break

    def _heapify_down(self, index):
        while 2 * index + 1 < self.currSize:
            left = 2 * index + 1
            right = 2 * index + 2
            max_index = index

            if left < self.currSize and self.student[left].value > self.student[max_index].value:
                max_index = left
            if right < self.currSize and self.student[right].value > self.student[max_index].value:
                max_index = right
            if max_index != index:
                self.student[index], self.student[max_index] = self.student[max_index], self.student[index]
                index = max_index
            else:
                break

def main():
    def maxProduct(l):
        if len(l) < 2:
            return 0

        a = StudentMaxHeap(len(l))
        for num in l:
            a.insert(Student(num))

        i = a.removeBestStudent().value
        j = a.removeBestStudent().value
        return (i - 1) * (j - 1)

    nums = [3,4,5,2]
    print(maxProduct(nums))

main()
