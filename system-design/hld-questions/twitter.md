# Twitter

### Resources

* Whimsical Board [link](https://whimsical.com/twitter-63T4oateDAL6ZdsaJ5LdHT)
* Video [link](https://www.youtube.com/watch?v=wYk0xPP\_P\_8\&ab\_channel=TechDummiesNarendraL)
* thinksoftware: [link](https://www.youtube.com/watch?v=1\_HIpTBUHAs\&ab\_channel=ThinkSoftware)

## 1. Requirement Gathering&#x20;

### **1.1 FRs**

* Post a tweet
* Delete a tweet
* <mark style="color:yellow;">**=>DISCUSS:**</mark>** **updating a tweet is not allowed
* max tweet size = 140 chars
* like a tweet
* follow a user
* See timelines. Type of timelines:&#x20;
  * **user timeline **(user's past tweets)
  * **home timeline **(whom user follows)
* **Search** tweets based on keywords
* Login/Signup to start tweeting
* a tweet can be:
  * text
  * photo <mark style="color:yellow;">=> dont support for now</mark>
  * video <mark style="color:yellow;">=> dont support for now</mark>
* **trends**
  * see all the tending topics/hastags

### 1.2 Out Of Scopes

* retweeting / replying on tweets
* tweet notification
* suggestion - whom to follow
* user tagging
* analytics
* See trends

### **1.2 NFRs**

* Highly available
* Low latency for timeline generation
* Consistency can take a hit:
  * if a user doesn’t see a tweet for a while, it should be fine.
  * i.e. Eventual Consistency
* Durability : no tweet/follow should get deleted
* User traffic will be distributed unevenly throughout the day

## 2. BOTEC

### **2.1 Scale of System**

* Daily Active Users(DAU) : 200M
* write: 2 tweets per user per day
  * \=> daily writes = 2\*200M = 400M/day
* read:write = 1000:1
  * \=> daily reads = 400B/day
  * system is read-heavy

### **2.2 Storage size estimation**

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

### **2.3 Bandwidth estimation**

* view tweets:
  * **text**:
    * \=> text: 28B\*280b = 7840GB/day = **90MB/sec**
  * user see all the **photos** of every tweet
    * \=> 28B/5\*200KB = 13GB/s
  * user plays 1 in every 3 **videos** of tweet
    * \=> (28B/10/3)\*2MB = 22GB/s
  * **=> total** = 35Gb/s

## 3. APIs&#x20;

#### 3.1 Tweet APIs

* **`post_tweet`**`(api_dev_key, tweet_data, tweet_location, user_location, media_ids)`
  * \=> returns tweet\_id&#x20;
* **`delete_tweet`**`(api_dev_key, tweet_id)`
* **`like_or_unlike_tweet`**`(api_dev_key, tweet_id, like_bool)`
* **`follow_user`**`(api_dev_key, user_id)`
  * `user_id `=> whom we want to follow( not self's duh)

#### 3.2 Timeline APIs

* **`get_user_timeline`**`(api_dev_key, page_token, page_size)`
* **`get_home_timeline`**`(api_dev_key, page_token, page_size)`

#### 3.3 Search API

* **`search`**`(api_dev_key, search_terms, maximum_results_to_return, sort, page_token)`
  * \=> JSON containing information about a list of tweets

## 4. Tables

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 4.51.34 AM.png>)

* **Relations:**
  * 1-Many in User ---- Tweet
  * 1-Many in User ---- Follower
* <mark style="color:yellow;">\[?] Retweets:</mark>
  * are to be considered a unique tweet & store in 'Tweet' table itself

## **5. DB choice**

* photos+vidoes => DFS
  * HDFS/S3
  * can be queued
* User, Tweet, Follower tables => NoSQL
  * Distributed NoSQL
  * \=> RDBMS, though good for relations here wont be scalable enough
* Relationship b/w tables: use key-value DB i.e. **Redis✅**
  * `<userID> -> [tweetIDs]`
  * `<userID> -> [followerIDs]`

####

## 6. HLD (microservice based architecture)

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 4.48.37 AM.png>)

## 7. Components Discussion:

### 7.1 Tweet Service

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 4.52.12 AM.png>)

### 7.2 Social Graph Service

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 4.53.04 AM.png>)

### 7.3 Fanout Service 🟢

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 4.54.09 AM.png>)

### 7.4 Search Service 🟢

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 4.54.23 AM.png>)

## 8. Detailed Discussions

1. **How User Timeline is generated?**
   * Go to Redis table#1 : \<userID> -> \[tweetIDs]
   * SCALING UP: **cache**
2. **How to generate Home Timeline**
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
       1. user makes a new tweet
       2. Store it in Tweets table
       3. Push this tweet into his 'User Timeline'
       4. Fan-out this tweet into 'Home Timeline' of ALL his followers
     * Hence; no DB query is required!!!
     * **NOTE**: Do not do this precomputation for **'Passive users'**

![](../../.gitbook/assets/screenshot-2021-08-28-at-12.42.25-pm.png)

3\. **How to Handle Celebrity Tweets?**

* celebrity has MILLIONS of followers
*   **WORKING:**

    * **Celebrity side:**
      1. celebrity makes a tweet
      2. Store it in his Tweets table
      3. Push it to his 'User Timeline'
      4. **DO NOT FAN OUT**
    * **Fan Side:**
      * Every fan has a list of celebrities he follows
      * When the fan opens his 'Home Timeline':
        * Go to all the celebrities he follows & check their latet tweets
        * \=> All these operations are Redis operations => wont take much time
    * Store these latest celebrity tweets in a separate sorted list
    * Show these tweets along with users timeline tweets in his 'Home Timeline'
    * **NOTE**: Do not do this precomputation for **'Passive users'**

    ***

![](../../.gitbook/assets/screenshot-2021-08-28-at-12.44.37-pm.png)

#### 4.Generate #Trends

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

#### 5. **Twitter Search Timeline | Indexing🚀🚀**

* Twitter uses **EarlyBird**
  * \=> inverted full text indexing
* **HOW:**
  1. Breakdown/stemming every tweet into **keywords**
  2. Store all these keywords in a DISTRIBUTED BIG TABLE (mapped with their resp. tweetIDs)
  3. **Map/Reduce** works here
* **Scaling:**
  * \*\*Sharding \*\*based on keyword / Location
  * **Caching**
  * \*\*Ranking \*\*by popularity
