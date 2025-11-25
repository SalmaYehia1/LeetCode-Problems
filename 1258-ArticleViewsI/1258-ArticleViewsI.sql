-- Last updated: 11/25/2025, 5:01:39 PM
# Write your MySQL query statement below
select distinct V.author_id as id
from Views as V 
where author_id= viewer_id 
order by author_id