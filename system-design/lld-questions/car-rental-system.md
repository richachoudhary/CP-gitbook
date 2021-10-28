# Car Rental System

##

#### System Requirements:

* **Add/Remove/Edit vehicle:** To add, remove or modify a vehicle.
* **Search catalog:** To search for vehicles by type and availability.
* **Register new account/Cancel membership:** To add a new member or cancel an existing membership.
* **Reserve vehicle:** To reserve a vehicle.
* **Check-out vehicle:** To rent a vehicle.
* **Return a vehicle:** To return a vehicle which was checked-out to a member.
* **Add equipment:** To add an equipment to a reservation like navigation, child seat, etc.
* **Update car log:** To add or update a car log entry, such as refueling, cleaning, damage, etc.

#### **Classes**

**1.Constants ===============================================================**

* **BillItemType**
* **VehicleLogType**
* **CarType**
* **VehicleStatus**
* **ReservationStatus**
* **AccountStatus**
* **PaymentStatus**
* **Person**
  * name
  * address
  * email
  * phone

**2.Acc\_Types ===============================================================**

* **Account** - interface
  * password
  * name
  * email
  * reset\_password(self)
* **Customer(Account)**
  * total\_vehicles\_reserved
  * get\_reservations()

**3.Car Rental System ===============================================================**

* **CarRentalLocation**
  * name
  * location
  * get\_location
* **CarRentalSystem**
  * name
  * location
  * add\_new\_location(self, location)

**4.Vehicle ===============================================================**

* **Vehicle** : parent
  * license\_number
  * barcode status
  * model
  * manufacturing\_year
  * mileage
  * reserve\_vehicle()
  * return\_vehicle()
* **Car(Vehicle)**
* **Bike(Vehicle)**
* **VehicleReservation**
  * reservation\_number
  * creation\_date
  * status
  * due\_date
  * return\_date
  * pickup\_location\_name
  * return\_location\_name
  * customer\_id
  * vehicle
  * bill
  * additional\_drivers
  * insurances
  * fetch\_reservation\_details(reservation\_number)

**5.Search ===============================================================**

* \*\*Search : \*\*interface
  * search\_by\_type()
  * search\_by\_model()
* **VehicleInventory**
  * vehicle\_types
  * vehicle\_models
  * search\_by\_type()
  * search\_by\_model()

{% tabs %}
{% tab title="constants.py" %}
```python
from enum import Enum


class BillItemType(Enum):
    BASE_CHARGE, ADDITIONAL_SERVICE, FINE, OTHER = 1, 2, 3, 4


class VehicleLogType(Enum):
    ACCIDENT, FUELING, CLEANING_SERVICE, OIL_CHANGE, REPAIR, OTHER = 1, 2, 3, 4, 5, 6

class CarType(Enum):
    ECONOMY, COMPACT, INTERMEDIATE, STANDARD, FULL_SIZE, PREMIUM, LUXURY = 1, 2, 3, 4, 5, 6, 7


class VehicleStatus(Enum):
    AVAILABLE, RESERVED, LOANED, LOST, BEING_SERVICED, OTHER = 1, 2, 3, 4, 5, 6


class ReservationStatus(Enum):
    ACTIVE, PENDING, CONFIRMED, COMPLETED, CANCELLED, NONE = 1, 2, 3, 4, 5, 6


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5


class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETED, FILLED, DECLINED, CANCELLED, ABANDONED, SETTLING, SETTLED, REFUNDED = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


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
from abc import ABC
from .constants import AccountStatus


# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.


class Account:
    def __init__(self, id, password, status=AccountStatus.Active):
        self.__id = id
        self.__password = password
        self.__status = status

    def reset_password(self):
        None


# from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account


class Customer(Person):
    def make_booking(self, booking):
        None

    def get_bookings(self):
        None


class Admin(Person):
    def add_movie(self, movie):
        None

    def add_show(self, show):
        None


class Guest:
    def register_account(self):
        None
```
{% endtab %}

{% tab title="car_rental.py" %}
```python
class CarRentalLocation:
    def __init__(self, name, address):
        self.__name = name
        self.__location = address

    def get_location(self):
        return self.__location


class CarRentalSystem:
    def __init__(self, name):
        self.__name = name
        self.__locations = []

    def add_new_location(self, location):
        None
```
{% endtab %}

{% tab title="vehicle.py" %}
```python
from abc import ABC
from datetime import datetime
from .constants import ReservationStatus


class Vehicle(ABC):
    def __init__(self, license_num, stock_num, capacity, barcode, has_sunroof, status, model, make, manufacturing_year,
                 mileage):
        self.__license_number = license_num
        self.__barcode = barcode
        self.__status = status
        self.__model = model
        self.__manufacturing_year = manufacturing_year
        self.__mileage = mileage

    def reserve_vehicle(self):
        None

    def return_vehicle(self):
        None


class Car(Vehicle):
    def __init__(self, license_num, stock_num, capacity, barcode, has_sunroof, status, model, make, manufacturing_year,
                 mileage, type):
        super().__init__(license_num, stock_num, capacity, barcode,
                         has_sunroof, status, model, make, manufacturing_year, mileage)
        self.__type = type


class Bike(Vehicle):
    def __init__(self, license_num, stock_num, capacity, barcode, has_sunroof, status, model, make, manufacturing_year,
                 mileage, type):
        super().__init__(license_num, stock_num, capacity, barcode,
                         has_sunroof, status, model, make, manufacturing_year, mileage)
        self.__type = type


class VehicleReservation:
    def __init__(self, reservation_number):
        self.__reservation_number = reservation_number
        self.__creation_date = datetime.date.today()
        self.__status = ReservationStatus.ACTIVE
        self.__due_date = datetime.date.today()
        self.__return_date = datetime.date.today()
        self.__pickup_location_name = ""
        self.__return_location_name = ""

        self.__customer_id = 0
        self.__vehicle = None
        self.__bill = None
        self.__additional_drivers = []
        self.__insurances = []
        self.__equipments = []
        self.__services = []

    def fetch_reservation_details(self, reservation_number):
        None
```
{% endtab %}

{% tab title="search.py" %}
```python
from abc import ABC


class Search(ABC):
    def search_by_type(self, type):
        None

    def search_by_model(self, model):
        None


class VehicleInventory(Search):
    def __init__(self):
        self.__vehicle_types = {}
        self.__vehicle_models = {}

    def search_by_type(self, query):
        # return all vehicles of the given type.
        return self.__vehicle_types.get(query)

    def search_by_model(self, query):
        # return all vehicles of the given model.
        return self.__vehicle_models.get(query)
```
{% endtab %}

{% tab title="booking.py" %}
```python
from datetime import datetime
from .cinema import CinemaHallSeat


class Booking:
    def __init__(self, booking_number, number_of_seats, status, show, show_seats, payment):
        self.__booking_number = booking_number
        self.__number_of_seats = number_of_seats
        self.__created_on = datetime.date.today()
        self.__status = status
        self.__show = show
        self.__seats = show_seats
        self.__payment = payment

    def make_payment(self, payment):
        None

    def cancel(self):
        None

    def assign_seats(self, seats):
        None


class Payment:
    def __init__(self, amount, transaction_id, payment_status):
        self.__amount = amount
        self.__created_on = datetime.date.today()
        self.__transaction_id = transaction_id
        self.__status = payment_status
```
{% endtab %}
{% endtabs %}

##
