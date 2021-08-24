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



## 3. TinyURL

## 4. Twitter

## 5. Netflix/Youtube

## 6. BookMyShow

## 7. Pastebin

## 8. Whatsapp/FB Messenger 

## 9. Google Docs

## 10. Twitter/Uber Search\(&lt;elasticsearch&gt;\)

## 11. Typehead Suggestion

## \#More From Leetcode

