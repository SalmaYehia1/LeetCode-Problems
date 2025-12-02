-- Last updated: 12/2/2025, 2:11:51 AM
select c.name as Customers
from Customers as c
left join  Orders as o on o.customerId=c.id
WHERE o.customerId IS NULL;