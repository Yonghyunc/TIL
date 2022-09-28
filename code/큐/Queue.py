n = 3
q = [0] * n
front = -1
rear = -1

rear += 1  # enqueue(10)
q[rear] = 10

rear += 1  # enqueue(20)
q[rear] = 20

rear += 1  # enqueue(30)
q[rear] = 30

front += 1  # dequeue()
print(q[front])

front += 1  # dequeue()
print(q[front])

front += 1  # dequeue()
print(q[front])
