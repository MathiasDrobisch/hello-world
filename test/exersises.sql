-- Use subselect statement in order to use revenue in WHERE clause

SELECT name,
       revenue
FROM
  (SELECT name,
          sum(CASE
                  WHEN memid=0 THEN guestcost*slots
                  ELSE slots*membercost
              END) AS revenue
   FROM cd.bookings
   LEFT JOIN cd.facilities USING (facid)
   GROUP BY 1
   ORDER BY 1) x
WHERE revenue < 1000
