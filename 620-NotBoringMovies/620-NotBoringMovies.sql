-- Last updated: 3/8/2026, 3:16:12 PM
select id,movie, description ,rating 
from Cinema
where id % 2=1
and description != "boring"
order by rating desc