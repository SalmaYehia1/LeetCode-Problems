-- Last updated: 12/2/2025, 2:11:54 AM
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
