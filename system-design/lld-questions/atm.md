# ATM

## ATM

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
  * make\_transaction(self, transaction)
  * get\_billing\_address(self)
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
  * install\_atm(atm)
* **ATM**
  * atm\_id
  * location
  * cash\_dispenser
  * cash\_deposit
  * authenticate\_user(self)
  * make\_transaction(self, customer, transaction)
* **CashDispenser**
  * total\_amount
  * is\_healthy()
  * dispense\_cash(self, amount)
* **CashDeposit**
  * total\_amount
  * is\_healthy()
  * deposit\_cash(self, amount)

**4.Transaction ===============================================================**

* \*\*Transaction : \*\*interface
  * transaction\_id
  * creation\_time
  * status
  * make\_transation()
* \*\*BalanceInquiry(Transaction) \*\*
* \*\*Deposit(Transaction) \*\*
  * amount
  * get\_amount()
* \*\*CheckDeposit(Deposit) \*\*
* \*\*CashDeposit(Deposit) \*\*
* **Transfer(Transaction)**
  * destination\_account\_number
  * get\_destination\_account()

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

##
