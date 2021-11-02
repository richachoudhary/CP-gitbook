# HLD:Questions

## 0.Template

```
* Multiple Instance of each service
* API Gateway(LB+Proxy)
* Zookeeper
* CDN
* Varnish
* Cache(write back)-Redis
* SQL
    * Read replicas
    * sharding(user_id/location)
* NoSQL
    * Replicas/Distributed
* Kafka/worker
* Stateless Microservices
* Hystrix
* HDFS/S3
* local cache : last 50 msgs
```

```
#1. Requirement Gathering ======================================
        1.1 Functional Requirements
        1.2 NonFunctional Requirements - Usage Patterns(read heavy/CAP tradeoffs)
        1.3 Out of Scope
#2. Back-of-the-envelope estimation ============================
        2.1 Scale of System
        2.2 Storage size estimation
        2.3 Bandwidth esitmation(read+write)
#3. APIs =======================================================
        GET  /name/:id      Req:{}, Res:{}
        POST /name/:id      Req:{} 
#4. Models:Classes, DB Schema & ER diagrams=====================
        * Tables
        
        * DBs & choice(NoSQL/SQL)
#5. Draw 'Basic HLD'=============================================
#6. EVOLVE & 'Draw Detailed HLD' with the discussion on each comp =====
#7. Walk down flow of every action =============================
#7. Identifying and resolving bottlenecks ======================
```



## 4. BookMyShow

* Whimisical Board [link](https://whimsical.com/bookmyshow-SiSmppUMB3mrGzyr8YFyY5)

{% tabs %}
{% tab title="requirements.md" %}
````
# 1. Requirement Gathering ======================================
        1.1 Functional Requirements
            
            * Other sevices(like Paytm) can also book seats in same hall
            * Show multiple cities
            * Each theater can have multiple halls
            * Each hall can run 1 movie at 1 time
            * Movies will have multiple shows
            * Customers can search movie by title, language, genre, release date, city.
                => Redirect search reqs to Elastic Search
                * It also works as Analytics Engine
            * Customers can see the theaters as per their filtered search
            * Customers can see seating arrangement of halls & select any city they want
            * Customers can see booked/free tickets
            * Payments - 3P
            * Show movie info
            * Ensure No two customers can reserve the same seat.

        1.2 NonFunctional Requirements - Usage Patterns(read heavy/CAP tradeoffs)
            
            * Highly Concurrent
            
        1.3 Out of Scope

            * Moive suggestions
            * Give Reviews, Ratings
            * Send ticket my sms/whatsapp/mail
            * Add discount coupon during payment
# 2. Back-of-the-envelope estimation ============================
        2.1 Scale of System
        2.2 Storage size estimation
# 3. APIs =======================================================
# 4. Models:Classes, DB Schema & ER diagrams=====================

# Notes: ==================================================== 

* Lock mechanism on seat booking:
    * If he doesn’t book within 10 min, release the seat.

* For Search Queries:
    => Redirect search reqs to Elastic Search
    * It also works as Analytics Engine

* For caching use: Redis or memcached
    * Redis is better choice as its distributed & persistent

* Choice of DB: 
    => use both RDBMS + NoSQL
    * RDMBS: store ACID/static data:
        * movie halls
        * seats
        * cities
        * userInfo
        * => Sharding
        * => Master/Slave for Read/Writes
    * NoSQL : 
        below data is Big data i.e. too much for RDBMS to digest
        so use NoSQL for it
        * movie related info-cast/story/reviews etc
        * => Geo-distributed backups

* Use Kafka queues to send tickets on mail/sms/generate pdfs in ASYNC

* For Recommendation system:
    * Dump all data on HDFS
    * Process with Apache Spark
    * Run Hive queries
    * Build ML models & recommend

* For concurrency:

```s
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
 
BEGIN TRANSACTION;
 
    -- Suppose we intend to reserve three seats (IDs: 54, 55, 56) for ShowID=99 
    Select * From ShowSeat where ShowID=99 && ShowSeatID in (54, 55, 56) && isReserved=0 
 
    -- if the number of rows returned by the above statement is NOT three, we can return failure to the user.
    update ShowSeat table...
    update Booking table ...
 
COMMIT TRANSACTION;
```
````
{% endtab %}

{% tab title="classes.py(OOP shell)" %}
```python
from enum import Enum


class BookingStatus(Enum):
    REQUESTED, PENDING, CONFIRMED, CHECKED_IN, CANCELED, ABANDONED = 1, 2, 3, 4, 5, 6


class SeatType(Enum):
    REGULAR, PREMIUM, ACCESSIBLE, SHIPPED, EMERGENCY_EXIT, OTHER = 1, 2, 3, 4, 5, 6


class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6


class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETED, FILLED, DECLINED, CANCELLED, ABANDONED, SETTLING, SETTLED, REFUNDED = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

#------------------------------------

from abc import ABC

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

    def block_user(self, customer):
        None


class FrontDeskOfficer(Person):
    def create_booking(self, booking):
        None


class Guest:
    def register_account(self):
        None

#------------------------------------

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
        self.__movie_added_by = added_by

        self.__shows = []

    def get_shows(self):
        None
#----------------------------

class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country
        

class City:
    def __init__(self, name, state, zip_code):
        self.__name = name
        self.__state = state
        self.__zip_code = zip_code


class Cinema:
    def __init__(self, name, total_cinema_halls, address, halls):
        self.__name = name
        self.__total_cinema_halls = total_cinema_halls
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

#------------------------------------

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


class ShowSeat(CinemaHallSeat):
    def __init__(self, id, is_reserved, price):
        self.__show_seat_id = id
        self.__is_reserved = is_reserved
        self.__price = price


class Payment:
    def __init__(self, amount, transaction_id, payment_status):
        self.__amount = amount
        self.__created_on = datetime.date.today()
        self.__transaction_id = transaction_id
        self.__status = payment_status
#--------------------------------------
from abc import ABC

class Search(ABC):
    def search_by_title(self, title):
        None

    def search_by_language(self, language):
        None

    def search_by_genre(self, genre):
        None

    def search_by_release_date(self, rel_date):
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

        # ...

        def search_by_city(self, city_name):
            return self.__movie_cities.get(city_name)
```
{% endtab %}

{% tab title="working_code.py" %}
```python
global f
f = 0
 
#this t_movie function is used to select movie name
def t_movie():
    global f
    f = f+1
    print("which movie do you want to watch?")
    print("1,movie 1 ")
    print("2,movie 2 ")
    print("3,movie 3")
    print("4,back")
    movie = int(input("choose your movie: "))
    if movie == 4:
      # in this it goes to center function and from center it goes to movie function and it comes back here and then go to theater
      center()
      theater()
      return 0
    if f == 1:
      theater()
 
# this theater function used to select screen
def theater():
    print("which screen do you want to watch movie: ")
    print("1,SCREEN 1")
    print("2,SCREEN 2")
    print("3,SCREEN 3")
    a = int(input("choose your screen: "))
    ticket = int(input("number of ticket do you want?: "))
    timing(a)
 
# this timing function used to select timing for movie
def timing(a):
    time1 = {
        "1": "10.00-1.00",
        "2": "1.10-4.10",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
    }
    time2 = {
        "1": "10.15-1.15",
        "2": "1.25-4.25",
        "3": "4.35-7.35",
        "4": "7.45-10.45"
    }
    time3 = {
        "1": "10.30-1.30",
        "2": "1.40-4.40",
        "3": "4.50-7.50",
        "4": "8.00-10.45"
    }
    if a == 1:
        print("choose your time:")
        print(time1)
        t = input("select your time:")
        x = time1[t]
        print("successfull!, enjoy movie at "+x)
    elif a == 2:
        print("choose your time:")
        print(time2)
        t = input("select your time:")
        x = time2[t]
        print("successfull!, enjoy movie at "+x)
    elif a == 3:
        print("choose your time:")
        print(time3)
        t = input("select your time:")
        x = time3[t]
        print("successfull!, enjoy movie at "+x)
    return 0
 
 
def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("wrong choice")
 
 
def center():
    print("which theater do you wish to see movie? ")
    print("1,Inox")
    print("2,Icon")
    print("3,pvp")
    print("4,back")
    a = int(input("choose your option: "))
    movie(a)
    return 0
 
# this function is used to select city
def city():
    print("Hi welcome to movie ticket booking: ")
    print("where you want to watch movie?:")
    print("1,city 1")
    print("2,city 2 ")
    print("3,city 3 ")
    place = int(input("choose your option: "))
    if place == 1:
      center()
    elif place == 2:
      center()
    elif place == 3:
      center()
    else:
      print("wrong choice")
 
 
city() # it calls the function city
```
{% endtab %}
{% endtabs %}

![](../../.gitbook/assets/screenshot-2021-08-25-at-8.57.20-pm.png)

## 5. Ketto/Go Fund Me

* Whimsical: [link](https://whimsical.com/ketto-2S14YgGQ5Er7SLUPxdep5g)
* Source: [LC](https://leetcode.com/discuss/interview-question/system-design/1397022/Go-Fund-me-System-design)

```
#1. Requirement Gathering ======================================
        1.1 Functional Requirements

            * Registered users can create campaigns to fund their cause.
            * Registered users can view a campaign by campaign ID
            * Registered users can collect money against a campaign
            * Registered users could contribute to a campaign based on campaign ID
            * Once a day we flush the collected money into the creator’s account

        1.2 NonFunctional Requirements - Usage Patterns/Tradeoffs

            * Low latency
            * Durability changes made to the campaigns or newly created campaign should not be lost
            * Eventual consistency
            * It is a growing system

        1.3 Out of Scope
            * User registration
            * Analytics
            * Recommendation
            * Search
            * Guest flow

#2. Back-of-the-envelope estimation ============================
        2.1 Scale of System
            * Total Active users: 50M
            * New users added daily: 50K (as 'growing system')
            * CAMPAIGN CREATION:
                1 user creates 5 campaigns => 5*50 => 250M campaigns
            * CAMPAIGN VIEWING:
                5M view capaigns daily => 5M/(24*3600) => 60 cmps/sec
            * => Hence, Load on the system isnt much

        2.2 Storage size estimation
            * SKIPPED (nothing much of storage here)

#3. APIs =======================================================
        * createCampaign(userId, String campaignName, CampaignDetails campaignDetails) 
            → returns campaignId of the created campaign

        * getCampaignDetails(userId, campaignId) 
            → Returns CamapignDetails of the given camapignId

        * pay(userId, CampaignId, PaymentDetails paymentDetails) 
            → return a boolean if the payment was successful or not also updates the total collected amount against the campaign

#4. Models:Classes, DB Schema & ER diagrams=====================
    * SKIPPED

#5. Draw Basic HLD =============================================
    * Campaign Creator Service
    * Campaign Viewer Service

#6. EVOLVE HLD to scale & indepth discussion of components =====
    Add/disucss on these optimisations:
    * Load balancer - which is entry point to our website
    * Gateway -- which would be responsible for filtering requests and authentication and authorization
    * Service discovery --- Would be responsible for providing service end points to internal services and also load balancing internally
    * Caching
    
```

![](../../.gitbook/assets/screenshot-2021-08-28-at-6.23.13-am.png)

![](../../.gitbook/assets/screenshot-2021-08-28-at-6.36.56-am.png)





## 13. Search Engine | Indexing | Elastic Search

* 3 Steps of A Search Engine:

![](../../.gitbook/assets/screenshot-2021-08-29-at-12.04.51-am.png)

![](../../.gitbook/assets/screenshot-2021-08-29-at-12.05.58-am.png)

**1. Crawling:**

* Google servers keep crawling chunks of internet
* while crawing, it keeps \*\*rank \*\*of each page(using **page\_rank**)
  * if more & reputed sites are directing to a site, it has high rank
  * **Damping factor**(e.g. dp = 0.85) for **random access**
    * i.e. 85% of the time crawler will get move to the directed site
    * 15% of the time crawler will jump to **any random page on** **whole internet**

**2. Inverted Indexing**

* Working(below pic)
* puts all this \*\*metadata \*\*in **metadata\_db**
* **Implemented using B-Trees - `O(logN)`**

![](../../.gitbook/assets/screenshot-2021-08-29-at-12.09.36-am.png)

**3. Querying/Searching**

* Sanitize, filter, stemm, lemmatize the search query to get **query\_keywords**
* **e.g.: Keyword targeting @flipkart 😎**
* **Approaches:**
  1. **Conjunctive Querying -> AND**
     * Performs\*\* AND operation\*\* on all the\*\* `words in query_keywords` \*\*
     * returns only those docs which have all the keywords present in them
  2. \*\*Disjunctive Querying -> UNION \*\*
     * Takes all the document which have **ANY of the keyword present**
     * then performs **UNION** on these docs
     * Then removes **duplicates** from the result
  3. **Conjunctive with Positioning**
     * The order of words in query is also imp!!!
       * E.g: if query is `men in black`
       * And if you dont consider the order of words; you'll also return results for `black in men`😂
     * HOW does it work?
       1. get results of normal **Conjunctive Querying**
       2. filter only those results which have **relative ordering** in place
          * E.g.
            * QUERY: men-0, in-1, black-2
            * Valid results: men-12, in-100, black-150✅
            * Invalid results: men-100, in-20, black-5❌



## 15. OTP Generation

* See\*\* #TinyUrl\*\*

## 16. Distributed Locks

* [Video](https://www.youtube.com/watch?v=v7x75aN9liM\&ab\_channel=TechDummiesNarendraL)
* See \*\*#GoogleDoc \*\*& **#APIRateLimiter**
* Use\*\* LockManager\*\*

## 17. Yelp | TripAdvisor | find Nearest Friend

* **Location DBs**
  * See #**Uber**

## 18. Distributed Logger

#### System Requirements

* High availability
* High consistency: no conflict
* Minimum data loss
* Low latency
* Minimum operation overhead

#### 1.Approach#1 : Log Consolidation

* \*\*How does it work? \*\*
  * In each of the distributed server we, install an agent which will monitor any logs that are written on this server
  * The App writes logs to the defined destination(e.g. logs to console)
  * Then the agent in background picks it and sends it to **centralize server(eg. `splunk`, `logstash`)**

![Approach#1. Log Consolidatgion](../../.gitbook/assets/screenshot-2021-08-29-at-8.21.21-pm.png)

#### 2.Approach#2: Log Streaming

* **How does it work?**
  * All the servers push their logs in Kafka queue
  * Kafka sends these logs to multiple subscribers
  * These subscribers process these logs & write them on a centrailzed place/run analytics
  * \*\*used@Pinterest \*\*(below pic from **Pinterest's** conference)

![Approach#2. Log Streaming](../../.gitbook/assets/screenshot-2021-08-29-at-8.21.43-pm.png)

* **Issues with This Approach (**#2: Log Streaming\*\*)\*\*
  * \*\*DATA LOSS: \*\*when an **Kafka broker fails**; it result in **Data Loss**.
    * \*\*FIX: \*\*
      * pick a kafka leader;
      * this leader keeps track of health of its children brokers
      * leader decides which kafka broker have to choose/remove/rep
  * \*\*OPERATION OVERHEAD: \*\*Have to **reconfigure all the dependent services; when we add/replace a new kafka broker**
    * **FIX**:
      * leader decides which kafka broker have to choose/remove/replace
  * \*\*DaTA DUPLICATION: \*\*multiple copies of message among brokers
    * \*\*FIX: \*\*
      * Use a sanitisation service before writing logs to S3/HDFS

![Approach#2. Log Streaming @Pinterest](../../.gitbook/assets/screenshot-2021-08-29-at-9.03.49-pm.png)

#### #ISSUE with these approaches: `Correlation ID`

* service A runs in server1, it calls service B that runs in server 2 and then another service C that runs in server 3. **How to correlate all the 3 logs for 1 single workflow?**
* **How to fix this?**
  * \=> attach a unique ID(`request_id`or `context_id` ) at **API gateway level** with this request
  * Now this ID will remain same for this log across microservices. Bazinga!

![](../../.gitbook/assets/screenshot-2021-08-29-at-8.24.50-pm.png)

## 19. Slack @coinbase

* [Whimsical](https://whimsical.com/slack-NTe7cDhHvX3AWfF7k9quyw)

#### #1. Requirement Gathering ======================================

#### 1.1 Functional Requirements

* Use should be able to send & receive chat messages from his/her contacts who are also on slack
* Group chat (upto 250 members) ??
* Track messages status: sent/delivered/read ??
  * \=> Slack shows notification if msg was unable to send
* Account registration using mail/phone
* Push Notifications: when the user is offline- send notifications for new msgs
* When the use comes online; he should be able to see all new msgs
* Adding support for media files(img.video.audio)
* E2E encryption

#### 1.2 NonFunctional Requirements - Usage Patterns(read heavy/CAP tradeoffs)

* High availability
* Fault Tolerant
* Consistency
* Scalable
* Minimum latency (real-time chat experience)
* Durability(keep chat history)

#### 1.3 Out of Scope

* Suppor for Slack-web ?
* Analytics/Monitoring

#### #2. Back-of-the-envelope estimation ============================

#### 2.1 Scale of System

* DAU = 500M
* 1 user sends 100 msgs daily
* \==> 50B msgs per day

#### 2.2 Storage size estimation

* size of 1 msg = 100bytes
  * \=> total size = 20B\*100 byte = 2TB/day
    * \=> 5PB for 5 years

#### 2.3 Bandwidth estimation(read+write)

* incoming & outgoing data = 2TB/(24\*3600) = 25MB/s

#### #3. APIs =======================================================

* **1-to-1 Chat**
  * `createAccount(API_key, use_id, name, email...)`
  * `validateAccount(API_key, user_id, validation_code)`
  * `initiateDirectChatSession(API_key, sender_id, receiver_id, handshake_info)`
    * \=> for initial handshake
  * `sendMessage(API_key, session_id, msg_type, msg)`
    * `Returns msg_id`
  * `getMessageStatus(API_key, message_id)`
  * `readNewMessage(API_key,session_id, last_msg_id)`
    * `last_msg_id`to be used as **pointer** to separate b/w read & not-read msgs
* **Group chats**
*
  * `createGrop(API_key, group_id, group_name, `**`admin, [members]`**`)`
  * `addUserToGroup(API_Key, group_id, user_id,admin_id)`
  * `removeUserFromGroup(API_Key, group_id, user_id,admin_id)`
  * `promoteMemberToGroup(API_key,group_id,user_id)`

#### #4. Models:Classes, DB Schema & ER diagrams=====================

#### 4.1 Tables Schemas

* **User**
  * user\_id: PK
  * name
  * email
  * ...
* **Group**
  * groupID: PK
  * name
  * created\_time
  * member\_count
* **GroupMembership**
  * groupID: **PK**
  * userID: **SK(Secondary Key)**
  * creation\_time : datetime
  * user\_type: ADMIN,MEMBER
* **Sessions**
  * session\_id : PK
  * user\_id
  * appserver\_id
  * last\_activity
  * timestamp

#### 4.2 DBs choices(NoSQL/SQL)

* **How to shard GroupMembership table**
  * \*\*Option#1: \*\*Shard by groupID => Called **Local Index**
    * \=> then membership info will be spread across all the shards to which user belongs
  * \*\*Option#2: \*\*Shard by userID(**SK**)=> Called **Global Index**
    * \=> group info will be spread
  * **WHich one to choose:**
    * it seems to me that **creating groups and updating their membership is potentially less frequent** than the ongoing msgs posted into the group chats by users.
    * So the Session and Fanout service benefits **more from a global index on userID**.
    * Users who create/update a group will necessarily have to wait for scatter/gather across partitions but this is less frequent than the msg posts occurring within the group chats.

#### #5. Draw 'Basic HLD'=============================================

### #WebSockets

* **USE CASE: chatting @whatsapp**
* In the beginning; a **Handshake** connection(usually **HTTP**) is established b/w client & server
* After this; the client & server communicate through a **bi-directional long-lived TCP connection**
* **PROS:**
  * bidirecional low latency communication
  * Reduced overhead of HTTP requests
* **CONS:**
  * Clients are responsible for connections
  * Scalability challanges

**Hystrix:**

* \=> Hystrix is a\*\* latency and fault tolerance library\*\* designed to isolate points of access to remote systems, services and 3rd party libraries
* Advantages:
  * Stop cascading failures i.e. reject the request if it cant be handled
  * Realtime **monitoring** of configurations changes
  * Concurrency aware request caching
  * Automated batching through request collapsing
* IE. If a micro service is failing then return the default response and wait until it recovers.

#### 1. Gateway Service

* Responsible for creating \*\*websocket connection \*\*b/w app server & user
* Makes all the API calls to other services as per the user's request

#### 2. Sessions Service

* stores info: which client is connected to which server
* When clientA sends a msg to clientB:
  * clientA sends msg to geteway\_service
  * gateway\_service is pretty dumb(doesnt have inofo on usr's session)
  * gateway\_service passes this req to sessionService
  * session services returns with the details of clientB
  * then gateway service sends that msg to client B
* **+--> Enters WebSockets**

#### 3. UserActivity Service

* takes care of last seen/typing....
* polling/webSockets

#### 4. Group Service

* How does group msging work?
* Fanout sevies asks group srervice for all group data
* then it fans out msgs to all the members
* **DO: batch\_processing /limit the number of users**

#### **5. Someone's typing...**

* typing indicator was triggered on the first keystroke and repeated as more keystrokes occurred.
* If no keystrokes were registered after 10 seconds, the indicator would no longer be displayed. Either you were typing, or you weren’t.
* **If a user stops typing for five seconds, Slack removes the “person is typing” indicator.**
* So when user starts typing update your database and set isTyping true.
* Dont forget to check if isTyping set to true so it will not update every time user presses the key
*   EVENT is Implement using a <mark style="color:orange;">**pub/sub trigger**</mark>

    ```
    {
      "isTyping":true,
      "fromDeviceToken": "xxxx",
      "timestamp": 12345
    }
    ```
* **ISSUE: **If user A **connection is lost during typin**g then the status will be always remain true until he resumes the connection. To solve this problem you can have one DateTime field in your firebase object

#### #6. Detailed HLD ================================================

![](../../.gitbook/assets/screenshot-2021-09-01-at-7.24.13-pm.png)

![](../../.gitbook/assets/screenshot-2021-09-01-at-5.10.18-pm.png)



## 20. Stocks Exchange

![](../../.gitbook/assets/screenshot-2021-09-01-at-5.57.17-pm.png)

![](../../.gitbook/assets/screenshot-2021-09-01-at-6.10.25-pm.png)

![](../../.gitbook/assets/screenshot-2021-09-01-at-6.05.36-pm.png)

![](../../.gitbook/assets/screenshot-2021-08-31-at-7.00.38-pm.png)



## 22. Github - code deployment system

* Clemment's mock interview: [link](https://www.youtube.com/watch?v=q0KGYwNbf-0\&ab\_channel=Cl%C3%A9mentMihailescu)

## #More From Leetcode
