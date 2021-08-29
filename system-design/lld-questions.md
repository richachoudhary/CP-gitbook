# LLD:Questions

## \# Resources:

* Grokking OO Interview: [Git repo + solutions \(in python\)](https://github.com/tssovi/grokking-the-object-oriented-design-interview/tree/master/object-oriented-design-case-studies)

## 0. Template 🔖

```text
# Name: <app_name>

# Objective:

# Features:
* 

# ====================================================

# Classes: (nouns)

* class1
    * attr1
    * attr2
    * method1(attr1, attr2)
    * method2(attr1)

# ==================================================== [forSelf]

## Steps for LLD:

1. create Project in VSCode
2. `Req Gathering` create `design.md` file as ^
3. `Creating Frames` create all the empty classes & their attrs, methods; (some things might change during as interview discussion moves).
    * NOTE: add basic `doc_string` descripiton as many places as you can - leaves good impression
4. `Implementation + UnitTesting` : do your thing. Also introduce abstraction/inheritance etc as per the need.
    * NOTE: Splint the screen & keep `main.py` open on right(along with what you're coding on left) => to continueously checking for bugs & correctness(hence avoinding the rabbit-hole-debugging in the end)
5. `Run + Integration Tests + Edge Cases + Bonus Features`
6. `Writing UTs` : if time permits
```



## 1. Library Management System

#### System Requirements:

* **Add/Remove/Edit book:** To add, remove or modify a book or book item.
* **Search catalog:** To search books by title, author, subject or publication date.
* **Register new account/cancel membership:** To add a new member or cancel the membership of an existing member.
* **Check-out book:** To borrow a book from the library.
* **Reserve book:** To reserve a book which is not currently available.
* **Renew a book:** To re-borrow an already checked-out book.
* **Return a book:** To return a book to the library which was issued to a member.

#### Classes:

* **NOTE:** 
  * For simplicity, we are not defining getter and setter functions. 
  * **Assume** that: all class attributes are private and **accessed** through their respective **public getter methods** and **modified** only through their **public** **setter** methods function.
* **Models:  ============================================================**
* **BookReservation**
  * creation\_date
  * status
  * book\_item\_barcode
  * member\_id
  * fetch\_reservation\_details\(barcode\)
* **BookLending**
  * creation\_date
  * due\_date
  * return\_date
  * book\_item\_barcode
  * member\_id
  * lend\_book\(barcode, member\_id\)
  * fetch\_lending\_details\(barcode\)
* **Fine**
  * creation\_date
  * book\_item\_barcode
  * member\_id
  * collect\_fine\(member\_id, days\)
* **Book**
  * book\_id
  * title
  * subject
  * publisher
  * language
  * authors = \[\]
* **BookItem\(Book\)**
  * barcode
  * borrowed
  * due\_date
  * price
  * status
  * placed\_at
  * **checkout**\(member\_id\)
* **Reck** //optional
  * number 
  * location\_identifier
* **AccountTypes============================================================**
* **Account:**
  * id
  * pwd
  * status : ENUM\(ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE\)
  * Person :
* **Librarian\(Account\)**
  * add\_book\_item\(\)
* **Member\(Account\)**
  * date\_of\_membership
  * total\_books\_checkedout
  * get\_total\_books\_checkedout\(\)
  * **reserve\_book\_item**\(\)
  * increment\_total\_books\_checkedout\(\)
  * **renew\_book\_item**\(\)
  * **checkout\_book\_item**\(\)
  * check\_for\_fine\(\)
  * **return\_book\_item**\(\)
  * **renew\_book\_item**\(\)
* **Searching Books ============================================================**
  * **Search**
    * search\_by\_title\(\)
    * search\_by\_author\(\)
    * search\_by\_subject\(\)
    * search\_by\_pub\_date\(\)
  * **Catalog\(Search\)  -**-------&gt; implemented separately, as in future new search metrics might come up
    * search\_by\_title\(\)
    * search\_by\_author\(\)

{% tabs %}
{% tab title="constants.py" %}
```python
from abc import ABC
from enum import Enum

class BookFormat(Enum):
    HARDCOVER, PAPERBACK, AUDIO_BOOK, EBOOK, NEWSPAPER, MAGAZINE, JOURNAL = 1, 2, 3, 4, 5, 6, 7

class BookStatus(Enum):
    AVAILABLE, RESERVED, LOANED, LOST = 1, 2, 3, 4

class ReservationStatus(Enum):
    WAITING, PENDING, CANCELED, NONE = 1, 2, 3, 4

class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 4, 5

class Person(ABC):
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone

class Constants:
    def __init__(self):
      self.MAX_BOOKS_ISSUED_TO_A_USER = 5
      self.MAX_LENDING_DAYS = 10
```
{% endtab %}

{% tab title="models.py" %}
```python
from abc import ABC, abstractmethod
from .constants import *

class BookReservation:
    def __init__(self, creation_date, status, book_item_barcode, member_id):
        self.__creation_date = creation_date
        self.__status = status
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id

    def fetch_reservation_details(self, barcode):
        None


class BookLending:
    def __init__(self, creation_date, due_date, book_item_barcode, member_id):
        self.__creation_date = creation_date
        self.__due_date = due_date
        self.__return_date = None
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id

    def lend_book(self, barcode, member_id):
        None

    def fetch_lending_details(self, barcode):
        None


class Fine:
    def __init__(self, creation_date, book_item_barcode, member_id):
        self.__creation_date = creation_date
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id

    def collect_fine(self, member_id, days):
        None

class Book(ABC):
    def __init__(self, book_id, title, subject, publisher):
        self.__book_id = book_id
        self.__title = title
        self.__subject = subject
        self.__publisher = publisher
        self.__authors = []

class BookItem(Book):
    def __init__(self, barcode, is_reference_only, borrowed, due_date, price, book_format, status,
                 date_of_purchase, publication_date, placed_at):
        self.__barcode = barcode
        self.__is_reference_only = is_reference_only
        self.__borrowed = borrowed
        self.__due_date = due_date
        self.__price = price
        self.__status = status
        self.__placed_at = placed_at

    def checkout(self, member_id):
        if self.get_is_reference_only():
            print("self book is Reference only and can't be issued")
            return False
        if not BookLending.lend_book(self.get_bar_code(), member_id):
            return False
        self.update_book_item_status(BookStatus.LOANED)
        return True


class Rack:
    def __init__(self, number, location_identifier):
        self.__number = number
        self.__location_identifier = location_identifier

```
{% endtab %}

{% tab title="account\_types.py" %}
```python
from abc import ABC, abstractmethod
from datetime import datetime

from .constants import *
from .models import *

class Account(ABC):
    def __init__(self, id, password, person, status=AccountStatus.Active):
        self.__id = id
        self.__password = password
        self.__status = status
        self.__person = person

    def reset_password(self):
        None


class Librarian(Account):
    def __init__(self, id, password, person, status=AccountStatus.Active):
        super().__init__(id, password, person, status)

    def add_book_item(self, book_item):
        None

class Member(Account):
    def __init__(self, id, password, person, status=AccountStatus.Active):
        super().__init__(id, password, person, status)
        self.__date_of_membership = datetime.date.today()
        self.__total_books_checkedout = 0

    def get_total_books_checkedout(self):
        return self.__total_books_checkedout

    def reserve_book_item(self, book_item):
        None

    def increment_total_books_checkedout(self):
        None

    def renew_book_item(self, book_item):
        None

    def checkout_book_item(self, book_item):
        if self.get_total_books_checked_out() >= Constants.MAX_BOOKS_ISSUED_TO_A_USER:
            print("The user has already checked-out maximum number of books")
            return False
        
        book_reservation = BookReservation.fetch_reservation_details(book_item.get_barcode())
        
        if book_reservation != None and book_reservation.get_member_id() != self.get_id():
            # book item has a pending reservation from another user
            print("self book is reserved by another member")
            return False
        elif book_reservation != None:
            # book item has a pending reservation from the give member, update it
            book_reservation.update_status(ReservationStatus.COMPLETED)

        if not book_item.checkout(self.get_id()):
            return False

        self.increment_total_books_checkedout()
        return True

    def check_for_fine(self, book_item_barcode):
        book_lending = BookLending.fetch_lending_details(book_item_barcode)
        due_date = book_lending.get_due_date()
        today = datetime.date.today()
        # check if the book has been returned within the due date
        if today > due_date:
            diff = today - due_date
            diff_days = diff.days
            Fine.collect_fine(self.get_member_id(), diff_days)

    def return_book_item(self, book_item):
        self.check_for_fine(book_item.get_barcode())
        book_reservation = BookReservation.fetch_reservation_details(book_item.get_barcode())
        if book_reservation != None:
            # book item has a pending reservation
            book_item.update_book_item_status(BookStatus.RESERVED)
            book_reservation.send_book_available_notification()
            book_item.update_book_item_status(BookStatus.AVAILABLE)

    def renew_book_item(self, book_item):
        self.check_for_fine(book_item.get_barcode())
        book_reservation = BookReservation.fetch_reservation_details(
        book_item.get_barcode())
        # check if self book item has a pending reservation from another member
        if book_reservation != None and book_reservation.get_member_id() != self.get_member_id():
            print("self book is reserved by another member")
            self.decrement_total_books_checkedout()
            book_item.update_book_item_state(BookStatus.RESERVED)
            book_reservation.send_book_available_notification()
            return False
        elif book_reservation != None:
            # book item has a pending reservation from self member
            book_reservation.update_status(ReservationStatus.COMPLETED)

        BookLending.lend_book(book_item.get_bar_code(), self.get_member_id())
        book_item.update_due_date(datetime.datetime.now().AddDays(Constants.MAX_LENDING_DAYS))
        return True


```
{% endtab %}

{% tab title="search\_books.py" %}
```python
from abc import ABC

class Search(ABC):
    def search_by_title(self, title):
        None

    def search_by_author(self, author):
        None

    def search_by_subject(self, subject):
        None

    def search_by_pub_date(self, publish_date):
        None

class Catalog(Search):
    def __init__(self):
        self.__book_titles = {}
        self.__book_authors = {}
        self.__book_subjects = {}
        self.__book_publication_dates = {}

    def search_by_title(self, query):
        # return all books containing the string query in their title.
        return self.__book_titles.get(query)    #NOTE: assume DB connection

    def search_by_author(self, query):
        # return all books containing the string query in their author's name.
        return self.__book_authors.get(query)   #NOTE: assume DB connection 

```
{% endtab %}
{% endtabs %}

## 3. Amazon

#### System Requirements:

1. **Add/update products catalog**; Users should be able to add new products to sell.
2. **Search** for products by their name or category.
3. **Add/remove** product items in the **shopping cart**.
4. **Check-out to buy** product items in the **shopping cart**.
5. **Make a payment** to place an order.
6. **Add** a new **product category.**
7. Send notifications to members with **shipment updates.**

#### **Classes**

**1.Constants ===============================================================**

* **OrderStatus**: UNSHIPPED, PENDING, SHIPPED, COMPLETED, CANCELED, REFUND\_APPLIED
* **ShipmentStatus**: PENDING, SHIPPED, DELIVERE
* **PaymentStatus**: UNPAID, PENDING, COMPLETED, DECLINED, CANCELLED, REFUNDED

**2.Acc\_Types ===============================================================**

* **Account** - interface
  * user\_name 
  * password 
  * name 
  * email 
  * phone 
  * shipping\_address 
  * status 
  * add\_product\(self, product\)
  * add\_productReview\(self, review\)
  * reset\_password\(self\)
* **Customer\(Account\)**
  * get\_shopping\_cart\(self\)
  * add\_item\_to\_cart\(self, item\)
  * remove\_item\_from\_cart\(self, item\)
  * place\_order\(self, order\)
* **Guest\(Account\)**
  * register\(\)

**3.Products ===============================================================**

* **ProductCategory**
  * name
  * description
* **ProductReview**
  * rating
  * review
    * reviewer
* **Product**
  * product\_id
  * name
  * description
  * price
  * category
  * available\_item\_count
  * seller
  * get\_available\_count\(\)
  * update\_price\(price\)

**4.Search ===============================================================**

* **Search** : parent
  * search\_products\_by\_name\(self, name\)
  * search\_products\_by\_category\(self, category\)
* **Catalog\(Search\)**
  * product\_names
  * product\_categories
  * search\_products\_by\_name\(self, name\)
  * search\_products\_by\_category\(self, category\)

**5.Shopping ===============================================================**

* **Item**
  * product\_id
  * quantity
  * price
  * update\_quantity\(quantity\)
* **ShoppingCart**
  * items = \[\]
  * add\_item\(self, item\)
  * remove\_item\(self, item\)
  * update\_item\_quantity\(self, item, quantity\)
  * get\_items\(self\)
  * checkout\(self\)
* **Order**
  * order\_number
  * status
  * order\_date
  * order\_log = \[\]
  * send\_for\_shipment\(self\)
  * make\_payment\(self, payment\)
  * add\_order\_log\(self, order\_log\)
* **OrderLogs**
  * order\_number
  * creation\_date
  * status

**6.Shipment ===============================================================**

* **Shipment**
  * shipment\_number
  * shipment\_date
  * ETA
  * shipmentLogs . = \[\]
* **ShipmentLog**
  * shipment\_number
  * status
  * creation\_date
* **Notification**
  * notification\_id
  * created\_on
  * content
  * send\_notification\(account\)

{% tabs %}
{% tab title="constants.py" %}
```python
from enum import Enum

class OrderStatus(Enum):
    UNSHIPPED, PENDING, SHIPPED, COMPLETED, CANCELED, REFUND_APPLIED = 1, 2, 3, 4, 5, 6

class ShipmentStatus(Enum):
    PENDING, SHIPPED, DELIVERED = 1, 2, 3

class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETED, DECLINED, CANCELLED, REFUNDED = 1, 2, 3, 4, 5, 6

```
{% endtab %}

{% tab title="account\_types.py" %}
```python
from abc import ABC
from .constants import *


# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.

class Account:
    def __init__(self, user_name, password, name, email, phone, shipping_address, status=AccountStatus):
        self.__user_name = user_name
        self.__password = password
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__shipping_address = shipping_address

    def add_product(self, product):
        None

    def add_productReview(self, review):
        None

    def reset_password(self):
        None


class Customer(ABC):
    def __init__(self, cart, order):
        self.__cart = cart
        self.__order = order

    def get_shopping_cart(self):
        return self.__cart

    def add_item_to_cart(self, item):
        None

    def remove_item_from_cart(self, item):
        None
    def place_order(self, order):
        None


class Guest(Customer):
    def register_account(self):
        None

```
{% endtab %}

{% tab title="product.py" %}
```python
class ProductCategory:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description


class ProductReview:
    def __init__(self, rating, review, reviewer):
        self.__rating = rating
        self.__review = review
        self.__reviewer = reviewer


class Product:
    def __init__(self, id, name, description, price, category, seller_account):
        self.__product_id = id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__category = category
        self.__available_item_count = 0

        self.__seller = seller_account

    def get_available_count(self):
        return self.__available_item_count

    def update_price(self, new_price):
        None
```
{% endtab %}

{% tab title="search.py" %}
```python
from abc import ABC

class Search(ABC):
    def search_products_by_name(self, name):
        None

    def search_products_by_category(self, category):
        None


class Catalog(Search):
    def __init__(self):
        self.__product_names = {}
        self.__product_categories = {}

    def search_products_by_name(self, name):
        return self.product_names.get(name)

    def search_products_by_category(self, category):
        return self.product_categories.get(category)
```
{% endtab %}

{% tab title="shopping.py" %}
```python
from datetime import datetime
from .constants import *

class Item:
    def __init__(self, id, quantity, price):
        self.__product_id = id
        self.__quantity = quantity
        self.__price = price

    def update_quantity(self, quantity):
        None


class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        None

    def remove_item(self, item):
        None

    def update_item_quantity(self, item, quantity):
        None

    def get_items(self):
        return self.__items

    def checkout(self):
        None

class Order:
    def __init__(self, order_number, status=OrderStatus.PENDING):
        self.__order_number = 0
        self.__status = status
        self.__order_date = datetime.date.today()
        self.__order_log = []

    def send_for_shipment(self):
        None

    def make_payment(self, payment):
        None

    def add_order_log(self, order_log):
        None

class OrderLog:
    def __init__(self, order_number, status=OrderStatus.PENDING):
        self.__order_number = order_number
        self.__creation_date = datetime.date.today()
        self.__status = status
```
{% endtab %}

{% tab title="shipment.py" %}
```python
from abc import ABC
from datetime import datetime
from .constants import *

class Shipment:
    def __init__(self, shipment_number, shipment_method):
        self.__shipment_number = shipment_number
        self.__shipment_date = datetime.date.today()
        self.__estimated_arrival = datetime.date.today()
        self.__shipment_method = shipment_method
        self.__shipmentLogs = []

    def add_shipment_log(self, shipment_log):
        None

class ShipmentLog:
    def __init__(self, shipment_number, status=ShipmentStatus.PENDING):
        self.__shipment_number = shipment_number
        self.__status = status
        self.__creation_date = datetime.date.today()

class Notification(ABC):
    def __init__(self, id, content):
        self.__notification_id = id
        self.__created_on = datetime.date.today()
        self.__content = content

    def send_notification(self, account):
        None

```
{% endtab %}
{% endtabs %}

## 3. BookMyShow

#### System Requirements:

* **Search movies:** To search movies by title, genre, language, release date, and city name.
* **Create/Modify/View booking:** To book a movie show ticket, cancel it or view details about the show.
* **Make payment for booking:** To pay for the booking.
* **Add a coupon to the payment:** To add a discount coupon to the payment.
* **Assign Seat:** Customers will be shown a seat map to let them select seats for their booking.
* **Refund payment:** Upon cancellation, customers will be refunded the payment amount as long as the cancellation occurs within the allowed time frame.

#### **Classes**

**1.Constants ===============================================================**

* **BookingStatus**: PENDING, CONFIRMED, CHECKED\_IN, CANCELED
* **SeatType**:REGULAR, PREMIUM
* **PaymentStatus**: UNPAID, PENDING, COMPLETED, DECLINED, CANCELLED, REFUNDED

**2.Acc\_Types ===============================================================**

* **Account** - interface
  * password 
  * name 
  * email 
  * reset\_password\(self\)
* **Customer\(Account\)**
  * make\_booking\(self, booking\)
  * get\_bookings\(\)
* **Admin\(Account\)**
  * add\_movie\(self, movie\) 
  * add\_show\(self, show\)
* **Guest\(Account\)**
  * register\(\)

**3.Shows ===============================================================**

* **Show**
  * show\_id 
  * created\_on 
  * start\_time 
  * end\_time 
  * played\_at 
  * movie
* **Movie**
  * title 
  * description 
  * duration 
  * language
  * release\_date 
  * country 
  * genre 
  * shows = \[\]
  * get\_shows\(\)

**4.Cinema ===============================================================**

* **Search** : parent
  * search\_products\_by\_name\(self, name\)
  * search\_products\_by\_category\(self, category\)
* **Catalog\(Search\)**
  * product\_names
  * product\_categories
  * search\_products\_by\_name\(self, name\)
  * search\_products\_by\_category\(self, category\)

**5.Search ===============================================================**

* **Search :** interface
  * search\_by\_title\(self, title\)
  * search\_by\_language\(self, language\)
  * search\_by\_genre\(self, genre\)
  * search\_by\_city\(self, city\_name\)
* **Catalog**
  * movie\_titles = {}
  * movie\_languages = {}
  * movie\_genres = {}
  * movie\_release\_dates = {}
  * movie\_cities = {}
  * search\_by\_title\(self, title\) 
  * search\_by\_language\(self, language\) 
  * search\_by\_city\(self, city\_name\)

**6.Booking ===============================================================**

* **Booking**
  * booking\_number
  * number\_of\_seats
  * created\_on
  * status
  * show
  * seats
  * payment
  * make\_payment\(self, payment\)
  * cancel\(self\)
  * assign\_seats\(self, seats\)
* **Payment**
  * amount
  * created\_on
  * transaction\_id
  * status

{% tabs %}
{% tab title="constants.py" %}
```python
from enum import Enum

class BookingStatus(Enum):
    PENDING, CONFIRMED, CHECKED_IN, CANCELED = 1, 2, 3, 4

class SeatType(Enum):
    REGULAR, PREMIUM = 1, 2

class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETED, DECLINED, CANCELLED, REFUNDED = 1, 2, 3, 4, 5, 6

```
{% endtab %}

{% tab title="account\_types.py" %}
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

{% tab title="show.py" %}
```python
from datetime import datetime

class Show:
    def __init__(self, id, played_at, movie, start_time, end_time):
        self.__show_id = id
        self.__created_on = datetime.date.today()
        self.__start_time = start_time
        self.__end_time = end_time
        self.__played_at = played_at
        self.__movie = movie


class Movie:
    def __init__(self, title, description, duration_in_mins, language, release_date, country, genre, added_by):
        self.__title = title
        self.__description = description
        self.__duration_in_mins = duration_in_mins
        self.__language = language
        self.__release_date = release_date
        self.__country = country
        self.__genre = genre

        self.__shows = []

    def get_shows(self):
        None
```
{% endtab %}

{% tab title="cinema.py" %}
```python
class City:
    def __init__(self, name, state, zip_code):
        self.__name = name
        self.__state = state
        self.__zip_code = zip_code

class Cinema:
    def __init__(self, name, total_cinema_halls, address, halls):
        self.__name = name
        self.__location = address

        self.__halls = halls


class CinemaHall:
    def __init__(self, name, total_seats, seats, shows):
        self.__name = name
        self.__total_seats = total_seats

        self.__seats = seats
        self.__shows = shows


class CinemaHallSeat:
    def __init__(self, id, seat_type):
        self.__hall_seat_id = id
        self.__seat_type = seat_type
```
{% endtab %}

{% tab title="search.py" %}
```python
from abc import ABC

class Search(ABC):
    def search_by_title(self, title):
        None

    def search_by_language(self, language):
        None

    def search_by_genre(self, genre):
        None

    def search_by_city(self, city_name):
        None


class Catalog(Search):
    def __init__(self):
        self.__movie_titles = {}
        self.__movie_languages = {}
        self.__movie_genres = {}
        self.__movie_release_dates = {}
        self.__movie_cities = {}

        def search_by_title(self, title):
            return self.__movie_titles.get(title)

        def search_by_language(self, language):
            return self.__movie_languages.get(language)

        def search_by_city(self, city_name):
            return self.__movie_cities.get(city_name)
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

## 4. Parking Lot \| `Singleton🟢`

#### System Requirements:

* **Take ticket:** To provide customers with a new parking ticket when entering the parking lot.
* **Scan ticket:** To scan a ticket to find out the total charge.
* **Make payment:** To pay the ticket fee with credit card
* **Add/Modify parking rate:** To allow admin to add or modify the hourly parking rate.

#### Out of Scope

* **Add/Remove/Edit parking floor:** To add, remove or modify a parking floor from the system. Each floor can have its own display board to show free parking spots.
* **Add/Remove/Edit parking spot:** To add, remove or modify a parking spot on a parking floor.
* **Add/Remove a parking attendant:** To add or remove a parking attendant from the system.
* **3rd party payment integration**

**Classes:**

**1.Constants =================================================================**

* **VehicleTypes**: CAR, BIKE, TRUCK
* **ParkingSpotType:HANDICAPPED**, COMPACT, REGULAR, LARGE
* **ParkingTicketStatus**: ACTIVE, PAID, LOST
* **Person**
  * name
  * address
  * email
  * phone

**2.Acc Types =================================================================**

* **Account** : interface
  * name
  * password
  * person 
  * reset\_pwd\(\)
* **Admin\(Account\)**
  * `add`\_`parking_spot(spot)`
* **ParkingAttendent\(Account\)**
  * `process_ticket(ticket_number )`
* **User\(Account\)**

#### 3.Vehicles ===================================================================

* **Vehicle** : interface
  * id
  * type
  * ticket
  * license\_number
  * assign\_ticket\(\)
* **Car\(Vehicle\)**
* **Bike\(Vehicle\)**
* **Truck\(Vehicle\)**

#### 4.ParkingSpots ===============================================================

* **ParkingSpot :** interface
  * number
  * free:bool
  * vehicle: Vehicle
  * type
  * is\_free\(\)
  * assign\_vehicle\(\)
  * remove\_vehicle\(\)
* **HandicappedSpot\(ParkingSpot\)**
* **CompactSpot\(ParkingSpot\)**
* **RegularSpot\(ParkingSpot\)**
* **LargeSpot\(ParkingSpot\)**

#### 5.ParkingLot \(main system class\) ================================================

* **ParkingLot**
  * name
  * rates = \[\]
  * `curr_vehicle_counts`
  * `curr_active_tickets = []`
  * `generate_new_parking_ticket()`
  * **NOTE!!!!** Our system will have only **one object of this class**. This can be enforced by using the [**Singleton**](https://en.wikipedia.org/wiki/Singleton_pattern) **pattern**. 💫🟢🟢🟢🟢
    * **WHAT IS SINGLETON PATTERN:** is a software design pattern that **restricts the instantiation of a class to only one object**.
    * Everywhere: entry/exit \|\| checkin/checkout: **ONLY this object CAN create new parking ticket**: using method `get_new_parking_ticket()`

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

{% tab title="account\_types.py" %}
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

{% tab title="parking\_spot.py" %}
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

{% tab title="parking\_lot.py🟢" %}
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

## 5. ATM

#### System Requirements:

1. **Balance inquiry:** To see the amount of funds in each account.
2. **Deposit cash:** To deposit cash.
3. **Deposit check:** To deposit checks.
4. **Withdraw cash:** To withdraw money from their checking account.
5. **Transfer funds:** To transfer funds to another account.

#### **Classes**

**1.Constants ===============================================================**

* **TransactionType**: BALANCE\_INQUIRY, DEPOSIT\_CASH, DEPOSIT\_CHECK, WITHDRAW, TRANSFER
* **TransactionStatus**: SUCCESS, FAILURE, NONE
* **CustomerStatus:ACTIVE**, BLOCKED, UNKNOWN

**2.Customer ===============================================================**

* **Customer** 
  * name 
  * address 
  * email 
  * phone 
  * status 
  * card
  * account
  * make\_transaction\(self, transaction\) 
  * get\_billing\_address\(self\)
* **Card**
  * card\_number 
  * customer\_name 
  * card\_expiry 
  * pin
* **Account**
  * account\_number 
  * total\_balance = 0.0 
  * available\_balance = 0.0

**3.Bank ===============================================================**

* **Bank**
  * name
  * ifsc
  * install\_atm\(atm\)
* **ATM**
  * atm\_id 
  * location
  * cash\_dispenser
  * cash\_deposit
  * authenticate\_user\(self\) 
  * make\_transaction\(self, customer, transaction\)
* **CashDispenser**
  * total\_amount
  * is\_healthy\(\)
  * dispense\_cash\(self, amount\)
* **CashDeposit**
  * total\_amount
  * is\_healthy\(\)
  * deposit\_cash\(self, amount\)

**4.Transaction ===============================================================**

* **Transaction :** interface
  * transaction\_id 
  * creation\_time 
  * status
  * make\_transation\(\)
* **BalanceInquiry\(Transaction\)** 
* **Deposit\(Transaction\)** 
  * amount
  * get\_amount\(\)
* **CheckDeposit\(Deposit\)** 
* **CashDeposit\(Deposit\)** 
* **Transfer\(Transaction\)**
  * destination\_account\_number
  * get\_destination\_account\(\)

{% tabs %}
{% tab title="constants.py" %}
```python
from enum import Enum

class TransactionType(Enum):
    BALANCE_INQUIRY, DEPOSIT_CASH, DEPOSIT_CHECK, WITHDRAW, TRANSFER = 1, 2, 3, 4, 5

class TransactionStatus(Enum):
    SUCCESS, FAILURE, NONE = 1, 2, 3

class CustomerStatus(Enum):
    ACTIVE, BLOCKED, UNKNOWN = 1, 2, 3

```
{% endtab %}

{% tab title="customer.py" %}
```python
class Customer:
    def __init__(self, name, address, email, phone, status):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = status
        self.__card = Card()
        self.__account = Account

    def make_transaction(self, transaction):
        None

    def get_billing_address(self):
        None

class Card:
    def __init__(self, number, customer_name, expiry, pin):
        self.__card_number = number
        self.__customer_name = customer_name
        self.__card_expiry = expiry
        self.__pin = pin

    def get_billing_address(self):
        None

class Account:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__total_balance = 0.0
        self.__available_balance = 0.0

    def get_available_balance(self):
        return self.__available_balance


```
{% endtab %}

{% tab title="bank.py" %}
```python
from abc import ABC

class Bank:
  def __init__(self, name, bank_code):
    self.__name = name
    self.__bank_code = bank_code

  def get_bank_code(self):
    return self.__bank_code

  def add_atm(self, atm):
    None

class ATM:
  def __init__(self, id, location):
    self.__atm_id = id
    self.__location = location
    self.__cash_dispenser = CashDispenser()
    self.__cash_deposit = CashDeposit()


  def authenticate_user(self):
    None

  def make_transaction(self, customer, transaction):
    None
  
class CashDispenser:
  def __init__(self):
    self.__total_amount = 0.0

  def dispense_cash(self, amount):
    None

  def is_healthy(self):
    None
    
class CashDeposit:
  def __init__(self):
    self.__total_amount = 0.0

  def deposit_cash(self):
    None
  def is_healthy(self):
    None

```
{% endtab %}

{% tab title="transactions.py" %}
```python
from abc import ABC


class Transaction(ABC):
    def __init__(self, id, creation_date, status):
        self.__transaction_id = id
        self.__creation_time = creation_date
        self.__status = status

    def make_transation(self):
        None


class BalanceInquiry(Transaction):
    def __init__(self, account_id):
        self.__account_id = account_id

    def get_account_id(self):
        return self.__account_id


class Deposit(Transaction):
    def __init__(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount


class CheckDeposit(Deposit):
    def __init__(self, check_number, bank_code):
        self.__check_number = check_number
        self.__bank_code = bank_code

    def get_check_number(self):
        return self.__check_number


class CashDeposit(Deposit):
    def __init__(self, cash_deposit_limit):
        self.__cash_deposit_limit = cash_deposit_limit


class Withdraw(Transaction):
    def __init__(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount


class Transfer(Transaction):
    def __init__(self, destination_account_number):
        self.__destination_account_number = destination_account_number

    def get_destination_account(self):
        return self.__destination_account_number

```
{% endtab %}
{% endtabs %}

## 6. Airline Management System

#### System Requirements:

* **Search Flights:** To search the flight schedule to find flights for a suitable date and time.
* **Create/Modify/View reservation:** To reserve a ticket, cancel it, or view details about the flight or ticket.
* **Assign seats to passengers:** To assign seats to passengers for a flight instance with their reservation.
* **Make payment for a reservation:** To pay for the reservation.
* **Update flight schedule:** To make changes in the flight schedule, and to add or remove any flight.
* **Assign pilots and crew:** To assign pilots and crews to flights.

#### **Classes**

**1.Constants ===============================================================**

* **FlightStatus**: PENDING, CONFIRMED, CHECKED\_IN, CANCELED
* **PaymentStatus**  :REGULAR, PREMIUM
* **ReservationStatus** : UNPAID, PENDING, COMPLETED, DECLINED, CANCELLED, REFUNDED
* **SeatClass** : 
* **SeatType** : 

**2.Accounts ===============================================================**

* **Account** - interface
  * password 
  * name 
  * status 
  * reset\_password\(self\)
* **Customer**
  * name 
  * address 
  * email 
  * phone 
  * account
* **Admin\(Account\)**
  * add\_movie\(self, movie\) 
  * add\_show\(self, show\)
* **Passenger\(Customer\)**
  * passport\_number
  * get\_passport\_number\(\)

**3.Airport ===============================================================**

* **Airport**
  * name 
  * address 
  * code
  * get\_flights\(\) 
* **Aircraft**
  * name 
  * model 
  * manufacturing\_year 
  * seats = \[\]
  * get\_flights\(\)
* **Seat**
  * seat\_number 
  * type 
  * seat\_class
* **FlightSeat**
  * fare

**4.Airline Manager==============================================================**

* **Flight** : 
  * flight\_number 
  * departure 
  * arrival 
  * schedule = \[\]
* **FlightReservation**
  * reservation\_number 
  * flight 
  * seat\_map 
  * creation\_date 
  * status
  * fetch\_reservation\_details\(self, reservation\_number\) 
  * get\_passengers\(self\)
* **Itinerary**
  * customer\_id 
  * starting\_airport 
  * final\_airport 
  * creation\_date 
  * reservations = \[\]
  * get\_reservations\(self\) 
  * make\_reservation\(self\) 
  * make\_payment\(self\)

{% tabs %}
{% tab title="constants.py" %}
```python
from enum import Enum

class FlightStatus(Enum):
    ACTIVE, SCHEDULED, DELAYED, DEPARTED, LANDED, IN_AIR = 1, 2, 3, 4, 5, 6, 7


class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETED, CANCELLED, SETTLING, REFUNDED = 1, 2, 3, 4, 5, 6


class ReservationStatus(Enum):
    PENDING, CONFIRMED, CHECKED_IN, CANCELLED = 1, 2, 3, 4

class SeatClass(Enum):
    ECONOMY BUSINESS = 1, 2


class SeatType(Enum):
    REGULAR, EMERGENCY_EXIT, EXTRA_LEG_ROOM = 1, 2, 3
```
{% endtab %}

{% tab title="account.py" %}
```python
from abc import ABC
from .constants import *


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


class Customer(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account

class Passenger(Customer):
    def __init__(self, name, passport_number):
        self.__passport_number = passport_number

    def get_passport_number(self):
        return self.__passport_number
```
{% endtab %}

{% tab title="airport.py" %}
```python
class Airport:
    def __init__(self, name, address, code):
        self.__name = name
        self.__address = address
        self.__code = code

    def get_flights(self):
        None


class Aircraft:
    def __init__(self, name, model, manufacturing_year):
        self.__name = name
        self.__model = model
        self.__manufacturing_year = manufacturing_year
        self.__seats = []

    def get_flights(self):
        None


class Seat:
    def __init__(self, seat_number, type, seat_class):
        self.__seat_number = seat_number
        self.__type = type
        self.__seat_class = seat_class


class FlightSeat(Seat):
    def __init__(self, fare):
        self.__fare = fare

    def get_fare(self):
        return self.__fare
```
{% endtab %}

{% tab title="airline\_manager.py" %}
```python
class Flight:
    def __init__(self, flight_number, departure, arrival, duration_in_minutes):
        self.__flight_number = flight_number
        self.__departure = departure
        self.__arrival = arrival

        self.__schedule = []

class FlightReservation:
    def __init__(self, reservation_number, flight, aircraft, creation_date, status):
        self.__reservation_number = reservation_number
        self.__flight = flight
        self.__seat_map = {}
        self.__creation_date = creation_date
        self.__status = status

    def fetch_reservation_details(self, reservation_number):
        None

    def get_passengers(self):
        None


class Itinerary:
    def __init__(self, customer_id, starting_airport, final_airport, creation_date):
        self.__customer_id = customer_id
        self.__starting_airport = starting_airport
        self.__final_airport = final_airport
        self.__creation_date = creation_date
        self.__reservations = []

    def get_reservations(self):
        None

    def make_reservation(self):
        None

    def make_payment(self):
        None

```
{% endtab %}
{% endtabs %}

## 7. Stocks Exchange \| `Singleton🟢`

#### System Requirements:

* **Register new account/Cancel membership:** To add a new member or cancel the membership of an existing member.
* **Add/Remove/Edit watchlist:** To add, remove or modify a watchlist.
* **Search stock inventory:** To search for stocks by their symbols.
* **Place order:** To place a buy or sell order on the stock exchange.
* **Cancel order:** Cancel an already placed order.
* **Deposit/Withdraw money:** Members can deposit or withdraw money via check, wire or electronic bank transfer.

**Classes:**

**1.Constants =================================================================**

* **ReturnStatus**: SUCCESS, FAIL, INSUFFICIENT\_FUNDS, NO\_STOCK\_AVAILABLE
* **OrderStatus** :OPEN, FILLED, PARTIALLY\_FILLED, CANCELLED
* **TimeBoundOrderType**  : GOOD\_TILL\_CANCELLED, IMMEDIATE\_OR\_CANCEL, ON\_MARKET\_OPEN, ON\_MARKET\_CLOSE
* **AccountStatus** : ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE

**2.Orders =================================================================**

* **Order** : interface
  * order\_id 
  * is\_buy\_order 
  * status 
  * `time_bounder_order_type` 
  * creation\_time
  * set\_status\(self, status\) 
  * save\_in\_DB\(self\) 
  * add\_order\_parts\(self, parts\)
  * cancel\_order\(\)
  * ~~place\_order\(\)~~ =&gt; Not placed here\(placed in **stock\_exchang** as **SINGLETON**\)
* **LimitOrder\(Order\)**
  * price\_limit = 0.0

#### 3.Stock Exchange ===================================================================

* **StockExchange** : singleton🟢
  * **`place_order()`** : the only place at which orders can be placed

#### 4.Members ===============================================================

* **Account:** interface
  * id
  * password 
  * name 
  * email 
  * phone 
  * status : AccountStatus.NONE
  * reset\_password\(\)
* **Member\(Account\)**
  * available\_funds\_for\_trading = 0.0 
  * date\_of\_membership 
  * stock\_positions = {} 
  * active\_orders = {}
  * place\_sell\_limit\_order\(self, stock\_id, quantity, limit\_price, enforcement\_type\)
  * callback\_stock\_exchange\(self, order\_id, order\_parts, status\)
    * this function will be invoked whenever there is an update from stock exchange against an order

{% tabs %}
{% tab title="constants.py" %}
```python
from enum import Enum


class ReturnStatus(Enum):
    SUCCESS, FAIL, INSUFFICIENT_FUNDS, NO_STOCK_AVAILABLE = 1, 2, 3, 4


class OrderStatus(Enum):
    OPEN, FILLED, PARTIALLY_FILLED, CANCELLED = 1, 2, 3, 4


class TimeBoundOrderType(Enum):
    GOOD_TILL_CANCELLED, IMMEDIATE_OR_CANCEL, ON_THE_OPEN, ON_MARKET_CLOSE = 1, 2, 3, 4, 5


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 5
```
{% endtab %}

{% tab title="order.py" %}
```python
from abc import ABC
from datetime import datetime
from .constants import OrderStatus, TimeBoundOrderType


class Order(ABC):
    def __init__(self, id):
        self.__order_id = id
        self.__is_buy_order = False
        self.__status = OrderStatus.OPEN
        self.__time_enforcement = TimeBoundOrderType.ON_THE_OPEN
        self.__creation_time = datetime.now()

        self.__parts = {}

    def set_status(self, status):
        self.status = status

    def save_in_DB(self):
        None

    # save in the database

    def add_order_parts(self, parts):
        for part in parts:
            self.parts[part.get_id()] = part


class LimitOrder(Order):
    def __init__(self):
        self.__price_limit = 0.0from .order import Order


class StockExchange:
    # singleton, used for restricting to create only one instance
    instance = None

    class __OnlyOne:
        def __init__(self):
            None

    def __init__(self):
        if not StockExchange.instance:
            StockExchange.instance = StockExchange.__OnlyOne()

    def place_order(self, order):
        return_status = self.get_instance().submit_order(Order)
        return return_status

```
{% endtab %}

{% tab title="stock\_exchange.py🟢" %}
```python
from .order import Order


class StockExchange:
    # singleton, used for restricting to create only one instance
    instance = None

    class __OnlyOne:
        def __init__(self):
            None

    def __init__(self):
        if not StockExchange.instance:
            StockExchange.instance = StockExchange.__OnlyOne()

    # the only place to place an order
    def place_order(self, order):
        return_status = self.get_instance().submit_order(Order)
        return return_status

```
{% endtab %}

{% tab title="members.py" %}
```python
from datetime import datetime
from abc import ABC
from .constants import OrderStatus, AccountStatus, ReturnStatus
from .order import LimitOrder
from .stock_exchange import StockExchange


class Account(ABC):
    def __init__(self, id, password, name, address, email, phone, status=AccountStatus.NONE):
        self.__id = id
        self.__password = password
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = AccountStatus.NONE

    def reset_password(self):
        None


class Member(Account):
    def __init__(self):
        self.__available_funds_for_trading = 0.0
        self.__date_of_membership = datetime.date.today()
        self.__stock_positions = {}
        self.__active_orders = {}

    def place_sell_limit_order(self, stock_id, quantity, limit_price, enforcement_type):
        # check if member has this stock position
        if stock_id not in self.__stock_positions:
            return ReturnStatus.NO_STOCK_POSITION

        stock_position = self.__stock_positions[stock_id]
        # check if the member has enough quantity available to sell
        if stock_position.get_quantity() < quantity:
            return ReturnStatus.INSUFFICIENT_QUANTITY

        order = LimitOrder(stock_id, quantity, limit_price, enforcement_type)
        order.is_buy_order = False
        order.save_in_DB()
        success = StockExchange.place_order(order)
        if not success:
            order.set_status(OrderStatus.FAILED)
            order.save_in_DB()
        else:
            self.active_orders.add(order.get_order_id(), order)
        return success


    # this function will be invoked whenever there is an update from
    # stock exchange against an order
    def callback_stock_exchange(self, order_id, order_parts, status):
        order = self.active_orders[order_id]
        order.add_order_parts(order_parts)
        order.set_status(status)
        order.update_in_DB()

        if status == OrderStatus.FILLED or status == OrderStatus.CANCELLEd:
            self.active_orders.remove(order_id)

```
{% endtab %}
{% endtabs %}

## 8. Car Rental System

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
  * reset\_password\(self\)
* **Customer\(Account\)**
  * total\_vehicles\_reserved
  * get\_reservations\(\)

**3.Car Rental System ===============================================================**

* **CarRentalLocation** 
  * name 
  * location
  * get\_location
* **CarRentalSystem**
  * name
  * location
  * add\_new\_location\(self, location\)

**4.Vehicle ===============================================================**

* **Vehicle** : parent
  * license\_number
  *  barcode status 
  * model 
  * manufacturing\_year 
  * mileage
  * reserve\_vehicle\(\)
  * return\_vehicle\(\)
* **Car\(Vehicle\)**
* **Bike\(Vehicle\)**
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
  * fetch\_reservation\_details\(reservation\_number\)

**5.Search ===============================================================**

* **Search :** interface
  * search\_by\_type\(\) 
  * search\_by\_model\(\)
* **VehicleInventory**
  * vehicle\_types 
  * vehicle\_models
  * search\_by\_type\(\) 
  * search\_by\_model\(\)

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

{% tab title="account\_types.py" %}
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

{% tab title="car\_rental.py" %}
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

## 9. LinkedIn

#### System Requirements:

* **Add/update profile:** Any member should be able to create their profile to reflect their experiences, education, skills, and accomplishments.
* **Search:** Members can search other members, companies or jobs. Members can send a connection request to other members.
* **Follow or Unfollow member or company:** Any member can follow or unfollow any other member or a company.
* **Send message:** Any member can send a message to any of their connections.
* **Create post:** Any member can create a post to share with their connections, as well as like other posts or add comments to any post.
* **Send notifications:** The system will be able to send notifications for new messages, connection invites, etc.

#### **Classes**

**1.Constants ===============================================================**

* **ConnectionInvitationStatus**: PENDING, ACCEPTED, CONFIRMED, REJECTED, CANCELED
* **AccountStatus**: ACTIVE, BLOCKED, UNKNOWN

**2.Profile ===============================================================**

* **Profile** 
  * summary 
  * experiences 
  * educations 
  * skills 
  * accomplishments 
  * recommendations
  * add\_experience\(self, experience\) 
  * add\_education\(self, education\) 
  * add\_skill\(self, skill\) 
  * add\_accomplishment\(self, accomplishment\)
* **Experience**
  * title 
  * company 
  * location 
  * from 
  * to 
  * description

**3.Acc\_Types ===============================================================**

* **Account** 
  * id 
  * password 
  * status
  * reset\_password
* **Person**
  * name 
  * address 
  * email 
  * phone account
* **Member\(Person\)**
  * date\_of\_membership
  * headline
  * photo
  * member\_follows
  * member\_connections
  * company\_follows
  * group\_follows
  * profile
  * send\_message\(self, message\)
  * create\_post\(self, post\)
  * send\_connection\_invitation\(self, connection\_invitation\)
  * block\_user\(self, customer\)
  * unblock\_user\(self, customer\)

**4.Company ===============================================================**

* **Company** : 
  *  name
  * description
  * type
  * company\_size
  * active\_job\_postings
* **JobPosting**
  * date\_of\_posting
  * description
  * employment\_type
  * location
  * is\_fulfilled
* **Bike\(Vehicle\)**
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
  * fetch\_reservation\_details\(reservation\_number\)

**5.Messagin & Posting=============================================================**

* **Group :** 
  * name
  * description
  * total\_members
  * members = \[\]
* **Post**
  * text 
  * total\_likes
  * total\_shares 
  * owner
* **Message**
  * sent\_to 
  * message\_body 
  * media

**6.Searching =============================================================**

* **Search :** 
  * search\_member\(self, name\) 
  * search\_company\(self, name\) 
  * search\_job\(self, title\)
* **SearchIndex\(Search\):**
  * member\_names 
  * company\_names 
  * job\_titles
  * search\_member\(self, name\) 
  * search\_company\(self, name\) 
  * search\_job\(self, title\)

{% tabs %}
{% tab title="constants.py" %}
```python
from enum import Enum

class ConnectionInvitationStatus(Enum):
    PENDING, ACCEPTED, CONFIRMED, REJECTED, CANCELED = 1, 2, 3, 4, 5

class AccountStatus(Enum):
    ACTIVE, BLOCKED, UNKNOWN = 1, 2, 3, 4, 5, 6
```
{% endtab %}

{% tab title="profile.py" %}
```python
class Profile:
    def __init__(self, summary, experiences, educations, skills, accomplishments, recommendations):
        self.__summary = summary
        self.__experiences = experiences
        self.__educations = educations
        self.__skills = skills
        self.__accomplishments = accomplishments

    def add_experience(self, experience):
        None

    def add_education(self, education):
        None

    def add_skill(self, skill):
        None

    def add_accomplishment(self, accomplishment):
        None

class Experience:
    def __init__(self, title, company, location, date_from, date_to, description):
        self.__title = title
        self.__company = company
        self.__location = location
        self.__from = date_from
        self.__to = date_to
        self.__description = description

```
{% endtab %}

{% tab title="acc\_type.py" %}
```python
from abc import ABC
from datetime import datetime
from .constants import AccountStatus
from .profile import Profile


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


class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account


class Member(Person):
    def __init__(self):
        self.__date_of_membership = datetime.date.today()
        self.__headline = ""
        self.__photo = []
        self.__member_follows = []
        self.__member_connections = []
        self.__company_follows = []
        self.__group_follows = []
        self.__profile = Profile()

    def send_message(self, message):
        None

    def create_post(self, post):
        None

    def send_connection_invitation(self, connection_invitation):
        None


class Admin(Person):
    def block_user(self, customer):
        None

    def unblock_user(self, customer):
        None

```
{% endtab %}

{% tab title="comapny.py" %}
```python
from datetime import datetime


class Company:
    def __init__(self, name, description, type, company_size):
        self.__name = name
        self.__description = description
        self.__type = type
        self.__company_size = company_size
        self.__active_job_postings = []


class JobPosting:
    def __init__(self, description, employment_type, location, is_fulfilled):
        self.__date_of_posting = datetime.date.today()
        self.__description = description
        self.__employment_type = employment_type
        self.__location = location
        self.__is_fulfilled = is_fulfilled

```
{% endtab %}

{% tab title="group\_post.py" %}
```python
class Group:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__total_members = 0
        self.__members = []

    def add_member(self, member):
        None

    def update_description(self, description):
        None


class Post:
    def __init__(self, text, owner):
        self.__text = text
        self.__total_likes = 0
        self.__total_shares = 0
        self.__owner = owner


class Message:
    def __init__(self, sent_to, message_body, media):
        self.__sent_to = sent_to
        self.__message_body = message_body
        self.__media = media
```
{% endtab %}

{% tab title="search.py" %}
```python
class Search:
    def search_member(self, name):
        None

    def search_company(self, name):
        None

    def search_job(self, title):
        None


class SearchIndex(Search):
    def __init__(self):
        self.__member_names = {}
        self.__company_names = {}
        self.__job_titles = {}

    def search_member(self, name):
        return self.__member_names.get(name)

    def search_company(self, name):
        return self.__company_names.get(name)

    def search_job(self, title):
        return self.__job_titles.get(title)

```
{% endtab %}
{% endtabs %}

## 

## 10. CrickInfo

## 11.Facebook

## 12. Hotel Management System

## 13. Blackjack

## 14. Chess





















## 15. CardWars

{% tabs %}
{% tab title="main.py" %}
```python
from player import Player
from deck import Deck
from war_card_game import WarCardGame

player = Player("Nora", Deck(is_empty=True))
computer = Player("Computer", Deck(is_empty=True), is_coumputer=True)
deck = Deck()

game = WarCardGame(player,computer, deck)

game.print_welcome_msg()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()
    
    # NOTE: comment out below to run till end of game
    ans = input("\n Are you ready for next round? Press ENTER to continue.Enter X to Stop.")
    
    if ans.lower() == 'x':
        break
    
```
{% endtab %}

{% tab title="card.py" %}
```python
class Card:

    SPECIAL_CARDS = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    def is_special(self):
        return 11 <= self.value <= 14

    def show(self):
        card_value = self._value
        card_suit = self._suit.description.capitalize()
        suit_symbol = self._suit.symbol

        if self.is_special():
            card_description = Card.SPECIAL_CARDS[card_value]
            print(f"{card_description} of {card_suit} {suit_symbol}")
        else:
            print(f"{card_value} of {card_suit} {suit_symbol}")
            

```
{% endtab %}

{% tab title="deck.py" %}
```python
import random
from card import Card
from suit import Suit


class Deck:

    SUITS = ("club", "diamond", "heart", "spade")

    def __init__(self, is_empty=False):
        self._cards = []

        if not is_empty:
            self.build()

    @property
    def size(self):
        return len(self._cards)

    def build(self):
        for value in range(2, 15):
            for suit in Deck.SUITS:
                self._cards.append(Card(Suit(suit), value))

    def show(self):
        for card in self._cards:
            card.show()

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if self._cards:
            return self._cards.pop()
        else:
            return None

    def add(self, card):
        self._cards.insert(0, card)

```
{% endtab %}

{% tab title="player.py" %}
```python
class Player:
    def __init__(self, name, deck, is_coumputer=False):
        self.name = name
        self._deck = deck
        self._is_computer = is_coumputer

    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def deck(self):
        return self._deck

    def has_empty_deck(self):
        return self._deck.size == 0
    
    def draw_card(self):
        if not self.has_empty_deck():
            return self._deck.draw()
        else:
            return None
        
    def add_card(self,card):
        self._deck.add(card)
```
{% endtab %}

{% tab title="suit.py" %}
```python
class Suit:
    SYMBOLS = {"club": "♣", "diamond": "♦", "heart": "♥", "spade": "♠"}

    def __init__(self, description):
        self._description = description
        self._symbol = Suit.SYMBOLS[description.lower()]

    @property
    def description(self):
        return self._description

    @property
    def symbol(self):
        return self._symbol
```
{% endtab %}

{% tab title="war\_card\_game.py" %}
```python
class WarCardGame:

    PLAYER = 0
    COMPUTER = 1
    TIE = 2

    def __init__(self, player, computer, deck):
        self._player = player
        self._computer = computer
        self._deck = deck

        self.make_initial_decks()

    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)

    def make_deck(self, user):
        for i in range(26):
            card = self._deck.draw()
            user.add_card(card)

    def start_battle(self, cards_from_war=None):
        print("\n === Lests start the battle ===\n")

        player_card = self._player.draw_card()
        computer_card = self._computer.draw_card()

        print(f'Your Card:', end = ' ')
        player_card.show()
        print(f'Computer Card:', end = ' ')
        computer_card.show()

        winner = self.get_round_winner(player_card, computer_card)
        cards_won = self.get_cards_won(player_card, computer_card, cards_from_war)

        if winner == WarCardGame.PLAYER:
            print("\nYou've won this Round")
            self.add_cards_to_user(self._player, cards_won)
        elif winner == WarCardGame.COMPUTER:
            print("\nThe Computer has won this Round")
            self.add_cards_to_user(self._computer, cards_won)
        else:  # tie
            print("\n\n Its a Tie. This is a war!")
            self.start_war(cards_won)

        return winner

    def get_round_winner(self, player_card, computer_card):
        if player_card.value > computer_card.value:
            return WarCardGame.PLAYER
        elif player_card.value < computer_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE

    # returns list
    def get_cards_won(self, player_card, computer_card, previous_cards):
        if previous_cards:
            return [player_card, computer_card] + previous_cards
        else:
            return [player_card, computer_card]

    def add_cards_to_user(self, user, list_of_cards):
        for card in list_of_cards:
            user.add_card(card)

    def start_war(self, cards_from_battle):
        player_cards = []
        computer_cards = []

        for _ in range(3):
            player_card = self._player.draw_card()
            computer_card = self._computer.draw_card()

            player_cards.append(player_card)
            computer_cards.append(computer_card)

        print("Six Hidden cards: XXX XXX")
        self.start_battle(player_cards + computer_cards + cards_from_battle)

    def check_game_over(self):
        if self._player.has_empty_deck():
            print("=========================================")
            print("|            Game Over                  |")
            print("=========================================")
            print("Try Again. The Computer Won")
            return True
        elif self._computer.has_empty_deck():
            print("=========================================")
            print("|            Game Over                  |")
            print("=========================================")
            print(f"Congrats {self._player.name}, you won!!")
            return True
        return False

    def print_stats(self):
        print("\n------")
        print(f"You have {self._player.deck.size} cards on your deck")
        print(f"The Computer has {self._computer.deck.size} cards on your deck")
        print("------")

    def print_welcome_msg(self):
        print("=========================================")
        print("|          War Card Game                 |")
        print("=========================================")

```
{% endtab %}
{% endtabs %}

## 16. TicTacToe\(Naive\)

{% tabs %}
{% tab title="main.py" %}
```python
from board import Board
from player import Player


print("**************")
print(" Tic-Tac-Toe!")
print("**************")

board = Board()
player = Player()
computer = Player("O", False)

board.print_board()

while True:
    # Ask human user move
    move = player.get_player_move()
    # Submit move
    board.submit_move(move, player)
    # Print board
    board.print_board()

    if board.is_move_valid(move) and board.is_winner(player, move[0], move[1]):
        print("You win!")
        break

    # Ask computer player move
    comp_move = computer.get_player_move()
    # Submit move
    board.submit_move(comp_move, computer)
    # Print board
    board.print_board()

    if board.is_winner(computer, comp_move[0], comp_move[1]):
        print("The Computer Won!")
        break

    if board.check_tie():
        print("There was a tie!")
        break
```
{% endtab %}

{% tab title="board.py" %}
```python
class Board:
    
    EMPTY = 0
    COLUMNS = {"A": 0, "B": 1, "C": 2}
    ROWS = (1, 2, 3)

    def __init__(self, game_board=None):
        if game_board:
            self.game_board = game_board
        else:
            self.game_board = [[0, 0, 0],
                               [0, 0, 0],
                               [0, 0, 0]]

    def print_board(self):
        print("    A   B   C")
        for i, row in enumerate(self.game_board, 1):
            print(i, end=" | ")
            for col in row:
                if col != Board.EMPTY:
                    print(col, end=" | ")
                else:
                    print("  | ", end="")
            print("\n---------------")

    def submit_move(self, move, player):
        if not self.is_move_valid(move):
            print("Invalid Input: Please Enter the row and column of your move (Example: 1A)")
            return
        else:
            row_index = int(move[0])-1
            col_index = Board.COLUMNS[move[1]]

            value = self.game_board[row_index][col_index]

            if value == Board.EMPTY:
                self.game_board[row_index][col_index] = player.marker
            else:
                print("This space is already taken.")

    def is_move_valid(self, move):
        return ((len(move) == 2)
            and (int(move[0]) in Board.ROWS)
            and (move[1] in Board.COLUMNS))

    def is_winner(self, player, row, col):
        if self.check_row(row, player):
            return True
        elif self.check_col(col, player):
            return True
        elif self.check_diagonal(player):
            return True
        elif self.check_antidiagonal(player):
            return True
        else:
            return False

    def check_row(self, row, player):
        row_index = int(row)-1
        board_row = self.game_board[row_index]

        if board_row.count(player.marker) == 3:
            return True
        else:
            return False

    def check_col(self, col, player):
        col_index = Board.COLUMNS[col]
        total_markers = 0

        for i in range(3):
            if self.game_board[i][col_index] == player.marker:
                total_markers += 1

        if total_markers == 3:
            return True
        else:
            return False
        
    def check_diagonal(self, player):
        total_markers = 0

        for i in range(3):
            if self.game_board[i][i] == player.marker:
                total_markers += 1

        if total_markers == 3:
            return True
        else:
            return False

    def check_antidiagonal(self, player):
        total_markers = 0

        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                total_markers += 1

        if total_markers == 3:
            return True
        else:
            return False

    def check_tie(self):
        total_empty = 0
        
        for row in self.game_board:
            total_empty += row.count(Board.EMPTY)

        if total_empty == 0:
            return True
        else:
            return False
```
{% endtab %}

{% tab title="player.py" %}
```python
import random

class Player:

    def __init__(self, marker="X", is_human=True):
        self._marker = marker
        self._is_human = is_human

    @property
    def marker(self):
        return self._marker

    @property
    def is_human(self):
        return self._is_human

    def get_player_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()
            
    def get_human_move(self):
        move = input("Player move (X): ")
        return move

    def get_computer_move(self):
        row = random.choice([1, 2, 3])
        col = random.choice(["A", "B", "C"])
        move = str(row) + col

        print("Computer move (O): ", move)

        return move
```
{% endtab %}

{% tab title="requirements.txt" %}
```
* The game shallstart by displaying a welcome message and an empty 3x3 board.

* There will be two players: the userand the computer player.
* The user will have the X marker.
* The computer player will have the Omarker.
* The user will be promptedto enter his/her move with theformat rowcolumn(e.g 1A) where:
    * Row can be 1, 2, or 3(top to bottom)* Column can be A, B, or C(left to right).
    These values shall be displayed on the board as a reference.

* If the user or the computer player selectsa position that is already taken, a descriptive message shouldbe displayed. * The updated board shallbe displayed after entering or generating the move.

* For a player towinthe gamethere must be a full row, column, or diagonal with its corresponding marker.

*The game ends when there is a tie (full board) or when the user or the computer player wins.

* The program shall assume that the user input will be in a correct format. 
```
{% endtab %}
{% endtabs %}

## 17. Parking Lot ☑️

{% tabs %}
{% tab title="main.py" %}
```python
from parking_lot import ParkingLot, Car, Bike, Bus

if __name__ == '__main__':
    parkingLotObj = ParkingLot(3, 10)
    
    parkingLotObj.parkVehicle(Car(10, "Google"))
    parkingLotObj.companyParked("Google"), [Car(10, "Google")]
    parkingLotObj.leaveOperation(Car(10, "Google"))
    parkingLotObj.companyParked("Google"), []
    
```
{% endtab %}

{% tab title="parking\_lot.py" %}
```python
from enum import Enum


# Vehicle type class for what all type of vehicles can come for parking
class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    BUS = 3


# Vehicle class for license plate, company name and their type
class Vehicle:
    def __init__(self, licensePlate, companyName, type_of_vehicle):
        self.licensePlate = licensePlate
        self.companyName = companyName
        self.type_of_vehicle = type_of_vehicle

    def getType(self):
        return self.type_of_vehicle

    """overwrite __eq__ methods to correctly check if two vehicle objects are same. Otherwise, they will be 
    checked at hashcode level not at content level."""

    def __eq__(self, other):
        if other is None:
            return False
        if self.licensePlate != other.licensePlate:
            return False
        if self.companyName != other.companyName:
            return False
        if self.type_of_vehicle != other.type_of_vehicle:
            return False
        return True


# Car class inherited from Vehicle class for license plate, company name and their type
class Car(Vehicle):
    def __init__(self, licensePlate, companyName):
        Vehicle.__init__(self, licensePlate, companyName, VehicleType.CAR)


# Bike class inherited from Vehicle class for license plate, company name and their type
class Bike(Vehicle):
    def __init__(self, licensePlate, companyName):
        Vehicle.__init__(self, licensePlate, companyName, VehicleType.BIKE)


# Bus class inherited from Vehicle class for license plate, company name and their type
class Bus(Vehicle):
    def __init__(self, licensePlate, companyName):
        Vehicle.__init__(self, licensePlate, companyName, VehicleType.BUS)


class Slots:
    def __init__(self, lane, spotNumber, type_of_vehicle):
        # self.level = level
        self.lane = lane
        self.spotNumber = spotNumber
        self.vehicle = None
        self.type_of_vehicle = type_of_vehicle

    def isAvailable(self):
        return self.vehicle == None

    def park(self, vehicle):
        if vehicle.type_of_vehicle == self.type_of_vehicle:
            self.vehicle = vehicle
            return True
        else:
            return False

    def removeVehicle(self):
        self.vehicle = None
        return self.vehicle

    def getVehicle(self):
        return self.vehicle


"""Level class - Each level is an independent entity with a floor number, its lanes and the slots within it. 
The number of lanes are designed based on the number of slots. 10 slots make one lane"""


class Levels:
    def __init__(self, floorNumber, no_of_slots):
        self.floorNumber = floorNumber
        self.spots_per_lane = 10
        self.lanes = no_of_slots / self.spots_per_lane
        self.parkingSlots = set()
        self.availableSpots = []

        # Check available spots in a lane
        for lane in range(int(self.lanes)):
            for i in range(self.spots_per_lane):
                import random

                # We will randomly assign a type to each slot.
                self.availableSpots.append(
                    Slots(lane, i, random.choice(list(VehicleType)))
                )
                # self.availableSpots.append(Slots(lane, i, type_of_vehicle))

    # Park vehicle is spot is available
    def park(self, vehicle):
        for slot in self.availableSpots:
            if slot.park(vehicle):
                return True
        return False

    # Remove vehicle from a spot
    def remove(self, vehicle):
        for spot in self.availableSpots:
            if spot.getVehicle() == vehicle:
                spot.removeVehicle()
                return True
        return False

    # Company name for the vehicle parked at the available spots
    def companyParked(self, companyName):
        all_vehicles = []
        for spot in self.availableSpots:
            vehicle = spot.getVehicle()
            if (vehicle is not None) and (vehicle.companyName == companyName):
                all_vehicles.append(vehicle)
                # print(all_vehicles)
        return all_vehicles


# A parking lot is made up of 'n' number of levels/floors and 'm' number of slots per floor.
class ParkingLot:
    def __init__(self, no_of_floor, no_of_slot):
        self.levels = []
        for i in range(no_of_floor):
            self.levels.append(Levels(i, no_of_slot))

    # This operation inserts a vehicle accordingly, also takes care of what company vehicle it is.
    def parkVehicle(self, vehicle):
        for level in self.levels:
            if level.park(vehicle):
                return True
        return False

    # This operation exits a vehicle 'C' in a level 'm'.
    def leaveOperation(self, vehicle):
        for level in self.levels:
            if level.remove(vehicle):
                return True

    # This operation allows the user to view the list of vehicles parked for a particular company.
    def companyParked(self, companyName):
        all_vehicles = []
        for level in self.levels:
            all_vehicles.extend(level.companyParked(companyName))
        return all_vehicles

```
{% endtab %}

{% tab title="test\_parking\_lot.py" %}
```python
import unittest
from parking_lot import ParkingLot, Car, Bike, Bus


class TestParkingLot(unittest.TestCase):

    def test_park(self):
        parkingLotObj = ParkingLot(6, 30)
        res2 = parkingLotObj.parkVehicle(Car(10, "Amazon"))
        res3 = parkingLotObj.parkVehicle(Bike(20, "Amazon"))
        res4 = parkingLotObj.parkVehicle(Bus(30, "Microsoft"))

        self.assertEqual(res2, True)
        self.assertEqual(res3, True)
        self.assertEqual(res4, True)


    def test_leave_operation(self):
        parkingLotObj = ParkingLot(6, 30)
        self.assertTrue(parkingLotObj.parkVehicle(Car(20, "Google")))
        #self.assertTrue(parkingLotObj.leaveOperation(Car(10, "Google")))
        self.assertTrue(parkingLotObj.leaveOperation(Car(20, "Google")))
        self.assertEqual(parkingLotObj.leaveOperation(Car(20, "Google")), None)


    def test_companyParked(self):
        parkingLotObj = ParkingLot(6, 30)
        # res1 = parkingLotObj.parkVehicle(Car(20, "Google"))
        # res2 = parkingLotObj.companyParked("Google")
        self.assertTrue(parkingLotObj.parkVehicle(Car(20, "Google")))
        self.assertEqual(parkingLotObj.companyParked("Google"), [Car(20, "Google")])
        #self.assertEqual(parkingLotObj.companyParked("Google"), Car(10, "Google"))
        print(parkingLotObj.companyParked("Google"))

        
    def test_all(self):
        parkingLotObj = ParkingLot(3, 10)
        # Atleast 1 parking spot for car.
        # First park a car, it should return True.
        self.assertTrue(parkingLotObj.parkVehicle(Car(10, "Google")))
        # Get the list of cars, it should give one car we parked.
        self.assertEqual(parkingLotObj.companyParked("Google"), [Car(10, "Google")])
        # Remove that car successfully.
        self.assertTrue(parkingLotObj.leaveOperation(Car(10, "Google")))
        # Now the list of cars should be empty.
        self.assertEqual(parkingLotObj.companyParked("Google"), [])


if __name__ == '__main__':
    unittest.main()
```
{% endtab %}
{% endtabs %}

## 5. Elevator

{% tabs %}
{% tab title="Design.md" %}
```text
# Features:
* Extenal Request: press button outside(Up/Down) lift to call it
* Internal Request: press floor button inside(0...N) lift to make a drop request

# ====================================================

# Classes: (nouns)

* Direction(enum)
    * UP
    * DOWN

* State(enum)
    * IDLE
    * MOVING

* ReqType       -> in future: Alaram etc.
    * EXTERNAL
    * INTERNAL
    
* Elevator:
    * id
    * curr_direction
    * curr_state
    * curr_floor
    * curr_jobs[SortedList]           -> jobs which are being processed
    * up_pending_jobs[SortedList]     -> up jobs which cannot be processed now so put in pending queue
    * down_pending_jobs[SortedList]   -> down jobs which cannot be processed now so put in pending queue
    * move()    -> simulation: sleep for 5 seconds
    -----------[Phase#2]------------
    * is_elevator_free()
    * ...
    * start_evelator()

* Request:  #interface
    * elevator_id
    * req_type

* ExternalRequest(Request):
    * source_floor
    * direction(enum)

* InternalRequest(Request):
    * destination_floor



# [Design Discussion Points]===================================

* Implement with single elevator for now=> scale up later

* How to resolve conflicts?
    * 1. Keep requests sorted by timestamp & porcess by them
        * => Doesnt really make sense; elevator will keep moving to-n-frow
    * 2. Better: if an elevator is moving up-it'll keep moving up till last req floor
        * if anyone presses button on 'above' floors; he can hop in

* Give priority to InternalReqs > ExtRequests
    * person outside lift can wait=> is free/has other options+wifi
    * But, person stuck inside lift will frustrate more=> claustrophobia/suffocation+no internet

* Multiple Elevators in building
    * All free elevators will start rushing towards single req

## SRC: https://www.youtube.com/watch?v=FptCbX7fRHw&ab_channel=JavaStructures


```
{% endtab %}

{% tab title="Constants.py" %}
```python
from enum import Enum

class State(Enum):
    IDLE = "IDLE"
    MOVING = "MOVING"


class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    NONE = "NONE"


class ReqType(Enum):
    EXTERNAL = "EXTERNAL"
    INTERNAL = "INTERNAL"
```
{% endtab %}

{% tab title="Request.py" %}
```python
from abc import ABC, abstractmethod

class Request(ABC):
    def __init__(self, elevator_id, req_type):
        self._elevator_id = elevator_id
        self._req_type = req_type

    @property
    def elevator_id(self):
        return self._elevator_id

    @property
    def req_type(self):
        return self._req_type


class InternalRequest(Request):
    def __init__(self, req_type, elevator_id, destination_floor):
        Request.__init__(self, elevator_id, req_type)
        self._destination_floor = destination_floor

    @property
    def destination_floor(self):
        return self._destination_floor

    @destination_floor.setter
    def destination_floor(self, floor):
        self._destination_floor = floor


class ExternalRequest(Request):
    def __init__(self, elevator_id, req_type, source_floor, direction):
        Request.__init__(self, elevator_id, req_type)
        self._source_floor = source_floor
        self._direction = direction

    @property
    def source_floor(self):
        return self._source_floor

    @source_floor.setter
    def source_floor(self, floor):
        self._source_floor = floor

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction
```
{% endtab %}

{% tab title="Elevator.py" %}
```python
import uuid
from sortedcontainers import SortedList
import time

class Elevator:

    ids = 1

    def __init__(self,curr_direction=Direction.UP,
        curr_state=State.IDLE,
        curr_floor=0,
        curr_jobs=SortedList([]),
        up_pending_jobs=SortedList([]),
        down_pending_jobs=SortedList([])):
            self._id = Elevator.ids
            self._curr_direction = curr_direction
            self._curr_state = curr_state
            self._curr_floor = curr_floor
            self._curr_jobs = curr_jobs
            self._up_pending_jobs = up_pending_jobs
            self._down_pending_jobs = down_pending_jobs

        Elevator.ids += 1

    """ getters/setters"""

    @property
    def curr_direction(self):
        return self._curr_direction

    @curr_direction.setter
    def curr_direction(self, dir):
        self._curr_diection = dir

    @property
    def curr_state(self):
        return self._curr_state

    @curr_state.setter
    def curr_state(self, state):
        self._curr_state = state

    @property
    def curr_floor(self):
        return self._curr_floor

    @curr_floor.setter
    def curr_floor(self, floor):
        self._curr_floor = floor

    @property
    def curr_jobs(self):
        return self._curr_jobs

    """ ------------------------- [Phase#2]------------------------- """
    """ ---------- methods ---------- """

    def move(self):
        time.sleep(5)

    # checks if elevator has any CURRENTLY Processing jobs
    def is_elevator_free(self):
        return len(self.curr_jobs) == 0

    def add_to_curr_job(self, job):
        self._curr_jobs.append(job)

    # TOOD: make these methods private

    def add_to_pending_reqs(self, req):
        if req.direction == Direction.UP:
            self._up_pending_jobs.add(req)  # add because SortedList
        else:
            self._down_pending_jobs.add(req)  # add because SortedList

    def add_new_req(self, req):
        if self.curr_state == State.IDLE:  # khali baitha hua hai
            self.curr_state = State.MOVING

            # first req has to be an external req
            if req.req_type == ReqType.INTERNAL:
                print("Invalid Move OR a person was stuck inside somehow!")
                return
            else:
                self.add_to_curr_job(req)
                self.curr_direction = req.direction
                self.curr_state = State.MOVING

        else:  # khali nhi baitha hua
            # 1. this req is NOT in the same dirn as elevator - for both EXT/INT req
            if req.direction != self.curr_direction:
                self.add_to_pending_reqs(req)
            # handle internal requests - business logic goes here
            elif req.req_type == ReqType.INTERNAL:
                if (
                    req.direction == Direction.UP
                    and req.destination_floor > self.curr_floor
                ):
                    self.add_to_curr_job(req)
                elif (
                    req.direction == Direction.DOWN
                    and req.destination_floor < self.curr_floor
                ):
                    self.add_to_curr_job(req)

    def process_up_req(self, req):
        # move from curr -> src --> destination
        start_floor = self.curr_floor
        for i in range(start_floor, req.source_floor):
            self.curr_floor = start_floor
            print(f"@ Floor : {i}")
            self.move()

        print("---------- Opening Door: welcome ------------")
        start_floor = self.curr_floor
        for i in range(start_floor, req.destination_floor):
            print(f"@ Floor : {i}")
            self.curr_floor = start_floor
            self.move()

    def process_down_req(self, req):
        # move from curr -> src --> destination
        start_floor = self.curr_floor
        for i in range(start_floor, req.source_floor):
            self.curr_floor = start_floor
            print(f"@ Floor : {i}")
            self.move()

        print("---------- Opening Door: welcome ------------")
        start_floor = self.curr_floor
        for i in range(start_floor, req.destination_floor,-1):
            print(f"@ Floor : {i}")
            self.curr_floor = start_floor
            self.move()

    def add_pending_up_reqs_to_curr_req(self):
        if self._up_pending_jobs:
            self.curr_jobs = self._up_pending_jobs
            self.curr_direction = Direction.UP
            self.curr_state = State.MOVING
        else:
            self.curr_state = State.IDLE

    def add_pending_down_reqs_to_curr_req(self):
        if self._down_pending_jobs:
            self.curr_jobs = self._down_pending_jobs
            self.curr_direction = Direction.DOWN
            self.curr_state = State.MOVING
        else:
            self.curr_state = State.IDLE

    # process curr jobs
    def start_elevator(self):
        while not self.is_elevator_free():

            if self.curr_direction == "UP":  # process all UP requests
                req_to_be_served = self.curr_jobs.pop(0)
                self.process_up_req(req_to_be_served)
                if len(self.curr_jobs) == 0:
                    self.add_pending_up_reqs_to_curr_req()

            elif self.curr_direction == "DOWN":
                req_to_be_served = self.curr_jobs.pop(-1)
                self.process_down_req(req_to_be_served)
                if len(self.curr_jobs) == 0:
                    self.add_pending_down_reqs_to_curr_req()
            else:
                self.curr_state = "IDLE"
                return
```
{% endtab %}
{% endtabs %}

## 18. Logger

## 















