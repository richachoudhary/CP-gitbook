# LinkedIn

##

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
  * add\_experience(self, experience)
  * add\_education(self, education)
  * add\_skill(self, skill)
  * add\_accomplishment(self, accomplishment)
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
* **Member(Person)**
  * date\_of\_membership
  * headline
  * photo
  * member\_follows
  * member\_connections
  * company\_follows
  * group\_follows
  * profile
  * send\_message(self, message)
  * create\_post(self, post)
  * send\_connection\_invitation(self, connection\_invitation)
  * block\_user(self, customer)
  * unblock\_user(self, customer)

**4.Company ===============================================================**

* **Company** :
  * name
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

**5.Messagin & Posting=============================================================**

* \*\*Group : \*\*
  * name
  * description
  * total\_members
  * members = \[]
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

* \*\*Search : \*\*
  * search\_member(self, name)
  * search\_company(self, name)
  * search\_job(self, title)
* **SearchIndex(Search):**
  * member\_names
  * company\_names
  * job\_titles
  * search\_member(self, name)
  * search\_company(self, name)
  * search\_job(self, title)

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

{% tab title="acc_type.py" %}
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

{% tab title="group_post.py" %}
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
