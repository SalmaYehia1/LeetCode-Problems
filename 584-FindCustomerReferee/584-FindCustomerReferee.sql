-- Last updated: 11/25/2025, 5:01:45 PM
# Write your MySQL query statement below
select C.name 
from Customer as C 
where C.referee_id != 2 or C.referee_id is null