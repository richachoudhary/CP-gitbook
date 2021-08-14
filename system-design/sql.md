# SQL

## NOTES:

* **Group By:**
  * The `GROUP BY` statement groups rows that have the same values into summary rows, like "find the number of customers in each country".
  * The `GROUP BY` statement is often used with aggregate functions \(`COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()`\) to group the result-set by one or more columns.
  * ```sql
    SELECT COUNT(CustomerID), Country
    FROM Customers
    GROUP BY Country;
    ```

    * 
* **Wildcards** in Mysql

| Symbol | Description | Example |
| :--- | :--- | :--- |
| % | Represents zero or more characters | bl% finds bl, black, blue, and blob |
| \_ | Represents a single character | h\_t finds hot, hat, and hit |
| \[\] | Represents any single character within the brackets | h\[oa\]t finds hot and hat, but not hit |
| ^ | Represents any character not in the brackets | h\[^oa\]t finds hit, but not hot and hat |
| - | Represents a range of characters | c\[a-b\]t finds cat and cbt |

* **Like** Operator with wildcards

| Like | Description |
| :--- | :--- |
| WHERE CustomerName LIKE 'a%' | Finds any values that start with "a" |
| WHERE CustomerName LIKE '%a' | Finds any values that end with "a" |
| WHERE CustomerName LIKE '%or%' | Finds any values that have "or" in any position |
| WHERE CustomerName LIKE '\_r%' | Finds any values that have "r" in the second position |
| WHERE ContactName LIKE 'a%o' | Finds any values that start with "a" and ends with "o" |

* **REGEX**
  * Practiced from [regexone.com](https://regexone.com/lesson/misc_meta_characters?)
  * Using regex in SQL queries: 
    * `select distinct city from station where city` **`regexp`** `'^[aeiou]';`

| Regex | Matches |
| :--- | :--- |
| abc.. | letters |
| 123… | Digits |
| \d | Any Digit |
| \D | Any Non-digit character |
| . | Any Character |
| \. | Period |
| \[abc\] | Only a, b, or c |
| \[^abc\] | Not a, b, nor c |
| \[a-z\] | Characters a to z |
| \[0-9\] | Numbers 0 to 9 |
| \w | Any Alphanumeric character |
| \W | Any Non-alphanumeric character |
| {m} | m Repetitions |
| {m,n} | m to n Repetitions |
| \* | Zero or more repetitions |
| + | One or more repetitions |
| ? | Optional character |
| \s | Any Whitespace |
| \S | Any Non-whitespace character |
| ^…$ | Starts and ends |
| \(…\) | Capture Group |
| \(a\(bc\)\) | Capture Sub-group |
| \(.\*\) | Capture all |
| \(abc\|def\) | Matches abc or def |

## Questions: 

### 1. SELECT

* \*\*\*\*[**Weather Observation Station 5**](https://www.hackerrank.com/challenges/weather-observation-station-5/problem) **\|** Query the two cities in **STATION** with the shortest and longest _CITY_ names, as well as their respective lengths

```sql
SELECT CITY,LENGTH(CITY)  FROM STATION 
    WHERE LENGTH(CITY)=(SELECT MIN(LENGTH(CITY)) FROM STATION)  
    ORDER BY CITY ASC LIMIT 1;
SELECT CITY ,LENGTH(CITY) FROM STATION 
    WHERE LENGTH(CITY)=(SELECT MAX(LENGTH(CITY)) FROM STATION)  
    ORDER BY CITY ASC LIMIT 1;
```

* \*\*\*\*[**Weather Observation Station 9**](https://www.hackerrank.com/challenges/weather-observation-station-9/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen) **\|** Query the list of _CITY_ names starting DOES NOT with vowels \(i.e., `a`, `e`, `i`, `o`, or `u`\) from **STATION**

```sql
 --> starts with ke liye
 select city from station where city like '[aeiou]%' order by city;
--OR --> does not start with ke liye
select distinct city from station where left(city,1) not in ('a','e','i','o','u');
--OR
select distinct city from station where city not regexp '^[aeiou]';
```

* \*\*\*\*[**Type of Triangle**](https://www.hackerrank.com/challenges/what-type-of-triangle/problem) **\|** query identifying the _type_ of each record in the **TRIANGLES** table using its three side lengths **\| UAGE: `CASE` ✅**

```sql
SELECT CASE
    WHEN 2 * GREATEST(A, B, C) >= (A + B + C) THEN "Not A Triangle"
    WHEN A = B AND A = C                      THEN "Equilateral"
    WHEN A = B OR A = C OR B = C              THEN "Isosceles"
                                              ELSE "Scalene"
    END
FROM TRIANGLES
```

* \*\*\*\*[**The PADS**](https://www.hackerrank.com/challenges/the-pads/problem) **\| ✅✅**
  * Query an _alphabetically ordered_ list of all names in **OCCUPATIONS**, immediately followed by the first letter of each profession as a parenthetical \(i.e.: enclosed in parentheses\). For example: `AnActorName(A)`, `ADoctorName(D)`, `AProfessorName(P)`, and `ASingerName(S)`.
  * \#2. Query the number of ocurrences of each occupation in **OCCUPATIONS**. Sort the occurrences in _ascending order_, and output them in the following format: `There are a total of [occupation_count] [occupation]s.`

```sql
-- 1ST 
SELECT 
    CONCAT(NAME,"(",SUBSTR(OCCUPATION,1,1),")") 
FROM OCCUPATIONS 
ORDER BY NAME ASC;
-- 2ND 
SELECT 
    CONCAT("There are a total of ",COUNT(OCCUPATION)," ",LOWER(OCCUPATION),'s.') 
FROM OCCUPATIONS 
GROUP BY OCCUPATION 
ORDER BY COUNT(OCCUPATION);
```

* \*\*\*\*[**The Blunder**](https://www.hackerrank.com/challenges/the-blunder/problem) **\|** '0' key was broken. Calculate correct average

  ```sql
  SELECT CEIL(AVG(Salary)-AVG(REPLACE(Salary,'0',''))) FROM EMPLOYEES;
  ```

### 2. JOINS

* \*\*\*\*[**Population Census** ](https://www.hackerrank.com/challenges/asian-population/problem)\| learn syntax

  ```sql
  SELECT SUM(CITY.POPULATION)
  FROM CITY
  JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
  WHERE COUNTRY.CONTINENT = 'Asia';
  ```

* \*\*\*\*[**The Report**](https://www.hackerrank.com/challenges/the-report/problem) **\|** join on range ✅

  ```sql
  --1st way
  SELECT IF(GRADE < 8, NULL, NAME), GRADE, MARKS
  FROM STUDENTS JOIN GRADES
  WHERE MARKS BETWEEN MIN_MARK AND MAX_MARK
  ORDER BY GRADE DESC, NAME
  --2nd way
  SELECT
     CASE WHEN G.Grade > 7 THEN S.Name ELSE 'NULL' END AS NameOrNull
      , G.Grade
      , S.Marks
  FROM Students S
  JOIN Grades G ON S.Marks BETWEEN G.Min_Mark AND G.Max_Mark
  ORDER BY G.Grade DESC, NameOrNull ASC, S.Marks ASC;
  ```

* \*\*\*\*[**Top Competitors**](https://www.hackerrank.com/challenges/full-score/problem) **\|** join on multiple tables. MOST IMP QUESTION ON JOINS!! ✅✅🚀⭐️

  ```sql
  select h.hacker_id, h.name
      from submissions s
      inner join challenges c
          on s.challenge_id = c.challenge_id
      inner join difficulty d
          on c.difficulty_level = d.difficulty_level 
      inner join hackers h
          on s.hacker_id = h.hacker_id
      where s.score = d.score and c.difficulty_level = d.difficulty_level
      group by h.hacker_id, h.name
      having count(s.hacker_id) > 1
  order by count(s.hacker_id) desc, s.hacker_id asc
  ```

* \*\*\*\*[**Ollivander's Inventory**](https://www.hackerrank.com/challenges/harry-potter-and-wands/problem) ****

  ```sql
  select w.id, p.age, w.coins_needed, w.power from Wands w
  inner join Wands_Property p on p.code = w.code
  inner join (
  select p.age, w.power, min(w.coins_needed) as coins from Wands w
  inner join Wands_Property p on p.code = w.code
  where p.is_evil = 0
  group by p.age, w.power ) s on s.age = p.age and s.power = w.power and s.coins = w.coins_needed
  order by w.power desc, p.age desc
  ```

* \*\*\*\*[**Placements**](https://www.hackerrank.com/challenges/placements/problem) ****

  ```sql
  SELECT s.name
      FROM students s
      JOIN friends f
          ON s.id = f.id
      JOIN packages p
          ON f.id = p.id
      JOIN packages p2
          ON f.friend_id = p2.id
      WHERE p.salary < p2.salary
  ORDER BY p2.salary;
  ```

* **LC.181.** [**Employees Earning More Than Their Managers**](https://leetcode.com/problems/employees-earning-more-than-their-managers/) **\|** Join the table with itself, for each row compare the salaries of employee and manager.

  ```sql
  Select a.Name
  From Employee a JOIN Employee b
  ON a.ManagerId = b.Id
  Where a.Salary > b.Salary;
  ```

* **LC.183.** [**Customers Who Never Order**](https://leetcode.com/problems/customers-who-never-order/)\*\*\*\*

  ```sql
  select customers.name as 'Customers'
  from customers
  where customers.id not in
  (
      select customerid from orders
  );
  ```

* **LC.184.** [**Department Highest Salary**](https://leetcode.com/problems/department-highest-salary/)\*\*\*\*

  ```sql
  select d.Name as Department, e.Name as Employee, e.Salary
  from Employee as e
      join Department as d
      on e.DepartmentId = d.Id
      join (
          select max(Salary) as Salary, DepartmentId
          from Employee
          group by DepartmentId
      ) as mx
      on e.Salary = mx.Salary and e.DepartmentId = mx.DepartmentId
  ;
  ```

### 3. RANK :: learn more about it ☑️

* **LC.176.** [**Second Highest Salary**](https://leetcode.com/problems/second-highest-salary/)\*\*\*\*

  ```sql
  Select Max(Salary) AS SecondHighestSalary
  From Employee
  Where Salary < (Select Max(Salary) From Employee);
  ```

* **LC.177.** [**Nth Highest Salary**](https://leetcode.com/problems/nth-highest-salary/)\*\*\*\*

  ```sql
  CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
  BEGIN
  SET N=N-1;
    RETURN (
        SELECT DISTINCT Salary 
        FROM Employee
        ORDER BY Salary DESC
        LIMIT 1 
        OFFSET N
    );
  END
  ```

* \#

  ```sql

  ```

### 4. Basics

* **182.** [**Duplicate Emails**](https://leetcode.com/problems/duplicate-emails/)\*\*\*\*

  ```sql
  Select Email From Person
  Group by Email
  Having count(*) > 1;
  ```

* **196.** [**Delete Duplicate Emails**](https://leetcode.com/problems/delete-duplicate-emails/)\*\*\*\*

  ```sql
  /* retain the unique emails*/
  Select Min(Id) AS minId, Email From Person
  Group by Email

  /* delete the emails which don't appear in the unique emails*/
  Delete From Person
  Where Id not in (
      Select minId From (
          Select min(Id) AS minId, Email
          From Person
          Group by Email
      ) AS tmp
  );
  ```

* \#

  ```sql

  ```

* \#

## RESOURCES:

* **\[x\]** [**Summary of SQL Questions on Leetcode**](https://byrony.github.io/summary-of-sql-questions-on-leetcode.html)\*\*\*\*
* **\[.\]** [**shawlu95**](https://github.com/shawlu95)**/**[**Beyond-LeetCode-SQL**](https://github.com/shawlu95/Beyond-LeetCode-SQL)\*\*\*\*
* \*\*\*\*[**mrinal1704**](https://github.com/mrinal1704)**/**[**SQL-Leetcode-Challenge**](https://github.com/mrinal1704/SQL-Leetcode-Challenge)\*\*\*\*

