class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

print("Ex1")
stack = Stack()
stack.push(5)
stack.push(10)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0) if self.items else None

    def peek(self):
        return self.items[0] if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

print("Ex2")
queue = Queue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.pop())
print(queue.pop())

class Matrix:
    def __init__(self, rows, cols, init_value=0):
        self.rows = rows
        self.cols = cols
        self.data = []
        for _ in range(rows):
            row = []
            for _ in range(cols):
                row.append(init_value)
            self.data.append(row)

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        print("Index out of bounds.")
        return None

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            print("Index out of bounds.")

    def transpose(self):
        transposed_matrix = Matrix(self.cols, self.rows)
        for i in range(self.cols):
            for j in range(self.rows):
                transposed_matrix.data[i][j] = self.data[j][i]
        return transposed_matrix

    def multiply(self, other):
        if self.cols != other.rows:
            print("Matrix dimensions do not allow multiplication.")
            return None
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.data[i][j] = 0
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def transform(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = func(self.data[i][j])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

print("Ex3")
matrix = Matrix(2, 3)
matrix.set(0, 1, 5)
print("Get method:")
print(matrix.get(0, 1))
print("Print matrix:")
print(matrix)

transposed = matrix.transpose()
print("Transposed method:")
print(transposed)

matrix_b = Matrix(3, 2)
print("Print matrix:")
print(matrix_b)
result = matrix.multiply(matrix_b)
print("Multiply method:")
print(result)

matrix.transform(lambda x: x + 1)
print("Print transform with lambda:")
print(matrix)
