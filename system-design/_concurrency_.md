# \_concurrency\_

## `multiprocessing` module \| [playlist](https://www.youtube.com/watch?v=RR4SoktDQAw&list=PL5tcWHG-UPH3SX16DI6EP1FlEibgxkg_6&index=1&ab_channel=LucidProgramming)

* Allows us to bypass python's GIL & run the process on multiple threads
* Normal run: single process

```python
def square(x):
    print(f'square({x}) = {x*x}')
    
if __name__ == '__main__':
    nums = [1,2,3,4]
    
    for x in nums:
        square(x)
'''
square(1) = 1
square(2) = 4
square(3) = 9
square(4) = 16
'''
```

* Using **`Process`**, **`current_process`**
  * **Style \(demo\) :** 
    * **run lots of long process\(with delay: `time.sleep(.5)`\)**
    * **terminal -&gt; "`htop`" -&gt; F4 -&gt; filter python & voila!**

```python
import os
import time
from multiprocessing import Process, current_process

def square(x):
    res = x*x
    time.sleep(2)
    # we can use 'os' module to print the ProcessID 
    # assigned to the call of this function by the OS
    process_id = os.getpid()
    
    # we can also use 'current_process' pkg to get the
    # name of the Process obj
    process_name = current_process().name
    print(f'Process ID = {process_id} , Process Name = {process_name}')
    
    print(f'square({x}) = {res}')
    
if __name__ == '__main__':
    nums = range(1000)
    processes = []
    
    for x in nums:
        process = Process(target=square, args=(x,)) # agar >1 arg hota toh comma nhi aata=> args=(x,y)
        processes.append(process)
        process.start()
    
    # to ensure that all processes have been completed        
    for process in processes:
        process.join()
    print('============== Multiprocessing Complete ============')
'''
Process ID = 87375 , Process Name = Process-1
square(1) = 1
Process ID = 87376 , Process Name = Process-2
square(2) = 4
Process ID = 87377 , Process Name = Process-3
square(3) = 9
Process ID = 87378 , Process Name = Process-4
square(4) = 16
'''
```

## 1.Lock\(synonym = Mutex\)

* **WHAT is Lock/Mutex:** 
  * A lock or mutex is a **synchronisation mechanism** to **enforce limits** on **access to a resource** in an environment where there are **many threads of execution**.



## 2. Semaphore



## 3. Event



## 4. Barrier



## 5. Condition







