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

#### #1. Requirement Gathering ======================================

#### 1.1 Functional Requirements

*

#### 1.2 NonFunctional Requirements - Usage Patterns(read heavy/CAP tradeoffs)

*

#### 1.3 Out of Scope

*

#### #2. Back-of-the-envelope estimation ============================

#### 2.1 Scale of System

*

#### 2.2 Storage size estimation

*

#### 2.3 Bandwidth estimation(read+write)

*

#### #3. APIs =======================================================

*

#### #4. Models:Classes, DB Schema & ER diagrams=====================

#### 4.1 Tables Schemas

*

#### 4.2 DBs choices(NoSQL/SQL)

*

#### #5. Draw 'Basic HLD'=============================================

#### #6. Detailed HLD ================================================


















## 15. OTP Generation

* See\*\* #TinyUrl\*\*

## 16. Distributed Locks

* [Video](https://www.youtube.com/watch?v=v7x75aN9liM\&ab\_channel=TechDummiesNarendraL)
* See \*\*#GoogleDoc \*\*& **#APIRateLimiter**
* Use\*\* LockManager\*\*

## 17. Yelp | TripAdvisor | find Nearest Friend

* **Location DBs**
  * See #**Uber**





## 20. Stocks Exchange

![](../../.gitbook/assets/screenshot-2021-09-01-at-5.57.17-pm.png)

![](../../.gitbook/assets/screenshot-2021-09-01-at-6.10.25-pm.png)

![](../../.gitbook/assets/screenshot-2021-09-01-at-6.05.36-pm.png)

![](../../.gitbook/assets/screenshot-2021-08-31-at-7.00.38-pm.png)



## #More From Leetcode
