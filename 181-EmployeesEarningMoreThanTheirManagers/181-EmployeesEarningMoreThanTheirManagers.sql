-- Last updated: 12/2/2025, 2:11:52 AM
select e.name as Employee
from employee e
join employee as m on e.managerId =m.id
where e.salary>m.salary