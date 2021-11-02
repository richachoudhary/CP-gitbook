# Typeahead Suggestion

### Resources

* Whimsical [link](https://whimsical.com/typeahead-Rf18XgXGQ5bFU7wEgEGJds)
* Video [link](https://www.youtube.com/watch?v=xrYTjaK5QVM\&t=1s\&ab\_channel=TechDummiesNarendraL)

### Concept:

* Trie

## 1. Requirement Gathering&#x20;

### 1.1 FRs

* Response Time (<100ms) => looks like real-time
* Relevance & context of predictions
* Sorted results
* Top **K** results

## 2. BOTEC

### 2.1 Scale of System

* Google gets **5B searches** every day:
* \*\*20% \*\*of these searches are **unique**(yes, there are lots of duplications)
* we want to index only \*\*top 50% words \*\*(we can get rid of a lot of less frequently searched queries)
  * \=> will have **100 million unique terms** for which we want to build an **index**

### 2.2 Storage size estimation

* query consists of\*\* 3 words\*\*
* average length of a word is **5 characters**
  * \=> this will give us
* we need 2 bytes to store a character
* total storage we will need = 100M \*(15\*2byte) => **3GB**



## 3. Tables

* User
* Trending Keywords
* Prefix hash table:
  * prefix
  * `top_k_suggestions`

#### 4.2 DBs choices(NoSQL/SQL)

* Cassandra

####

## 4. HLD

![](../../.gitbook/assets/screenshot-2021-08-28-at-9.37.18-pm.png)

## 5. Detailed Discussion

### **5.1 Relevance/Context:**

* give rank to each word; based on
  * how many times user has searched
  * trending keywords
  * NLP based
* **Precompute**: this rank to all the words

### **5.2 Search Algo:**

* Normal Trie implementation:
  * **Complexity: `O(L) + O(N) + O(klogk)`**
    * L : length of the prefix typed
    * N: total number of child nodes under prefix node
    * k: number of  <mark style="color:orange;">sorted predictions</mark> required by the system
* **How to make the algo Faster?**
  * \=> <mark style="color:orange;">**Precompute**</mark> top K words for each node😎
    * \===> no traversal required
  * **Complexity Now**: **`O(L)`**

![](../../.gitbook/assets/screenshot-2021-08-28-at-9.27.31-pm.png)

* **How to store Trie in DB?**
  * **=> use prefix hash table**
* **How to update the Trie?**
  * Updating trie is extremely **resource intensive**
  * Do it **offline**, after certain interval, periodically
  * Employ **Map/Reduce** here
  * These MR jobs will calculate frequencies of all searched terms in the past hour. We can then update our trie with this new data. We can take the current snapshot of the trie and update it with all the new terms and their frequencies. We should do this offline as we don’t want our read queries to be blocked by update trie requests. We can have two options:
    1. We can make a copy of the trie on each server to update it offline. Once done we can switch to start using it and discard the old one.
    2. Another option is we can have a master-slave configuration for each trie server. We can update slave while the master is serving traffic. Once the update is complete, we can make the slave our new master. We can later update our old master, which can then start serving traffic, too.
* **How to store trie in a file so that we can rebuild our trie easily - this will be needed when a machine restarts?**&#x20;
  * We can take a snapshot of our trie periodically and store it in a file.&#x20;
  * This will enable us to rebuild a trie if the server goes down.&#x20;
  * To store, we can start with the root node and save the trie level-by-level. With each node, we can store what character it contains and how many children it has. Right after each node, we should put all of its children.
    * Eg.`A1, B2,C2, D3, E4, A4, ...`

