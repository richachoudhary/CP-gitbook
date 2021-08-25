# HLD:Questions

## 0.Template

```text
#1. Requirement Gathering ======================================
        1.1 Functional Requirements
        1.2 NonFunctional Requirements - Usage Patterns(read heavy/CAP tradeoffs)
        1.3 Out of Scope
#2. Back-of-the-envelope estimation ============================
        2.1 Scale of System
        2.2 Storage size estimation
#3. APIs =======================================================
        GET  /name/:id      Req:{}, Res:{}
        POST /name/:id      Req:{} 
#4. Models:Classes, DB Schema & ER diagrams=====================
#5. Draw Basic HLD =============================================
#6. EVOLVE HLD to scale & indepth discussion of components =====
#7. Walk down flow of every action =============================
#7. Identifying and resolving bottlenecks ======================
```

## 1.Instagram

* Whimiscal [Board Link](https://whimsical.com/instagram-TofiB1JrEPSiGg9tHkXTgN)

![](../.gitbook/assets/screenshot-2021-08-24-at-5.27.15-pm.png)

```text
#1. Requirement Gathering ======================================
        
        * Functional Requirements:
                1. Users can create account
                2. Users can make posts(photos/text)
                3. Users can follow other users
                4. Users can like+comment on others/self' posts
                        *[?] Comment on a comment? => how many recursion levels(1?)
                        *[?] like a comment?  
                5. Timeline of all those whom user follow
        
        * Non-functional Requirements:
                1. Service is hightly available
                2. The acceptable latency of the system is 200ms for News Feed generation.
                3. Consistency can take a hit (in the interest of availability), 
                        if a user doesn’t see a photo for a while; it should be fine.
                4. The system should be highly reliable; any uploaded photo or video should never be lost.
        
        * Out of Scope:
                * Notifications?
                        * Push notifications => normal user
                        * Celebrity ===> PULL Notifications  
                * Adding tags to photos
                * searching photos on tags
                * commenting on photos
                * tagging users to photos
                * follow recommendation
        
        
#2. Back-of-the-envelope estimation ============================
        2.1 Scale of System
                * Total Userbase    : 500M
                * Daily Active Users: 1M
                * 2 new photos per user day => 2M new photos per day
        
        2.2 Storage size estimation
                * size of 1 photo = 5MB
                 => Space required per day : 2M*5MB  = 10 TB
                 => Total space required for 10 years = (10 TB )(365)(10) = 36.5 PB
                                                                          ~ 40 PB (accounting dec in camera price)
                
        2.3 CAP Tradeoffs
                * System is read heavy
                * Users can upload as many photos as they want 
                        => Storage management is crucial
                * Low latency is expected while viewing photos
                * Data should be 100% reliable. 
                        If a user uploads a photo, the system will guarantee that it will never be lost.


#3. APIs =======================================================
        1. POST /user/:id :: {userData}      
        2. GET /user/:id 
        3. POST /follow/:followeeID
        4. POST /like/:postID
        5. POST /comment/:parentID
        6. GET  /getFeed
                * Feed Generation Service PRECOMPUTES user's feed "hourly" & stores in cache
                        * Based On:
                        * GET /getUsersFollowedBuy/:userID    => set<userID> 
                        * then-> GET /getPostsByUser/:userID  => set<postID> # N-latest posts by each
        
        
#4. Models : Defining Classes & ER Diagrams======================
        1. User
        2. Post
                * postID(PK,UUID)
                * text
                * imangeUrl
                * timestamp
                * userId
        3. Like
                * likeId(PK, UUID)
                * parentId (could be postId or commentId)
                * parentType (comment/post)
                * userId
                * timestamp
        4. Comment
                * commentID(PK, uuid)
                * text
                * timestamp
                * userId
        5. Follow
                * followerID
                * followeeID
                * timestamp
#5. Draw Basic HLD =============================================
#6. EVOLVE HLD to scale & indepth discussion of components =====
#7. Identifying and resolving bottlenecks ======================
```

![](../.gitbook/assets/screenshot-2021-08-24-at-5.26.54-pm.png)

## 2. Parking Lot

* Whimsical Board: [link](https://whimsical.com/parking-lot-9Jq2YZsmfcmUpRbkSgFSr7)
* Code: `/Users/aayush/Sandbox/llds/ParkingLot`

```text
#1. Requirement Gathering ======================================
        1.1 Functional Requirements
                * Reserve a parking spot
                * Receive a ticket/receipt
                * Make payment
                * 3 Types of parking spots: Compact, Regular, large
                * Flat pricing for each spot, per hour 
        1.2 NonFunctional Requirements 
                * High consistency (no 2 people should reserve same spot)
                        * Go for Strong Consistency (rather than Eventual Consitency)
                        * Hence RDBMS (ACID transactions)
                * Reads >>> Writes
        1.3 Out of Scope
                * In-house payment system
#2. Back-of-the-envelope estimation ============================
        2.1 Scale of System
                * 10 floors per garage, 200 spots per floors => 2000 spots
                        * => Not applicable for big data
        2.2 Storage size estimation
#3. APIs =======================================================
        3.1 External Endpoints:
                * POST /create_account
                        * Params: email, pwd(hashed), name, (3rd party login)
                * POST /reserve
                        * Params: garage_id, start_time, end_time
                        * Returns: reservation_id, spot_id
                * /payment => 3-rd party
                        * Params: reservation_id
                        * [?] to be called internally by /reserve
                * POST /cancel
                        * Params: reservation_id
        3.2 Internal Endpoints:
                * /calculate_payment/:reservation_id
                * /check_free_spots
                        * Has logic if smaller vehicles can fit into one large spot
                * /allocate_spot
                        * Params: garage_id, vehicle_type, time

#4. Models : Classes, DB Schema & ER diagrams=====================
        * Reservations
                * id : PK, serial
                * garage_id: FK, int
                * spot_id: FK, int
                * start: int
                * end: int
                * paid: boolean
        * Garage
                * id: PK, serial
                * zipcode: varchar
                * rate_compact: decimal
                * rate_regular: decimal
                * rate_large: decimal
        * Spots
                * id: PK, serial
                * garage_id: FK, int
                * vehicle_type: ENUM
                * status: ENUM
        * Users
                * id: PK, serial
                * email: varchar
                * password: varchar(NOTE: this is probably SHA-256 hashed)
                * name: varchar
        * Vehicles
                * id: PK, serial
                * user_id: FK, int
                * license: varchar
                * vehicle_type: ENUM

#5. Draw Basic HLD =============================================
#6. EVOLVE HLD to scale & indepth discussion of components =====
#7. Walk down flow of every action =============================
#7. Identifying and resolving bottlenecks ======================
```

![](../.gitbook/assets/screenshot-2021-08-25-at-2.27.04-am.png)

## 3. TinyURL

* Whimsical board: [link](https://whimsical.com/tinyurl-XRrbRGZFccA2bhgqDBsRGp)

```text
#1. Requirement Gathering ======================================
        1.1 Functional Requirements
                * customer Login
                * Given a URL; generte a shorter & unique alias of it: www.short.ly/abc123
                        * [?] length of short url
                * getLongUrl(short_url)
                * Expiry/TTL for each short URL
        1.2 NonFunctional Requirements - Usage Patterns(read heavy/CAP tradeoffs)
                * High Availability (for reads to work)
                * High consistency (to avoid duplicate writes)
                * Short ULR should be unique
        1.3 Out of Scope
                * customized short url
                * analytics
                * API support

#2. Back-of-the-envelope estimation ============================

        2.1 Scale of System
                * New URLs per month(write) = 500 M
                * QPS = 500M/(30*24*60*60) = 200 URLS write per second
                * Read:Write = 100:1
                        => #urls read per month = 500M*100 = 50B
        2.2 Storage size estimation
                * store all ursl for 5 years
                        * => Total urls stored in 5 year = 500M*5*12 = 30B
                * size of single stored obj = 500bit
                        * => total storage reqd = 30B * 500 bit = 15 TB
                * CACHING:
                        * assume 80-20 rule:
                                * i.e. 20% of URLs generate 80% of traffic
                                * cache these 20% hot URLs
                                * cache size per second = 20K*(500bit) = 10MB
                                * => cache size per day = 10MB*24*3600 = 100GB
        2.3 Bandwidht Estimate
                * Incoming(write) req = 200 * 500 bytes = 100 KB/s
                * Outgoing(read) req  = 20K * 500 bytes = 10 MB/s 
                
#3. APIs =======================================================
        * createURL(api_dev_key, original_url, custom_alias=None, user_id=None, expire_date=None)
                * returns short URL string
        * getLongURL(api_dev_key, short_url,user_id) 
                * returns original LONG url string
        * deleteURL(api_dev_key, short_url)
        
        * NOTE: how to prevent abuse: 
                To prevent abuse, we can limit users via their api_dev_key
                
#4. Models:Classes, DB Schema & ER diagrams=====================
        * URL
                * short_url : PK, varchar
                * original_url : varchar
                * createdOn : datetime
                * expiresOn : datetime
                * createdBy : user_id, FK
        * User
                * user_id : PK, varchar
                * name: varchar
                * email: varchar
                * password: varchar (hashed)
                * createdOn : datetime
                * last_login: datetime
                
#5. Draw Basic HLD =============================================

* Encoding Algos
        1. base36 ([a-z ,0-9]) 
        2. base62 ([A-Z, a-z, 0-9]) 
        3. Base64 (if we add ‘+’ and ‘/’)
        4. MD5/ SHA256
* [? ]what should be the length of the short key? 6, 8, or 10 characters?
        * Using base64 encoding, a 6 letters long key would result in 64^6 = ~68.7 billion possible strings
        * Using base64 encoding, an 8 letters long key would result in 64^8 = ~281 trillion possible strings
        * ASSUME(len = 6) With 68.7B unique strings, let’s assume six letter keys would suffice for our system.

* MD5 algorithm as our hash function, it’ll produce a 128-bit hash value.
* After base64 encoding, we’ll get a string having more than 21 characters 
        *(since each base64 character encodes 6 bits of the hash value). 
* Now we only have space for 8 characters per short key, how will we choose our key then? 
        * We can take the first 6 (or 8) letters for the key. This could result in key duplication, to resolve that, we can choose some other characters out of the encoding string or swap some characters.


# How to avoid duplicate entries(by multiple server instances)
        1. Keep generating urls until its unique
        2. Append a unique key to url before encoding it
                * Unique key could be:
                        1. UserID (if exists)
                        2. increasing Counter per machine
        2.1 ISSUE: how do you manage counters on individual machine: overflow/machine failure/addition
                * => Use zookeeper
                        * a centralized service for providing configuration information, naming, synchronization and group services over large clusters in distributed systems. 
                        * The goal is to make these systems easier to manage with improved, more reliable propagation of changes
                        
# Cleaup Util        
```

![](../.gitbook/assets/screenshot-2021-08-25-at-1.56.32-pm.png)

## 4. BookMyShow

* Whimisical Board [link](https://whimsical.com/bookmyshow-SiSmppUMB3mrGzyr8YFyY5)

{% tabs %}
{% tab title="requirements.md" %}
```python
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
            * Payments - 3P
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
```
{% endtab %}

{% tab title="classes.py\(OOP shell\)" %}
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

{% tab title="working\_code.py" %}
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

![](../.gitbook/assets/screenshot-2021-08-25-at-8.57.20-pm.png)

## 4. Netflix/Youtube

## 5. Twitter

## 6. BookMyShow

## 7. Whatsapp/FB Messenger

## 8. Pastebin

## 9. Google Docs

## 10. Dropbox

## 11. Twitter/Uber Search\(&lt;elasticsearch&gt;\)

## 12. Typehead Suggestion

## \#More From Leetcode

