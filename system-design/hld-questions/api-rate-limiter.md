# API Rate Limiter

### Resources

* Video: [link](https://www.youtube.com/watch?v=mhUQe4BKZXs\&ab\_channel=TechDummiesNarendraL)

### **Use Cases:**

* Security: prevent DDoS attacks
* Freemium model(e.g. ML APIs)

## **Type of Rate limiting:**

* number of request allowed per user per hour/day
* Concurrent(system wide): prevent DDoS attacks
* location/IP based

## **Algorithms available to do Rate Limiting:**

1. **Token Bucket**
   * For every user; store his last API hit time & number of tokens left
   * **e.g: ProductHunt API**
   * `user_id -> {last_hit_time, tokens_left}`
   * store this in **key-val DB (Redis)**
   * for each new request; update the values in DB
   * Deny request when tokens\_left = 0
2. **Leaky Bucket**
   * maintain a **fixed-size-queue**
   * All the incoming req(from all users) are processed via this queue(in \*\*FIFO \*\*order)
   * when the queue size is full; deny the incoming requests
3. **Fixed Window Counter**
   * only **N** requests can be processed in a time \*\*T \*\*
   * so for every window of **`|t .... t+T| `**; count the incoming reqs;
     * when the **counter reached N**; deny the further reqs in this **time duration**

* **Issues in Distributed API Rate limiter**
  1. **Global Inconsistency : Race condition**
     * if every node of the distributed system has its own LB & count-keeper DB;
     * \=> user can hit multiple LBs(situated in diff regions) & bypass the **global-counter check**
     * **How to solve it?**
     * **#1.**=> use **Sticky sessions**
       * i.e. always redirect User1 to Node1
       * **Still issues:**
         * this approach can increase load on certain LBs(while other LBs are free)
     * **#2:** => use **Locking**
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

![](../../.gitbook/assets/screenshot-2021-08-28-at-11.10.46-pm.png)

fa
