# concurrency: Questions

## LC:

* [x] LC [1114. Print in Order](https://leetcode.com/problems/print-in-order/) ✅

{% tabs %}
{% tab title="1114-1 : Lock" %}
```python
'''
Start with two locked locks. First thread unlocks the first lock that the second thread is waiting on. Second thread unlocks the second lock that the third thread is waiting on.
'''
from threading import Lock

class Foo:
    def __init__(self):
        self.locks = (Lock(), Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None: 
        printFirst()
        self.locks[0].release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.locks[0].acquire()
        try:
            printSecond()
        finally:
            self.locks[1].release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.locks[1].acquire()
        try:
            printThird()
        finally:
            self.locks[1].release()
```
{% endtab %}

{% tab title="1114- 2: Semaphore" %}
```python
'''
Start with two closed gates represented by 0-value semaphores. Second and third thread are waiting behind these gates. When the first thread prints, it opens the gate for the second thread. When the second thread prints, it opens the gate for the third thread.
'''
from threading import Semaphore

class Foo:
    def __init__(self):
        self.gates = (Semaphore(0),Semaphore(0))
        
    def first(self, printFirst):
        printFirst()
        self.gates[0].release()
        
    def second(self, printSecond):
        with self.gates[0]:
            printSecond()
            self.gates[1].release()
            
    def third(self, printThird):
        with self.gates[1]:
            printThird()
```
{% endtab %}

{% tab title="1114-3: Barrier" %}
```python
'''
Raise two barriers. Both wait for two threads to reach them.

First thread can print before reaching the first barrier. Second thread can print before reaching the second barrier. Third thread can print after the second barrier.
'''
from threading import Barrier

class Foo:
    def __init__(self):
        self.first_barrier = Barrier(2)
        self.second_barrier = Barrier(2)
            
    def first(self, printFirst):
        printFirst()
        self.first_barrier.wait()
        
    def second(self, printSecond):
        self.first_barrier.wait()
        printSecond()
        self.second_barrier.wait()
            
    def third(self, printThird):
        self.second_barrier.wait()
        printThird()
```
{% endtab %}

{% tab title="1114-4: Event" %}
```python
'''
Set events from first and second threads when they are done. Have the second thread wait for first one to set its event. Have the third thread wait on the second thread to raise its event.
'''
from threading import Event

class Foo:
    def __init__(self):
        self.done = (Event(),Event())
        
    def first(self, printFirst):
        printFirst()
        self.done[0].set()
        
    def second(self, printSecond):
        self.done[0].wait()
        printSecond()
        self.done[1].set()
            
    def third(self, printThird):
        self.done[1].wait()
        printThird()
```
{% endtab %}

{% tab title="1114-5: Condition" %}
```python
'''
Have all three threads attempt to acquire an RLock via Condition. The first thread can always acquire a lock, while the other two have to wait for the order to be set to the right value. First thread sets the order after printing which signals for the second thread to run. Second thread does the same for the third.
'''
from threading import Condition

class Foo:
    def __init__(self):
        self.exec_condition = Condition()
        self.order = 0
        self.first_finish = lambda: self.order == 1
        self.second_finish = lambda: self.order == 2

    def first(self, printFirst):
        with self.exec_condition:
            printFirst()
            self.order = 1
            self.exec_condition.notify(2)

    def second(self, printSecond):
        with self.exec_condition:
            self.exec_condition.wait_for(self.first_finish)
            printSecond()
            self.order = 2
            self.exec_condition.notify()

    def third(self, printThird):
        with self.exec_condition:
            self.exec_condition.wait_for(self.second_finish)
            printThird()
```
{% endtab %}
{% endtabs %}



* [x] LC [1115. Print FooBar Alternately](https://leetcode.com/problems/print-foobar-alternately/) ✅

{% tabs %}
{% tab title="1 : Lock" %}
```python
'''
Use two locks for the threads to signal to each other when the other should run. 
bar_lock starts in a locked state because we always want foo to print first.
'''
from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo):
        for i in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

	def bar(self, printBar):
        for i in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()
```
{% endtab %}

{% tab title=" 2: Semaphore" %}
```python
'''
Use two Semaphores just as we used two locks. 
The foo_gate semaphore starts with a value of 1 because we want foo to print first.
'''
from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_gate = Semaphore(1)
        self.bar_gate = Semaphore(0)

    def foo(self, printFoo):
        for i in range(self.n):
            self.foo_gate.acquire()
            printFoo()
            self.bar_gate.release()

    def bar(self, printBar):
        for i in range(self.n):
            self.bar_gate.acquire()
            printBar()
            self.foo_gate.release()
```
{% endtab %}

{% tab title="3: Barrier" %}
```python
'''
Raise a barrier which makes both threads wait for each other before they are allowed to continue. 
foo prints before reaching the barrier. 
bar prints after reaching the barrier.
'''
from threading import Barrier

class FooBar:
    def __init__(self, n):
        self.n = n
        self.barrier = Barrier(2)

    def foo(self, printFoo):
        for i in range(self.n):
            printFoo()
            self.barrier.wait()

    def bar(self, printBar):
        for i in range(self.n):
            self.barrier.wait()
            printBar()
```
{% endtab %}

{% tab title="4: Event" %}
```python
'''
Each thread can wait on each other to set their corresponding foo_printed and bar_printed events. Each thread also resets the corresponding printed events with .clear() for the next loop iteration.
'''

from threading import Event

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_printed = Event()
        self.bar_printed = Event()
        self.bar_printed.set()

    def foo(self, printFoo):
        for i in range(self.n):
            self.bar_printed.wait()
            self.bar_printed.clear()
            printFoo()
            self.foo_printed.set()            

    def bar(self, printBar):
        for i in range(self.n):
            self.foo_printed.wait()
            self.foo_printed.clear()
            printBar()
            self.bar_printed.set()         
```
{% endtab %}

{% tab title="5: Condition" %}
```python
'''
Count the number of times foo and bar was printed and only print foo if the number of times is equal. bar prints if foo was printed fewer times. Use Condition and wait_for to syncrhonize the threads.
'''
from threading import Condition
class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_counter = 0
        self.bar_counter = 0
        self.condition = Condition()

    def foo(self, printFoo):
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda: self.foo_counter == self.bar_counter)
                printFoo()
                self.foo_counter += 1
                self.condition.notify(1)

    def bar(self, printBar):
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda: self.foo_counter > self.bar_counter)
                printBar()
                self.bar_counter += 1
                self.condition.notify(1)

```
{% endtab %}
{% endtabs %}

* [x] LC [1188.Design Bounded Blocking Queue](https://leetcode.libaoj.in/design-bounded-blocking-queue.html) \| @rubrik

{% tabs %}
{% tab title="1188" %}
```python
from collections import deque
from threading import Condition

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.condition = Condition()
        
    def enqueue(self, element: int) -> None:
        with self.condition: # acquire and release
            while len(self.queue) >= self.capacity:
                self.condition.wait()
            
            self.queue.append(element)
            self.condition.notify()

    def dequeue(self) -> int:
        with self.condition:
            while len(self.queue) == 0:
                self.condition.wait()
            
            element = self.queue.popleft()
            self.condition.notify()
            return element
        
    def size(self) -> int:
        with self.condition:
            return len(self.queue)
            
# ============================================ [Running It] ===============
queue = BoundedBlockingQueue(2)
# norm_queue = deque()

def pop_from_queue():
    ans = queue.dequeue()
    print(f'Popped {ans} from queue: \t Q = {queue}')

def add_to_queue(x):
    queue.enqueue(x)
    print(f'Added {x} to queue: \t Q = {queue}')

def get_size():
    print(queue.size())

th = Thread(target=pop_from_queue)
th.start()
print(queue)
time.sleep(2)
th = Thread(target=get_size)
th.start()
th.join()
print(queue)
time.sleep(2)
th = Thread(target=pop_from_queue)
th.start()
th.join()
print(queue)
th = Thread(target=get_size)
th.start()
th.join()
time.sleep(2)
th = Thread(target=add_to_queue, args=[1])
th.start()
th.join()
print(queue)
th = Thread(target=get_size)
th.start()
th.join()
th = Thread(target=pop_from_queue)
th.start()
th.join()
th = Thread(target=get_size)
th.start()
th.join()
print(queue)
    
print('done............')
```
{% endtab %}
{% endtabs %}

* [x] Design Threadsafe stack using LinkedList \| @Rubrik

{% tabs %}
{% tab title="with\_threadsafe" %}
```python
import time
from threading import Thread,Condition

class Node:
    # Class to create nodes of linked list
    def __init__(self,data):
        self.data = data
        self.next = None
     
class SafeStack:
     
    # head is default NULL
    def __init__(self,capacity: int):
        self.capacity = capacity
        self.head = None
        self.condition = Condition()
     
    # O(1)
    def push(self,data):
        with self.condition:    # acquire & release
            while self.get_length() >= self.capacity:
                self.condition.wait()
                
            if self.head == None:
                self.head=Node(data)
            else:
                newnode = Node(data)
                newnode.next = self.head
                self.head = newnode
            
            self.condition.notify()
     
    # : O(1)
    def pop(self):
        with self.condition:    # acquire & release
            while self.get_length() == 0:
                self.condition.wait()
                
            # Removes the head node and makes
            #the preceeding one the new head
            popeed = self.head
            self.head = self.head.next
            popeed.next = None
            self.condition.notify()
            return popeed.data
     
    # Returns the head node data
    # O(1)
    def peek(self):
        with self.condition:    # acquire & release
            return self.head.data
        
    # Checks if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def get_length(self):
        l = 0
        curr = self.head
        while curr:
            l += 1
            curr = curr.next
        return l
     
    # Prints out the stack    
    def display(self):
        iternode = self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            while(iternode != None):
                print(iternode.data,"->",end = " ")
                iternode = iternode.next
            print('\n')
            return

# =================================================== [Run]

def push_to_stk(stk,x):
    stk.push(x)
    print(f'>> Pushed {x} to stk')
    time.sleep(1)
    
def pop_from_stk(stk):
    x = stk.pop()
    print(f'>> Popped {x} from stk')
    time.sleep(1) 
       
def peek_from_stk(stk):
    x = stk.peek()
    print(f'>> Peeking : got {x}')
    time.sleep(1) 
    
def display_stk(stk):
    stk.display()
    time.sleep(1) 
    
# ********************* [Running Without Thread] **********************************
    
# stk = Stack(2)
# pop_from_stk(stk)
# display_stk(stk)
# push_to_stk(stk,1)
# display_stk(stk)
# push_to_stk(stk,2)
# display_stk(stk)
# pop_from_stk(stk)
# display_stk(stk)
# print('================ FINISHED ======================')

# ********************* [Running Without Thread] **********************************
# safestk = SafeStack(2)

# # NORMAL (working) order :: works w/o fail for non-thread too------------------
# th = Thread(target=push_to_stk, args = [safestk,1])
# th.start()
# th.join()
# time.sleep(1)

# th = Thread(target=display_stk, args = [safestk])
# th.start()
# th.join()
# time.sleep(1)

# th = Thread(target=push_to_stk, args = [safestk,2])
# th.start()
# th.join()
# time.sleep(1)

# th = Thread(target=display_stk, args = [safestk])
# th.start()
# th.join()
# time.sleep(1)

# th = Thread(target=pop_from_stk, args = [safestk])
# th.start()
# th.join()
# time.sleep(1)

# th = Thread(target=display_stk, args = [safestk])
# th.start()
# th.join()
# time.sleep(1)

# print('================ FINISHED ======================')

# THREADED (working) order :: works w/o fail ONLY for threaded------------------
safestk = SafeStack(2)

th = Thread(target=push_to_stk, args = [safestk,1])
th.start()
th.join()
time.sleep(1)

th = Thread(target=pop_from_stk, args = [safestk])
th.start()
th.join()
time.sleep(1)

th = Thread(target=display_stk, args = [safestk])
th.start()
th.join()
time.sleep(1)

th = Thread(target=pop_from_stk, args = [safestk])
th.start()
th.join()
time.sleep(1)

th = Thread(target=display_stk, args = [safestk])
th.start()
th.join()
time.sleep(1)

th = Thread(target=display_stk, args = [safestk])
th.start()
th.join()
time.sleep(1)

th = Thread(target=push_to_stk, args = [safestk,2])
th.start()
th.join()
time.sleep(1)

th = Thread(target=display_stk, args = [safestk])
th.start()
th.join()
time.sleep(1)

th = Thread(target=pop_from_stk, args = [safestk])
th.start()
th.join()
time.sleep(1)

th = Thread(target=display_stk, args = [safestk])
th.start()
th.join()
time.sleep(1)

print('================ FINISHED ======================')
```
{% endtab %}

{% tab title="without\_threadsafe" %}
```python
class Node:
    # Class to create nodes of linked list
    def __init__(self,data):
        self.data = data
        self.next = None
     
class Stack:
     
    # head is default NULL
    def __init__(self,capacity: int):
        self.capacity = capacity
        self.head = None
        #self.condition = Condition() ## Not used in 'without_threading'
     
    # Method to add data to the stack
    # adds to the start of the stack
    # O(1)
    def push(self,data):
        if self.head == None:
            self.head=Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
     
    # Remove element that is the current head (start of the stack)
    # : O(1)
    def pop(self):
        if self.isempty():
            return None
        else:
            # Removes the head node and makes
            #the preceeding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
     
    # Returns the head node data
    # O(1)
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    
    # Checks if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
     
    # Prints out the stack    
    def display(self):
        iternode = self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            while(iternode != None):
                print(iternode.data,"->",end = " ")
                iternode = iternode.next
            print('\n')
            return

# =================================================== [Run]
      

def push_to_stk(stk,x):
    stk.push(x)
    print(f'>> Pushed {x} to stk')
    time.sleep(1)
    
def pop_from_stk(stk):
    x = stk.pop()
    print(f'>> Popped {x} from stk')
    time.sleep(1) 
       
def peek_from_stk(stk):
    x = stk.peek()
    print(f'>> Peeking : got {x}')
    time.sleep(1) 
    
def display_stk(stk):
    stk.display()
    time.sleep(1) 
    
# ********************* [Running Without Thread] **********************************
    
stk = Stack(2)
pop_from_stk(stk)
display_stk(stk)
push_to_stk(stk,1)
display_stk(stk)
push_to_stk(stk,2)
display_stk(stk)
pop_from_stk(stk)
display_stk(stk)

print('================ FINISHED ======================')
```
{% endtab %}
{% endtabs %}

* [ ] LC [1117. Building H2O](https://leetcode.com/problems/building-h2o/)
* [ ] LC  [1195. Fizz Buzz Multithreaded](https://leetcode.com/problems/fizz-buzz-multithreaded/)
* [ ] LC [1226. The Dining Philosophers](https://leetcode.com/problems/the-dining-philosophers/)

{% tabs %}
{% tab title="1117" %}
```python
'''
Here's how I picture this mentally:

* You have a waiting area.
* No more than two hydrogens are allowed into the waiting area at a time.
* No more than one oxygen is allowed into the waiting area at a time.
* Once the waiting area is full (and before admitting any additional atoms), the three waiting atoms leave together to form a molecule.
'''
from threading import Barrier, Semaphore
class H2O:
    def __init__(self):
        self.b = Barrier(3)
        self.h = Semaphore(2)
        self.o = Semaphore(1)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.acquire()
		    self.b.wait()
        releaseHydrogen()
        self.h.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.acquire()
		    self.b.wait()
        releaseOxygen()
        self.o.release()
```
{% endtab %}

{% tab title="1195" %}
```python
# IDEA: use four semaphores with only number one starting unlocked, number-thread will loop numbers and distribute work
# to other threads with releases, number-thread will set done flag when its loop finishes and other threads will break on this flag

class FizzBuzz:
    def __init__(self, n: int):
        self.done = False        
        self.n = n
        self.fSem = threading.Semaphore(0)
        self.bSem = threading.Semaphore(0)
        self.fbSem = threading.Semaphore(0)
        self.nSem = threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.fSem.acquire()
            if self.done: break
            printFizz()
            self.nSem.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.bSem.acquire()
            if self.done: break
            printBuzz()
            self.nSem.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fbSem.acquire()
            if self.done: break
            printFizzBuzz()
            self.nSem.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.nSem.acquire()
            if i % 15 == 0:
                self.fbSem.release()
            elif i % 3 == 0:
                self.fSem.release()
            elif i % 5 == 0:
                self.bSem.release()
            else:
                printNumber(i)
                self.nSem.release()
        self.nSem.acquire() # needed so this thread waits to set done flag only when other threads are done with printing
        self.done = True
        self.fSem.release()  # let all other threads to break and finish
        self.bSem.release()  #
        self.fbSem.release() #
```
{% endtab %}

{% tab title="1226" %}
```python
'''
In both solutions, we have to analyze when a deadlock happens. If a philosopher picks up 2 forks, then they will set them down after. So a philosopher could only really get stuck on 0 or 1 forks. Its easy to see that this means a deadlock only occurs if 5 forks are picked up (1 for each philosopher).

Solution 1:
Enforce that at most 4 philosophers can approach the table with sizelock. Then at most 4 forks are picked up, so there can't be a deadlock.

Solution 2:
Enforce that some philosophers pick up forks left then right, and others pick them up right then left. Then a fork is preferred by two neighboring philosophers, guaranteeing that if one of them has 1 fork, the other has 0, and thus at most 4 forks are picked up.
'''
# 1. ============================================================
from threading import Semaphore

class DiningPhilosophers:
    def __init__(self):
        self.sizelock = Semaphore(4)
        self.locks = [Semaphore(1) for _ in range(5)]

    def wantsToEat(self, index, *actions):
        left, right = index, (index - 1) % 5
        with self.sizelock:
            with self.locks[left], self.locks[right]:
                for action in actions:
                    action()

# 2. =============================================================
from threading import Semaphore

class DiningPhilosophers:
    def __init__(self):
        self.locks = [Semaphore(1) for _ in range(5)]

    def wantsToEat(self, index, *actions):
        left, right = index, (index - 1) % 5
        
        if index:
            with self.locks[left], self.locks[right]:
                for action in actions:
                    action()
        else:
            with self.locks[right], self.locks[left]:
                for action in actions:
                    action()
```
{% endtab %}
{% endtabs %}

## Q: Scheduled Executor Service

```java
#Question
Implement following method of ScheduledExecutorService interface in Java

* schedule(Runnable command, long delay, TimeUnit unit)
Creates and executes a one-shot action that becomes enabled after the given delay.

* scheduleAtFixedRate(Runnable command, long initialDelay, long period, TimeUnit unit)
Creates and executes a periodic action that becomes enabled first after the given initial delay, 
and subsequently with the given period; that is executions will 
    commence after initialDelay then initialDelay+period, then initialDelay + 2 * period, and so on.

* scheduleWithFixedDelay(Runnable command, long initialDelay, long delay, TimeUnit unit)
Creates and executes a periodic action that becomes enabled first after the given initial delay, and subsequently with the given delay between the termination of one execution and the commencement of the next.
```

{% tabs %}
{% tab title="\[diff\]: theadsafe" %}
```python
import time
from threading import Timer, Lock

class RepeatedTimer(object):
    """
    A periodic task running in threading.Timers
    """

    def __init__(self, interval, function, *args, **kwargs):
        self._lock = Lock()
        self._timer = None
        self.function = function
        self.interval = interval
        self.args = args
        self.kwargs = kwargs
        self._stopped = True
        if kwargs.pop('autostart', True):
            self.start()

    def start(self):
        self._lock.acquire()
        if self._stopped:
            self._stopped = False
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self._lock.release()

    def _run(self):
        self.start()
        self.function(*self.args, **self.kwargs)

    def stop(self):
        self._lock.acquire()
        self._stopped = True
        self._timer.cancel()
        self._lock.release()

def print_bio(name, age):
    print(f'Your name is {name} & age is {age}')

print("starting...")
rt = RepeatedTimer(1, print_bio, "Sam", age=20,autostart=True) # it auto-starts, no need of rt.start()
try:
    time.sleep(5) # your long-running job goes here...
finally:
    rt.stop() # better in a try/finally block to make sure the program ends!
```
{% endtab %}

{% tab title="\[easy\]:timer-threadsafe out of the box; relies on 3P" %}
```python
import time
from threading import Timer

def repeat_every(n, func, *args, **kwargs):
    def and_again():
        func(*args, **kwargs)
        t = Timer(n, and_again)
        t.daemon = True
        t.start()
    t = Timer(n, and_again)
    t.daemon = True
    t.start()


def scheduled_task(msg='hello, world', **kwargs):
    print (time.time(), "scheduled_task:", msg, kwargs)

repeat_every(.5, scheduled_task )
repeat_every(1, scheduled_task, "Slow", name="Hand luke")

for x in range(5):
    print(time.time(), "Main: busy as a bee.")
    time.sleep(3)
```
{% endtab %}
{% endtabs %}

## Q: Multithreaded Queue Like Kafka

{% tabs %}
{% tab title="Kakfa" %}
```python
"""

We have to design a message queue supporting publisher-subscriber model.
It should support following operations:

1. It should support multiple topics where messages can be published.
2. Publisher should be able to publish a message to a particular topic.
3. Subscribers should be able to subscribe to a topic.
4. Whenever a message is published to a topic, all the subscribers, who are
   subscribed to that topic, should receive the message.
5. Subscribers should be able to run in parallel


createTopic(topicName) -> topicId
subscribe(topicId, subscriber) -> boolean
publish(topicId, message) -> boolean
resetOffset(topidId, subscriber, offset) -> boolean




publisher        MessagingService        subscriber-1       subscriber-2
    |  create -> t1,t2   |                     |   t1 <-- subscribe  |
    |------------------->|<--------------------|---------------------|
    |                    |<--------------------|                     |
    |                    | t2,t1 <-- subscribe |                     |
    |                    |                     |                     |
    |  msg -> (t1, hi)   |                     |                     |
    |------------------->|         hi          |                     |
    |                    |-------------------->|      hi             |
    |                    |---------------------|-------------------->|
    |                    |         hi          |                     |
    |  msg -> (t2, hello)|                     |                     |
    |------------------->|         hello       |                     |
    |                    |-------------------->|                     |


Threads: 
    1. Thread/Subscriber to manage sending of the message to subscriber
    2. Thread/Published_Message to accept message from publisher and
       to send to all subscribed users.
    3. Thread/OffsetReset to push messages from the offset till current to
       subscribed user of that offset change. 

Classes:
    1. Message
    2. ISubscriber
    3. SleepingSubscriber (:: ISubscriber)
    4. TopicSubscriber
    5. Topic - Needs Lock to allow writting messages in order
    6. TopicHandler
    7. SubscriberWorker - Condition(wait, notify) with Lock to consume till 
            current offset and wait until new message is published.
    8. MessagingService

"""
import time
import abc
import threading
import concurrent.futures

class Message:
    """
    Represents message.
    """
    def __init__(self, data:str) -> None:
        self.data = data

class ISubscriber(abc.ABC):
    """
    Abstract subscriber class
    """
    @abc.abstractmethod
    def consume(self, message: Message, offset: int) -> None:
        """
        Consume published messages with concrete implementation.
        """
        raise NotImplementedError()

class SleepingSubscriber(ISubscriber):
    """
    Concrete implementation of the subscriber class.
    """

    def __init__(self, name: str, sleep_time: float) -> None:
        self.name = name
        self.sleep_time = sleep_time

    def consume(self, message: Message, offset: int) -> None:
        """
        Consume message with delay.
        """
        # print(f'Subscriber name={self.name}, started consuming msg={message.data} at {offset=}')
        time.sleep(self.sleep_time)
        print(f'Subscriber name={self.name}, consumed msg={message.data} at {offset=}')


class TopicSubscriber:
    """Represents a subscriber of a given topic"""
    def __init__(self, subscriber: ISubscriber) -> None:
        self.subscriber = subscriber
        self.offset = 0

    def reset_offset(self) -> None:
        """Reset the offset"""
        self.offset = 0

    def increment_offset(self, prev_offset: int) -> None:
        """Increment offset if prev offset value matches the current offset"""
        if prev_offset == self.offset:
            self.offset += 1

class Topic:
    """Topic to store messages in order of their publish time"""
    def __init__(self, name:str) -> None:
        self.name = name
        self.messages = []
        self.subscribers = []
        self.lock = threading.Lock()

    def add_message(self, message: str) -> None:
        """Add message to the topic"""
        # Acquire lock before updating the message queue.
        with self.lock:
            self.messages.append(Message(message))

    def add_subscriber(self, subscriber: TopicSubscriber) -> None:
        self.subscribers.append(subscriber)


class TopicHandler:
    """Handler responsible for pushing messages to subscribers"""
    def __init__(self, topic: Topic, workers: int=10) -> None:
        self.topic = topic
        # create thread pool to for concurrent message handling
        self.thread_pool = concurrent.futures.ThreadPoolExecutor(workers)
        self.t_subscribers = {}

    def shutdown(self) -> None:
        # terminate running thread
        for t_sub in self.t_subscribers.keys():
            self.t_subscribers[t_sub].terminate()

        # shutdown thread pool executor
        self.thread_pool.shutdown(wait=True)

    def publish(self) -> None:
        # publish message to all subscriber of this topic
        for t_sub in self.topic.subscribers:
            self.start_subscriber_worker(t_sub)

    def start_subscriber_worker(self, t_sub:TopicSubscriber) -> None:
        print(t_sub)
        # submit notify job to subscriber worker if topic subscriber was
        # consuming messages before.
        if t_sub not in self.t_subscribers:
            self.t_subscribers[t_sub] = SubscriberWorker(self.topic, t_sub)
            self.thread_pool.submit(
                self.t_subscribers[t_sub].notify)
        else:
            # just poke the subscriber to indicate that new message has
            # be pushed.
            self.t_subscribers[t_sub].poke()

class SubscriberWorker:
    """Worker that is responsible of pushing messages to subscriber"""
    def __init__(self, topic: Topic, topic_sub: TopicSubscriber):
        self.topic = topic
        self.topic_sub = topic_sub
        self.condition = threading.Condition()
        self.exit = False
    
    def terminate(self) -> None:
        self.exit = True
        with self.condition:
            self.condition.notify()

    def notify(self) -> None:
        while True:
            with self.condition:
                curr_offset = self.topic_sub.offset
                while curr_offset >= len(self.topic.messages):
                    if self.exit:
                        return
                    self.condition.wait()
                    # read current offset when poked to read the up-to date
                    # offset value
                    curr_offset = self.topic_sub.offset
                message = self.topic.messages[curr_offset]
                self.topic_sub.subscriber.consume(message, curr_offset)
                self.topic_sub.increment_offset(curr_offset)

    def poke(self) -> None:
        """Wakes up the worker to notify subscriber for new message"""
        with self.condition:
            self.condition.notify()



class MessagingService:
    """Messaging queue service implementation"""
    def __init__(self) -> None:
        # stores all topic handlers
        self.topic_handlers = {}
        self.threads = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # join all threads
        for t in self.threads:
            t.join()
        # shutdown threadpool executor running per handler
        for t_h in self.topic_handlers.keys():
            self.topic_handlers[t_h].shutdown()

    def create_topic(self, name: str) -> None:
        """
        Create a new topic and add it to handler.
        """
        topic = Topic(name)
        self.topic_handlers[name] = TopicHandler(topic)
        return topic

    def subscribe(self, sub_name: str, topic: Topic) -> None:
        """
        Subscribe to a topic.
        """
        topic.add_subscriber(TopicSubscriber(sub_name))

    def publish(self, topic: Topic, msg: str) -> None:
        """
        Publish message to a topic"""
        topic.add_message(msg)
        # spawn a new thread to notify handler about the new message.
        t = threading.Thread(target=self.topic_handlers[topic.name].publish)
        t.start()

    def reset_offset(self, topic: Topic, subscriber: ISubscriber, offset: int) -> bool:
        for t_sub in topic.subscribers:
            if t_sub.subscriber == subscriber:
                t_sub.offset = offset
                t = threading.Thread(
                    target=self.topic_handlers[
                        topic.name].start_subscriber_worker, args=(t_sub,))
                t.start()
                return True
        return False


with MessagingService() as ms:
    subscriber = SleepingSubscriber('sub1', 0.1)
    subscriber2 = SleepingSubscriber('sub2', 0.1)
    # subscriber3 = SleepingSubscriber('sub3', 0.1)
    # subscriber4 = SleepingSubscriber('sub4', 0.1)
    # subscriber5 = SleepingSubscriber('sub5', 0.1)
    # subscriber6 = SleepingSubscriber('sub6', 0.1)
    # subscriber7 = SleepingSubscriber('sub7', 0.1)
    topic = ms.create_topic('product')
    ms.subscribe(subscriber, topic)
    # ms.subscribe(subscriber2, topic)
    # ms.subscribe(subscriber3, topic)
    # ms.subscribe(subscriber4, topic)
    # ms.subscribe(subscriber5, topic)
    # ms.subscribe(subscriber6, topic)
    # ms.subscribe(subscriber7, topic)
    i = 0
    while i < 10:
        ms.publish(topic, 'Car')
        # ms.publish(topic, 'Truck')
        # ms.publish(topic, 'Bus')
        # ms.publish(topic, 'Cycle')
        # ms.publish(topic, 'Tri-Cycle')
        # ms.publish(topic, 'Van')
        # ms.publish(topic, 'Mini')
        print('-----------')
        i += 1
    time.sleep(5)
    ms.reset_offset(topic, subscriber, 5)
```
{% endtab %}
{% endtabs %}

