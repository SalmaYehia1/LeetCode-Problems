-- Last updated: 11/25/2025, 5:01:42 PM
# Write your MySQL query statement below
select S.year , S.price ,P. product_name 
from Sales as S 
join Product as P on P.product_id = S.product_id
