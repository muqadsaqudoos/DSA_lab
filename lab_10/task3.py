
class Student:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

class StudentMaxHeap:
    def __init__(self, size):
        self.maxSize = size
        self.currSize = 0
        self.student = [None] * size

    def isEmpty(self):
        return self.currSize == 0

    def isFull(self):
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
        max_student = self.student[0]
        self.student[0] = self.student[self.currSize - 1]
        self.student[self.currSize - 1] = None
        self.currSize -= 1
        self._heapify_down(0)
        return max_student


    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.student[index].freq > self.student[parent].freq:
                self.student[parent], self.student[index] = self.student[index], self.student[parent]
                index = parent
            else:
                break

    def _heapify_down(self, index):
        while 2 * index + 1 < self.currSize:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < self.currSize and self.student[left].freq > self.student[largest].freq:
                largest = left
            if right < self.currSize and self.student[right].freq > self.student[largest].freq:
                largest = right

            if largest != index:
                self.student[largest], self.student[index] = self.student[index], self.student[largest]
                index = largest
            else:
                break



def sortCharacter(s):
    d = {}
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    obj = StudentMaxHeap(len(d))
    for char, freq in d.items():
        obj.insert(Student(char, freq))
    b = []
    while not obj.isEmpty():
        c = obj.removeBestStudent()
        b.append(c.char * c.freq)
    return ''.join(b)


print(sortCharacter("tree"))  
print(sortCharacter("cccaaa")) 
print(sortCharacter("Aabb")) 
