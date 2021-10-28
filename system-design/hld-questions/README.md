# HLD:Questions

HLD:Questions

## 0.Template <a href="0.template" id="0.template"></a>

1\* Multiple Instance of each service2\* API Gateway(LB+Proxy)3\* Zookeeper4\* CDN5\* Varnish6\* Cache(write back)-Redis7\* SQL8\* Read replicas9\* sharding(user\_id/location)10\* NoSQL11\* Replicas/Distributed12\* Kafka/worker13\* Stateless Microservices14\* Hystrix15\* HDFS/S316\* local cache : last 50 msgsCopied!1#1. Requirement Gathering ======================================21.1 Functional Requirements31.2 NonFunctional Requirements - Usage Patterns(read heavy/CAP tradeoffs)41.3 Out of Scope5#2. Back-of-the-envelope estimation ============================62.1 Scale of System72.2 Storage size estimation82.3 Bandwidth esitmation(read+write)9#3. APIs =======================================================10GET /name/:id Req:{}, Res:{}11POST /name/:id Req:{}12#4. Models:Classes, DB Schema & ER diagrams=====================13\* Tables1415\* DBs & choice(NoSQL/SQL)16#5. Draw 'Basic HLD'=============================================17#6. EVOLVE & 'Draw Detailed HLD' with the discussion on each comp =====18#7. Walk down flow of every action =============================19#7. Identifying and resolving bottlenecks ======================Copied!

#### #1. Requirement Gathering ====================================== <a href="1.-requirement-gathering" id="1.-requirement-gathering"></a>

#### 1.1 Functional Requirements <a href="1.1-functional-requirements" id="1.1-functional-requirements"></a>

* ​

#### 1.2 NonFunctional Requirements - Usage Patterns(read heavy/CAP tradeoffs) <a href="1.2-nonfunctional-requirements-usage-patterns-read-heavy-cap-tradeoffs" id="1.2-nonfunctional-requirements-usage-patterns-read-heavy-cap-tradeoffs"></a>

* ​

#### 1.3 Out of Scope <a href="1.3-out-of-scope" id="1.3-out-of-scope"></a>

* ​

#### #2. Back-of-the-envelope estimation ============================ <a href="2.-back-of-the-envelope-estimation" id="2.-back-of-the-envelope-estimation"></a>

#### 2.1 Scale of System <a href="2.1-scale-of-system" id="2.1-scale-of-system"></a>

* ​

#### 2.2 Storage size estimation <a href="2.2-storage-size-estimation" id="2.2-storage-size-estimation"></a>

* ​

#### 2.3 Bandwidth estimation(read+write) <a href="2.3-bandwidth-estimation-read+write" id="2.3-bandwidth-estimation-read+write"></a>

* ​

#### #3. APIs ======================================================= <a href="3.-apis" id="3.-apis"></a>

* ​

#### #4. Models:Classes, DB Schema & ER diagrams===================== <a href="4.-models-classes-db-schema-and-er-diagrams" id="4.-models-classes-db-schema-and-er-diagrams"></a>

#### 4.1 Tables Schemas <a href="4.1-tables-schemas" id="4.1-tables-schemas"></a>

* ​

#### 4.2 DBs choices(NoSQL/SQL) <a href="4.2-dbs-choices-nosql-sql" id="4.2-dbs-choices-nosql-sql"></a>

* ​

#### #5. Draw 'Basic HLD'============================================= <a href="5.-draw-basic-hld" id="5.-draw-basic-hld"></a>

#### #6. Detailed HLD ================================================ <a href="6.-detailed-hld" id="6.-detailed-hld"></a>

## 1.Instagram <a href="1.instagram" id="1.instagram"></a>

* Whimiscal [Board Link](https://whimsical.com/instagram-TofiB1JrEPSiGg9tHkXTgN)​

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-2064a3feb30e91889a1367696f10ad6bd6665026%2FScreenshot%202021-08-24%20at%205.27.15%20PM.png?alt=media)1#1. Requirement Gathering ======================================23\* Functional Requirements:41. Users can create account52. Users can make posts(photos/text)63. Users can follow other users74. Users can like+comment on others/self' posts8\*\[?] Comment on a comment? => how many recursion levels(1?)9\*\[?] like a comment?105. Timeline of all those whom user follow1112\* Non-functional Requirements:131. Service is hightly available142. The acceptable latency of the system is 200ms for News Feed generation.153. Consistency can take a hit (in the interest of availability),16if a user doesn’t see a photo for a while; it should be fine.174. The system should be highly reliable; any uploaded photo or video should never be lost.1819\* Out of Scope:20\* Notifications?21\* Push notifications => normal user22\* Celebrity ===> PULL Notifications23\* Adding tags to photos24\* searching photos on tags25\* commenting on photos26\* tagging users to photos27\* follow recommendation282930#2. Back-of-the-envelope estimation ============================312.1 Scale of System32\* Total Userbase : 500M33\* Daily Active Users: 1M34\* 2 new photos per user day => 2M new photos per day35362.2 Storage size estimation37\* size of 1 photo = 5MB38=> Space required per day : 2M\*5MB = 10 TB39=> Total space required for 10 years = (10 TB )(365)(10) = 36.5 PB40\~ 40 PB (accounting dec in camera price)41422.3 CAP Tradeoffs43\* System is read heavy44\* Users can upload as many photos as they want45=> Storage management is crucial46\* Low latency is expected while viewing photos47\* Data should be 100% reliable.48If a user uploads a photo, the system will guarantee that it will never be lost.49​50​51#3. APIs =======================================================521. POST /user/:id :: {userData}532. GET /user/:id543. POST /follow/:followeeID554. POST /like/:postID565. POST /comment/:parentID576. GET /getFeed58\* Feed Generation Service PRECOMPUTES user's feed "hourly" & stores in cache59\* Based On:60\* GET /getUsersFollowedBuy/:userID => set\<userID>61\* then-> GET /getPostsByUser/:userID => set\<postID> # N-latest posts by each626364#4. Models : Defining Classes & ER Diagrams======================651. User662. Post67\* postID(PK,UUID)68\* text69\* imangeUrl70\* timestamp71\* userId723. Like73\* likeId(PK, UUID)74\* parentId (could be postId or commentId)75\* parentType (comment/post)76\* userId77\* timestamp784. Comment79\* commentID(PK, uuid)80\* text81\* timestamp82\* userId835. Follow84\* followerID85\* followeeID86\* timestamp87#5. Draw Basic HLD =============================================88#6. EVOLVE HLD to scale & indepth discussion of components =====89#7. Identifying and resolving bottlenecks ======================Copied!![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-c721bcaf404c10ffbf29a37b761ea26fd4416577%2FScreenshot%202021-08-24%20at%205.26.54%20PM.png?alt=media)

## 2. Parking Lot <a href="2.-parking-lot" id="2.-parking-lot"></a>

* Whimsical Board: [link](https://whimsical.com/parking-lot-9Jq2YZsmfcmUpRbkSgFSr7)​
* Code: `/Users/aayush/Sandbox/llds/ParkingLot`

1#1. Requirement Gathering ======================================21.1 Functional Requirements3\* Reserve a parking spot4\* Receive a ticket/receipt5\* Make payment6\* 3 Types of parking spots: Compact, Regular, large7\* Flat pricing for each spot, per hour81.2 NonFunctional Requirements9\* High consistency (no 2 people should reserve same spot)10\* Go for Strong Consistency (rather than Eventual Consitency)11\* Hence RDBMS (ACID transactions)12\* Reads >>> Writes131.3 Out of Scope14\* In-house payment system15#2. Back-of-the-envelope estimation ============================162.1 Scale of System17\* 10 floors per garage, 200 spots per floors => 2000 spots18\* => Not applicable for big data192.2 Storage size estimation20#3. APIs =======================================================213.1 External Endpoints:22\* POST /create\_account23\* Params: email, pwd(hashed), name, (3rd party login)24\* POST /reserve25\* Params: garage\_id, start\_time, end\_time26\* Returns: reservation\_id, spot\_id27\* /payment => 3-rd party28\* Params: reservation\_id29\* \[?] to be called internally by /reserve30\* POST /cancel31\* Params: reservation\_id323.2 Internal Endpoints:33\* /calculate\_payment/:reservation\_id34\* /check\_free\_spots35\* Has logic if smaller vehicles can fit into one large spot36\* /allocate\_spot37\* Params: garage\_id, vehicle\_type, time38​39#4. Models : Classes, DB Schema & ER diagrams=====================40\* Reservations41\* id : PK, serial42\* garage\_id: FK, int43\* spot\_id: FK, int44\* start: int45\* end: int46\* paid: boolean47\* Garage48\* id: PK, serial49\* zipcode: varchar50\* rate\_compact: decimal51\* rate\_regular: decimal52\* rate\_large: decimal53\* Spots54\* id: PK, serial55\* garage\_id: FK, int56\* vehicle\_type: ENUM57\* status: ENUM58\* Users59\* id: PK, serial60\* email: varchar61\* password: varchar(NOTE: this is probably SHA-256 hashed)62\* name: varchar63\* Vehicles64\* id: PK, serial65\* user\_id: FK, int66\* license: varchar67\* vehicle\_type: ENUM68​69#5. Draw Basic HLD =============================================70#6. EVOLVE HLD to scale & indepth discussion of components =====71#7. Walk down flow of every action =============================72#7. Identifying and resolving bottlenecks ======================Copied!![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-91a01232222864d55bfad6e597da8f4392f2f0aa%2FScreenshot%202021-08-25%20at%202.27.04%20AM.png?alt=media)

## 3. \~TinyURL <a href="3.-tinyurl" id="3.-tinyurl"></a>

* Whimsical board: [link](https://whimsical.com/tinyurl-XRrbRGZFccA2bhgqDBsRGp)​
* Amazing similar read: HN: [How does Google Authenticator work?](https://prezu.ca/post/2021-07-30-totp-1/) 🤯

1#1. Requirement Gathering ======================================21.1 Functional Requirements3\* customer Login4\* Given a URL; generte a shorter & unique alias of it: www.short.ly/abc1235\* \[?] length of short url6\* Expiry/TTL for each short URL7\* getLongUrl(short\_url)891.2 NonFunctional Requirements - Usage Patterns(read heavy/CAP tradeoffs)10\* High Availability (for reads to work)11\* High consistency (to avoid duplicate writes)12\* Short ULR should be unique131.3 Out of Scope14\* customized short url15\* analytics16\* API support17​18#2. Back-of-the-envelope estimation ============================19​202.1 Scale of System21\* New URLs per month(write) = 500 M22\* QPS = 500M/(30\*24\*60\*60) = 200 URLS write per second23\* Read:Write = 100:124=> #urls read per month = 500M\*100 = 50B252.2 Storage size estimation26\* store all ursl for 5 years27\* => Total urls stored in 5 year = 500M\*5\*12 = 30B28\* size of single stored obj = 500bit29\* => total storage reqd = 30B \* 500 bit = 15 TB30\* CACHING:31\* assume 80-20 rule:32\* i.e. 20% of URLs generate 80% of traffic33\* cache these 20% hot URLs34\* cache size per second = 20K\*(500bit) = 10MB35\* => cache size per day = 10MB\*24\*3600 = 100GB362.3 Bandwidth Estimate37\* Incoming(write) req = 200 \* 500 bytes = 100 KB/s38\* Outgoing(read) req = 20K \* 500 bytes = 10 MB/s3940#3. APIs =======================================================41\* createURL(api\_dev\_key, original\_url, custom\_alias=None, user\_id=None, expire\_date=None)42\* returns short URL string43\* getLongURL(api\_dev\_key, short\_url,user\_id)44\* returns original LONG url string45\* deleteURL(api\_dev\_key, short\_url)4647\* NOTE: how to prevent abuse:48To prevent abuse, we can limit users via their api\_dev\_key4950#4. Models:Classes, DB Schema & ER diagrams=====================51\* URL52\* short\_url : PK, varchar53\* original\_url : varchar54\* createdOn : datetime55\* expiresOn : datetime56\* createdBy : user\_id, FK57\* User58\* user\_id : PK, varchar59\* name: varchar60\* email: varchar61\* password: varchar (hashed)62\* createdOn : datetime63\* last\_login: datetime6465#5. Draw Basic HLD =============================================66​67\* Encoding Algos681. base36 (\[a-z ,0-9])692. base62 (\[A-Z, a-z, 0-9])703. Base64 (if we add ‘+’ and ‘/’)714. MD5/ SHA25672\* \[?]what should be the length of the short key? 6, 8, or 10 characters?73\* Using base64 encoding, a 6 letters long key would result in 64^6 = \~68.7 billion possible strings74\* Using base64 encoding, an 8 letters long key would result in 64^8 = \~281 trillion possible strings75\* ASSUME(len = 6) With 68.7B unique strings, let’s assume six letter keys would suffice for our system.76​77\* MD5 algorithm as our hash function, it’ll produce a 128-bit hash value.78\* After base64 encoding, we’ll get a string having more than 21 characters79\*(since each base64 character encodes 6 bits of the hash value).80\* Now we only have space for 8 characters per short key, how will we choose our key then?81\* We can take the first 6 (or 8) letters for the key. This could result in key duplication, to resolve that, we can choose some other characters out of the encoding string or swap some characters.82​83​84# How to avoid duplicate entries(by multiple server instances)851. Keep generating urls until its unique862. Append a unique key to url before encoding it87\* Unique key could be:881. UserID (if exists)892. increasing Counter per machine902.1 ISSUE: how do you manage counters on individual machine: overflow/machine failure/addition91\* => Use zookeeper92\* a centralized service for providing configuration information, naming, synchronization and group services over large clusters in distributed systems.93\* The goal is to make these systems easier to manage with improved, more reliable propagation of changes9495# Cleaup UtilCopied!![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-6b4b6ef807d3242c7d21fceef15bf027126c3bf4%2FScreenshot%202021-08-25%20at%201.56.32%20PM.png?alt=media)

## 4. BookMyShow <a href="4.-bookmyshow" id="4.-bookmyshow"></a>

* Whimisical Board [link](https://whimsical.com/bookmyshow-SiSmppUMB3mrGzyr8YFyY5)​

requirements.mdclasses.py(OOP shell)working\_code.py1# 1. Requirement Gathering ======================================21.1 Functional Requirements34\* Other sevices(like Paytm) can also book seats in same hall5\* Show multiple cities6\* Each theater can have multiple halls7\* Each hall can run 1 movie at 1 time8\* Movies will have multiple shows9\* Customers can search movie by title, language, genre, release date, city.10=> Redirect search reqs to Elastic Search11\* It also works as Analytics Engine12\* Customers can see the theaters as per their filtered search13\* Customers can see seating arrangement of halls & select any city they want14\* Customers can see booked/free tickets15\* Payments - 3P16\* Show movie info17\* Ensure No two customers can reserve the same seat.18​191.2 NonFunctional Requirements - Usage Patterns(read heavy/CAP tradeoffs)2021\* Highly Concurrent22231.3 Out of Scope24​25\* Moive suggestions26\* Give Reviews, Ratings27\* Send ticket my sms/whatsapp/mail28\* Add discount coupon during payment29# 2. Back-of-the-envelope estimation ============================302.1 Scale of System312.2 Storage size estimation32# 3. APIs =======================================================33# 4. Models:Classes, DB Schema & ER diagrams=====================34​35# Notes: ====================================================36​37\* Lock mechanism on seat booking:38\* If he doesn’t book within 10 min, release the seat.39​40\* For Search Queries:41=> Redirect search reqs to Elastic Search42\* It also works as Analytics Engine43​44\* For caching use: Redis or memcached45\* Redis is better choice as its distributed & persistent46​47\* Choice of DB:48=> use both RDBMS + NoSQL49\* RDMBS: store ACID/static data:50\* movie halls51\* seats52\* cities53\* userInfo54\* => Sharding55\* => Master/Slave for Read/Writes56\* NoSQL :57below data is Big data i.e. too much for RDBMS to digest58so use NoSQL for it59\* movie related info-cast/story/reviews etc60\* => Geo-distributed backups61​62\* Use Kafka queues to send tickets on mail/sms/generate pdfs in ASYNC63​64\* For Recommendation system:65\* Dump all data on HDFS66\* Process with Apache Spark67\* Run Hive queries68\* Build ML models & recommend69​70\* For concurrency:71​72\`\`\`s73SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;7475BEGIN TRANSACTION;7677-- Suppose we intend to reserve three seats (IDs: 54, 55, 56) for ShowID=9978Select \* From ShowSeat where ShowID=99 && ShowSeatID in (54, 55, 56) && isReserved=07980-- if the number of rows returned by the above statement is NOT three, we can return failure to the user.81update ShowSeat table...82update Booking table ...8384COMMIT TRANSACTION;85\`\`\`Copied!![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-d4dee280362b202e9bd51d43faca460f7bb6f106%2FScreenshot%202021-08-25%20at%208.57.20%20PM.png?alt=media)

## 4. Netflix/Youtube <a href="4.-netflix-youtube" id="4.-netflix-youtube"></a>

* Whimsical Board [link](https://whimsical.com/netflix-FeHCqLHW73v8wVuAD5r8T4)​
* Source: [article+video](https://www.youtube.com/watch?v=psQzyFfsUGU\&ab\_channel=TechDummiesNarendraL)​

1#1. Requirement Gathering ======================================2​31.1 Functional Requirements4\* upload videos.5\* view videos.6\* perform searches based on video titles.7\* record stats of videos, e.g., likes/dislikes, total number of views, etc.8\* add and view comments on videos.9101.2 NonFunctional Requirements11\* Highly reliable, no uploaded video should be lost12\* Service should be highly available13\* Consistency can take a hit14\* Real time UX; no lag15161.3 Out of Scope17\* Video recommendation18\* most popular videos19\* channels20\* subscriptions21\* watch later22\* favorites2324#2. Back-of-the-envelope estimation ============================252.1 Scale of System26\* Total users: 5B27\* Daily active users: 1 B28\* 1 User views 5 videos per day29=> total\_views\_per\_second = 1M\*5/(24\*2600) = 60K videos/sec30\* Ratio upload:view = 500:131=> total\_uploads\_per\_second = 120 videos/sec32332.2 Storage size estimation34\* size of 1 minute video(including all formats) = 50MB35=> upload\_size\_per\_day = 50MB\*120\*3600\*24 = 500TB3637#3. APIs =======================================================38\* uploadVideo(api\_dev\_key, video\_title, vide\_description, tags\[], category\_id, default\_language, recording\_details, video\_contents)39=> Returns HTTP 202(request accepted)40-> from Kafka/queue41\* Once video is uploaded; user will get an email42\* searchVideo(api\_dev\_key, search\_query, user\_location, maximum\_videos\_to\_return, page\_token)43=> Returns JSON of videos\_list:44\* video title45\* a thumbnail46\* video creation date47\* view count4849\* streamVideo(api\_dev\_key, video\_id, offset, codec, resolution)50=> Returns A media stream (a video chunk) from the given offset5152#4. Models:Classes, DB Schema & ER diagrams=====================53#5. Draw Basic HLD =============================================54#6. EVOLVE HLD to scale & indepth discussion of components =====Copied!

#### Notes on some components: <a href="notes-on-some-components" id="notes-on-some-components"></a>

* **Netflix's Cloud:**
  * Netflix operates in two clouds: **AWS and Open Connect.**
  * Both clouds must work together seamlessly to deliver endless hours of customer-pleasing video.
  * All video related things are handled by **Open Connect.**
  * Anything that doesn’t involve serving video is handled in **AWS**
    * login/billing/search/recommendation

1. 1.**Client**
   * lots of platforms
   * mobile
   * webapp
   * tv
   * xbox
   * \=> built using **ReactJS** - fast as **virtual DOM**
2. 2.**CDN** => **OpenConnect:**
   * Netflix's own CDN
   * they've placed lots of servers in every part of world- to play videos better
   * Region-wise movie collection:
     * Bollywood vs South indian movies
3. 3.ELB : **Amazon's ELB**
   * has 2 tier LB:
   * ELB’s are setup such that load is balanced across **zones** first, then **instances**
4. 4.**New Movie/Video Onboarding Service**(microservice)
   * Before this movie is made available to users, Netflix must convert the video into a format that works best for your device. This process is called\*\* transcoding or encoding.\*\*
   * **Transcoding/Encoding**
     * \*\*=> \*\*process that converts a video file from one format to another, to make videos viewable across different platforms and devices.
     * \*\*Why do we need it? \*\*why not just play the original video
       * device compatability resolution
       * internet speed
       * Pricing plan
   * NOTE: Netflix supports 2200 different devices
   * Netflix has 100-1000 versions of each movie
   * After transcoding, each format is \*\*pushed \*\*to all of the **OpenConnect CDNs**(for users to **start streaming**)
5. 5.\*\*ZUUL \*\*
   * intermediary network of servers to filter incoming/outgoing req & responses
   * i.e. req/response sanitation
   * Also used for beta testing / canary testing
6. 6.**Hystrix:**
   * \=> Hystrix is a\*\* latency and fault tolerance library\*\* designed to isolate points of access to remote systems, services and 3rd party libraries
   * Advantages:
     * Stop cascading failures i.e. reject the request if it cant be handled
     * Realtime **monitoring** of configurations changes
     * Concurrency aware request caching
     * Automated batching through request collapsing
   * IE. If a micro service is failing then return the default response and wait until it recovers.
7. 7.**Microservices:**
   * How to scale:
     * \*\*Isolation of critical endpoints: \*\*decouple critical microservicess to make them independent
     * \*\*Stateless: \*\*These services are designed such that any service instance can serve any request in a timely fashion and so if a server fails it’s not a big deal.
     * \*\*In the failure case \*\*requests can be routed to another service instance and we can automatically spin up a new node to replace it.
8. 8.**SSDs for Caching**
   * Storing large amounts of data in volatile memory\*\* (RAM) is expensive\*\*.
   * Modern disk technologies based on [SSD](https://en.wikipedia.org/wiki/Solid-state\_drive) are providing **fast access** to data but at a **much lower cost when compared to RAM**.
   * Hence, we wanted to move part of the data out of memory without sacrificing availability or performance.
   * The cost to store 1 TB of data on SSD is much lower than storing the same amount in RAM.
9. 9.**Databases:**
   1. 1.**SQL (EC2)**
      * used for all \*\*ACID \*\*transactions: like Billing
   2. 2.**NoSQL (Cassandra) : distributed**
      * user viewing history
      * read >> write => so Netflix had modified Cassandra
10. 10.**Kafka Analytics**
    * Viewing History
    * UI Activity
    * Analytics
    * Recommendation, ML Models\\

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-8169d4b2461c27647f6bd723fb46b924c3055371%2FScreenshot%202021-08-26%20at%205.45.02%20PM.png?alt=media)

## 5. Ketto/Go Fund Me <a href="5.-ketto-go-fund-me" id="5.-ketto-go-fund-me"></a>

* Whimsical: [link](https://whimsical.com/ketto-2S14YgGQ5Er7SLUPxdep5g)​
* Source: [LC](https://leetcode.com/discuss/interview-question/system-design/1397022/Go-Fund-me-System-design)​

1#1. Requirement Gathering ======================================21.1 Functional Requirements3​4\* Registered users can create campaigns to fund their cause.5\* Registered users can view a campaign by campaign ID6\* Registered users can collect money against a campaign7\* Registered users could contribute to a campaign based on campaign ID8\* Once a day we flush the collected money into the creator’s account9​101.2 NonFunctional Requirements - Usage Patterns/Tradeoffs11​12\* Low latency13\* Durability changes made to the campaigns or newly created campaign should not be lost14\* Eventual consistency15\* It is a growing system16​171.3 Out of Scope18\* User registration19\* Analytics20\* Recommendation21\* Search22\* Guest flow23​24#2. Back-of-the-envelope estimation ============================252.1 Scale of System26\* Total Active users: 50M27\* New users added daily: 50K (as 'growing system')28\* CAMPAIGN CREATION:291 user creates 5 campaigns => 5\*50 => 250M campaigns30\* CAMPAIGN VIEWING:315M view capaigns daily => 5M/(24\*3600) => 60 cmps/sec32\* => Hence, Load on the system isnt much33​342.2 Storage size estimation35\* SKIPPED (nothing much of storage here)36​37#3. APIs =======================================================38\* createCampaign(userId, String campaignName, CampaignDetails campaignDetails)39→ returns campaignId of the created campaign40​41\* getCampaignDetails(userId, campaignId)42→ Returns CamapignDetails of the given camapignId43​44\* pay(userId, CampaignId, PaymentDetails paymentDetails)45→ return a boolean if the payment was successful or not also updates the total collected amount against the campaign46​47#4. Models:Classes, DB Schema & ER diagrams=====================48\* SKIPPED49​50#5. Draw Basic HLD =============================================51\* Campaign Creator Service52\* Campaign Viewer Service53​54#6. EVOLVE HLD to scale & indepth discussion of components =====55Add/disucss on these optimisations:56\* Load balancer - which is entry point to our website57\* Gateway -- which would be responsible for filtering requests and authentication and authorization58\* Service discovery --- Would be responsible for providing service end points to internal services and also load balancing internally59\* Caching60Copied!![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-c4dab407fe412d46741f867b78d7e2d2dbda673a%2FScreenshot%202021-08-28%20at%206.23.13%20AM.png?alt=media)![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-906dc9b9a42c13e31dbed780ac2412cb2772d22e%2FScreenshot%202021-08-28%20at%206.36.56%20AM.png?alt=media)

## 6. Twitter <a href="6.-twitter" id="6.-twitter"></a>

* Whimsical Board [link](https://whimsical.com/twitter-63T4oateDAL6ZdsaJ5LdHT)​
* Video [link](https://www.youtube.com/watch?v=wYk0xPP\_P\_8\&ab\_channel=TechDummiesNarendraL)​

#### #1. Requirement Gathering ============================================= <a href="1.-requirement-gathering-1" id="1.-requirement-gathering-1"></a>

* **1.1 Functional Requirements**
  * tweet
    * text
    * photo
    * video
  * **trends**
    * see all the tending topics/hastags
  * follow others
  * timeline
    * home timeline(whom user follows)
    * user timeline(user history)
    * search timeline(all tweets as per searched keyword)
* **1.2 NonFunctional Requirements** - Usage Patterns(read heavy/CAP tradeoffs)
  * Highly available
  * Acceptable latency for timeline generation
  * Consistency can take a hit:
    * if a user doesn’t see a tweet for a while, it should be fine.
    * \*\*Eventual Consistency \*\*
  * User traffic will be distributed unevenly throughout the day
* **1.3 Out of Scope**
  * replying on tweets
  * tweet notification
  * suggestion - whom to follow
  * user tagging

#### #2. Back-of-the-envelope estimation ========================================= <a href="2.-back-of-the-envelope-estimation-1" id="2.-back-of-the-envelope-estimation-1"></a>

* **2.1 Scale of System**
  * Daily Active Users(DAU) : 200M
  * write: 2 tweets per user per day
    * \=> daily writes = 2\*200M = 400M/day
  * read:write = 1000:1
    * \=> daily reads = 400B/day
    * system is read-heavy
* **2.2 Storage size estimation**
  * **Text**: 140 chars a tweet
    * 2 bytes to store 1 char (w/o any compression)
    * \+30 bytes for tweet metadata(timestamp, location, userID)
    * \=> 400M\*(280b+30b) = 120GB/day
  * **photo**: 1 in 5 tweets has a photo
    * size of 1 photo = 200KB
    * \=> 400M\*200KB/5 = 400M\*40KB = 16MB\*M = 16TB
  * **video**: 1 in 10 tweets has a video
    * size of 1 video = 2MB
    * \=> 400M\*2MB/10 = 80TB
  * **=> Total daily storage reqd** = 120GB + 16TB + 80TB
    * \= 96.12 TB/day
    * \=> 1.11 GB/sec
* **2.3 Bandwidth estimation**
  * view tweets:
    * **text**:
      * \=> text: 28B\*280b = 7840GB/day = **90MB/sec**
    * user see all the **photos** of every tweet
      * \=> 28B/5\*200KB = 13GB/s
    * user plays 1 in every 3 **videos** of tweet
      * \=> (28B/10/3)\*2MB = 22GB/s
    * **=> total** = 35Gb/s

#### #3. APIs ======================================================= <a href="3.-apis-1" id="3.-apis-1"></a>

* **tweet**(api\_dev\_key, tweet\_data, tweet\_location, user\_location, media\_ids)
  * \=> returns tweet url to view
* **search**(api\_dev\_key, search\_terms, maximum\_results\_to\_return, sort, page\_token)
  * \=> JSON containing information about a list of tweets

#### #4. Table Schemas & DB Choices===================== <a href="4.-table-schemas-and-db-choices" id="4.-table-schemas-and-db-choices"></a>

* **Tables:**
  * **User**
    * userID : PK, int
    * name
    * email
    * pwd(hashed)
    * 3rd party login OAuth
    * last login
  * **Tweet**
    * tweetID: PK,int
    * userID
    * text
    * createdAt(ts)
    * locationCordinates
    * mediaAddress
  * **Follower**
    * followerID : FK
    * followeeID : FK
    * timestamp
* **Relations:**
  * 1-Many in User ---- Tweet
  * 1-Many in User ---- Follower
* \[?] Retweets:
* are to be considered a unique tweet & store in 'Tweet' table itself
* **DB choice:**
  * photos+vidoes => DFS
    * HDFS/S3
    * can be queued
  * User, Tweet, Follower tables => NoSQL
    * Distributed NoSQL
    * \=> RDBMS, though good for relations here wont be scalable enough
  * Relationship b/w tables: use\*\* key-value DB \*\*i.e. **Redis✅**
    * `<userID> -> [tweetIDs]`
    * `<userID> -> [followerIDs]`

#### #5. Draw 'Basic HLD'============================================= <a href="5.-draw-basic-hld-1" id="5.-draw-basic-hld-1"></a>

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-8dce893659dce1358bc9a9a90195cba85deb6549%2FScreenshot%202021-08-28%20at%201.25.03%20PM.png?alt=media)

#### #6. EVOLVE & 'Draw Detailed HLD' with the discussion on each comp ===== <a href="6.-evolve-and-draw-detailed-hld-with-the-discussion-on-each-comp" id="6.-evolve-and-draw-detailed-hld-with-the-discussion-on-each-comp"></a>

1. 1.\*\* How User Timeline is generated?\*\*
   * Go to Redis table#1 : \<userID> -> \[tweetIDs]
   * SCALING UP: **cache**
2. 2.**How to generate Home Timeline**
   * **Steps using Join**
     * get all followers of the user
     * get their latest tweets
     * merge, sort & display
   * **SCALING UP:**
   * ❌Shard/NoSQL/multiple nodes => wont be as fast as twitter
   * ✅ use "**Fanout**"
   * **Fanout**
     * Fanout => when a new tweet is generated; process it & DISTRIBUTE it to user timelines
     * **WORKING**:
       1. 1.user makes a new tweet
       2. 2.Store it in Tweets table
       3. 3.Push this tweet into his 'User Timeline'
       4. 4.Fan-out this tweet into 'Home Timeline' of ALL his followers
     * Hence; no DB query is required!!!
     * **NOTE**: Do not do this precomputation for **'Passive users'**

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-3cc8ecf93d04c7eed59db1977f07cdd99f2b799f%2FScreenshot%202021-08-28%20at%2012.42.25%20PM.png?alt=media)13\\. \*\*How to handle celebrity tweets?\*\*Copied!

* celebrity has MILLIONS of followers
*   **WORKING:**

    * **Celebrity side:**
      1. 1.celebrity makes a tweet
      2. 2.Store it in his Tweets table
      3. 3.Push it to his 'User Timeline'
      4. 4.**DO NOT FAN OUT**
    * **Fan Side:**
    * Every fan has a list of celebrities he follows
    * When the fan opens his 'Home Timeline':
      * Go to all the celebrities he follows & check their latet tweets
      * \=> All these operations are Redis operations => wont take much time
    * Store these latest celebrity tweets in a separate sorted list
    * Show these tweets along with users timeline tweets in his 'Home Timeline'
    * **NOTE**: Do not do this precomputation for **'Passive users'**

    ​

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-be73ead3a2015baf2a26521bc7cde9def2c716a9%2FScreenshot%202021-08-28%20at%2012.44.37%20PM.png?alt=media)

#### 4.\*\* Generate #Trends\*\* <a href="4.-generate-trends" id="4.-generate-trends"></a>

* How to see if a topic is trending?
  * It has more #tweets in short span
  * i.e. topic with 1000 tweets in 5 min is a #TredningTopic
  * But a topic with 10,000 tweets in 1 month is #NotATrendingTopic
  * Eg.: election result, movie, cricket store, oplymics/game
* **HOW TO GENERATE:**
  * Collect & Realtime process all tweets
    * Filter out redundant Hashtags (#Enjoy, #Life, #YOLO, #FOOD etc)
    * Policy violation
    * Copy-write violation
  * using \*\*Kafka+Spark \*\*
  * Store it in Trending Db(Redis)

#### 5. **Twitter Search Timeline | Indexing🚀🚀** <a href="5.-twitter-search-timeline-or-indexing" id="5.-twitter-search-timeline-or-indexing"></a>

* Twitter uses **EarlyBird**
  * \=> inverted full text indexing
* **HOW:**
  1. 1.Breakdown/stemming every tweet into **keywords**
  2. 2.Store all these keywords in a DISTRIBUTED BIG TABLE (mapped with their resp. tweetIDs)
  3. 3.**Map/Reduce** works here
* **Scaling:**
  * \*\*Sharding \*\*based on keyword / Location
  * **Caching**
  * \*\*Ranking \*\*by popularity

## 7. WhatsApp/FB Messenger <a href="7.-whatsapp-fb-messenger" id="7.-whatsapp-fb-messenger"></a>

* Whimsical [link](https://whimsical.com/whatsapp-PTxBKeAFpZyHk3WNT2kzpi)​
* Video: [link](https://www.youtube.com/watch?v=L7LtmfFYjc4\&ab\_channel=TechDummiesNarendraL)​

#### #1. Requirement Gathering ====================================== <a href="1.-requirement-gathering-2" id="1.-requirement-gathering-2"></a>

#### 1.1 Functional Requirements <a href="1.1-functional-requirements-1" id="1.1-functional-requirements-1"></a>

* one-to-one chat
* Send media
* keep track of the online/**last\_seen** statuses of its users
* support the persistent storage of chat history
* Group Chats
* Push Notifications : to offline users
* End-to-end Encryption

#### 1.2 NonFunctional Requirements - Usage Patterns(read heavy/CAP tradeoffs) <a href="1.2-nonfunctional-requirements-usage-patterns-read-heavy-cap-tradeoffs-1" id="1.2-nonfunctional-requirements-usage-patterns-read-heavy-cap-tradeoffs-1"></a>

* Real time exp with minimum latency
* Highly consistent: same chat history on all their devices
* Target high availability; but can be traded off for consistency

#### 1.3 Out of Scope <a href="1.3-out-of-scope-1" id="1.3-out-of-scope-1"></a>

* Voice call/video call

#### #2. Back-of-the-envelope estimation ============================ <a href="2.-back-of-the-envelope-estimation-2" id="2.-back-of-the-envelope-estimation-2"></a>

#### 2.1 Scale of System <a href="2.1-scale-of-system-1" id="2.1-scale-of-system-1"></a>

* DAU = 500M
* 1 user sends 40 msgs daily
* \==> 20B msgs per day

#### 2.2 Storage size estimation <a href="2.2-storage-size-estimation-1" id="2.2-storage-size-estimation-1"></a>

* size of 1 msg = 100bytes
  * \=> total size = 20B\*100 byte = 2TB/day
    * \=> 5PB for 5 years

#### 2.3 Bandwidth estimation(read+write) <a href="2.3-bandwidth-estimation-read+write-1" id="2.3-bandwidth-estimation-read+write-1"></a>

* incoming & outgoing data = 2TB/(24\*3600) = 25MB/s

#### #3. APIs ======================================================= <a href="3.-apis-2" id="3.-apis-2"></a>

* ​

#### #4. Models:Classes, DB Schema & ER diagrams===================== <a href="4.-models-classes-db-schema-and-er-diagrams-1" id="4.-models-classes-db-schema-and-er-diagrams-1"></a>

#### 4.1 Tables Schemas <a href="4.1-tables-schemas-1" id="4.1-tables-schemas-1"></a>

* Users
* Key value: u\_id -> processing\_msgs
* Key value: u\_id -> pending\_msgs
* key value: msgID -> mediaID

#### 4.2 DBs choices(NoSQL/SQL) <a href="4.2-dbs-choices-nosql-sql-1" id="4.2-dbs-choices-nosql-sql-1"></a>

* RDBMS or NoSQL wont scale this much
  * we cannot afford to\*\* read/write a row\*\* from the database **every time a user receives/sends** a message
* Instead use: **BigTable/HBase**

#### #5. Draw 'Basic HLD'============================================= <a href="5.-draw-basic-hld-2" id="5.-draw-basic-hld-2"></a>

#### #6. Detailed HLD ================================================ <a href="6.-detailed-hld-1" id="6.-detailed-hld-1"></a>

* Whatsapp is e.g. of \*\*Duplex Connection (\*\*implemented with **HTTP long polling❌)WebSocket✅**
  * i.e. connection can start from any client end
  * i.i.e chatting can be initiated from anyone to the other person
  * Other type of connections: **TCP, UDP, WebSocket✅**
* **How sending & receiving of msg takes place:**
  * A wants to send msg to B
  * **WHAT DOESNT WORK:**
    * \*\*Poll Model: \*\*Users can periodically ask the server if there are any new messages for them
      * \*\*issue: \*\*latency
      * \*\*issue: \*\*wastage of resources(when there's no message)
  * \*\*WHAT DOES WORK: \*\*
    * **Push Model**: Users can keep a connection open with the server and can depend upon the server to notify them whenever there are new messages.
  * **@A's end**
    1. 1.clientA sends a msg to clientB
    2. 2.this msg gets stored in phone's local db - **sqlite**
    3. 3.android app sends this msg from db to **App server**
  * **@B's end**
    * **if B is online(i.e. is connected to App server)**
      * App Server sends this msg to B
    * **elif B is offline(i.e. not connected to App server)**
      * App server stores this msg in DB
      * As soon as B is online next time; server sends the msg to B
* **How does Messaging Server work:**
  * It makes a \*\*Queue \*\*for all the msgs sent by users
  * It also has a \*\*table \*\*mapping pid to msgs\_lists
  * if B is online; it sends the msg directly
  * if B is offline: it keeps the msg in B's queue -> sends when B's up
  * if B is doesnt have a whatsapp acc: server dumps A's msg in a **separate DB**
* **How does Acknowledgement work? ✔️☑️| tick, double tick, blue tick**
  * **Single Tick**
    * is sent to clientA when server receives its msg
  * **Double Tick**
    * when server has found a connection to clientB(see **Duplex above**); it sends msg to clientB
    * clientB sends ack that it has received the msg
    * server sends ack to A that B has received the msg
  * **Blue Tick**
    * when B reads msg; it sends ack to server
    * server sends ack to A; that ur msg has been read
* **Last Seen**
  * Server keeps on sending \*\*heartbeats \*\*every 5 sec or so
  * and updates last seen value in the table
* **Sending Media**
  * A sends media to server
  * server uploads this media on a CDN
  * and returns the link to A
  * then server shares this link to B; so that it can access that media
* **End to end encryption**
  * A and B exchange their **public keys**
  * every msg sent from A is first encrypted using A's public key
  * upon receiving this msg; B decrypts it with its private key
* **Group chat(for small group <200):**
  * the message from User A is copied to each group member’s message sync queue: one for User B and the second for User C. You can think of the message sync queue as an inbox for a recipient.
  * This design choice is good for small group chat because:
    * it simplifies message sync flow as each client only needs to check its own inbox to get new messages.
    * when the group number is small, storing a copy in each recipient’s inbox is not too expensive.

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-f421fb184d3f0bd1d36ce193aafbfaa84b918495%2FScreenshot%202021-08-28%20at%203.39.18%20PM.png?alt=media)

## 8. \~Dropbox/Drive | @CoinBase <a href="8.-dropbox-drive-or-coinbase" id="8.-dropbox-drive-or-coinbase"></a>

* Whimsical: [link](https://whimsical.com/dropbox-Pxo3WmfgEvHq4MXhYeme84)​

#### #1. Requirement Gathering ====================================== <a href="1.-requirement-gathering-3" id="1.-requirement-gathering-3"></a>

#### 1.1 Functional Requirements <a href="1.1-functional-requirements-2" id="1.1-functional-requirements-2"></a>

* upload/download
* automatic synchronization between devices
* history of updates(versioning)
* should support offline editing

#### 1.2 NonFunctional Requirements - Usage Patterns(read heavy/CAP tradeoffs) <a href="1.2-nonfunctional-requirements-usage-patterns-read-heavy-cap-tradeoffs-2" id="1.2-nonfunctional-requirements-usage-patterns-read-heavy-cap-tradeoffs-2"></a>

* Cross device consistency: all the data should be in sync
* ACID-ity is required
* Read == Write

#### 1.3 Out of Scope <a href="1.3-out-of-scope-2" id="1.3-out-of-scope-2"></a>

* ​

#### #2. Back-of-the-envelope estimation ============================ <a href="2.-back-of-the-envelope-estimation-3" id="2.-back-of-the-envelope-estimation-3"></a>

#### 2.1 Scale of System <a href="2.1-scale-of-system-2" id="2.1-scale-of-system-2"></a>

* Total users = 500M
* DAU = 100M
* each user connects from 3 different devices
* 1 user has 200 files/photos
  * \=> Total files = 100B
* 10 requests per user per day
  * \=> 100M requests/day
* High write & read

#### 2.2 Storage size estimation <a href="2.2-storage-size-estimation-2" id="2.2-storage-size-estimation-2"></a>

* avg file size = 1MB
  * \=> total space reqd = 1MB\*100B = **100 PB**

#### 4.2 DBs choices(NoSQL/SQL) <a href="4.2-dbs-choices-nosql-sql-2" id="4.2-dbs-choices-nosql-sql-2"></a>

* **Metadata DB:**
  * has to be \*\*ACID \*\*(for conflict resolve)
  * \=> SQL

#### #5. Draw 'Basic HLD'============================================= <a href="5.-draw-basic-hld-3" id="5.-draw-basic-hld-3"></a>

#### #6. Detailed HLD ================================================ <a href="6.-detailed-hld-2" id="6.-detailed-hld-2"></a>

* **How versioning works?✅**
  * **OPTION#1**: keep a separate copy in cloud after every change.
    * \*\*Issue with this approach: \*\*in a 2GB file, even for a single char change; we'll have to keep a full 2GB file in cloud. => Huge wastage of resources
  * \*\*OPTION#2: \*\*break down the file into **1000 chunks** (2MB each)
    * On first upload: all \*\*1000 chunks \*\*& **1 metadata file** are uploaded to cloud
    * On subsequent changes; lets say only\*\* chunk#1 & chunk#10\*\*1 were change; so **only these 2 chunks** & **metadata file** gets uploaded in **version2.0**
    * \*\*Another adv: \*\*the upload script can work in \*\*parallel to upload \*\*each chunk individually.
* **Client:**
  * is configured to keep track of files inside the folder
  * Client Application monitors the workspace folder on the user’s machine and syncs all files/folders in it with the remote Cloud Storage
  * operations for the client:
    1. 1.Upload and download files.
    2. 2.Detect file changes in the workspace folder.
    3. 3.Handle conflict due to offline or concurrent updates.
  * Based on the above considerations, we can divide our client into following **four parts**:
  * **Watcher:**
    * gets **notified** when a **new file is added** to folder
    * Watcher passes this info (alog with the meta-data of changes) to **chunker & indexer**
  * **Chunker**
    * breaks down the new file into chunks
    * calculate **hash of each chunk**
    * uploads all the chunks to **Cloud(S3)**
    * **passes** this info to **indexer**:
      * **Url** it got after uploading to S3
      * **hash** of each chunk
  * **Indexer**
    * \*\*receives \*\*this info from **chunker:**
      * **Url** it got after uploading to S3
      * **hash** of each chunk
    * \*\*updates \*\*this info in \*\*internal DB \*\*against that file for which those **hash** belong to
    * \*\*indexer \*\*also passes this info to \*\*sync service \*\*via \*\*messaging queue \*\*for:
      * **conflict resolution(** updates could happen from multiple **Clients**, no?**)**
      * store metadata if device is **offline**
* **Sync Service:**
  * sends back the updated info of this file to all the **clients**
  * \*\*Indexer \*\*receives this info & updates corresponding files in the **folder**
  * \*\*=> this is how files remain in sync across all devices ✅ \*\*

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-b18548c4b85205f4210e4cb97a8ce324c4b448b6%2FScreenshot%202021-08-28%20at%207.17.52%20PM.png?alt=media)![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-7e213e7c59caa94a1182ab20c73f65032712e59c%2FScreenshot%202021-08-28%20at%207.17.59%20PM.png?alt=media)

## 9. Google Docs 🐽 <a href="9.-google-docs" id="9.-google-docs"></a>

* Video: [here](https://www.youtube.com/watch?v=2auwirNBvGg\&ab\_channel=TechDummiesNarendraL)​
* Part 2: [here](https://www.youtube.com/watch?v=U2lVmSlDJhg\&ab\_channel=TechDummiesNarendraL)​
  * this video's text in [this article](https://www.linkedin.com/pulse/system-design-google-docs-rahul-arram/)​

#### #6. Detailed HLD ================================================ <a href="6.-detailed-hld-3" id="6.-detailed-hld-3"></a>

* **Will Locking work?**
  * \*\*=> NO, \*\*as 100s of people use the doc at the same time
  * \=> We've to use a **lock-free design**
* **Optimistic Concurrency Control:**
  * using
    1. 1.Versioning
    2. 2.Conflict Resolution
* **Sync Strategies**
  1. 1.**Event Passing**
     * character-by-character sync
     * keep track of full file for each user & sync it
     * every change made by user: (CRUD, font change etc) has to be sent as \*\*an event \*\*to all the other people who are editing the doc
     * **==> Google doc uses this✅**
  2. 2.**Differential Sync**
     * similar to `git diff`
     * Just keep the diff's of users & keep sending it to all of them to maintain the sync
     * might be tedious if many people update the same file section
* **Operational Transformation**

## 10. Pastebin/gist <a href="10.-pastebin-gist" id="10.-pastebin-gist"></a>

* Code/file snipped sharing service
* whimsical [link](https://whimsical.com/pastebin-4xky1h5bhCG2S9YL7VEB7k)​

#### #1. Requirement Gathering ====================================== <a href="1.-requirement-gathering-4" id="1.-requirement-gathering-4"></a>

#### 1.1 Functional Requirements <a href="1.1-functional-requirements-3" id="1.1-functional-requirements-3"></a>

* paste (max file size allowed = 10MB)
* generate custom URL path for sharing
* snippets expiry (after 6 months/ customisable?)
* user login / Anonymous ; to see all his previous snippets

#### 1.2 NonFunctional Requirements - Usage Patterns(read heavy/CAP tradeoffs) <a href="1.2-nonfunctional-requirements-usage-patterns-read-heavy-cap-tradeoffs-3" id="1.2-nonfunctional-requirements-usage-patterns-read-heavy-cap-tradeoffs-3"></a>

* Durability
  * Once you write data; it will always be there
  * irrespective of:
    * High load
    * server crashes
    * DB full
    * DB down
* High availability
* Low latency
  * user should be able to access the gist from url, as fast as possible

#### 1.3 Out of Scope <a href="1.3-out-of-scope-3" id="1.3-out-of-scope-3"></a>

* Analytics
* API Support

#### #2. Back-of-the-envelope estimation ============================ <a href="2.-back-of-the-envelope-estimation-4" id="2.-back-of-the-envelope-estimation-4"></a>

#### 2.1 Scale of System <a href="2.1-scale-of-system-3" id="2.1-scale-of-system-3"></a>

* **100K** users **create** new snippets daily
  * \=> 100K/(24\*3600) = **150 writes/sec**
  * **=> 30% buffer ===> 200 reads/sec**
* read:write = 10:1 => **100K reads**
  * \*\*=> **reads =** 1500 reads/sec \*\*
  * **=> 30%Buffer ===> 2K reads/sec**

#### 2.2 Storage size estimation <a href="2.2-storage-size-estimation-3" id="2.2-storage-size-estimation-3"></a>

* \*\*worst\_case: \*\*max size of a snippet = 10MB
  * \=> 10MB\*100K = **1000GB/day (worst\_case)**
  * \*\*=> \*\*1000GB\*365 = **365 TB/year**
* **avg\_case:** avg. size of snippet = 100KB
  * \=> 100KB\*100K = **10 GB/day (avg\_case)**

#### #3. APIs ======================================================= <a href="3.-apis-3" id="3.-apis-3"></a>

* `addPaste(api_dev_key, paste_data, custom_url=None user_name=None, paste_name=None, expire_date=None)`
  * **Returns:** (string)
* `getPaste(api_dev_key, api_paste_key)`
  * Returns JSON blob
* `deletePaste(api_dev_key, api_paste_key)`

#### #4. Models:Classes, DB Schema & ER diagrams===================== <a href="4.-models-classes-db-schema-and-er-diagrams-2" id="4.-models-classes-db-schema-and-er-diagrams-2"></a>

#### 4.1 Tables Schemas <a href="4.1-tables-schemas-2" id="4.1-tables-schemas-2"></a>

* **User**
  * id
  * name
  * createdAt
  * metaData
* **Snippet**
  * id
  * content(10KB)
  * s3\_link
  * createdAt
  * expiresAt
  * userID

#### 4.2 DBs choices(NoSQL/SQL) <a href="4.2-dbs-choices-nosql-sql-3" id="4.2-dbs-choices-nosql-sql-3"></a>

* **Metadata DB**: SQL or NoSQL ( both are fine)
  * this has just the reference of snippet
* \*\*Blob/Object DB \*\*: For storing the actual snippets
  * **S3**
* **\[Hybrid Approach]For better UX:**
  * store small chunk (10KB) of snippet in \*\*Metadata DB \*\*as well;
  * so that user doesnt have to wait for async req of Blob pull

#### #5. Draw 'Basic HLD'============================================= <a href="5.-draw-basic-hld-4" id="5.-draw-basic-hld-4"></a>

#### #6. Detailed HLD ================================================ <a href="6.-detailed-hld-4" id="6.-detailed-hld-4"></a>

* Go **severless/lamda** for APIs!!!
* **Url creator :: Distributed Key Generation Service (DKGS)**
  * have a separate Service for this
  * This service has precomputed keys(stored in **redis)**; which we can fetch to generate unique url with **minimum SLA**
    * Another approach was; to get row\_id from metadataDB itself & use it in url=> but this will increase SLA
  * Similar technique(\*\*DKGS) \*\*is used by **twitter as well!!**
  * \*\*ADDED\_BONUS: sprinkle \*\*some \*\*salt \*\*of userID/fileName etc to make it uniquely hashed

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-938a303a639e216a3d3bb30ee35b1fccc1522873%2FScreenshot%202021-08-28%20at%208.50.24%20PM.png?alt=media)

## 11. Typeahead Suggestion <a href="11.-typeahead-suggestion" id="11.-typeahead-suggestion"></a>

\>>> Use **Trie**

* Whimsical [link](https://whimsical.com/typeahead-Rf18XgXGQ5bFU7wEgEGJds)​
* Video [link](https://www.youtube.com/watch?v=xrYTjaK5QVM\&t=1s\&ab\_channel=TechDummiesNarendraL)​

#### #1. Requirement Gathering ====================================== <a href="1.-requirement-gathering-5" id="1.-requirement-gathering-5"></a>

#### 1.1 Functional Requirements <a href="1.1-functional-requirements-4" id="1.1-functional-requirements-4"></a>

* Response Time (<100ms) => looks like real-time
* Relevance & context of predictions
* Sorted results
* Top **K** results

#### #2. Back-of-the-envelope estimation ============================ <a href="2.-back-of-the-envelope-estimation-5" id="2.-back-of-the-envelope-estimation-5"></a>

#### 2.1 Scale of System <a href="2.1-scale-of-system-4" id="2.1-scale-of-system-4"></a>

* Google gets **5B searches** every day:
* \*\*20% \*\*of these searches are **unique**(yes, there are lots of duplications)
* we want to index only \*\*top 50% words \*\*(we can get rid of a lot of less frequently searched queries)
  * \=> will have **100 million unique terms** for which we want to build an **index**

#### 2.2 Storage size estimation <a href="2.2-storage-size-estimation-4" id="2.2-storage-size-estimation-4"></a>

* query consists of\*\* 3 words\*\*
* average length of a word is **5 characters**
  * \=> this will give us
* we need 2 bytes to store a character
* total storage we will need = 100M \*(15\*2byte) => **3GB**

#### 2.3 Bandwidth estimation(read+write) <a href="2.3-bandwidth-estimation-read+write-2" id="2.3-bandwidth-estimation-read+write-2"></a>

* ​

#### #3. APIs ======================================================= <a href="3.-apis-4" id="3.-apis-4"></a>

* ​

#### #4. Models:Classes, DB Schema & ER diagrams===================== <a href="4.-models-classes-db-schema-and-er-diagrams-3" id="4.-models-classes-db-schema-and-er-diagrams-3"></a>

#### 4.1 Tables Schemas <a href="4.1-tables-schemas-3" id="4.1-tables-schemas-3"></a>

* User
* Trending Keywords
* Prefix hash table:
  * prefix
  * `top_k_suggestions`

#### 4.2 DBs choices(NoSQL/SQL) <a href="4.2-dbs-choices-nosql-sql-4" id="4.2-dbs-choices-nosql-sql-4"></a>

* ​

#### #5. Draw 'Basic HLD'============================================= <a href="5.-draw-basic-hld-5" id="5.-draw-basic-hld-5"></a>

#### #6. Detailed HLD ================================================ <a href="6.-detailed-hld-5" id="6.-detailed-hld-5"></a>

* **Relevance/Context:**
  * give rank to each word; based on
    * how many times user has searched
    * trending keywords
    * NLP based
  * \*\*Precompute \*\*this rank to all the words
* **Search Algo:**
  * Normal Trie implementation:
    * **Complexity: `O(L) + O(N) + O(klogk)`**
      * L : length of the prefix typed
      * N: total number of childnodes under prefix node
      * k: number of\*\* sorted predictions\*\* required by the system
  * **How to make the algo Faster?**
    * \*\*=> Precompute \*\*top K words for each node😎
      * \===> no traversal required
    * **Complexity Now**: **`O(L)`**

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-356cc34468eed0029da7141b17ed044b017da38f%2FScreenshot%202021-08-28%20at%209.27.31%20PM.png?alt=media)

* **How to store Trie in DB?**
  * **=> use prefix hash table**
* **How to update the Trie?**
  * Updating trie is extremely **resource intensive**
  * Do it **offline**, after certain interval, periodically
  * Employ **Map/Reduce** here

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-2f9cd57e1ed8ca8e150faf5fef0cbfa2cd5f6c30%2FScreenshot%202021-08-28%20at%209.37.18%20PM.png?alt=media)

## 12. API Rate Limiter <a href="12.-api-rate-limiter" id="12.-api-rate-limiter"></a>

* \*\*Video: \*\*[link](https://www.youtube.com/watch?v=mhUQe4BKZXs\&ab\_channel=TechDummiesNarendraL)​
* **Use Cases:**
  * Security: prevent DDoS attacks
  * Freemium model(e.g. ML APIs)
* **Type of Rate limiting:**
  * number of request allowed per user per hour/day
  * Concurrent(system wide): prevent DDoS attacks
  * location/IP based
* **Algorithms available to do Rate Limiting:**
  1. 1.**Token Bucket**
     * For every user; store his last API hit time & number of tokens left
     * **e.g: ProductHunt API**
     * `user_id -> {last_hit_time, tokens_left}`
     * store this in **key-val DB (Redis)**
     * for each new request; update the values in DB
     * Deny request when tokens\_left = 0
  2. 2.**Leaky Bucket**
     * maintain a **fixed-size-queue**
     * All the incoming req(from all users) are processed via this queue(in \*\*FIFO \*\*order)
     * when the queue size is full; deny the incoming requests
  3. 3.**Fixed Window Counter**
     * only **N** requests can be processed in a time \*\*T \*\*
     * so for every window of **`|t .... t+T| `**; count the incoming reqs;
       * when the **counter reached N**; deny the further reqs in this **time duration**
* **Issues in Distributed API Rate limiter**
  1. 1.**Global Inconsistency : Race condition**
     * if every node of the distributed system has its own LB & count-keeper DB;
     * \=> user can hit multiple LBs(situated in diff regions) & bypass the **global-counter check**
     * **How to solve it?**
     * **#1.**=> use **Sticky sessions**
       * i.e. always redirect User1 to Node1
       * **Still issues:**
         * this approach can increase load on certain LBs(while other LBs are free)
     * \*\*#2: \*\*=> use **Locking**
       * \=> Put a lock on user1 key in central DB, each time its updated
       * So that no 2 simultaneous requests can update the **req\_count for the same user**
       * **Its better than Sticky sessions:**
         * as now we can hit all LBs equally
       * **The Bad:**
         * it increases overall response time of the API
     * **Other solutions:**
       * add some buffer to \*\*rate limit \*\*(allow +5%)
         * **The Bad:** defeats the purpose of keeping rate limit
       * keep syncing data b/w nodes
         * \*\*The BAD: \*\*increases latency

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-cb4b1fdac8bb00523771aad53ff87b727d22836a%2FScreenshot%202021-08-28%20at%2011.10.46%20PM.png?alt=media)

## 13. Search Engine | Indexing | Elastic Search <a href="13.-search-engine-or-indexing-or-elastic-search" id="13.-search-engine-or-indexing-or-elastic-search"></a>

* 3 Steps of A Search Engine:

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-7c35d0cce37ff874ed7b7b041b19d1cd59ca5bee%2FScreenshot%202021-08-29%20at%2012.04.51%20AM.png?alt=media)![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-27b8404926d51390e925ea2d45d298a92272d437%2FScreenshot%202021-08-29%20at%2012.05.58%20AM.png?alt=media)**1. Crawling:**

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

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-352979cd217e90db5a8dadad5f876e75757f9af5%2FScreenshot%202021-08-29%20at%2012.09.36%20AM.png?alt=media)**3. Querying/Searching**

* Sanitize, filter, stemm, lemmatize the search query to get **query\_keywords**
* **e.g.: Keyword targeting @flipkart 😎**
* **Approaches:**
  1. 1.**Conjunctive Querying -> AND**
     * Performs\*\* AND operation\*\* on all the\*\* `words in query_keywords` \*\*
     * returns only those docs which have all the keywords present in them
  2. 2.\*\*Disjunctive Querying -> UNION \*\*
     * Takes all the document which have **ANY of the keyword present**
     * then performs **UNION** on these docs
     * Then removes **duplicates** from the result
  3. 3.**Conjunctive with Positioning**
     * The order of words in query is also imp!!!
       * E.g: if query is `men in black`
       * And if you dont consider the order of words; you'll also return results for `black in men`😂
     * HOW does it work?
       1. 1.get results of normal **Conjunctive Querying**
       2. 2.filter only those results which have **relative ordering** in place
          * E.g.
            * QUERY: men-0, in-1, black-2
            * Valid results: men-12, in-100, black-150✅
            * Invalid results: men-100, in-20, black-5❌

## 14. Uber <a href="14.-uber" id="14.-uber"></a>

*   **Location DBs**

    * \*\*\*\*[GauravSen](https://www.youtube.com/watch?v=OcUKFIjhKu0\&ab\_channel=GauravSen)​
    * zip codes aren't practical
    * \*\*Fractals: \*\*divide the space into smaller spaces:
      * Store as **B-Tree**

    ​

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-74c705e91b376b8b32f1e4b99e010bb3e3271022%2FScreenshot%202021-08-29%20at%2012.45.36%20AM.png?alt=media)![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-f301d01d5ecec5311f9fbf511dfbc55a304c4a49%2FScreenshot%202021-08-28%20at%2011.43.23%20PM.png?alt=media)![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-429e472fecfb4e1218355572867af8adcd4130fb%2FScreenshot%202021-08-28%20at%2011.42.25%20PM.png?alt=media)

## 15. OTP Generation <a href="15.-otp-generation" id="15.-otp-generation"></a>

* See\*\* #TinyUrl\*\*

## 16. Distributed Locks <a href="16.-distributed-locks" id="16.-distributed-locks"></a>

* ​[Video](https://www.youtube.com/watch?v=v7x75aN9liM\&ab\_channel=TechDummiesNarendraL)​
* See \*\*#GoogleDoc \*\*& **#APIRateLimiter**
* Use\*\* LockManager\*\*

## 17. Yelp | TripAdvisor | find Nearest Friend <a href="17.-yelp-or-tripadvisor-or-find-nearest-friend" id="17.-yelp-or-tripadvisor-or-find-nearest-friend"></a>

* **Location DBs**
  * See #**Uber**

## 18. Distributed Logger <a href="18.-distributed-logger" id="18.-distributed-logger"></a>

#### System Requirements <a href="system-requirements" id="system-requirements"></a>

* High availability
* High consistency: no conflict
* Minimum data loss
* Low latency
* Minimum operation overhead

#### 1.Approach#1 : Log Consolidation <a href="1.approach-1-log-consolidation" id="1.approach-1-log-consolidation"></a>

* \*\*How does it work? \*\*
  * In each of the distributed server we, install an agent which will monitor any logs that are written on this server
  * The App writes logs to the defined destination(e.g. logs to console)
  * Then the agent in background picks it and sends it to **centralize server(eg. `splunk`, `logstash`)**

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-893dbb8db89e9ee2292997f47c9786d8a63f97d6%2FScreenshot%202021-08-29%20at%208.21.21%20PM.png?alt=media)Approach#1. Log Consolidatgion

#### 2.Approach#2: Log Streaming <a href="2.approach-2-log-streaming" id="2.approach-2-log-streaming"></a>

* **How does it work?**
  * All the servers push their logs in Kafka queue
  * Kafka sends these logs to multiple subscribers
  * These subscribers process these logs & write them on a centrailzed place/run analytics
  * \*\*used@Pinterest \*\*(below pic from **Pinterest's** conference)

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-d31887818d7651426accc7df72713e9e783c7652%2FScreenshot%202021-08-29%20at%208.21.43%20PM.png?alt=media)Approach#2. Log Streaming

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

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-b9cc67d53aacb44af8d6ef3ba31a2bfc79a18304%2FScreenshot%202021-08-29%20at%209.03.49%20PM.png?alt=media)Approach#2. Log Streaming @Pinterest

#### #ISSUE with these approaches: `Correlation ID` <a href="issue-with-these-approaches-correlation-id" id="issue-with-these-approaches-correlation-id"></a>

* service A runs in server1, it calls service B that runs in server 2 and then another service C that runs in server 3. **How to correlate all the 3 logs for 1 single workflow?**
* **How to fix this?**
  * \=> attach a unique ID(`request_id`or `context_id` ) at **API gateway level** with this request
  * Now this ID will remain same for this log across microservices. Bazinga!

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-554f0b57ffc362e6c353e84092cee87e6453f35e%2FScreenshot%202021-08-29%20at%208.24.50%20PM.png?alt=media)

## 19. Slack @coinbase <a href="19.-slack-coinbase" id="19.-slack-coinbase"></a>

* ​[Whimsical](https://whimsical.com/slack-NTe7cDhHvX3AWfF7k9quyw)​

#### #1. Requirement Gathering ====================================== <a href="1.-requirement-gathering-6" id="1.-requirement-gathering-6"></a>

#### 1.1 Functional Requirements <a href="1.1-functional-requirements-5" id="1.1-functional-requirements-5"></a>

* Use should be able to send & receive chat messages from his/her contacts who are also on slack
* Group chat (upto 250 members) ??
* Track messages status: sent/delivered/read ??
  * \=> Slack shows notification if msg was unable to send
* Account registration using mail/phone
* Push Notifications: when the user is offline- send notifications for new msgs
* When the use comes online; he should be able to see all new msgs
* Adding support for media files(img.video.audio)
* E2E encryption

#### 1.2 NonFunctional Requirements - Usage Patterns(read heavy/CAP tradeoffs) <a href="1.2-nonfunctional-requirements-usage-patterns-read-heavy-cap-tradeoffs-4" id="1.2-nonfunctional-requirements-usage-patterns-read-heavy-cap-tradeoffs-4"></a>

* High availability
* Fault Tolerant
* Consistency
* Scalable
* Minimum latency (real-time chat experience)
* Durability(keep chat history)

#### 1.3 Out of Scope <a href="1.3-out-of-scope-4" id="1.3-out-of-scope-4"></a>

* Suppor for Slack-web ?
* Analytics/Monitoring

#### #2. Back-of-the-envelope estimation ============================ <a href="2.-back-of-the-envelope-estimation-6" id="2.-back-of-the-envelope-estimation-6"></a>

#### 2.1 Scale of System <a href="2.1-scale-of-system-5" id="2.1-scale-of-system-5"></a>

* DAU = 500M
* 1 user sends 100 msgs daily
* \==> 50B msgs per day

#### 2.2 Storage size estimation <a href="2.2-storage-size-estimation-5" id="2.2-storage-size-estimation-5"></a>

* size of 1 msg = 100bytes
  * \=> total size = 20B\*100 byte = 2TB/day
    * \=> 5PB for 5 years

#### 2.3 Bandwidth estimation(read+write) <a href="2.3-bandwidth-estimation-read+write-3" id="2.3-bandwidth-estimation-read+write-3"></a>

* incoming & outgoing data = 2TB/(24\*3600) = 25MB/s

#### #3. APIs ======================================================= <a href="3.-apis-5" id="3.-apis-5"></a>

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
* ​
  * `createGrop(API_key, group_id, group_name, `**`admin, [members]`**`)`
  * `addUserToGroup(API_Key, group_id, user_id,admin_id)`
  * `removeUserFromGroup(API_Key, group_id, user_id,admin_id)`
  * `promoteMemberToGroup(API_key,group_id,user_id)`

#### #4. Models:Classes, DB Schema & ER diagrams===================== <a href="4.-models-classes-db-schema-and-er-diagrams-4" id="4.-models-classes-db-schema-and-er-diagrams-4"></a>

#### 4.1 Tables Schemas <a href="4.1-tables-schemas-4" id="4.1-tables-schemas-4"></a>

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

#### 4.2 DBs choices(NoSQL/SQL) <a href="4.2-dbs-choices-nosql-sql-5" id="4.2-dbs-choices-nosql-sql-5"></a>

* **How to shard GroupMembership table**
  * \*\*Option#1: \*\*Shard by groupID => Called **Local Index**
    * \=> then membership info will be spread across all the shards to which user belongs
  * \*\*Option#2: \*\*Shard by userID(**SK**)=> Called **Global Index**
    * \=> group info will be spread
  * **WHich one to choose:**
    * it seems to me that **creating groups and updating their membership is potentially less frequent** than the ongoing msgs posted into the group chats by users.
    * So the Session and Fanout service benefits **more from a global index on userID**.
    * Users who create/update a group will necessarily have to wait for scatter/gather across partitions but this is less frequent than the msg posts occurring within the group chats.

#### #5. Draw 'Basic HLD'============================================= <a href="5.-draw-basic-hld-6" id="5.-draw-basic-hld-6"></a>

### #WebSockets <a href="websockets" id="websockets"></a>

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

#### 1. Gateway Service <a href="1.-gateway-service" id="1.-gateway-service"></a>

* Responsible for creating \*\*websocket connection \*\*b/w app server & user
* Makes all the API calls to other services as per the user's request

#### 2. Sessions Service <a href="2.-sessions-service" id="2.-sessions-service"></a>

* stores info: which client is connected to which server
* When clientA sends a msg to clientB:
  * clientA sends msg to geteway\_service
  * gateway\_service is pretty dumb(doesnt have inofo on usr's session)
  * gateway\_service passes this req to sessionService
  * session services returns with the details of clientB
  * then gateway service sends that msg to client B
* **+--> Enters WebSockets**

#### 3. UserActivity Service <a href="3.-useractivity-service" id="3.-useractivity-service"></a>

* takes care of last seen/typing....
* polling/webSockets

#### 4. Group Service <a href="4.-group-service" id="4.-group-service"></a>

* How does group msging work?
* Fanout sevies asks group srervice for all group data
* then it fans out msgs to all the members
* **DO: batch\_processing /limit the number of users**

#### **5. Someone's typing...** <a href="5.-someones-typing..." id="5.-someones-typing..."></a>

* typing indicator was triggered on the first keystroke and repeated as more keystrokes occurred.
* If no keystrokes were registered after 10 seconds, the indicator would no longer be displayed. Either you were typing, or you weren’t.
* **If a user stops typing for five seconds, Slack removes the “person is typing” indicator.**
* So when user starts typing update your database and set isTyping true.
* Dont forget to check if isTyping set to true so it will not update every time user presses the key
* \*\*EVENT is \*\*Implement using a \*\*pub/sub \*\*trigger1{2"isTyping":true,3"fromDeviceToken": "xxxx",4"timestamp": 123455}Copied!
* \*\*ISSUE: \*\*If user A **connection is lost during typin**g then the status will be always remain true until he resumes the connection. To solve this problem you can have one DateTime field in your firebase object

#### #6. Detailed HLD ================================================ <a href="6.-detailed-hld-6" id="6.-detailed-hld-6"></a>

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-d8d4ba86cb33bbd4a8e74f252859d320b7ad857f%2FScreenshot%202021-09-01%20at%207.24.13%20PM.png?alt=media)![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-23be127aa6801698de7f8df4bdaec9c4f907f5b7%2FScreenshot%202021-09-01%20at%205.10.18%20PM.png?alt=media)

## 20. Stocks Exchange <a href="20.-stocks-exchange" id="20.-stocks-exchange"></a>

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-1c7baa54f5728eb03ad5eb2a1c836e3149ecb8f7%2FScreenshot%202021-09-01%20at%205.57.17%20PM.png?alt=media)![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-a2d4c2512b699b3bd9a2bc7d29d599900b5ed856%2FScreenshot%202021-09-01%20at%206.10.25%20PM.png?alt=media)![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-c7b74e756aff6b2d9679fa565bf1251284399ff4%2FScreenshot%202021-09-01%20at%206.05.36%20PM.png?alt=media)![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-d8c59b3b5efbffc52e71b56302d9c9ad98d2880d%2FScreenshot%202021-08-31%20at%207.00.38%20PM.png?alt=media)

## 21. Flash Sale/Vaccination Drive/Cowin <a href="21.-flash-sale-vaccination-drive-cowin" id="21.-flash-sale-vaccination-drive-cowin"></a>

#### Src: [amazing Shopify Video](https://www.youtube.com/watch?v=-I4tIudkArY\&ab\_channel=ShopifyEngineering)​ <a href="src-amazing-shopify-video" id="src-amazing-shopify-video"></a>

#### 1.1 What is the system? <a href="1.1-what-is-the-system" id="1.1-what-is-the-system"></a>

* **Limited availability system:** both in terms of
  1. 1.**quantity**: Number of ordering request is much larger than inventory size. (1 million users competing for 10,000 items/slots)
  2. 2.\*\*time: \*\*Large number of users come to the system at the same time, causing a spike in traffic. (sales starts at 6am and finishs at 6:30am)
* System is checkout-driven; ==> so its \*\*write-heavy \*\*
  * so we **cant** simply just push a **Cache** in front of everything & call it a day
* social-media bashing when/if you fail => **Reputation**

#### 1.2 What are the challenges we're dealing with? <a href="1.2-what-are-the-challenges-were-dealing-with" id="1.2-what-are-the-challenges-were-dealing-with"></a>

1. 1.**Handle load on read**. Users will constantly **refresh** the page\*\* to check available inventory\*\*. It’s also likely that all users will **request for other similar resource at the same time**, such as account, item description, etc.
2. 2.**Provide high throughput**. There will be many **concurrent read and write** to the limited inventory records, so the **database lock** may result in timeout for some of the requests.
3. 3.**Avoid** inventory from being **oversold or undersold.** how to handle the available inventory number?
   * An item may be oversold if multiple requests reserved the same inventory. A
   * n item may be undersold if the inventory is hold but the process failed and inventory is not released.
   * This happened to some e-commerce website, and usually they will call the customers to **refund**.
4. 4.**Prevent cheating with script**. user could write a script to fire request in a **loop**. so this user may generate many repeated requests

#### #2. Back-of-the-envelope estimation ============================ <a href="2.-back-of-the-envelope-estimation-7" id="2.-back-of-the-envelope-estimation-7"></a>

#### 2.1 Scale of System <a href="2.1-scale-of-system-6" id="2.1-scale-of-system-6"></a>

* ​

#### #3. APIs ======================================================= <a href="3.-apis-6" id="3.-apis-6"></a>

* /catalogue/:item\_id
* /checkout

#### #5. Draw 'Basic HLD'============================================= <a href="5.-draw-basic-hld-7" id="5.-draw-basic-hld-7"></a>

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-7d7159e5d14cf46cbc07028a46db898b3951361d%2FScreenshot%202021-09-04%20at%2012.13.31%20PM.png?alt=media)![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-992bf82f6a5a68c21034022256e380a1963788b7%2FScreenshot%202021-09-04%20at%2012.13.39%20PM.png?alt=media)

### How to scale-up for FlashSales <a href="how-to-scale-up-for-flashsales" id="how-to-scale-up-for-flashsales"></a>

* \*\*@client side: \*\*
  * **@UI:** Disable submit button once clicked
  * **@server side**: dont allow mulitple reqs with same `item_id `& `user_id`
* \*\*@DB(sql): \*\*
  * have a `serialisable` \*\*isolation level \*\*for the transaction which affects performance.
    * If we do not apply this isolation level, we may end up with phantom read and thought that we still have enough inventory this request, and then we sell more than what we have.
    * To handle this, we can use a **counter with atomicity**. **Redis** will be a good choice for atomic decrement when a request need to be processed.
  * read replicas
  * sharding
* Use Application LB (such as **NGNIX)**, it can be used for:
  * Reverse Proxy
  * Edge LB
  * Request throttling
  * SSL
* **Back Pressure/ Leaky Bucket: ---> to improve UX**
  * Even if you've optimized every query; you cant server all the requests
  * Make the platform handle back-pressure: "Hey wait, I'm at full capacity. Come back later"
  * This\*\* Back Pressure\*\* can be implemented using **Leaky Bucket**.
  * **LOGIC:================================**
    * \*\*Algorithms to Rate Limit the reqs (\*\*taken from #12. API **)**
    *   **Token Bucket❌**

        * For every user; store his last API hit time & number of tokens left
        * **e.g: ProductHunt API**
        * `user_id -> {last_hit_time, tokens_left}`
        * store this in **key-val DB (Redis)**
        * for each new request; update the values in DB
        * Deny request when tokens\_left = 0
        * \*\*Con: \*\*not useful here, as every req is from a new user

        **2. Leaky Bucket ✅**

        * maintain a **fixed-size-queue**
        * All the incoming req(from all users) are processed via this queue(in \*\*FIFO \*\*order)
        * when the queue size is full; deny the incoming requests

        **3. Fixed Window Counter❌**
    * only **N** requests can be processed in a time \*\*T \*\*
    * so for every window of **`|t .... t+T| `**; count the incoming reqs;
      * when the **counter reached N**; deny the further reqs in this **time duration**
      * **Con:** bad UX & data loss
  * **HOW TO IMPLEMENT =============================================**
    * when you cant handle new checkout requests, serve a **Throttle page**, saying-"Hey, we got your checkout; we'll process it soon.Pleas be patient"
    * **STEPS**:
    * user sends a` /checkout` req to LB
    * LB is out of capacity; so it asks for a **throttle page** from server
    * LB caches this throttle page for future requests & serve it to the user
    * this Throttle page has **Javascript** & some sort of **refresh tags**; that constantly **polls the LB in background**-"hey, do you have capacity now?"
    * when the LB has capacity; it would pass the req to App server
    * And the LB places a **cookie** on **user session**, that "hey, dont throttle this req anymore"
    * So to user; it looks like there wasn't any throttle at all.
  * **CON:**
    * if a user comes at min=0; he has to wait for 30 mins
    * if a user comes at min=29; he might get lucky & have to wait just 1 min
    * So overall; it wouldn't improve the user-chaos
    * **How to solve:**
      * add the timestamp(of when user entered into queue) with the cookie
      * each LB will process these reqs in FIFO
      * but since there are multiple LB's; the system won't be fully stateless; but decent enough

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdIzueM27LMSBgVl5Fn%2Fuploads%2Fgit-blob-caaecf4f3296ecb12ccc6313930e0c9951b7fc60%2FScreenshot%202021-09-04%20at%2011.36.14%20AM.png?alt=media)

## #More From Leetcode <a href="more-from-leetcode" id="more-from-leetcode"></a>
