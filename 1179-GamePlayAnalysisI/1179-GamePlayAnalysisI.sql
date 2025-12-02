-- Last updated: 12/2/2025, 11:35:53 PM
SELECT 
    player_id,
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
