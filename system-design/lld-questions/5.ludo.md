# Ludo

## Requirements

### 1. Functional Requirements

1. Users can create a game and invite their friends to join his game with a unique code.
2. Users should be able to join a game with a unique code.
3. At most 4 years can only join a game.
4. Players can roll dice, move their coins, and valid actions against the results of dice.
5. Game could be paused/resume.&#x20;
   * If a player is disconnected for some reason, when connected again she should be able to resume the game

### 2. Non-Functional Requirements

1. Consistency: The data and state across the clients that are involved in a match, must be consistent because any inconsistent state or behavior is not ideal and create a lot of chaos.
2. Availability: The application must be reliable and must be available and must be fault-tolerant.
3. Throughput: The servers must accept 1M requests and must not make any request in the waiting state to perform.
4. Scalability: Oh boy! this particular game must be ready for special occasions, during festivals, weekends and during the nationwide lockdown, those are some peak moments, which can make developer life miserable when the system is not scalable

## Scale

* Online users = 1M
  * \=> 0.3 M matches at a time ( even 2 players can have a match, so #matchs >= 0.5M)
* QPS: Each match makes 3 req/sec
  * \=> 1M req/sec

## Class Diagrams

![](<../../.gitbook/assets/Screenshot 2021-10-22 at 12.22.30 PM.png>)

## HLD Diagram

![](<../../.gitbook/assets/Screenshot 2021-10-22 at 12.30.52 PM.png>)

### Discussion on Components

* using **WebSockets** to connect with APIs because it provides a full-duplex connection and reduces request/response noise and obviously **we need the system to be event-driven**.
* I have chosen microservice architecture because we don’t want to overload any one system with those many requests. We have something called Orchestrator, So for any request, the journey starts from there, I will explain in more detail below but each and every service has multiple instances and inter-process communication between the orchestrator and services will be using Producer-consumer mechanism using Apache Kafka.
* The reason to choose Kafka is, it is more reliable and works well with low latency, and provides a partitioning feature to include more throughput.
* We have something called UpdateService, where this service is responsible for getting data from clients and storing it in DB. This update service is responsible for injecting the changes that have been done on the client-side into the Database. For Example: killing a coin of the opponent at X place by A coin on match Id: 987xyz, moving a coin 4 places by B player on match Id: XYZ.
* The database is MongoDB because it is the only NoSQL DB that I have worked on and Traditional DB is not suitable obviously. I have used a mechanism called sharding because we partition the DB based on match Id because we don’t want all matches to be updating on a single DB and make DB calls more expensive, this sharding helps in a more reliable way to process more operations among them.
* I have used a term called CQRS, which means **Command and Query Responsibility Segregation. The concept** here is we are segregating read and write operations, In this particular case only UpdateService is capable of making any changes into the DB. and only FetchService has permissions only to read from DB. The reason to have this mechanism: we can have highly scalable and consider, in a game only one player changes its state and other three players read that particular action, So there could be a lot of loads if we use the same sharded DB for reading/writing, which is why we want to segregate this read and write.
* We have one more keyword called:** Change Data Capture**: is an architecture that converts changes in a source database into event streams. You can capture CDC events with the MongoDB Kafka sink connector and perform corresponding insert, update, and delete operations to a destination MongoDB cluster. this fetch service takes that data change and sends it back to the consumers and updates the state of the match.
* matchmaking service is something self Explanatory so as UsersService.





## Resources:

* Blog: [https://medium.com/@saikarthik952/ludo-game-systems-design-493cca866612](https://medium.com/@saikarthik952/ludo-game-systems-design-493cca866612)
