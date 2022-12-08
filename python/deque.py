from collections import deque
queue = deque(["Emy", "Inno", "Tim"])
print(queue)
queue.append("Zipporah")
queue.append("Odetos")
queue.popleft()
queue.popleft()
print("New queue = {}".format(queue))
