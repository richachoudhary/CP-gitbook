# Parking Lot

## 1. Parking Lot | `🟢Singleton| OpenClose | Builder`

#### System Requirements:

* **Take ticket:** To provide customers with a new parking ticket when entering the parking lot.
* **Scan ticket:** To scan a ticket to find out the total charge.
* **Make payment:** To pay the ticket fee with credit card
* **Add/Modify parking rate:** To allow admin to add or modify the hourly parking rate.

#### Out of Scope

* Termnial
* \------------------------EntryTerminal : Terminal (multiple entry points per floor)
* \------------------------ExitTerminal : Terminal (multiple exit points per floor)
* ParkingAssignmentStrategy # consider **multiple entries on each floor** - **nearest dist**/**closest elevators** on floors etc
* Logger # uses **Observer Pattern**

{% tabs %}
{% tab title="schema.txt" %}
```
Enum VehicleType
--------CAR
--------BIKE

Enum SpotType
--------FREE
--------TAKEN
--------RESERVED (?)

Vehicle                        # Open Close Priciple(S-O-LID)
--------id
--------license
--------generateID() # uuid

Car : Vehicle
--------type : VehicleType.CAR

Bike : Vehicle
--------type : VehicleType.BIKE

Spot
--------id = generateID()
--------type : SpotType
--------generateID()

Payment
--------mode
--------type : VehicleType
--------inTime
--------outTime
--------rate : { VehicleType : float} #map of key-val pair
--------amount = calculateAmount(inTime,outTime,vehicle_type)
--------getRate(type)
--------setRate(type)
--------calculateAmount(inTime,outTime,vehicle_type)

Enum TicketStatus
-------- ACTIVE
-------- COMPLETE

Ticket
--------id : generateID() # uuid
--------vehicle_type
--------status : TicketStatus
--------inTime : getCurrTime()
--------outTime
--------payment : Payment
--------spot    : Spot
--------generateID()

ParkingLevel
--------name
--------spots = {VehicleType.CAR: {SpotType.FREE: [], SpotType.TAKEN: []}
--------addSpot(VehicleType, number_of_spots) # create new spots on floor
--------assignSpot(ticket)
--------unassignSpot(ticket)

DisplayBoard
--------show(ParkingLot)

ParkingLot
--------id = generateID()
--------name
--------address
--------generateID()    # uuid
--------levels : [ParkingLevel]
--------addLevel(level)
--------processEntry(ticket)
--------processExit(ticket)


# Out of Scope:

Termial
EntryTerminal : Termial
ExitTerminal : Termial
ParkingAssignmentStrategy   # consider multiple entries on each floor - nearest dist/closes elevators on floors etc
Logger # uses Observer Pattern

# Notes:

* If you choose to make diff parking slots using some `enums` ; it'll voilate the **OPEN CLOSE PRICIPLE**
* => Hence; make an `interface` `Vehicle` & extend each type of new parking spot from it
    * `Car(Vehicle)`
    * `Bike(Vehicle)`
```
{% endtab %}

{% tab title="parking_lot.py" %}
```python
import time
import uuid
from enum import Enum

class VehicleType(Enum):
    CAR = 1
    BIKE = 2


class SpotType(Enum):
    FREE = 1
    TAKEN = 2


class Vehicle:
    def __init__(self, license):
        self.id = self.generateID()
        self.license = license

    def generateID(self):
        yield range(100)


class Car(Vehicle):
    def __init__(self, license):
        super().__init__(license)
        self.type = VehicleType.CAR


class Bike(Vehicle):
    def __init__(self, license):
        super().__init__(license)
        self.type = VehicleType.CAR


class Spot:
    def __init__(self, type):
        self.id = self.generateID()
        self.type = type

    def generateID(self):
        # yield range(100)
        return uuid.uuid4()


class Payment:
    def __init__(self, inTime, outTime, vehicle_type):
        self.mode = None
        self.rate = [30, 20, 10]  # assume same tarrif for all vehicles for now
        self.amount = self.calculateAmount(inTime, outTime, vehicle_type)

    def getRate(self):
        return self.rate

    def setRate(self, rate):
        self.rate = rate

    def calculateAmount(self, inTime, outTime, vehicle_type):
        amount = (outTime - inTime) * self.getRate()[0]
        amount += (
            (outTime - inTime - 60) * self.getRate()[1]
            if outTime - inTime - 60 > 0
            else 0
        )
        amount += (
            (outTime - inTime - 120) * self.getRate()[2]
            if outTime - inTime - 120 > 0
            else 0
        )
        return amount


class TicketStatus(Enum):
    ACTIVE = 1
    COMPLETE = 2


class Ticket:
    def __init__(self, vehicle_type):
        self.id = self.generateID()
        self.vehicle_type = vehicle_type
        self.status = TicketStatus.ACTIVE
        self.inTime = time.time()
        self.outTime = None
        self.payment = None
        self.spot = None

    def generateID(self):
        # some ID generation mechanism
        # yield range(100)
        return uuid.uuid4()

class ParkingLevel:
    def __init__(self, name):
        self.name = name
        self.spots = {
            VehicleType.CAR: {SpotType.FREE: [], SpotType.TAKEN: []},
            VehicleType.BIKE: {SpotType.FREE: [], SpotType.TAKEN: []},
        }

    def assignSpot(self, ticket):
        if self.spots[ticket.vehicle_type.type][SpotType.FREE] != []:
            spot = self.spots[ticket.vehicle_type.type][SpotType.FREE].pop()
            ticket.spot = spot
            self.spots[ticket.vehicle_type.type][SpotType.TAKEN].append(spot)
            return ticket.spot
        return False

    def unassignSpot(self, ticket):
        self.spots[ticket.vehicle_type.type][SpotType.FREE].append(ticket.spot)
        self.spots[ticket.vehicle_type.type][SpotType.TAKEN].remove(ticket.spot)

    def addSpot(self, type, license):
        for eachnum in range(license):
            spot = Spot(type)
            self.spots[type][SpotType.FREE].append(spot)

class DisplayBoard:
    def show(self, P):
        for eachlevel in P.levels:
            print(P.name, "-", eachlevel.name, "- Available Parking Spots")
            print("Car  : ", len(eachlevel.spots[VehicleType.CAR][SpotType.FREE]))
            print("Bike : ", len(eachlevel.spots[VehicleType.BIKE][SpotType.FREE]))

class ParkingLot:
    def __init__(self, name, address):
        self.id = self.generateID()
        self.name = name
        self.address = address
        self.levels = []

    def generateID(self):
        # yield range(100)
        return uuid.uuid4()

    def addLevel(self, level):
        self.levels.append(level)

    def processEntry(self, ticket):
        for eachlevel in self.levels:
            if eachlevel.spots[ticket.vehicle_type.type][SpotType.FREE]:
                ticket.spot = eachlevel.assignSpot(ticket)
                print("Entry Completed For : ", ticket.vehicle_type.license)
                break

    def processExit(self, ticket):
        for eachlevel in self.levels:
            if ticket.spot in eachlevel.spots[ticket.vehicle_type.type][SpotType.TAKEN]:
                eachlevel.unassignSpot(ticket)
                break
        ticket.outTime = time.time()
        ticket.spots = None
        ticket.status = TicketStatus.COMPLETE
        ticket.payment = Payment(ticket.inTime, ticket.outTime, ticket.vehicle_type)
        print(
            "Exit Completed For  : ",
            ticket.vehicle_type.license,
            " Pay : ",
            int(ticket.payment.amount),
        )


# ----------------------- RUNNING ---------------------- #

P = ParkingLot("Nathuram Parking Spot", "Great India Mall, New Delhi")
F1 = ParkingLevel("F1")
F1.addSpot(VehicleType.CAR, 3)
F1.addSpot(VehicleType.BIKE, 3)
P.addLevel(F1)

Board = DisplayBoard()
Board.show(P)

T1 = Ticket(Car("BH05 AB 5454"))
P.processEntry(T1)

T2 = Ticket(Bike("BH05 AB 9000"))
P.processEntry(T2)

time.sleep(2)
P.processExit(T2)

Board = DisplayBoard()
Board.show(P)
```
{% endtab %}
{% endtabs %}

#### 5.ParkingLot (main system class) ================================================

* **ParkingLot**
  * name
  * rates = \[]
  * `curr_vehicle_counts`
  * `curr_active_tickets = []`
  * `generate_new_parking_ticket()`
  * **NOTE!!!! Our system will have only one object of this class. This can be enforced by using the **[**Singleton**](https://en.wikipedia.org/wiki/Singleton\_pattern)** pattern**. 💫🟢🟢🟢🟢
    * **WHAT IS SINGLETON PATTERN:** is a software design pattern that\*\* restricts the instantiation of a class to only one object\*\*.
    * Everywhere: entry/exit || checkin/checkout:\*\* ONLY this object CAN create new parking ticket\*\*: using method `get_new_parking_ticket()`
* Code from Grokking - old .......\*\* DONT USE\*\*❌

{% tabs %}
{% tab title="constants.py" %}
```python
from enum import Enum

class VehicleType(Enum):
    CAR, BIKE, TRUCK, BUS  = 1, 2, 3,4

class ParkingSpotType(Enum):
    HANDICAPPED, COMPACT, REGULAR, LARGE = 1, 2, 3, 4

class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1, 2, 3
    # ELECTRIC -> ??

class Person():
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
```
{% endtab %}

{% tab title="account_types.py" %}
```python
from .constants import *

class Account:
    def __init__(self, user_name, password, person):
        self.__user_name = user_name
        self.__password = password
        self.__person = person

    def reset_password(self):
        None


class Admin(Account):
    def __init__(self, user_name, password, person):
        super().__init__(user_name, password, person)

    def add_parking_spot(self, floor_name, spot):
        None

class ParkingAttendant(Account):
    def __init__(self, user_name, password, person):
        super().__init__(user_name, password, person)

    def process_ticket(self, ticket_number):
        None
```
{% endtab %}

{% tab title="vehicles.py" %}
```python
from abc import ABC
from .constants import  *

class Vehicle(ABC):
    def __init__(self, license_number, vehicle_type, ticket=None):
        self.__license_number = license_number
        self.__type = vehicle_type
        self.__ticket = ticket

    def assign_ticket(self, ticket):
        self.__ticket = ticket


class Car(Vehicle):
    def __init__(self, license_number, ticket=None):
        super().__init__(license_number, VehicleType.CAR, ticket)


class Bike(Vehicle):
    def __init__(self, license_number, ticket=None):
        super().__init__(license_number, VehicleType.BIKE, ticket)


class Truck(Vehicle):
    def __init__(self, license_number, ticket=None):
        super().__init__(license_number, VehicleType.TRUCK, ticket)
```
{% endtab %}

{% tab title="parking_spot.py" %}
```python
from abc import ABC
from .constants import  *

class ParkingSpot(ABC):
    def __init__(self, number, parking_spot_type):
        self.__number = number
        self.__free = True
        self.__vehicle = None
        self.__parking_spot_type = parking_spot_type

    def is_free(self):
        return self.__free

    def assign_vehicle(self, vehicle):
        self.__vehicle = vehicle
        free = False

    def remove_vehicle(self):
        self.__vehicle = None
        free = True


class HandicappedSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.HANDICAPPED)


class CompactSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.COMPACT)


class RegularSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.REGULAR)
        
class LargeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.LARGE)
```
{% endtab %}

{% tab title="parking_lot.py🟢" %}
```python
import threading
from .constants import *

class ParkingLot:
    # singleton ParkingLot to ensure only one object of ParkingLot in the system,
    # all entrance panels will use this object to create new parking ticket: get_new_parking_ticket(),
    # similarly exit panels will also use this object to close parking tickets
    instance = None

    class __OnlyOne:
        def __init__(self, name, address):
        # 1. initialize variables: read name, address and parking_rate from database
        # 2. initialize parking floors: read the parking floor map from database,
        #    this map should tell how many parking spots are there on each floor. This
        #    should also initialize max spot counts too.
        # 3. initialize parking spot counts by reading all active tickets from database

            self.__name = name
            self.__address = address
            self.__parking_rate = ParkingRate()

            self.__compact_spot_count = 0
            self.__regular_spot_count = 0
            self.__large_spot_count = 0

            self.__max_compact_count = 0
            self.__max_regular_count = 0
            self.__max_large_count = 0

            # all active parking tickets, identified by their ticket_number
            self.__active_tickets = {}

            self.__lock = threading.Lock()

    def __init__(self, name, address):
        if not ParkingLot.instance:
            ParkingLot.instance = ParkingLot.__OnlyOne(name, address)
        else:
            ParkingLot.instance.__name = name
            ParkingLot.instance.__address = addres

    def get_new_parking_ticket(self, vehicle):
        if self.is_full(vehicle.get_type()):
            raise Exception('Parking full!')
            
    # synchronizing to allow multiple entrances panels to issue a new
    # parking ticket without interfering with each other
    
        self.__lock.acquire()
        
        ticket = ParkingTicket()
        vehicle.assign_ticket(ticket)
        ticket.save_in_DB()
        # if the ticket is successfully saved in the database, we can increment the parking spot count
        self.__increment_spot_count(vehicle.get_type())
        self.__active_tickets.put(ticket.get_ticket_number(), ticket)
        
        self.__lock.release()
        return ticket

    def is_full(self, type):
        # trucks and bus can only be parked in LargeSpot
        if type == VehicleType.Truck or type == VehicleType.Bus:
            return self.__large_spot_count >= self.__max_large_count

        # cars can be parked at compact or large spots
        if type == VehicleType.Car:
            return (self.__compact_spot_count + self.__large_spot_count) >= (self.__max_compact_count + self.__max_large_count)

        # bikes car can be parked at compact, regular or large spots
        return (self.__compact_spot_count + self.__regular_spot_count + self.__large_spot_count) >= (self.__max_compact_count + self.__max_regular_count
                                                                                                  + self.__max_large_count)

    # increment the parking spot count based on the vehicle type
    def increment_spot_count(self, type):
        large_spot_count = 0
        motorbike_spot_count = 0
        compact_spot_count = 0
        electric_spot_count = 0
        if type == VehicleType.Truck or type == VehicleType.Bus:
            large_spot_count += 1
        elif type == VehicleType.Car:
            regular_spot_count += 1
        else:  # bike
            if self.__compact_spot_count < self.__max_compact_count:
                compact_spot_count += 1
            elif self.__regular_spot_count < self.__max_regular_count:
                regular_spot_count += 1
            else:
                large_spot_count += 1
```
{% endtab %}
{% endtabs %}

##
