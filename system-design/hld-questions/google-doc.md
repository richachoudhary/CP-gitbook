# Google Doc

### Resources

* video [link](https://www.youtube.com/watch?v=2auwirNBvGg\&t=1709s\&ab\_channel=TechDummiesNarendraL)

### Concept

* collaborative editing
* <mark style="color:orange;">**Optimistic Concurrency Control:**</mark>
  * OCC assumes that multiple transactions can frequently complete without interfering with each other.&#x20;
  * While running, transactions use data resources without acquiring locks on those resources.
  * Before committing, each transaction verifies that no other transaction has modified the data it has read. If the check reveals conflicting modifications, the committing transaction rolls back and can be restarted

## 0. Approaches Discussion  <a href="1.-requirement-gathering" id="1.-requirement-gathering"></a>

### <mark style="color:yellow;">0.1 Concurrency Control Approaches</mark> <a href="1.-requirement-gathering" id="1.-requirement-gathering"></a>

#### 0.1.1 <mark style="color:orange;">Pessimistic</mark> (using Locks) ❌

* \=> Wont let multiple people work on the same doc at the same time
* hence its not an appropriate solution

#### 0.1.2 <mark style="color:orange;">Optimistic</mark> <mark style="color:yellow;"></mark> (using versioning) ✅

* Its a combination of 2 strategies:
  * <mark style="color:orange;">**Versioning**</mark>
  * <mark style="color:orange;">**Conflict Resolution**</mark>
* <mark style="color:yellow;">What's OPTIMISTIC about it?</mark>
  * \=> We assume that nothing can go wrong & give access to everyone at the same time- to edit the doc.

### <mark style="color:yellow;">0.2 Sync Strategies : Based on Optimistic Concur. Ctrl (OCC)</mark>

i.e. if >2 people are working on the same piece of doc; how should we keep their changes in sync

#### 0.2.1 Event Passing sync ( a.k.a. <mark style="color:orange;">Oper</mark><mark style="color:orange;">**ational Transformation (OT)**</mark>** **) ✅

* <mark style="color:orange;">**sending periodic updates**</mark> of user's changes & <mark style="color:orange;">**resolve the updates**</mark>
* event could be:
  * line-by-line change: insert/update/delete/undo
  * font/styling change
  * etc...
* <mark style="color:yellow;">=> Google doc currently uses</mark> <mark style="color:yellow;">**OT**</mark> <mark style="color:yellow;">method only!!!!</mark>
  * OT was originally implemented in (now deprecated) **Google Wave.**
  * Google doc is a spinoff of Google Wave project
* <mark style="color:yellow;">**CONS: **</mark>
  * OT is not stable/reliable in the face of conflists
  * Too many messages to handle on server side
* **Demo:**
  * 2 users are tying to edit "HA"
  * using OT logic; the final state should be same to both of them

![DEMO: 2 users are tying to edit "HA"](<../../.gitbook/assets/Screenshot 2021-11-02 at 1.22.13 PM.png>)

* OT in real life( more complicated)

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 1.22.30 PM.png>)

#### 0.2.2 Differential Sync ❌

* Similar to <mark style="color:orange;">`git diff`</mark>
* might be tedious if many people update the same file section❌
* <mark style="color:yellow;">**CONS: **</mark>
  * diffing is an expensive & (generally) unnecessary step
  * size of diffs maybe large

## 1. Requirement Gathering             <a href="1.-requirement-gathering" id="1.-requirement-gathering"></a>

### 1.1 FRs <a href="1.1-frs" id="1.1-frs"></a>

* Multiple People can update the same doc at the same time

### 1.2 Out of Scope <a href="1.3-out-of-scope" id="1.3-out-of-scope"></a>

*

### 1.3 NFRs <a href="1.2-nfrs" id="1.2-nfrs"></a>

* Highly available
* Expect high realtime consistency

## 7. HLD <a href="7.-hld" id="7.-hld"></a>

![](<../../.gitbook/assets/Screenshot 2021-11-02 at 1.29.24 PM.png>)
