------------------------COMBINE TWO TABLES
/*SELECT firstname,lastname,city,state FROM
Person LEFT JOIN Address ON Person.personId = Address.personId */

------------------------SECOND HIGHEST SALARY
/*SELECT 
    (SELECT DISTINCT salary
     FROM Employee
     ORDER BY salary DESC
     LIMIT 1 OFFSET 1) AS SecondHighestSalary;*/

------------------------Nth HIGHEST SALARY
/*CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
  RETURN (
    select distinct salary from employee order by salary desc limit 1 offset n
  );
END*/

------------------------RANK SCORES
/* # Write your MySQL query statement below
SELECT s1.score,
    (SELECT COUNT(DISTINCT s2.score)
    FROM Scores s2
    WHERE s2.score >= s1.score) AS 'rank'
FROM Scores s1
ORDER BY s1.score DESC;*/

------------------------CONSECTIVE NUMBERS
/*# Write your MySQL query statement below
SELECT DISTINCT l1.num as ConsecutiveNums
FROM Logs l1,Logs l2,Logs l3
WHERE l1.id = l2.id-1
AND l2.id = l3.id-1
AND l1.num = l2.num
AND l2.num = l3.num*/

------------------------EMPLOYEES EARNING MORE THAN THEIR MANAGERS
/*# Write your MySQL query statement below
select a.name as Employee
from Employee a
join Employee b 
on a.managerId = b.id
where a.salary > b.salary*/

------------------------DUPLICATE EMAILs
/*# Write your MySQL query statement below
select distinct(a.email)  as Email
from Person a
join Person b on a.email = b.email and a.id <> b.id*/

-------------------------CUSTOMER WHO NEVER ORDERED
/*SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
  ON c.id = o.customerId
WHERE o.customerId IS NULL;*/

-------------------------DEPARTMENT HIGHEST SALARY
/*# Write your MySQL query statement below
select d.name as Department , e.name as Employee , e.salary as Salary
from Employee e
inner join Department d on e.departmentId = d.id
where e.salary = (select max(salary) FROM Employee WHERE d.id = Employee.departmentId);*/

--------------------------EXCHANGE SEATS
/*# Write your MySQL query statement below
select
case 
    when id = (select max(id) from seat) and id % 2=1 then id
    when id % 2=1 then id+1 else id-1 end as id,
student
from seat
order by id;*/