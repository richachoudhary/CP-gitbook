# Amazon

## Amazon

#### System Requirements:

1. **Add/update products catalog**; Users should be able to add new products to sell.
2. **Search** for products by their name or category.
3. **Add/remove** product items in the **shopping cart**.
4. \*\*Check-out to buy \*\*product items in the **shopping cart**.
5. **Make a payment** to place an order.
6. **Add** a new **product category.**
7. Send notifications to members with\*\* shipment updates.\*\*

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
  * add\_product(self, product)
  * add\_productReview(self, review)
  * reset\_password(self)
* **Customer(Account)**
  * get\_shopping\_cart(self)
  * add\_item\_to\_cart(self, item)
  * remove\_item\_from\_cart(self, item)
  * place\_order(self, order)
* **Guest(Account)**
  * register()

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
  * get\_available\_count()
  * update\_price(price)

**4.Search ===============================================================**

* **Search** : parent
  * search\_products\_by\_name(self, name)
  * search\_products\_by\_category(self, category)
* **Catalog(Search)**
  * product\_names
  * product\_categories
  * search\_products\_by\_name(self, name)
  * search\_products\_by\_category(self, category)

**5.Shopping ===============================================================**

* **Item**
  * product\_id
  * quantity
  * price
  * update\_quantity(quantity)
* **ShoppingCart**
  * items = \[]
  * add\_item(self, item)
  * remove\_item(self, item)
  * update\_item\_quantity(self, item, quantity)
  * get\_items(self)
  * checkout(self)
* **Order**
  * order\_number
  * status
  * order\_date
  * order\_log = \[]
  * send\_for\_shipment(self)
  * make\_payment(self, payment)
  * add\_order\_log(self, order\_log)
* **OrderLogs**
  * order\_number
  * creation\_date
  * status

**6.Shipment ===============================================================**

* **Shipment**
  * shipment\_number
  * shipment\_date
  * ETA
  * shipmentLogs . = \[]
* **ShipmentLog**
  * shipment\_number
  * status
  * creation\_date
* **Notification**
  * notification\_id
  * created\_on
  * content
  * send\_notification(account)

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

{% tab title="account_types.py" %}
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

##

##
