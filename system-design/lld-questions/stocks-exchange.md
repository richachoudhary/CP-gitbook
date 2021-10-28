# Stocks Exchange

## Stocks Exchange | `Singleton🟢`

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
* **TimeBoundOrderType** : GOOD\_TILL\_CANCELLED, IMMEDIATE\_OR\_CANCEL, ON\_MARKET\_OPEN, ON\_MARKET\_CLOSE
* **AccountStatus** : ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE

**2.Orders =================================================================**

* **Order** : interface
  * order\_id
  * is\_buy\_order
  * status
  * `time_bounder_order_type`
  * creation\_time
  * set\_status(self, status)
  * save\_in\_DB(self)
  * add\_order\_parts(self, parts)
  * cancel\_order()
  * ~~place\_order()~~ => Not placed here(placed in \*\*stock\_exchang \*\*as **SINGLETON**)
* **LimitOrder(Order)**
  * price\_limit = 0.0

#### 3.Stock Exchange ===================================================================

* **StockExchange** : singleton🟢
  * **`place_order()`** : the only place at which orders can be placed

#### 4.Members ===============================================================

* \*\*Account: \*\*interface
  * id
  * password
  * name
  * email
  * phone
  * status : AccountStatus.NONE
  * reset\_password()
* **Member(Account)**
  * available\_funds\_for\_trading = 0.0
  * date\_of\_membership
  * stock\_positions = {}
  * active\_orders = {}
  * place\_sell\_limit\_order(self, stock\_id, quantity, limit\_price, enforcement\_type)
  * callback\_stock\_exchange(self, order\_id, order\_parts, status)
    * this function will be invoked whenever there is an update from stock exchange against an order

{% tabs %}
{% tab title="combined_sys.py" %}
```python
from enum import Enum

from abc import ABC
from datetime import date


class ReturnStatus(Enum):
    SUCCESS, FAIL, INSUFFICIENT_FUNDS, NO_STOCK_AVAILABLE = 1, 2, 3, 4


class OrderStatus(Enum):
    OPEN, FILLED, PARTIALLY_FILLED, CANCELLED = 1, 2, 3, 4


class TimeBoundOrderType(Enum):
    GOOD_TILL_CANCELLED, IMMEDIATE_OR_CANCEL, ON_THE_OPEN, ON_MARKET_CLOSE = (
        1,
        2,
        3,
        4,
    )


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 4, 5


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
        self.__price_limit = 0.0


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


class Account(ABC):
    def __init__(
        self, id, password, name, address, email, phone, status=AccountStatus.NONE
    ):
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
    def __init__(
        self, id, password, name, address, email, phone, status=AccountStatus.NONE
    ):
        Account.__init__(
            self, id, password, name, address, email, phone, status=AccountStatus.NONE
        )
        self.__available_funds_for_trading = 0.0
        self.__date_of_membership = date.today()
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


if __name__ == "__main__":
    p1 = Member(
        id=1,
        password="abc",
        name="user1",
        address="123. bk st.",
        email="user1@emil.com",
        phone="+91-987654321",
    )

    p1.place_sell_limit_order(1,1,5,None)
```
{% endtab %}

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
```
{% endtab %}

{% tab title="stock_exchange.py🟢" %}
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

