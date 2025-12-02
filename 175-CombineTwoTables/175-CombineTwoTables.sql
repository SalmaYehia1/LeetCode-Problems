-- Last updated: 12/2/2025, 2:11:53 AM
select p.firstName ,p.lastName,a.city,a.state
from Person as p
left join Address as a on a.personId=p.personId