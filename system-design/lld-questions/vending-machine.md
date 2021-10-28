# Vending Machine



### &#x20;Vending Machine | 🟢STATE pattern

* [Code(JAVA)](https://github.com/prabhakerau/lowlevelsystemdesgin/tree/main/VendingMachine/src/com/lld/questions/vendingmachine)

\*\* Advantages of using State Pattern:\*\*

* The design pattern moves all state-related logic to a separate class thus reducing the coupling with the main context class & is following the Single Responsibility Principle
* State-related behaviour is declared in an interface. New states can be easily introduced without the need to modify & add conditional blocks of code. Code becomes open for extension & closed for modification

\*\* Disadvantages of using State Pattern:\*\*

* Individual states must be aware of the next states and those states need to be hardcoded
* The pattern becomes an overkill if the design only has one or two states or the state behaviour rarely changes

{% tabs %}
{% tab title="design" %}
```
# Requirements =======================================

* INVENTORY: Vending Machine must keep track of the inventory
* INSERT CASH & SELECT: A person should be able to insert cash(1,5,10,25 Cents i.e. penny, nickel, dime, and quarter.) into the machine & choose an item(Coke(25), Pepsi(35), Soda(45))
* The Machine should confirm the inserted cash with the price of the selected item
* The machine must display an error in case of insufficient cash or unavailable item
* DISPATCH: Finally, if all the above steps succeed then the user gets the selected item and remaining change if any
* RESET     : Allow reset operation for vending machine supplier.
* [@] REFUND    : Allow user to take refund by canceling the request.

# IMPLEMENTATION ====================================== 
* STATE PATTERN :
    * Transactions are atomic
    * If the machine is in the process of dispensing an item, then the user can’t insert cash and try to buy another item.
    * i.e. a user can buy a new item by either aborting or completing the existing transaction
* STATES:
1. Ready — Machine ready to accept cash
2. CashCollected — Machine has collected cash & user can now select the product or cancel the transaction
3. DispenseChange — Give back the change to the user
4. DispenseItem — Dispense the item upon successful validation of entered cash & the price of the selected item in inventory
5. TransactionCancelled — If the user cancels the transaction, return the cash given by the user

# Classes:


ITEM: Enum
------------PEPSI
------------COKE
------------SODA

COIN: Enum
------------PENNY:1
------------NICKEL:5
------------DIME:10
------------QUARTER:25

Item 
------------name
------------price
------------get_price()
------------get_name()

Cash
------------name
------------denominaiton
------------get_denominaiton()

ItemInventory
------------items: {} #item->quantity
------------add_item()
------------deduct_item()
------------is_item_available()
------------display_inventory()
------------reset()

CahsInventory
------------cash: {} #coin->quantity
------------add_cash()
------------deduct_cash()
------------has_chash()
------------get_change()
------------show_cash_inventory()

Exceptions
------------ItemNotAvailableException
------------InsufficientCashExcepiton
------------ChangeNotAvailableException
------------ItemNotSelectedExcepiton


VendingMachineState
------------insert_cash()
------------select_item()
------------proecss_request()
------------cancel_request()
------------dispatch_item_and_cash()


--> ReadyState(VendingMachineState)

--> CancelingState(VendingMachineState)

--> ProcessingState(VendingMachineState)

--> DispatchingState(VendingMachineState)


VendingMachineFactory
------------create_vending_machine()    
# Factory Method to create a VM.THis can be extended to create diff types of VMs

VendingMachine
------------selected_item = None   # Item
------------entered_cash = 0
------------vending_machine_state = VendingMachineState
------------item_inventory = ItemInventory()
------------cash_inventory = CahsInventory()
------------add_item()
------------deduct_item()
------------add_cash()
------------deduct_cash()
------------get_entered_cash_value()
------------reset_entered_cash_value()
------------get_selected_item()
------------set_selected_item()
------------reset_selected_item()
------------is_selected_item_available()
------------is_change_available_for_entered_cash()
```
{% endtab %}

{% tab title="code.py" %}
```python
from enum import Enum

# coin.py


class CASH(Enum):
    PENNY, NICKEL, DIME, QUARTER = 1, 2, 3, 4


class Cash:
    def __init__(self, name, denominaiton):
        self.name = name
        self.denominaiton = denominaiton

    def get_denomination(self)->int:
        return self.denominaiton


class Penny(Cash):
    def __init__(self):
        Cash.__init__(self, CASH.PENNY, 1)


class Nickel(Cash):
    def __init__(self):
        Cash.__init__(self, CASH.NICKEL, 5)


class Dime(Cash):
    def __init__(self):
        Cash.__init__(self, CASH.DIME, 10)


class Quarter(Cash):
    def __init__(self):
        Cash.__init__(self, CASH.QUARTER, 25)


# items.py


class ITEMS(Enum):
    COKE, PEPSI, SODA = 25, 20, 10


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


class Coke(Item):
    def __init__(self):
        Item.__init__(self, ITEMS.COKE, 25)


class Pepsi(Item):
    def __init__(self):
        Item.__init__(self, ITEMS.PEPSI, 35)


class Soda(Item):
    def __init__(self):
        Item.__init__(self, ITEMS.SODA, 45)


# exceptions.py


class ItemNotAvailableException(Exception):
    pass
class InsufficientCashExcepiton(Exception):
    pass
class ChangeNotAvailableException(Exception):
    pass
class ItemNotSelectedExcepiton(Exception):
    pass


# item_inventory.py
class ItemInventory:
    def __init__(self):
        self.items = dict()  # item->quantity

    def add_item(self, item: Item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def deduct_item(self, item: Item) -> bool:
        if self.is_item_available(item):
            self.items[item] -= 1
        else:
            raise ItemNotAvailableException(
                "Item Not Available at the moment. Come back later"
            )
    def is_item_available(self, item: Item):
        return (item in self.items) and (self.items[item] > 0)
    
    def display_inventory(self):
        print("\n===============[Inventory Content]=================")
        for k, v in self.items.items():
            print(f"{k.get_name()} ---> {v}")
        print("\n===================================================")

    def reset(self):
        self.inventory = dict()
        return


# inv = ItemInventory()
# inv.display_inventory()
# coke = Coke()
# pepsi = Pepsi()
# soda = Soda()
# inv.add_item(coke)
# inv.add_item(coke)
# inv.add_item(coke)
# inv.add_item(coke)
# inv.add_item(pepsi)
# inv.add_item(pepsi)
# inv.add_item(pepsi)
# inv.add_item(soda)
# inv.display_inventory()

# cash_inventory.py
class CahsInventory:
    def __init__(self):
        self.cash = dict()  # item.denomination->quantity

    def add_cash(self, cash: Cash):
        if cash.get_denomination() in self.cash:
            self.cash[cash.get_denomination()] += 1
        else:
            self.cash[cash.get_denomination()] = 1

    def deduct_cash(self, cash: Cash):
        if self.has_chash(cash):
            self.items[cash.get_denomination()] -= 1
        else:
            raise InsufficientCashExcepiton(
                "Cash Not Available. Thank you for the money :)"
            )
            
    def has_chash(self, cash):
        a =  (cash.get_denomination() in self.cash) 
        b = (self.cash[cash.get_denomination()] > 0)
        return a and b

    def get_change(self, balance: int):
        change = []
        while balance and len(self.cash) > 0:
            start_bal = balance
            if balance >= Quarter().get_denomination() and self.has_chash(Quarter()):
                change.append(Quarter())
                balance -= Quarter().get_denomination()
            elif balance >= Dime().get_denomination() and self.has_chash(Dime()):
                change.append(Dime())
                balance -= Dime().get_denomination()
            elif balance >= Nickel().get_denomination() and self.has_chash(Nickel()):
                change.append(Nickel())
                balance -= Nickel().get_denomination()
            elif balance >= Penny().get_denomination() and self.has_chash(Penny()):
                change.append(Penny())
                balance -= Penny().get_denomination()
            if start_bal == balance:
                break
        if balance != 0:
            raise InsufficientCashExcepiton(f'We dont have sufficient change right now. Please collect : {change}')
        return change
    
    def show_cash_inventory(self):
        print("\n===============[Cash Inventory]=================")
        for cash, val in self.cash.items():
            print(f' ${cash} --> {val}')
        print("\n===================================================")
        
                

# ci = CahsInventory()

# ci.add_cash(Penny())
# ci.add_cash(Penny())
# ci.add_cash(Penny())
# ci.add_cash(Penny())
# ci.add_cash(Nickel())
# ci.add_cash(Nickel())
# ci.add_cash(Nickel())
# ci.add_cash(Dime())
# ci.add_cash(Dime())
# ci.add_cash(Dime())
# ci.add_cash(Dime())
# ci.add_cash(Quarter())
# ci.add_cash(Quarter())
# ci.add_cash(Quarter())
# ci.show_cash_inventory()
# change = [x.get_denomination() for x in ci.get_change(12)]
# print(f'Here is your change for $12 sir: {change}')

from abc import ABC, abstractmethod

class VendingMachineState(ABC):
    def __init__(self, state):
        self.state = state
    
    @abstractmethod
    def insert_cash(self,cash: Cash):
        pass
    
    @abstractmethod
    def select_item(self,item: Item):
        pass
    
    @abstractmethod
    def proecss_request(self):
        pass
    
    @abstractmethod
    def cancel_request(self):
        pass
    
    @abstractmethod
    def dispatch_item_and_cash(self):
        pass
    
class ReadyState(VendingMachineState):
    def __init__(self, vending_machine):
        VendingMachineState.__init__(self,'READY STATE')
        self.vending_machine = vending_machine
        
    def insertCash(self,cash):
        self.vendingMachine.add_cash(cash)
        

    def select_item(self,item):
        self.vendingMachine.set_selected_item(item);

    def processRequest(self):
        self.vendingMachine.set_state(ProcessingState());
        self.vendingMachine.proecss_request()

    def cancelRequest(self):
        self.vendingMachine.set_state(CancelingState());
        self.vendingMachine.cancel_request()

class CancelingState(VendingMachineState):
    def __init__(self, vending_machine):
        VendingMachineState.__init__(self,'CANCEL STATE')
        self.vending_machine = vending_machine
        
    def cancel_request(self):
        pass
    
class ProcessingState(VendingMachineState):
    def __init__(self, vending_machine):
        VendingMachineState.__init__(self,'PROCESSING STATE')
        self.vending_machine = vending_machine
        
    def proecss_request(self):
        pass

class DispatchingState(VendingMachineState):
    def __init__(self, vending_machine):
        VendingMachineState.__init__(self,'DISPATCH STATE')
        self.vending_machine = vending_machine
        
    def dispatch_item_and_cash(self):
        pass
    

# Factory class to create instance of Vending Machine.
# this can be extended to create instance of
# different types of vending machines.
class VendingMachineFactory:
    def create_vending_machine(self):
        return VendingMachine()


class VendingMachine:
    def __init__(self):
        self.selected_item = None   # Item
        self.entered_cash = 0
        self.vending_machine_state = VendingMachineState
        self.item_inventory = ItemInventory()
        self.cash_inventory = CahsInventory()
        
    
    def add_item(self, item: Item):
        self.item_inventory.add_item(item)
    
    def deduct_item(self, item: Item):
        self.item_inventory.deduct_item(item)
    
    def add_cash(self, cash: Cash):
        self.cash_inventory.add_cash(cash)
    
    def deduct_cash(self, cash: Cash):
        self.cash_inventory.add_cash(cash)
        
    def get_entered_cash_value(self):
        return self.entered_cash
    
    def reset_entered_cash_value(self):
        self.entered_cash = 0
        
    def get_selected_item(self,item: Item):
        return self.selected_item
    
    def set_selected_item(self,item: Item):
        self.selected_item = item
    
    def reset_selected_item(self,item: Item):
        self.selected_item = item
        
    def is_selected_item_available(self, item:Item):
        return self.item_inventory.is_item_available(item)
    
    def is_change_available_for_entered_cash(self):
        balance = self.entered_cash - self.selected_item.get_price()
        if balance != 0:
            change = self.cash_inventory.get_change(balance)
            if change:
                return True
            else:
                return False
        return True

    def set_state(self, state : VendingMachineState):
        self.vending_machine_state = state
```
{% endtab %}
{% endtabs %}
