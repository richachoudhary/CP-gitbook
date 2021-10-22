# Google Calendar

### LLD features

* Create an event on the calendar - `event_type: [recurring , one_time]`
* Send the invite to people for the meeting.
* Look Up all the meetings on the calendar.
* Send the reminder before 30 mins of the meeting
* Cancel the meeting
* Modify the meeting
* Check availability of other member (Out of Scope)
* The main design challenge is handling re-occurring events.
  * When a user views the calendar, using the month's view, how can I display all the events for the given month?
  * \=> the row in the events table has an event\_type field that tells you what kind of event it is, since an event can be for a single date only, OR a re-occuring event every x days.
  * \=> Attempting to store each instance of every event seems like it would be really problematic and, well, impossible. If someone creates an event that occurs "every thursday, forever", you clearly cannot store all the future events
  * \=> You could try to generate the future events on demand, and populate the future events only when necessary to display them or to send notification about them

### HLD features

* Availability → High (99,999)\[ your system should not be down not more than 5 minutes]
* Consistency → Trade availability over consistency for this design.\[ When user can create meeting with 5 person so invite goes to all 5 people at same time and if it modifies then modify reflects all team mates]
* Latency → Low Latency of the system.\[Response should be minimum ]
*   Reliability →

    * Maintain data of all the users.
    * System should respond as expected.



## **2.Estimations (5-7 mins)**

* It has two part:&#x20;
  * 2.1.Capacity planning\[How many user]
  * 2.2.Query per second
*   Assume Data:

    * Assume that this system is designed for users: 100M&#x20;
    * Daily Active Users for creating meetings → 20M daily active.
    * On an avg. an active user will schedule 2 meetings in a day. → 20M
    * On an avg. a user will receive 4 meetings invites.  → 40M\
      \


    ### 2.1Capacity Planning

    * Users \[user details is to stored like name ,meeting time etc]
    * No. of users 100M, by end of year 200M
      * 1000Bytes → In an year:
      * Total = 200M \* 1000 B = 200 \* 10 ^ 9 = 200GB
    * Calendar Invites
      * Invites = 2 \* 20M \* 365
        * 200 Bytes&#x20;
          * Total = 40M \* 400 \* 200 Bytes = 32 \* 10 ^11 = 3200 GB
          * Total Space = 3200GB + 200 GB = 3.4 TB  = \~4 TB

### 2.2QPS Planning

* Read QPS
  * Check calendar, check availability
    * 40M(Invites received) \* 2 (times in a day) +  40M (Events created in a day) \* 3 (Check availability of 3 users)  = 200M
    * QPS = 2000&#x20;
*   Write QPS

    * Create, Cancel & modify
    * Create → 40M + 4M + 4M = \~50M
    * QPS = 50M / 86400 = 50 \* 10^6/ 10^5 = 500&#x20;

    ****

## **3.Detailed Design **

### **3.1 APIs**

* LoginAPI (UserName, Password)
* RegisterAPI (UserName, Password, UserInfo)
* CreateEvent( UserId, EventDetails, List\<UserId> Invitees)
* CheckCalendar(UserId)
* UpdateEvent (EventDetails, List\<UserId>, EventStatus)
  * Modify
  * Delete

### **3.2 Tables**

![basic tables](<../../.gitbook/assets/Screenshot 2021-10-22 at 12.13.13 PM.png>)

![table-relations](<../../.gitbook/assets/Screenshot 2021-10-22 at 12.14.19 PM.png>)

![Changes for TEAM CALENDAR](<../../.gitbook/assets/Screenshot 2021-10-22 at 12.14.46 PM.png>)

## 4. System Modeling



* \->First layer is security layer(Load balancer)
* \->Second layer is the frontend layer (web server) ,it is responsible for authorization and authentication and does not contain any business logic and take api and call particular services.
* \->then other layer <- (Load balancer)
* \->then different type service user service ,calendar service and notification service\[Back end layer]\[Business logic]
* \->then load balancer&#x20;
* \->then database

### 5. Scaling

* Horizontal  → Add more resources into your system
  * Complex as there are multiple machines performing the same operation.
* Vertical → Replace the current resource with the larger source
  * Might have  downtime



### 6. Sharding

* Range Based Sharding
  * Based on the start of the email Id A, B, C…. Z
    * AA – AP, AQ- AZ
  * Region Based
* Hash Based Sharding
  * Hash key for the UserId and a hash function
    * Consistent hashing

### 7.Replications\[Maintain consistency so prefer Master-slave ]

* Master-Slave configuration which writes at the same time on all the master-slaves.
  * Write to master and sync data with some slaves on real time
  * Read the data always from slaves.

### 8.Cache

* Not required.
* May try to cache the data for users who are invited in so many meetings. Famous Users.

### 9.Authentication and Authorization

* Login API → Pass Web tokens to the client
* And after login all the requests will contain web token and user id for which the request is sent.
* At the Frontend layer, you will authenticate the user with the web tokens passed and the userId passed as a part of the request.

###

### **10. Monitoring, Alerting and Backups\[System behave its expected]**

* Monitoring on the latency of each of the API
  * Helps to check if the APIs are not taking a long time to return the response.
* Monitoring on Success and Failure rate.
* Monitoring on resource consumption
* Users are creating events on a daily basis
* Cancelling or Updating events.
* Alerts → Latency is high
* Alerts → Failure to Success Ratio
* Alerts → Resources consumption
