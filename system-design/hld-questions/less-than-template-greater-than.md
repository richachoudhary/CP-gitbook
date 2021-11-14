# \<template>

### Resources <a href="resources" id="resources"></a>

* Whimsical board:
* ...

## 1. Requirement Gathering                -\[5-10 mins] <a href="1.-requirement-gathering" id="1.-requirement-gathering"></a>

### 1.1 FRs <a href="1.1-frs" id="1.1-frs"></a>

*

### 1.2 Out of Scope <a href="1.3-out-of-scope" id="1.3-out-of-scope"></a>

*

### 1.3 NFRs <a href="1.2-nfrs" id="1.2-nfrs"></a>

#### Availability:

* High Availability (for reads to work)
* Service is highly available
  * The acceptable latency of the system is 200ms for News Feed generation.

#### Consistency:

* High consistency (to avoid duplicate writes)
* Replication Consistency: eventual
* Consistency can take a hit:
  * if a user doesn’t see a tweet for a while, it should be fine.
  * i.e. Eventual Consistency

#### Durability:

* Fault tolerant
* The system should be highly reliable; any uploaded photo or video should never be lost.
* Durability : no tweet/follow should get deleted

#### Latency:

* Low latency for timeline generation
* Low latency is expected while viewing photos

#### Scaling:

* Scalable: system should scale with inc. in number of users

#### Bandwidth:

* Minimum bandwidth while file transfer

#### Storage:

* Users can upload as many photos as they want
  * \=> Storage management is crucial

#### Others:

* Ensure ACID-ity
* Shortened links should not be guessable (not predictable).
* System is read heavy
* Real time UX; no lag
* User traffic will be distributed unevenly throughout the day



## 2. BOTEC                                                           - \[5 mins] <a href="2.-botec" id="2.-botec"></a>

### 2.1 Scale of System <a href="2.1-scale-of-system" id="2.1-scale-of-system"></a>

*

### 2.2 Storage size estimation <a href="2.2-storage-size-estimation" id="2.2-storage-size-estimation"></a>

* try to bring numbers in Gb\*Million as <mark style="color:orange;">**1 TB = (1 GB \* 1 M)**</mark>

### 2.3 Bandwidth Estimate <a href="2.3-bandwidth-estimate" id="2.3-bandwidth-estimate"></a>

*

## 3. APIs                                                               - \[5 mins] <a href="3.-apis" id="3.-apis"></a>

* **​**

## 4. Tables                                                      - \[5-10 mins] <a href="4.-tables" id="4.-tables"></a>

*

## 5. DB Choice: SQL vs NoSQL <a href="5.-db-choice-sql-vs-nosql" id="5.-db-choice-sql-vs-nosql"></a>

### 5.1 DB Discussion <a href="5.1-db-discussion" id="5.1-db-discussion"></a>

#### <mark style="color:yellow;">**-> Discuss Pros & Cons of both: SQL & NoSQL**</mark> <a href="greater-than-discuss-pros-and-cons-of-both-sql-and-nosql" id="greater-than-discuss-pros-and-cons-of-both-sql-and-nosql"></a>

*
* \==> ✅ **Decision**: ..

​

### 5.2 Caching Discussion <a href="5.2-caching-discussion" id="5.2-caching-discussion"></a>

#### <mark style="color:yellow;">-> Discuss Global/Distributed Cache ✅ vs. Local Cache ❌</mark> <a href="31eb" id="31eb"></a>

## 6. Detailed Design Discussion <a href="6.-detailed-discussion-encoding-approaches" id="6.-detailed-discussion-encoding-approaches"></a>

*

## 7. HLD <a href="7.-hld" id="7.-hld"></a>

## 8. LLD: CODE (if any) <a href="8.-lld-code" id="8.-lld-code"></a>

​

## 9. Other Key Learnings <a href="9.-other-key-learnings" id="9.-other-key-learnings"></a>
