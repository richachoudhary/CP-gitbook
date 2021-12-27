# LeaderShip Principles

## FK excalidraw: [link](https://excalidraw.com/#json=PeYdvIiZxxhXq6UDl6A2J,8yQsL62OYzx0vhJQ1jbs3g)

## S.T.A.R. Format

\======> Situation -> Task -> Action -> Result

## Things To Talk About:

****

### **👉@Flipkart:**<mark style="color:red;">**Sampling**</mark>

#### <mark style="color:green;">**1. SITUATION**</mark>

* With the increasing scale of traffic + features, compute & storage requirements are increasing,
* and getting machines for them has become difficult and&#x20;
* we are heading towards a dead-end, where our batch pipelines would not be able to meet any SLAs in the future.&#x20;
* For big sale events like BBD 2021 where scale will increase multiple folds, we are seeing huge risk in providing data to our consumers in any defined SLA

#### <mark style="color:green;">2. TASK</mark>

* Even though our team was trying various optimisations on the batch processing jobs
* I had read up couple of articles on Uber's blogs - The whole tech community is marching towards a direction to make insight available as soon as possible with certain guaranteed accuracy and sampling is the key there.
* along with various optimizations we have to look upon approaches that can **bring down our compute+storage requirements and still meet consumer expectations with a certain degree of accuracy**
* Current compute asks: 20 TB
* Available reserved Compute: 9 TB (Dependency on bursting: 50%)
* Expected BBD 2021 ask: 28 TB

#### <mark style="color:green;">3. ACTION</mark>

* The whole tech community is marching towards a direction to make insight available as soon as possible with certain guaranteed accuracy&#x20;
* In place of doing a process with 100% data, we should <mark style="color:yellow;">work on a random sample of whole data and project numbers with acceptable accuracy.</mark>&#x20;

#### <mark style="color:green;">4.RESULT</mark>

* Runtime Improvements (BBD@21):
  * Avg job <mark style="color:orange;">runtime reduced by</mark> <mark style="color:orange;"></mark><mark style="color:orange;">**60%**</mark> from 40 mins daily avg to 16 mins daily avg..
  * Avg of <mark style="color:orange;">Total Map tasks time of job</mark> is reduced by <mark style="color:orange;">68.9%</mark> from 106 mins to 33 mins.&#x20;
  * Avg of <mark style="color:orange;">Total Reduce tasks time</mark> of job is reduced by <mark style="color:orange;">80.7%</mark> from 117 mins to 22 mins.&#x20;
  * Because of less data to process due to sampling, the <mark style="color:orange;">number of reducers required in fact MR job</mark> has also been reduced by <mark style="color:orange;">half</mark> (350 to 175 now).

#### **NOTES:**

* **Problem statement**&#x20;
  * With the increasing scale of traffic + features, compute & storage requirements are increasing, and getting machines for them has become difficult and we are heading towards a dead-end, where our batch pipelines would not be able to meet any SLAs in the future.&#x20;
  * For big sale events like BBD 2021 where scale will increase multiple folds, we are seeing huge risk in providing data to our consumers in any defined SLA.&#x20;
  * To address along with various optimizations we have to look upon approaches that can **bring down our compute+storage requirements and still meet consumer expectations with a certain degree of accuracy.**&#x20;
  * Let's take the example of our Neo Merch/Common Pipeline:
    1. Current compute asks: 20 TB (M3 Data Capacity Ask 2021)
    2. Available reserved Compute: 9 TB 3. Dependency on bursting: 50%
    3. Expected BBD 2021 ask: 28 TB
    4. After Optimization BBD2021 ask would become: 22 TB
* **About Sampling:**
  * The whole tech community is marching towards a direction to make insight available as soon as possible with certain guaranteed accuracy and sampling is the key there.
  * In place of doing a process with 100% data, we should <mark style="color:yellow;">work on a random sample of whole data and project numbers with acceptable accuracy.</mark>&#x20;
  * This will reduce our capacity asks multiple folds for example of Neo Pipeline. If we consider 40% as the sample size of the universe then compute requirement will come down by 50%.
* <mark style="color:orange;">**Metrics (Complete Data)**</mark>: views, clicks, spent, ctr, non-clicks engagements.&#x20;
* <mark style="color:orange;">**Metrics (Sampled Data):**</mark> served impressions, wins, loaded impressions, win rate, serving efficiency, view rate.
* Sampling in all the input raw events will be done on <mark style="color:orange;">**requestID**</mark>.&#x20;
  * &#x20;<mark style="color:yellow;">Sampling bucket = hash(requestID) % No of buckets</mark>
* **IMPACT (@BBD21)**
  * Runtime Improvements&#x20;
    * Avg job <mark style="color:orange;">runtime reduced by</mark> <mark style="color:orange;"></mark><mark style="color:orange;">**60%**</mark> from 40 mins daily avg to 16 mins daily avg..
    * Avg of <mark style="color:orange;">Total Map tasks time of job</mark> is reduced by <mark style="color:orange;">68.9%</mark> from 106 mins to 33 mins.&#x20;
    * Avg of <mark style="color:orange;">Total Reduce tasks time</mark> of job is reduced by <mark style="color:orange;">80.7%</mark> from 117 mins to 22 mins.&#x20;
    * Because of less data to process due to sampling, the <mark style="color:orange;">number of reducers required in fact MR job</mark> has also been reduced by <mark style="color:orange;">half</mark> (350 to 175 now).

### **👉@Flipkart:Jarvis**

#### <mark style="color:green;">**1. SITUATION**</mark>

* .Being on oncall is a painful, especially if you're in data team
  * Becau of the batch nature of our data pipelines; usually a failure means cascading failures
  * Reasons for failure:
    * something wrong with deployment
    * issue in data from ingestion
    * resource crunches
* We have a cron like dashboard- Azkaban; which schedules batch jobs & we can see logs there.
  * Give that at any point we're bursting 50% of the jobs
* But the issue is for an oncall person; he has to keep on monitoring all the running jobs (8\*3 at a time)&#x20;
  * OR the attribution slice-n-dice dashboards to see if there's an issue or not.
  * OR keep on looking out for job failure emails

#### <mark style="color:green;">2. TASK</mark>

* When I joined FK; was overwhelmed by the humane effort required in job monitoring itself.
* Sought out that there's a scope for automation.
* Build some sort of live consolidated dashboards; which shows the status of current & past jobs

#### <mark style="color:green;">3. ACTION</mark>

* Approach: regex on job logs & vis-a-vis on Apache spark logs.
* Build one simple,plain HTML+JS-tabled page for single pipeline over the weekend & showed it to the team in the next tech-thursday.

#### <mark style="color:green;">4.RESULT</mark>

* The idea was initially met with skepticism; because of its sheer simplicity - but it worked perfectly.
* We ended up including all the pipelines in it & evolved into one consolidated dashboard-JARVIS
* Job failure detection time got reduced to failure time + 2 mins(at max).

### **👉**@Flipkart: **Keyword Targeted Advertisements**

****

#### <mark style="color:green;">**1. SITUATION**</mark>

* Flipkart Ads Dashboard came up with keyword based advertisements.
* e.g:&#x20;
  * Adidas has some sale going on "Male Sweatshirts"
  * FK allows it to only show its ad when someone types in relevant keywords; so that Adidas can maximize its chances of win

#### <mark style="color:green;">2. TASK</mark>

* Our data team has to build this mapping:
  * take a list of custom keywords provided by the advertizer
  * take up the user raw search query
    * preprocess it: remove punctuations, non-weighted words etc
    * Lemmatisation lib by DS team
  * Run our batch job on these queries to do this matching

#### <mark style="color:green;">3. ACTION</mark>

* .

#### <mark style="color:green;">4.RESULT</mark>

* .

### **👉**@Flipkart: Pricing Service Feedback + Ads Merch Separation

// missing deadline

#### <mark style="color:green;">**1. SITUATION**</mark>

* While placing a bid; show last week's min & max bid won prices to the advertizer.
* This was to be done only on 3rd party ads & not FK's self ads (merch)

#### <mark style="color:green;">2. TASK/3. ACTION</mark>

* Even though the task was fairley simple; I used this as an opportunity to separate out ads + merch pipelines
* separate DAGs, separate resources; separate business logic

#### <mark style="color:green;">4.RESULT</mark>

* even though it extneded the delivery date; we were able to solve a long back tech-log.
  * Achieved optimisation & reduced SLA

### @Flipkart::Others

* <mark style="color:red;">Keyword Targeting</mark>
* <mark style="color:red;">Bidding Price Recommendation System</mark>
* Ads Merch Separation
* Pricing Service Feedback
* <mark style="color:red;">Jarvis</mark>
* RCAs
* NFRs

### **👉**@Rzp: Mozart



#### <mark style="color:green;">**1. SITUATION**</mark>

* .

#### <mark style="color:green;">2. TASK</mark>

* .

#### <mark style="color:green;">3. ACTION</mark>

* .

#### <mark style="color:green;">4.RESULT</mark>

* .

### **👉**@Rzp: Capital->ES (Early Settlements)

* Currently, payments disbursed in t+3 days, we get it in t+2 days.&#x20;
* ES Delivers payments in less than t+3 days to merchants.

**Types:**&#x20;

* Instant&#x20;
* On-demand

**Problem statement:**&#x20;

* To Improve ux engineering implementation tracking of ES volumes in dashboard

**User stories:**&#x20;

* Instant ES customer&#x20;
* On-demand ES customer&#x20;
* Churning ES customer( <mark style="color:orange;">to find reasons why merchants in v1 of ES stopped using this service, and incorporate the solution for the same in the current version</mark>)

**Features:**&#x20;

* Revamp db in ES&#x20;
* Merchant should be able to select specific txns for ES.&#x20;
* Automate integration of ES in merchant dashboard.&#x20;
* Revised eligibility rules and pricing model

#### 2. LOS: (Loan Operating System)

&#x20;:platform to collect critical customer information and enabling the Loan Processing&#x20;

Aim:&#x20;

* good customer exp&#x20;
* minimise data collection&#x20;
* smooth 3rd party integration&#x20;
* maximise conversions&#x20;

Success criteria:&#x20;

* funnel conversion rate >5%&#x20;
* customer input fields <15&#x20;
* minimise total loaning time(<5 min)&#x20;

User Types:&#x20;

* **Micro:** Consumer Bureau+GST+bank statement&#x20;
* **Medium-large:** Commercial + Consumer Bureau + CIN details for an MCA + GST&#x20;

Features:&#x20;

* easy KYC&#x20;
* robust Bureau connection&#x20;
* cash flow analysis(perfios)&#x20;
* Score for risk&#x20;
* integration of docs(e-sign,stamp etc)+loan agreement

####

### **@Rzp::Others**

* Mozart: integration + test\_coverage
* Capital: instant loans, instant refunds, KYC integration
* OTP-elf

### **@Nestaway**

* Linguini

### **@BITS**

* DTN project
* Apriori project

### **@BARC**

* Office Management System
* Telephone Directory

****

\====================================================================

#### <mark style="color:yellow;">🤨 ->WHY DO YOU WANT TO LEAVE FLIPKART?</mark>

* \==>&#x20;
  * I am a <mark style="color:orange;">growth oriented person who is yet to find my niche</mark>. Continuing here would lock me in data-side which I feel is too early to settle.
  * I <mark style="color:orange;">love</mark> what I was working on and the <mark style="color:orange;">team I've grown with</mark>, the <mark style="color:orange;">work and the culture were great</mark>. You simply feel like it's time for you to grow different skills and learn from new people, you've heard great things about the <mark style="color:orange;">culture and challenges at X and couldn't be more excited to be part of the team</mark>.
  * (<mark style="color:orange;">team switch</mark> is easier said than allowed)
  * When recruiters ask you why you’re leaving you don’t have to state your reason but you can reply with what you’re looking for. For instance you can say I’m looking to work in a product company, or a company that involves X. In other words tell them what you’re looking for, never why you’re leaving. That way you don’t have to involve your current employer.

#### <mark style="color:yellow;">🤨 -> WHY DO YOU WANT TO JOIN UBER?</mark>

* \==>&#x20;
  * Uber has been my dream company since college days.
    * since first job; I've been regular reader/visitor of **uber engg blogs.**&#x20;
    * It has shaped me as an engineer
  * My mom uses it. (It saved my uncle's life @4am)&#x20;
  * So, when Uber's **recruiter reached out**; I could not have not applied here! & <mark style="color:orange;">couldn't be more excited to be part of the team</mark>.
  * (looking at the **stocks**; its the right time to get some of'em 😋)
  * Uber’s mission statement is “**Transportation as reliable as running water, everywhere for everyone**.”&#x20;

#### <mark style="color:yellow;">🤨 -> Tell me about a time when you challenged the status quo.</mark>

\==>&#x20;

* 1\. Implemented Jarvis platform for oncall
  * failure detection moved from 1 hours (usual run time) to live-dashboard( based on log parsing)





or helping out oncall's redundant tasks ==> 2. Sampling

#### <mark style="color:yellow;"></mark>

#### <mark style="color:yellow;"></mark>

#### <mark style="color:yellow;"></mark>

#### <mark style="color:yellow;">🤨 -> Time when you were 75% through a project and realized you had the wrong goal.\</mark></mark>

\==> ?

#### <mark style="color:yellow;">🤨 -> Time when you pushed back a decision from your management for better long term benefits.\</mark></mark>

\==> brand & category enrichment in BSS:

* new platform | first time occurence during the Independence Day Sale
* typecast mismatch from Java's List to Sark's Wrapped Array
  * WrappedArray wraps an Array to give it extra functionality. It also have a bunch of types while array extends only serializable and cloneable, This allows an array to be wrapped so it can be used in places where some generic collection type like Seq is required.
* CORRECTIVE MEASURES:
  * fixed the bug in one night(during sale oncall) collaborating with the ingestion team & serving team
  * (post fix)published Detailed RCA in tech-session withdebugging steps &
  * increased learning of spark & how spark's typecasting work
* Implemented the same type-safety in pipeline's code & added UTs for the same
* IMPACT:Even though we missed the SLA for the first night of sale(Early Access); we fixed the issue on time for the smoother sale

#### <mark style="color:yellow;">🤨 -> Tell me about a time you faced an obstacle and how you overcame it.</mark>

\==> ?

#### <mark style="color:yellow;">🤨 -> Tell me a time you took some on some risk</mark>

\==> ?

#### <mark style="color:yellow;">🤨 -> Have you ever gone out of your way to help a peer? (ownership)\</mark></mark>

\==> 1. yes, several nights up till 2 AM/weekends helping out new joinees/ oncall issues

#### <mark style="color:yellow;">🤨 -> Tell me about a time when you learned new technologies\</mark></mark>

\==> 1. Learning about big data tech upon entering Flipkart

#### <mark style="color:yellow;">🤨 -> Tell me about a time you had multiple solutions and you had to select an optimal one</mark>

\==> 1. Keyword Targeting algos

\==> 2. Sampling

\==> 3. Linguini

#### <mark style="color:yellow;">🤨 -> Tell me about a time when you innovated and exceeded the expectation</mark>

\==> 1. Sampling : 60% job run time

\==> 2. Keyword targeting

#### <mark style="color:yellow;">🤨 -> Handling a tight deadline\</mark></mark>

\==> Sampling

#### <mark style="color:yellow;">🤨 -> How would you help a new employee who is facing technical difficulties?</mark>

\==>

#### <mark style="color:yellow;">🤨 -> disagree and commit and ownership LPs.</mark>

#### <mark style="color:yellow;">🤨 -> Tell me about a time when you had conflicting ideas with your teammates and how did you resolve them</mark>

\==> 1. Linguini

\==> 2. KeywordTargeting: algo selection

#### <mark style="color:yellow;">🤨 -> Tell me about time when you faced a difficult challenge.\</mark></mark>

\==> 1. Sampling

\==>

#### <mark style="color:yellow;">🤨 -> Tell me about a time when you needed help from someone during a project.</mark>

\==> 1. Onboardings - everywhere

\==> 2. Bidding Price Recommendation System : from data-science team

#### <mark style="color:yellow;">🤨 -> Tell me about a time when you thought of an unpopular idea.</mark>

\==> 1. Keyword targeting: not using standard Edit Dist. but researched-> N-Gram

\==> 2. Mozart- test coverage => build Tree & BFS ==> 3. Linguini

#### <mark style="color:yellow;">🤨 -> Tell me about a time when you had to decide upon something without consulting your superior.</mark>

\===> 1. Ads Merch separation

* SITUATION/TASK:
  * (cant disclose much internal details)
  * our deployment was impacted due to a recent(same day) deployment; which was not writing Unserved's data to correct sql tables => hence impacting their reporting
  * By the time I figured this out, it was 2AM & the (senior) person who had done the other deployment was slept(had to catch a flight next day)
* ACTION:
  * I got access to that project's config (by awaking some other team member at 2:30 AM)
  * first thing; I stopped the flow to wrong tables => to avoid <mark style="color:orange;">**false positives**</mark> & dedups
  * Fixed the issue by morning, got PR approved @8AM
  * Triggered reruns for the lost buckets with the help of oncall person

#### <mark style="color:yellow;">🤨 -> Tell me about a time when you did not meet your deadlines for a project | Tell me about a time when you had to face tight time constraints during a project.</mark>

\==> 1. Never(maybe in college lol)

\==> 2. tight timeline for Sampling before BBD'21. but stretched over 3 weekends to go live on time

<mark style="color:yellow;">🤨 -></mark> <mark style="color:yellow;">**a project you're proud of**</mark>

\==> Sampling@Rzp | Capital@Rzp

#### <mark style="color:yellow;">🤨 -> a time when you faced a setback initially but still achieved the goal.</mark>\ <mark style="color:yellow;">a time when you had to cut corners to meet a deadline</mark>

\==> Pricing Service Feedback @FK

* SITUATION/TASK:
  * It was a 2-sprint project, was working with 1 (senior) teammate
  * Nearly at the end of 1st sprint, he had to leave immediately due to a medical emeregency at his home(2nd <mark style="color:orange;">COVID</mark> wave)
  * All the responsibility fell onto my shoulders, I was new to that pipeline as well
* ACTION:
  * first thing I did for next 2 days was collected all the info about his tasks (over phone calls, syncing with other team's resp. people)
  * I documented everything & shared it with all the stakeholders for cross-verification
    * thanks for him, that we were able to have a phone call in around every 2 days; for doubt clarification
* RESULT:
  * We completed the project on time
  * It even got me a letter of praise by the multiple-teams & a gift voucher

#### <mark style="color:yellow;">🤨 -> Tell me about a time where you had to make a decision based on limited information and how it impacted the outcome</mark>

<mark style="color:yellow;">**🤨 -> Tell me about a time when you felt under pressure that you wouldn't be able to get something done or had to take a pivot at the last minute**</mark>

\==> Linguini@Nestaway

* 6 months internship; got project in the last 1.5 months
* change of 3 mentors caused too much skeweness in POC (spent enough time with image processing, comparing GCP/AWS/Azure, pricing) \\
* last 3 weeks remaind; panicked as mentor@college was asking for pre-demo & ppt
* improvised & went ahead with speech-to-text + targetted-keywords matching

#### <mark style="color:yellow;">🤨 -> Time when your team members were not supporting something but you pushed and went for a more optimal solution.\</mark></mark>

#### <mark style="color:yellow;">🤨 -> Tell me about a situation where you had a conflict with someone on your team. What was it about? What did you do? How did they react? What was the outcome?</mark>

\==>

#### <mark style="color:yellow;">🤨 -> Give an example of when you saw a peer struggling and decided to step in and help. What was the situation and what actions did you take? What was the outcome?\\</mark>

\==>

#### <mark style="color:yellow;">🤨 -> Tell me about a time you committed a mistake?</mark>

\==>

#### <mark style="color:yellow;">🤨 -> Tell me about a time when your earned your teammate's trust?</mark>

\==>

#### <mark style="color:yellow;">🤨 -> Tell me about a time when you couldn't meet your deadline?</mark>

\==>

#### <mark style="color:yellow;">🤨 -> Tell me about a time when your teammate didn't agree with you? What did you do?</mark>

\==>

#### <mark style="color:yellow;">🤨 -> Tell me about a time when you invented something?</mark>

\==>

#### <mark style="color:yellow;">🤨 -> Tell me about a time when you took important decision without any data?</mark>

\==>

#### <mark style="color:yellow;">🤨 -> Tell me about a time when you helped one of your teammates?</mark>

\==>

#### <mark style="color:yellow;">🤨 -> Have you ever been in a situation where you had to make a choice among a few options, but did not have a lot of time to explore each option</mark>

\==>

#### <mark style="color:yellow;">🤨 -> Have you ever failed at something? What did you learn from it?</mark>

\==>

#### <mark style="color:yellow;">🤨 -> name time when you went out of your way to help someone?</mark>

\==>

#### <mark style="color:yellow;">🤨 -> Time when you came up with novel solution.\</mark></mark>

\==>

#### <mark style="color:yellow;">🤨 -> Received negative feedback from manager and how you responded.\</mark></mark>

\==>

#### <mark style="color:yellow;">🤨 -> Time when you went above and beyond your job responsibilities.\</mark></mark>

\==>

#### <mark style="color:yellow;">🤨 -> Time when you did not have enough data and had to use judgement to make decision.\</mark></mark>

\==>

#### <mark style="color:yellow;">🤨 -> Time when you helped someone in their work.\</mark></mark>

\==>

#### <mark style="color:yellow;">🤨 -> Time when you helped someone grow in career and it benefited them.\</mark></mark>

\==>

#### <mark style="color:yellow;">🤨 -> Time when you helped someone grow but did not benefit them.\</mark></mark>

\==>

\==================================================================

**1. Why do you want to quit your current job ?**

* The job is becoming more data-engineering intensive; as things are progressing in the ecosystem.But I dont want to switch the domain from Software Developer to completely DE. -> this was the key factor I decided to start looking out.
* and unable to switch teams due to internal policies.
* <mark style="color:green;">not learning anything new as product is in a saturated state,</mark>
* <mark style="color:green;">NEVER EVER talk about bad boss, politics etc - it will backfire bigtime.</mark>

**2.What has been the biggest failure of your career till now ? OR What is the most critical feedback received from your boss in your entire career ?**

* \*\*WHAT: \*\*brand & category enrichment in BSS
  * new platform | first time occurence during the Independence Day Sale
  * typecast mismatch from Java's **`List`** to Sark's **`Wrapped Array`**
    * `WrappedArray` wraps an `Array` to give it extra functionality. It also have a bunch of types while array extends only serializable and cloneable, This allows an array to be wrapped so it can be used in places where some generic collection type like `Seq` is required.
* **CORRECTIVE MEASURES:**
  * fixed the bug in one night(during sale oncall) collaborating with the ingestion team & serving team
  * (post fix)
  * published Detailed RCA in tech-session with
    * debugging steps &
    * increased learning of spark & how spark's typecasting work
  * Implemented the same type-safety in pipeline's code & added UTs for the same
* **IMPACT:**
  * Even though we missed the SLA for the first night of sale(Early Access); we fixed the issue on time for the smoother sale.

***

**3. What would you like to improve at your current workplace ? OR What do you dislike/hate at your current job/workplace ?**

* <mark style="color:green;">a trap - if you badmouth your current employer or use any words like</mark> <mark style="color:green;">**hate**</mark> <mark style="color:green;">or</mark> <mark style="color:green;">**dislike**</mark><mark style="color:green;">, it is guaranteed to go against you.</mark>
* Talk about generic things like -
  * sometimes code reviews take a long time due to senior developers being busy
    * probably that can be streamlined.
  * Or say - we should invest more in enhancing the\*\* test automation infrastructure\*\*, which often takes a backseat due to various constraints
  * (!) too many senior people leaving - has resulted in a knowledge bottleneck
* <mark style="color:green;">Basically, try to stay around technical things, and avoid talking about poor cafeteria or no free cab pickup-drop services etc.</mark>
* <mark style="color:green;">The motive is to show your passion towards work related things and not focus on secondary things like cafeteria or cabs or playgrounds etc.</mark>

**4. Are you happy at your current job ?**

* <mark style="color:green;">This is also a big trap.</mark>\ <mark style="color:green;">If you talk only about goody-goody positive things, then this question will be immediately followed by -</mark> <mark style="color:green;">**if you like your job, then why are you looking around for another job**</mark><mark style="color:green;">?</mark>
* <mark style="color:green;">So, answer it diplomatically around point 1 of this post. Talk about good things like - I have gotten to learn a lot.</mark>
  * Got to explore data side
  * Worked on such big scale
* <mark style="color:green;">Then talk about negatives - again in polished way</mark>
  * Domain shift

**5. What would you do if you find your senior or boss doing something unethical or violating a company policy ?**

Always talk about that you would gently point out to that person directly, and request that person to follow the correct process. In case the violations continue, then I would like to know about the violation reporting policy of your company.

Here, you can turnaround the interview by **cross-questioning** your interviewer - "**by the way, can you give a brief insight into policy violation reporting mechanism which exists in this company ?**"

**6. What is your greatest weakness ?**

* <mark style="color:green;">No, NO, NO - please do not talk about</mark> <mark style="color:green;">**being impatient or pushing your team hard etc etc**</mark><mark style="color:green;">. These are all very very well-known answers.</mark>
* <mark style="color:green;">Talk about something more genuine and possibly not related to work -</mark> I am not so good at remembering names of people I interact with for first few times.
* <mark style="color:green;">But be prepared to answer -</mark> **what are you doing to overcome this weakness** ?
* <mark style="color:green;">Possible answers to above examples may be -</mark> **Hi X**, I am using this technique to use the name of the person I am interacting with first time in conversation



## 1. G\&L: Google's Principles

* "Our mission is to organise the world’s information and make it universally accessible and useful."
* "Do the right thing." (formally: "Dont be Evil")
* Google also looks for “Googliness” – a mashup of passion and drive that’s hard to define but easy to spot.

## 2. G\&L : About

* You have to show yourself as <mark style="color:orange;">**individual independent contributor**</mark> while working in team
* I have put rather more importance on what not to say than what to say.
* Evaluation Attributes(6-7):
  * **Googleyness**
    * <mark style="color:red;">**How do you value the feedback?**</mark>
      * How you demonstrate maturity while dealing with disagreement with coworkers
      * You're not offended by negative feedbacks & take them positively, adding those values to your skillset
    * <mark style="color:red;">**How you effectively challenge the status-quo**</mark>
      * How you challenge diff processes which are all settled in your team & people are comfortable with them
      * But you find out that there are gaps and you're on the top of it.
    * <mark style="color:red;">**Thriving in Ambiguity**</mark>
      * Demonstrate problem solving skills
    * <mark style="color:red;">**Put users first**</mark>
    * <mark style="color:red;">**Care about the team**</mark>
  * **Leadership**
    * <mark style="color:red;">**How you manager your project**</mark>
    * <mark style="color:red;">**Work as a team**</mark>
    * <mark style="color:red;">**Strive for self development**</mark>
* **Tips by HR:**
  * Take a <mark style="color:red;">**STAR**</mark> approach with 1-2 liners on each pointer. max 7-8 questions will be asked.
  * All scenarios should be industrial & not personal
  * Do not fake the scenarios. But be wise about what you say
  * Show signals that you are an independent contributor
  * DO NOT SHOW that you needed help from team members while implementing your tasks
    * you might tell that you discussed it with other team members; but you are the whole & sole owner of the product/project/module & you are delivering it.
  * In some scenarios even if you're not the decision maker, but you should be the one driving the project(see **BQ#3)**
  * In some situations where you have not been before: answer like this =>
    * Even though I havn't been in similar situation, but I would like to take a hypothetical approach to address this particular scenario
  * Do not give all the pointers on the first questions itself because there might be follow-ups to it

## 2 \[**Googleyness**] Behavioural Questions&#x20;

### <mark style="color:red;">**2.1 How do you value the feedback?**</mark>

#### **ABOUT:**

* How you demonstrate maturity while dealing with disagreement with coworkers
* You're not offended by negative feedbacks & take them positively, adding those values to your skillset
  * "Negative feedback is the best kind. It lets you know what to improve."

#### QUESTIONS:

* [ ] **\[BQ.1] **<mark style="color:orange;">**(i)Tell me about a time when you had an opinion diff that a peer.**</mark>&#x20;
  * [ ] <mark style="color:orange;">**(ii) How did you resolve it**</mark> @HR&#x20;
* [ ] **\[BQ.2] **<mark style="color:orange;">**(i) Tell me about a time when you have to adapt to a colleague's work style to finish a project?**</mark>&#x20;
  * [ ] <mark style="color:orange;">**(ii) What did you learn from his/her's work style**</mark>&#x20;
  * [ ] <mark style="color:orange;">**(iii) How did you apply those learning to any later project/situation?**</mark> @HR&#x20;
* [ ] **\[BQ.3] **<mark style="color:blue;">**Tell me a time when you have hard time working with any colleagues**</mark> => same as #2
* [ ] **\[BQ.4] **<mark style="color:blue;">**How do you value feedback? (ii) Most critical feedback received? (iii) Changes made in self from it?**</mark>

{% tabs %}
{% tab title="BQ.1" %}
## 0. IDEAL ANS:



* &#x20;ideal answer(of the one who got strong feedback) =>
* consulted with the other team members & pulled in others with their expertise in the area
* wrote a doc clearly listing pros & cons, to discuss with the other leads for conclusion
* it was resolved quickly as the peers agreed with the pros & cons as listed
* I also provided alternative designs that have convincibility

## NOTES: =>

* 1#Use data not opinions to make judgements. Ask the same of the other person.
* 2#Worst case, disagree and commit.

## #1. Keyword Targeting - Sampling?

### 1.1 SITUATION

* ..

### 1.2 TASK

* ...

### 1.3 ACTION

* ...

### 1.4 RESULT

* ...

## 2. Keyword Targeting -algo
{% endtab %}

{% tab title="BQ.2" %}
## NOTES:

* You have no obligation or expectation to like everyone at your company.
* The only important thing is that you should be able to work with someone regardless of your feelings toward them.
* I recently have a new colleague joined my team，but he is very **rigid and pushy**. Basically, he will ask you to **listen or follow him on everything**. If you have different opinion, he will get into an offending mode and try to argue with you with no respect. Once he set up a meeting, you need to do what he asked you to do. If he created a doc, you cannot change anything.
*   The thing is their opinion is usually wrong most of the time but they cannot see it. It’s a moot point trying to get them to change their mind. I would try to get other people 🆗 my side of the opinion before trying to convince him. Find key influencers on your team and influence them first before him.

    Ultimately, Accept your own shortcomings that you simply don’t have the power to change some people’s minds. And you don’t give a f\*\*\* if your coworker doesn’t change his mind.
* **Constructive disagreement?** If you disagree with him in something, be constructive and present your point.
*   ### Colleague with strong opinions

    I have a strong SDE in my team. <mark style="color:orange;">**He is really good at delivering stuff. He displays strong ownership too. But he is bit head strong and strong opinionated**</mark>.\
    \
    His choice of words and tone trips me off. I feel hostile when he points out any gaps or offers feedback to me and others.\
    \
    I don’t know if he is doing that intentionally or it’s just that he way he is conditioned.\
    \
    I <mark style="color:orange;">**have a good relation with this guy and I think he respects me**</mark>. But it really bothers me when he uses string words and strong tone.\
    \
    I raise my tone too when he uses his strong opinionated tone. It makes me feel bad later.\
    \
    I have no issue with disagreement or even accepting that I am wrong when the other person is soft spoken and polite. My debates with every other engineers have been smooth and I never had the issue that I am facing with this guy.

## 1. SITUATION : Keyword Targeting

* ..

## 2. TASK

* ...

## 3. ACTION

* ...

## 4. RESULT

* ...
{% endtab %}

{% tab title="BQ.4" %}
## #1. Being Impatient?

### 1.1 SITUATION

* ..

### 1.2 TASK

* ...

### 1.3 ACTION

* ...

### 1.4 RESULT

* ...
{% endtab %}
{% endtabs %}

### <mark style="color:red;">**2.2 How you effectively challenge the status-quo**</mark>

#### **ABOUT:**

* How you challenge diff processes which are all settled in your team & people are comfortable with them
* But you find out that there are gaps and you're on the top of it.

#### QUESTIONS:

* [x] **\[BQ.1] **<mark style="color:orange;">**(i) Tell me about a time when you implemented a new idea in team & met with resistance? (feel free to use work/school/extra curricular eg)**</mark>&#x20;
  * [ ] <mark style="color:orange;">**(ii) Why was the resistance?**</mark> =>my idea sounded so simple that people couldnt believe it
  * [ ] <mark style="color:orange;">**(iii) How did you overcome it?**</mark>&#x20;
  * [ ] <mark style="color:orange;">**(iv) What was the result?**</mark>&#x20;
  * [ ] <mark style="color:orange;">**(v) What could you have done differently?**</mark> @HR&#x20;
* [ ] **\[BQ.2] **<mark style="color:blue;">**Failed in Project Estimation? (ii) What diff approach you made to achieve end result?**</mark>

{% tabs %}
{% tab title="BQ.1" %}
## NOTES:

## #1. JARVIS

### 1.1 SITUATION

* ..

### 1.2. TASK

* ...

### 1.3. ACTION

* ...

### 1.4. RESULT

* ...

## #2. Sampling - try to keep it for later



### 2.1 SITUATION

* ..

### 2.2. TASK

* ...

### 2.3. ACTION

* ...

### 2.4. RESULT

* ...
{% endtab %}

{% tab title="[BQ.2]" %}
## #1. CynicalReader : hazels of scraping

## #2. Sampling : @BBD'21&#x20;
{% endtab %}
{% endtabs %}

### <mark style="color:red;">**2.3 Thriving in Ambiguity**</mark>

#### **ABOUT:**

* Demonstrate problem solving skills

#### QUESTIONS:

* [ ] **\[BQ.1] **<mark style="color:blue;">**How do you deal with Ambiguity?**</mark>
* [ ] **\[BQ.2]**

{% tabs %}
{% tab title="BQ.1" %}
## NOTES:

* The world is an ambiguous place. Multiple things can be true at the same time, which is hard to process. **Humans crave simplicity and linear relationships**. But the world isn't like that.
* Thriving in ambiguity means making better decisions
* \=> Use Data, facts instead of openions/feelings....

## #1. Rzp Capital- ES

## #2. Linguini @Nestaway&#x20;

My internship mentor gives me high level and ambiguous ideas and expects me to flesh them out. I don't have a problem with this, but when I do so, he rejects fleshed out ideas. He wants me to try again and gives me another bunch of new high level ideas.

This cycle repeats and I remain stuck. Once, I asked if he could give me more details to which he responded that's not his job and I should figure out things on my own. I am able to do the tasks which are clear comfortably, but have trouble with with these high level ideas.

I feel stupid and incompetent, and have become demotivated due to this.

\==>&#x20;

This is super common when you are new to a company or just to professional life. Don't lose heart. With experience you will get good at translating vague asks. Talk to other people first before you take your ideas back to the mentor. Also do research and find an example in the wild of whatever you are recommending. Then when you present, back up your recommendations with stats, just throw numbers at the mentor. Your specific response almost doesn't matter. Show in-depth work behind it.

### 1.1. SITUATION

* ..

## 2. TASK

* ...

## 3. ACTION

* ...

## 4. RESULT

* ...
{% endtab %}

{% tab title="BQ.2" %}
## 1. SITUATION

* ..

## 2. TASK

* ...

## 3. ACTION

* ...

## 4. RESULT

* ...
{% endtab %}
{% endtabs %}

### <mark style="color:red;">**2.4 Put users first**</mark>

#### **ABOUT:**

*

#### QUESTIONS:

* [ ] **\[BQ.1] **<mark style="color:blue;">**Tell me a time when you when above and beyond to deliver better customer experience**</mark>
* [ ] **\[BQ.2] **<mark style="color:blue;">**how would you handle customer reviews?**</mark>

{% tabs %}
{% tab title="BQ.1" %}
## #1. Rzp: Early Settlements

### 1.1. SITUATION

* Almost 90% users have stopped using ES feature after first week of onboarding;&#x20;
* Since it was a high revenue project; Rzp cusotmers team was calling them again to collect data points:
  * Bad UX
  * Not exactly ES ( takes \~2 days)
  * Merchant should be able to select specific txns for ES.&#x20;
  * Automate integration of ES in merchant dashboard.&#x20;
  * Revised eligibility rules and pricing model
  * Revamp db in ES&#x20;

### 1.2. TASK

* Built v2 from scratch

### 1.3. ACTION

* ...

### 1.4. RESULT

* ...

## #2. Ads Merch Separation



### 2.1. SITUATION

* ..

### 2.2. TASK

* ...

### 2.3. ACTION

* ...

### 2.4. RESULT

* ...
{% endtab %}

{% tab title="BQ.2" %}

{% endtab %}
{% endtabs %}

### <mark style="color:red;">**2.5 Care about the team**</mark>

#### **ABOUT:**

*

#### QUESTIONS:

* [ ] **\[BQ.1]**
* [ ] **\[BQ.2]**

{% tabs %}
{% tab title="BQ.1" %}
## 1. SITUATION

* ..

## 2. TASK

* ...

## 3. ACTION

* ...

## 4. RESULT

* ...
{% endtab %}
{% endtabs %}

## **3 \[Leadership]** Behavioural Questions&#x20;

* Behavioural questions usually start with phrases such as “tell me about a time when” or “give me an example of” or “describe a decision you made.” Interviewers are looking for examples of what you have done and how you have done it. They may follow up with more probing questions such as, “what did you do then?” or “what was the result?”

### <mark style="color:red;">**3.1 How you manager your project**</mark>

#### **ABOUT:**

*

#### QUESTIONS:

* [ ] **\[LS.1] **<mark style="color:orange;">**(i) At google you may be pulled in a number of directions by a project?**</mark>
  * [ ] &#x20;<mark style="color:orange;">**(ii) What is your strategy to work in an env with continuously changing priorities?**</mark>&#x20;
  * [ ] <mark style="color:orange;">**(iii) How does constant-changes-in-prioirty impact to your work quality**</mark>&#x20;
  * [ ] <mark style="color:orange;">**(iv) how do these changes impact your overall enjoyment of work?**</mark> @HR&#x20;
* [ ] **\[LS.2] **<mark style="color:blue;">**When you lead some design/ project within team**</mark>
* [ ] <mark style="color:blue;">**\[**</mark>**LS.3] **<mark style="color:blue;">**I was asked about any project that I have recently delivered and how I prepared for handling failure cases/ obstacles**</mark>
* [ ] <mark style="color:blue;">****</mark>

{% tabs %}
{% tab title="LS.1" %}
## 1. SITUATION

* ..

## 2. TASK

* ...

## 3. ACTION

* ...

## 4. RESULT

* ...
{% endtab %}

{% tab title="LS.2" %}
## 1. SITUATION

* ..

## 2. TASK

* ...

## 3. ACTION

* ...

## 4. RESULT

* ...
{% endtab %}
{% endtabs %}

### <mark style="color:red;">**3.2 Work as a team**</mark>

#### **ABOUT:**

*

#### QUESTIONS:

* [ ] **\[LS.1] **<mark style="color:blue;">**what process did you bring to your current team/company?**</mark>
* [ ] **\[LS.2]**

{% tabs %}
{% tab title="LS.1" %}
* tw -> Centralized documentation ( learnt from Rzp) on Confluence ; (better than scattered docs)
* Oncall Automation
  * JARVIS
  * Python lib - Collab of frequenty used things
    * better clean-up util => usage warning
* UT Coverage
* Sampling

## 1. SITUATION

* ..

## 2. TASK

* ...

## 3. ACTION

* ...

## 4. RESULT

* ...
{% endtab %}

{% tab title="LS.2" %}
## 1. SITUATION

* ..

## 2. TASK

* ...

## 3. ACTION

* ...

## 4. RESULT

* ...
{% endtab %}
{% endtabs %}

### <mark style="color:red;">**3.3 Strive for self development**</mark>

#### QUESTIONS:

* [x] **\[LS.1] **<mark style="color:orange;">**(i) Tell me about a time when you set up a difficult goal for yourself that you DID NOT achieve & what was the situation?**</mark>&#x20;
  * [ ] <mark style="color:orange;">**(ii) What was the rational for setting up this goal & what did you learn from this exp?**</mark>&#x20;
  * [ ] <mark style="color:orange;">**(iii) If you were to achieve the same goal again what would you do differently?**</mark> @HR&#x20;
* [x] **\[LS.2]  **<mark style="color:blue;">**Describe two specific goals you set for yourself and how successful you were in meeting them. What factors led to your success?**</mark>
  * Things to consider for your answer:&#x20;
    * ● Your objectives—be clear on those up front.&#x20;
    * ● Reasons you chose those particular goals.&#x20;
    * ● Any measures you set up to track progress.&#x20;
    * ● Obstacles you overcome and things learned along the way.
* [x] **\[LS.3] **<mark style="color:blue;">**Tell me about a time when you failed to meet a deadline. What did you fail to do? What did you learn?**</mark>&#x20;
  * Things to consider for your answer:&#x20;
    * ● The root cause.&#x20;
    * ● How you applied what you learned in future projects.

{% tabs %}
{% tab title="LS.1" %}
## #1. Automate Oncall Stuff @Flipkart

### 1.1. SITUATION

* ..

### 1.2. TASK

* ...

### 1.3. ACTION

* ...

### 1.4. RESULT

* ...

## #2. Mozart Testing Tree @Razorpay



### 2.1. SITUATION

* ..

### 2.2. TASK

* ...

### 2.3. ACTION

* ...

### 2.4. RESULT

* ...\


## #3. Learning About Big Data Tech @Flipkart



### 2.1. SITUATION

* ..

### 2.2. TASK

* ...

### 2.3. ACTION

* ...

### 2.4. RESULT

* ...
{% endtab %}

{% tab title="LS.2" %}
## #1. CynicalReader

### 1.1. SITUATION

* ..

### 1.2. TASK

* ...

### 1.3. ACTION

* ...

### 1.4. RESULT

* ...

## #2. Mozart Testing Tree @Razorpay



### 2.1. SITUATION

* ..

### 2.2. TASK

* ...

### 2.3. ACTION

* ...

### 2.4. RESULT

* ...


{% endtab %}

{% tab title="LS.3" %}
## #1. Sampling BBD'21

## Theory

* Make sure everyone is on the same page about the state of the project versus the deadline.
* Talk about what features might be cut or simplified to help.
* Never, ever commit to hitting the fake deadline, only commit to do your professional best to work as best you can. Don't do crazy overtime.
* 👉Pull in extra people if reqd

[https://www.reddit.com/r/ExperiencedDevs/comments/l1apcq/deadlines\_who\_should\_set\_them\_and\_how\_should\_they/](https://www.reddit.com/r/ExperiencedDevs/comments/l1apcq/deadlines\_who\_should\_set\_them\_and\_how\_should\_they/)
{% endtab %}
{% endtabs %}



<mark style="color:orange;">****</mark>

## 4. Hypothetical Questions

* Questions often begin with “Imagine that...” and are designed to assess your thought process rather than “right” or “wrong” solutions.

<!---->

* [x] **\[HQ.1] **<mark style="color:blue;">**your motivation for work.**</mark>
* [ ] **\[HQ.2] **<mark style="color:blue;">**Imagine you are in charge of organising the grand opening of a new Google office in Bangalore, India. What steps would you take to plan this event?**</mark>

<!---->

* Things to consider for your answer:&#x20;
  * ● The objective of the event, and measurement of success.&#x20;
  * ● Who will be invited to the event.&#x20;
  * ● Logistics around the event, set-up, location, timing.&#x20;
  * ● Stakeholders to involve in the process.

{% tabs %}
{% tab title="[HQ.1]" %}
## #1. Keyword Targeting Algo



**Answer@me:**

* challenging carres tasks
* <mark style="color:orange;">**Read a lot, experiment a lot, and play around as much as possible within what I control.**</mark>
  * <mark style="color:orange;">**👉EG:**</mark>** Keyword Targeting Algo:**
    * started playing around with standard DP-based "Edit Distance Algo" to make it distributed/multiprocess.
    * Implemented a basic version & then found out about **N-gram Levenshtein** algo
    * Build a doc with comparison with both & went ahead with N-gram
* working with smart people around me & learning from them on day-to-day basis (not just about work)
* keep learning new domain & latest tech
* side projects : Eurekea(spiders) | Supp(NextJS)
* post COVID :
  * \-> what's the point of capitalism and consumerism when there's no planet?
  * started giving time for self : eating habits +gym+ meditaition + reading (Snow Cash:Neal Stephenson) + podcasts( fernom street + tim ferris)
  * reattaching/reconnecting with family -@zakir khan ("lockdown mei sabse imp chiz-maine apni family ko firse apne paas kar liya")
  * financial awareness - investments/stocks&#x20;

## Theory:

* In the 1950s, Frederick Herzberg developed a theory that states there are two dimensions to job satisfaction: motivation and hygiene.
* <mark style="color:yellow;">**Hygiene factors**</mark> can minimize dissatisfaction at work, but they can’t make you love your job. These are factors like salary, supervision, and working conditions.
  * When you look back at the best moments of your career, they won’t really include the perks or the free lunches you got.
* Instead, you’ll look back and remember the _<mark style="color:yellow;">**motivators**</mark>_. These are factors like **recognition and achievement.** They mean that your work is **challenging** and that you’re **learning** about topics that you’re intrinsically interested in. These are the factors that’ll be the predominant source of your work satisfaction and what contribute to your **personal growth**.
{% endtab %}

{% tab title="Second Tab" %}

{% endtab %}
{% endtabs %}



## 5. Other Questions

* [x] <mark style="color:orange;">**\[OQ.1] Why do you want to join google?**</mark> @HR&#x20;

{% tabs %}
{% tab title="[OQ.1]" %}
* As my profile might have shown that this is my second attempt at Google(gave last one in March-April 2020).
* For any student since college/school days; getting to work has been a dream.&#x20;
* For me it came in a flight from college to home in first year; when I met an engineer @google.&#x20;
  * During that 2.5 hrs flight, I had&#x20;
  * mantra: "when you study/exp something, just ensure that you've got it full. Be the best in every part & eventually you'll be the best in whole."
  * (applied that to rubiks' cube)
  * Now in retro this advice might not as impactful as it was for me back then, but it did leave an impact on my mind to be like him.
* Followed Google's student curriculum guideline in college.



* Before HR reached out to me in my first attempt; I have not even thought that I'm even ready to interview at Google.
* Even though I failed on 2nd onsite; but it gave me confidence that Google is achievable by me.
* Asked for cooldown period from HR(6 months) & have been prepping hard since then & applied as soon as cooldown ended.


{% endtab %}
{% endtabs %}

## # Values (fillers on behavioural Qs)

* **Be Proactive**
  * be proactive before a situation is exploded
* **In Private:** Discuss critical feedbacks in private
* **Active Listening:**
  * if I'm not practicing active listening; then effectively I am not participating in communication/conflict
* **Empathetic & Perspecti**ve:
  * Be empathetic to person/situation
* **Positivity**
* **Data Driven Decisions**
* **Learnings**

###
