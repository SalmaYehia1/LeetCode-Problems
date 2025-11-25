-- Last updated: 11/25/2025, 5:01:46 PM
# Write your MySQL query statement below
select E.name , B.bonus
from Employee as E 
LEFT JOIN Bonus B ON E.empId = B.empId
where B.bonus <1000 or B.bonus is null