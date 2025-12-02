-- Last updated: 12/2/2025, 2:48:49 AM
select activity_date as day , count(DISTINCT user_id ) as active_users
from Activity
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'

group by activity_date
