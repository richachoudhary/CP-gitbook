# Distributed Logger

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