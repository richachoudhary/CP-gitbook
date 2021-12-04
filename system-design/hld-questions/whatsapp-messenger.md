# WhatsApp / Messenger

### Resources

* Whimsical [link](https://whimsical.com/whatsapp-PTxBKeAFpZyHk3WNT2kzpi)
* Video: [link](https://www.youtube.com/watch?v=L7LtmfFYjc4\&ab\_channel=TechDummiesNarendraL)
* thinksoftware: [link](https://www.youtube.com/watch?v=ovnrSH6G6vw\&ab\_channel=ThinkSoftware)

## &#x20;1. Requirement Gathering&#x20;

### 1.1 FRs

* user registration
  * using mobile number of fb account
* send & receive chat msgs in one-to-one chat
* group chat: 2-<mark style="color:yellow;">256</mark> members
* check message status ( tick/double tick/blue tick)
* Send Push Notifications : to offline users
* Receive msg when user comes online

### 1.3 Extended Requirements&#x20;

* Analytics/monitoring
* End-to-end Encryption
* Send media
* keep track of the online/**last\_seen** statuses of its users
* support the persistent storage of chat history

### 1.4 Out of Scope

* Voice call/video call
* Whatsapp web support

### 1.3 NFRs

* Real time exp with minimum latency
* Highly consistent: same chat history on all their devices
* Target high availability; but can be traded off for consistency
* Durability: keep last one month's msg in memory & move prev to backup

## 2. BOTEC

### 2.1 Scale of System

* DAU = 500M
* 1 user sends 50 msgs daily
* \==> 25B msgs per day

### 2.2 Storage size estimation

* size of 1 msg = 100bytes
  * \=> total size = 25B\*100 byte = 2.5TB/day
    * \=> 5PB for 5 years

### 2.3 Bandwidth estimation(read+write)

* incoming & outgoing data = 2.5TB/(24\*3600) = 30MB/s

## 3. APIs&#x20;

#### User APIs

* `register_account(api_key, user_info)`
* `validate_account(api_key, user_id, validation_code)`
  * `validation_code -> OTP`

#### Chat APIs

* **`initiate_direct_chat_session`**`(` `api_key, user_id, senders_id, handshake_info)  ->`` `**`session_id`**
* **`send_msg`**`(` `api_key, user_id, session_id, msg_body) ->`` `**`message_id`**
* **`read_new_msgs`**`(` `api_key, user_id, senders_id,`` `<mark style="color:orange;">`last_received_msg_id`</mark>`)`
  * <mark style="color:orange;">**`last_received_msg_id`**</mark>` ``` is used as a pointer to read all the unread msgs (which came after it)

#### GroupChat APIs

* **`initiate_group_chat_session`**`(` `api_key, group_info)   ->`` `**`group_id`**
  * creates a group with user being the admin
* **`add_user_to_group`**`(` `api_key, group_id, user_id)`   # only admins can execute
* **`remove_user_from_group`**`(api_key, group_id, user_id)` # only admins can execute
* **`promote_user_to_admin`**`(api_key, group_id, user_id)` # only admins can execute

## 4. Tables

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 2.22.00 AM.png>)

## 5. DB Choices: Hbase✅ | MySQL❌ | Mongo❌

* **Requirements from DB**
  * We need to have a database that <mark style="color:orange;">can support a</mark> <mark style="color:orange;"></mark><mark style="color:orange;">**very high rate of small updates**</mark> and also <mark style="color:orange;">**fetch a range of records quickly**</mark>**.**&#x20;
  * This is required because we have a huge number of small messages that need to be inserted in the database and, while querying, a <mark style="color:orange;">**user is mostly interested in sequentially accessing the messages**</mark>.
* <mark style="color:orange;">**WHY NOT SLQ & NoSQL (yep; both no):**</mark>
  * We cannot use RDBMS like MySQL or NoSQL like MongoDB <mark style="color:orange;">because we cannot afford to read/write a row from the database every time a user receives/sends a message</mark>.&#x20;
  * This will not only make the basic operations of our service run with <mark style="color:orange;">**high latency**</mark> but also create **a huge load** on databases.
* Go with Wide-Column DBs: <mark style="color:orange;">**HBase/BigTable**</mark>
  * Both of our requirements can be easily met with a wide-column database solution like [HBase](https://en.wikipedia.org/wiki/Apache\_HBase).&#x20;
* <mark style="color:yellow;">**ABOUT HBase:**</mark>&#x20;
  * HBase is a **column-oriented key-value NoSQL** database that can store multiple values against one key into multiple columns.&#x20;
  * HBase is modeled after Google’s [BigTable](https://en.wikipedia.org/wiki/Bigtable) and runs on top of Hadoop Distributed File System ([HDFS](https://en.wikipedia.org/wiki/Apache\_Hadoop)).&#x20;
  * HBase <mark style="color:orange;">groups data together</mark> to store new data in a memory buffer and, once the buffer is full, it dumps the data to the disk.&#x20;
  * This way of storage not only helps to **store a lot of small data quickly** but also **fetching rows by the key or scanning ranges of rows**.&#x20;
  * HBase is also an efficient database to **store variable sized data**, which is also required by our service.



## 6. HLD

### 6.1 Big Picture HLD ( lite lo iss design ko)

![](../../.gitbook/assets/screenshot-2021-08-28-at-3.39.18-pm.png)

### 6.2 Detailed HLD ([src](https://www.youtube.com/watch?v=ovnrSH6G6vw\&ab\_channel=ThinkSoftware)) 🟢

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 2.21.45 AM.png>)

## 7. Detailed Component Discussion

### 7.1 Routing Service ( similar to Uber) //copied

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 2.25.34 AM.png>)

### 7.2 User Service&#x20;

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 2.27.23 AM.png>)

### 7.3 User Registration Service

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 2.30.10 AM.png>)

### 7.4 Group Service

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 2.31.10 AM.png>)

### 7.5 Chat Session Service 🟢

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 2.31.41 AM.png>)

### 7.6 Fanout Service 🟢

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 2.32.18 AM.png>)

## 8. Other Discussions & Extended Features

### 8.1 Duplex Connection: <mark style="color:yellow;">Poll ❌ vs Push ✅</mark>

* Whatsapp is e.g. of <mark style="color:orange;">**Duplex Connection**</mark> ( implemented with **HTTP long polling❌)WebSocket✅**
  * i.e. connection can start from any client end
  * i.i.e chatting can be initiated from anyone to the other person
  * Other type of connections: **TCP, UDP, WebSocket✅**
* **How sending & receiving of msg takes place:**
  * A wants to send msg to B
  * **WHAT DOESNT WORK:**
    * <mark style="color:orange;">**❌ Poll Model:**</mark> Users can periodically ask the server if there are any new messages for them
      * **issue:** latency
      * **issue:** wastage of resources(when there's no message)
  * **WHAT DOES WORK:**&#x20;
    * <mark style="color:orange;">**✅ Push Model**</mark><mark style="color:orange;">:</mark> Users can keep a connection open with the server and can depend upon the server to notify them whenever there are new messages.
  * **@A's end**
    1. clientA sends a msg to clientB
    2. this msg gets stored in phone's local db - **sqlite**
    3. android app sends this msg from db to **App server**
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
* <mark style="color:orange;">****</mark>

### <mark style="color:orange;">**8.2 Tick, Double & Blue Tick:**</mark>** How does Acknowledgement work?**&#x20;

* **Single Tick**
  * is sent to clientA when server receives its msg
* **Double Tick**
  * when server has found a connection to clientB(see **Duplex above**); it sends msg to clientB
  * clientB sends ack that it has received the msg
  * server sends ack to A that B has received the msg
* **Blue Tick**
  * when B reads msg; it sends ack to server
  * server sends ack to A; that ur msg has been read

### <mark style="color:orange;">**8.3 Last Seen**</mark>

* Server keeps on sending <mark style="color:orange;">**heartbeats**</mark> every 5 sec or so
* and updates last seen value in the table

### <mark style="color:orange;">**8.4 Sending Media**</mark>

* A sends media to server
* server uploads this media on a CDN
* and returns the link to A
* then server shares this link to B; so that it can access that media

### <mark style="color:orange;">**8.5 End to end encryption**</mark>

* A and B exchange their **public keys**
* every msg sent from A is first encrypted using A's public key
* upon receiving this msg; B decrypts it with its private key

### <mark style="color:orange;">**8.6 Someone's typing...**</mark>

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
* **ISSUE:** If user A **connection is lost during typin**g then the status will be always remain true until he resumes the connection. To solve this problem you can have one DateTime field in your firebase object

### <mark style="color:orange;">**8.7 Group chat(for small group <200):**</mark>

* the message from User A is copied to each group member’s message sync queue: one for User B and the second for User C. You can think of the message sync queue as an inbox for a recipient.
* This design choice is good for small group chat because:
  * it simplifies message sync flow as each client only needs to check its own inbox to get new messages.
  * when the group number is small, storing a copy in each recipient’s inbox is not too expensive.

<mark style="color:orange;">****</mark>

##
