# LLD:Theory \(OOPs\)

## \#Notes

* \*\*\*\*[**A plain english introduction to CAP Theorem**](http://ksat.me/a-plain-english-introduction-to-cap-theorem)\*\*\*\*
* How to identify **classes, attributes & methods** in system? ✅⭐️🔥😎
  * **Classes =&gt; Noun**
  * **Attribute =&gt; Adjectives**
  * **Methods =&gt; Verbs**
* [VSCode: Using Black to automatically format Python](https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0)
* [Ducktyping](https://realpython.com/lessons/duck-typing/)??
  * This term comes from the saying “If it walks like a duck, and it quacks like a duck, then it must be a duck.” \(There are [other variations](https://en.wikipedia.org/wiki/Duck_test#History)\).
  * Duck typing is a concept related to **dynamic typing**, where the type or the class of an object is less important than the methods it defines. When you use duck typing, **you do not check types at all. Instead, you check for the presence of a given method or attribute.**
* **In python, objects are passed by REFERENCE!!!!!!!!!!!!!!!!!!!!!!**
* **Deployment:**
  * for **CLI** apps: [repl.com](https://replit.com/)
    * **Sharing with others**\(as run-only\) : append `?embed=1` in the end of url:
    * E.g: [https://replit.com/@ReaderMango/CardWars](https://replit.com/@ReaderMango/CardWars#main.py)?embed=1
  * for **GUI** apps: django/flask

## 1. Classes & Attributes

```python
"""
* A Class has 3 things:
    1. Attributes
    2. __init__()
    3. Methods

* self is "skipped" in arguments while we create an instance
"""
class Dog:

    id_counter = 1

    def __init__(self, name, age, color="Black"):
        self.id = Dog.id_counter
        self.name = name
        self.age = age
        self.color = color

        Dog.id_counter += 1

    def bark(self):
        print(f"ID = {self.id} name is {self.name} and I am {self.age} years old; col = {self.color}")
        
d1 = Dog("Dot", 4)
d1.bark()
```

## 2. Encapsulation

```python
class Car:

    id_counter = 1

    def __init__(self, name, model, year):
        self._id = Car.id_counter
        self._name = name
        self.model = model
        self.__year = year

        Car.id_counter += 1

    # Getter: Using @property Decorator
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
        self._name = new_name
    
    # # getter
    # def get_id(self):
    #     return self._id

    # # setter
    # def set_id(self, new_id):
    #     if isinstance(new_id, int) and new_id > 0:
    #         self._id = new_id
    #     else:
    #         print("Plese enter a valid id")

    # # using property
    # id = property(get_id, set_id)
```

* A Class has 2 main parts: 
  1.  **Interface** : the "visible" part of class with which user can interact 
     * Eg. Power **Switch** \(class = Fan\)
  2. **Implementation**: the actual code level logic which performs the functionality. 
     * Eg. Internal wiring of **fan** \(class = Fan\)
* **Abstraction**: =&gt; Show only the essential attributes & hide unnecessary details from user
* **Encapsulation** is implemented using:
  * public \| private
  * getters \| setters
* **Abstraction vs Encapsulation**
  * Encapsulation hides variables or some implementation that may be changed so often in a class to prevent outsiders access it directly. They must access it via getter and setter methods.
  * Abstraction is used to hide something too, but in a higher degree \(class, **interface**\). Clients who use an abstract class \(or interface\) do not care about what it was, they just need to know what it can do.
* **How to make attributes private:**
  * \(src: official doc\) _actual "**private**" thing doesnt exist in python._
  * However, there is a **convention**\(naming attrs as : `_attrName`\) followed in codes.
  * Technically, you CAN access `_attr` , but as per coding practice; you SHOULDNT
  * 2 ways of making attributes private:
    1. By Convention =&gt; `_<attribute>`
    2. Changing name\("Name Mangling"\)   =&gt; `__<attribute>`  \(used only for some special cases\)
       * Hides the attr more furhter
       * if you give two underscores in attr name \(`__attrName`\); python begins the process of **Name Mangling;** so you shouldnt give two underscores until you're fully sure.
       * **attr1 ==\[Name Mangling\]==&gt; \_class1**attr1
  * **NOTE**: dont use term 'private' for python\(as it doesnt exist\), instead use '**non-public**
* **@property Decorator:**

  * What is **Decorator**:
    * =&gt; A function that takes a function & **extends its behaviour w/o explicitly modifying it.**
    * i.e. its a "special" function extender
  * Why use Decorator:
    * cleaner code
    * easier to read/understand
    * avoid calling `property()` directly
  * SYNTAX:
    * getter: `@propety`
    * setter: `@attName.setter` \(NOTE: its NOT `@property.setter` baby\)
    * deleter: `@attName.deleter`

## 3. Abstraction

```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        raise NotImplementedError()


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass  # implement something meaningful here

p = Photocopier()
p.print('hahaha')
```

* **An abstract method:** is a method that is declared, but contains no implementation.
* **Abstract Classes**
  * =&gt; Abstract classes are classes that contain **one or more abstract methods**.
  * Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.
  * Python on its own doesn't provide abstract classes. Yet, Python comes with a module which provides the infrastructure for defining **Abstract Base Classes \(ABCs\)**
* **Section Highlights:**
  *  `raise NotImplementedError()` or `pass` =&gt; **both** can be used; as per the needs
  *  `from abc import ABC, abstractmethod`

## 4. Methods

```python
class Cart:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
            return self        # Merhod chainging:: prev method SHOULD return `self` in order for next method to work
        else:
            print("Add a valid item please!")

    def add_multiple_items(self, items):
        for item in items:
            self.add_item(item)

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            return 0

    def has_item(self, item):
        return item in self._item


mycart = Cart()
print(f"Before: items = {mycart.items}")
mycart.add_item("Nike Shoe").add_item("Sports Shoes")    # Method Chainging(see ^)
print(f"After: items = {mycart.items}")
```

## 5. Mutation & Cloning

* **Alisas**
  * =&gt; Two or more references to the same memory address 
  * i.e. Different name, Same object
* **Immutable Data Types in python:**
  * String
  * Tuples
* **Mutable Data Types in python:**
  * list
  * set
  * dict
* **Cloning**
  * =&gt; Creating an exact copy of the obj, completely independent from original obj
  * i.e. Antonym of 'Alias'
  * To clone a **list**: `b = a[:]`
  * To clone a **dict**: `d2 = d1.copy()`
  * **SHALLOW vs DEEP**
    * When you make a shallow copy of an object, you are making a new object in memory, a new reference, but the content of the object will still point to the same objects
    * With a deep copy, in addition to creating a copy of the "container" object, you also create a copy of the elements contained in the object

## 6. Inheritance

```python
class Polygon:
    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color
        
    def describe_me(self):
        print(f'I have {self.num_sides} sides & {self.color} color')


class Triangle(Polygon):

    NUM_SIDES = 3

    def __init__(self, base, height, color):
        Polygon.__init__(self, Triangle.NUM_SIDES, color)
        # super().__init__(Triangle.NUM_SIDES,color)
        self.base = base
        self.height = height

    def find_area(self):
        return (self.base*self.height)/2

class Square(Polygon):

    NUM_SIDES = 4

    def __init__(self, side_length, color):
        Polygon.__init__(self, Square.NUM_SIDES, color)
        self.side_length = side_length

    def find_area(self):
        return self.side_length**2

myt = Triangle(3, 5, "red")
mysq = Square(4, "black")
myt.describe_me()
print(myt.find_area())
mysq.describe_me()
print(mysq.find_area())


'''1. Multilevel Inheritence'''

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class Car(LandVehicle):
    pass


''' 2.Multiple Inheritence'''
class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color


class GUIElement:
    def click(self):
        print("The object was clicked...")


class Button(Rectangle, GUIElement):
    def __init__(self, length, width, color, text):
        Rectangle.__init__(self, length, width, color)
        self.text = text

```

* **Inheritence:**
  * =&gt; Designing classes that inherit attributes & methods from other classes
  * **check if subclass**: `issubclass(Dog, Animal)`
* **On using `super()`:**
  * If subclass doesnt has its own **init**\(\) ; it'll automatically inherit its parent's **init**\(\)
  * If subclass HAS its own **init**\(\) ; have to use SUPER:
    * SYNTAX:
      1. .**init**\(self,\)
      2. super\(\).**init**\(\)
* **Method Overriding**
  * =&gt; customize/extend the functionality of a method which is defined in superclass
  * in case of overriding\(same method name in superclass & subclass\), **method of subclass will be called first**
* **Method Overloading**
  * occurs when two methods in the same class have the same name but different parameters
  * So when you call the method, the version that is executed is determined by the data types of the arguments or by the number of arguments.
  * **Python does not support method overloading**. 
    * The closest thing that you could think of in Python is default arguments, because you can call a method passing a different number of arguments if you want to use the default values. But this is not method overloading per se.
  * Java does support method overloading 
    * because you need to explicitly declare the data type of each argument, so the compiler can match the number, sequence, and data types of the arguments with the number, sequence, and data types of the formal parameters to determine which version of the method it should call.
* **Polymorphism**
  * =&gt; Polymorphism means that an object can take many forms.
  * Tip: Polymorphism can be achieved through **method overriding** and method overloading \(method overloading is not supported in Python per se\).
  * **In Python, polymorphism can be implemented through inheritance** when you **override** methods from the superclass.
* **Section Highlight:** 
  * `Superclass.__init__(self)`
* What's the Object Oriented way to get rich? =&gt; Inheritance 🤣

## 7. Concurrency in Python

```python
import asyncio
import random

# 1 . Basic Implementation =============================================
async def my_coroutine_noob():
    print("hello")


def my_concurrency_noob():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_coroutine_noob())
    loop.close()


# 2. See the actual working =============================================


async def my_coroutine2(id):
    rand_process_time = random.randint(1, 5)
    await asyncio.sleep(rand_process_time)
    print(f"Process {id} got completed after {rand_process_time} seconds.")


async def run():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(my_coroutine2(i)))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    # my_concurrency_noob()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run())
    finally:
        loop.close()

'''
Process 0 got completed after 1 seconds.
Process 7 got completed after 1 seconds.
Process 8 got completed after 1 seconds.
Process 9 got completed after 1 seconds.
Process 1 got completed after 3 seconds.
Process 3 got completed after 3 seconds.
Process 6 got completed after 3 seconds.
Process 2 got completed after 4 seconds.
Process 4 got completed after 4 seconds.
Process 5 got completed after 4 seconds.
'''
```

## 8. SOLID Design Patterns

### 8.1. SRP =&gt; Single Responsibility Principle

* Its also called SOC \(Separation of Concerns\)
* **IDEA**: =&gt; A class should have a single region to change & that should be its PRIMARY responsibility

```python
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)
    
    
    '''
        SRP: instead of creating below (sort-of isolated) functions in same class; create a SEPARATE class - so that in future further classes can use it
    '''
    # break SRP     
    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass


class PersistenceManager:
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()
        
    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = r'c:\temp\journal.txt'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
```

### 8.2. OCP =&gt; Open Close Principle

* **IDEA** =&gt; classes should be OPEN for Extension, but CLOSED for Modification
  * i.e. after you've written a class; if a new business requirement comes =&gt; you should not modify it. You should ONLY extend it

### 8.3. LSP =&gt; Liskov Substituion Principle

### 8.4. ISP =&gt; Interface Segratation Principle

*  IDEA -&gt; Dont stick too many things\(atts/methods\) in an interface

### 8.5. DIP =&gt; Dependency Inversion Principle

* IDEA =&gt; high level modules should not depend on low level modules. Instead, they should depend on abstractions\(Interfaces\)

## 9. Testing in Python✅✅🧪

```python
import unittest
from parking_lot import ParkingLot, Car, Bike, Bus

class TestParkingLot(unittest.TestCase):
    # UT: test each function
    def test_park(self):
        parkingLotObj = ParkingLot(6, 30)
        res2 = parkingLotObj.parkVehicle(Car(10, "Amazon"))
        res3 = parkingLotObj.parkVehicle(Bike(20, "Amazon"))
        res4 = parkingLotObj.parkVehicle(Bus(30, "Microsoft"))

        self.assertEqual(res2, True)
        self.assertEqual(res3, True)
        self.assertEqual(res4, True)
    # IT: integration test
    def test_all(self):
        parkingLotObj = ParkingLot(3, 10)
        self.assertTrue(parkingLotObj.parkVehicle(Car(10, "Google")))

        self.assertTrue(parkingLotObj.leaveOperation(Car(10, "Google")))
        self.assertEqual(parkingLotObj.companyParked("Google"), [])


if __name__ == '__main__':
    unittest.main()    # runs all
```

## 10. Enums in Python OOP

```python
from enum import Enum

class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    NONE = "NONE"

class Elevator:

    def __init__(self, curr_direction=Direction.UP):
        self._id = Elevator.ids
        self._curr_direction = curr_direction

    @property
    def curr_direction(self):
        return Direction[self._curr_direction].name    # returns string 'UP'
if __name__ == "__main__":

    el = Elevator(curr_direction="DOWN", curr_state="IDLE", curr_floor=5)
    print(el.curr_direction)  #  # returns string 'DOWN' 
```

## 11. Design Patterns

### 1. SINGLETON

* "There can only be one!"
* i.e. **at one time; only one instance can exit**
* **e.g.**
  * 1 Moon \(anti `1Q84` hai, par real hai\)
  * 1 Sun
* **How:** each time you want to create a new instance
  * check if an instance exists =&gt; dont create another; just return it
  * if doesnt exit =&gt; create new
* In this way; all our instances will **point to single instance.**
* **@used:** ParkingLot

{% tabs %}
{% tab title="Singleton@ParkingLot.py" %}
```python
class ParkingLot:
    # singleton ParkingLot to ensure only one object of ParkingLot in the system,
    # all entrance panels will use this object to create new parking ticket: get_new_parking_ticket(),
    instance = None

    class __OnlyOne:
        def __init__(self, name, address):
            self.__name = name
            self.__address = address
            self.__parking_rate = ParkingRate()

    def __init__(self, name, address):
        if not ParkingLot.instance:
            ParkingLot.instance = ParkingLot.__OnlyOne(name, address)
        else:
            ParkingLot.instance.__name = name
            ParkingLot.instance.__address = address
```
{% endtab %}
{% endtabs %}

## \#Things to do:

* [x] Understand OOPs using Python
  * [x] **Beginner**: Udemy: [Python OOP - Object Oriented Programming for Beginners](https://razorpay.udemy.com/course/python-object-oriented-programming-oop/)
    * Implementation of OOPs concepts in python
  * [x] **Beginner:**Udemy: [Python OOP : Four Pillars of OOP in Python 3 for Beginners](https://razorpay.udemy.com/course/python-oops-beginners/)
    * `@abstractMethod`
  * [x] **Adv**: Udemy: [Advanced Python: Python OOP with 10 Real-World Programs](https://razorpay.udemy.com/course/the-python-pro-course/)
    * Structured process of LLD designing 💪
    * Deploying CLI apps\([repl.com](https://replit.com)\)
    * APIs =&gt; Django/Flask
* [x] Learn design principles - with implementation
  * [x] Udemy: [Design Patterns in Python](https://razorpay.udemy.com/course/design-patterns-python/) ☑️\| done **S.O.L.I.D.** \| **TODO**: finish rest later
  * [x] Udemy: [Pragmatic System Design](https://razorpay.udemy.com/course/pragmatic-system-design/)
* [ ] Revise Django, Node, React, Next - & have all the working code ready for interviews
  * [x] React2025
  * [ ] Udemy: [Full Stack Web Development with Python and Django Course](https://razorpay.udemy.com/course/crash-course-web-development-python-django/)
  * [ ] Udemy: [The Python Mega Course: Build 10 Real World Applications](https://razorpay.udemy.com/course/the-python-mega-course/)
  * [ ] Udemy: [React & Django Full Stack: web app, backend API, mobile apps](https://razorpay.udemy.com/course/react-django-full-stack/)
* [ ] Code up all the "stuff" we talk about in HLD & have working code ready.
* [ ] Solve as many questions as possible & have all the WORKING code in a repo
  * [ ] [Grokking the Object Oriented Design Interview](https://www.educative.io/courses/grokking-the-object-oriented-design-interview)
  * [ ] Git: [prasadgujar](https://github.com/prasadgujar)/[**low-level-design-primer**](https://github.com/prasadgujar/low-level-design-primer)
  * [ ] PDF: [Object-Oriented Design- Solutions & Algorithms](https://www.andiamogo.com/S-OOD.pdf)
  * [ ] [Leetcode Questions](https://leetcode.com/discuss/interview-question/object-oriented-design?currentPage=1&orderBy=hot&query)

## 

