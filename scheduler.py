import time
from collections import deque
import heapq


class Task:
    def __init__(self, function, delay):
        self.function = function
        self.delay = delay
        self.deadline = 0


class Scheduler:
    def __init__(self):
        self.ready = deque()     # Functions ready to execute
        self.sleeping = []       # Sleeping functions in a priority queue
        self.sequence = 0        # Used to break ties in the priority queue

    def schedule(self, task):
        delay = task.delay
        self.sequence += 1
        task.deadline = time.time() + delay     # Expiration time
        # self.ready.append(task)
        heapq.heappush(self.sleeping, (task.deadline, self.sequence, task))

    def start(self):
        while self.ready or self.sleeping:
            if self.ready:
                task = self.ready.popleft()
                task.function()
                self.schedule(task)

            else:
                deadline, _, task = heapq.heappop(self.sleeping)
                delta = deadline - time.time()
                if delta > 0:
                    time.sleep(delta)
                self.ready.append(task)

def wakeup():
    print("Waking up :(")

def coffee():
    print("Ah coffee :)")

def savetheword():
    print("Suit up")

def tired():
    print("**Yawns**")


sched = Scheduler()

# Schedul Wakeup every 10 secs
wakeup_task = Task(wakeup, 2)
sched.schedule(wakeup_task)

# Schedul Coffee every 5 secs
coffee_task = Task(coffee, 5)
sched.schedule(coffee_task)


# Schedul savetheword every 1 secs
savetheword_task = Task(savetheword, 1)
sched.schedule(savetheword_task)

# Schedul savetheword every 9 secs
tired_task = Task(tired, 9)
sched.schedule(tired_task)

# Start the scheduler
sched.start()
