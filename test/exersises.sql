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


-- Generate highest slot facid without using Limit
-- u need to use either having or where clause to achive this
SELECT facid,
       sum(slots) AS total
FROM cd.bookings
GROUP BY 1
HAVING sum(slots) =
  (SELECT max(sumslots)
   FROM
     (SELECT facid,
             sum(slots) AS sumslots
      FROM cd.bookings
      GROUP BY 1)x)

--- Other option is to use CTE (Common Table Expressions)
WITH SUM AS
  (SELECT facid,
          sum(slots) AS total
   FROM cd.bookings
   GROUP BY 1)
SELECT facid,
       total
FROM SUM
WHERE total = (SELECT max(total) FROM SUM)


with totals as (
  select facid, extract(month from starttime) as month, sum(slots) as total
  from cd.bookings
  where  extract(year from starttime) = 2012
  group by 1,2


-- Generate subtotals of each month, facid AND only facid and over ALL
WITH months AS
  ( SELECT facid,
           extract(MONTH FROM starttime) AS MONTH,
           sum(slots) AS slots
   FROM cd.bookings
   WHERE extract(YEAR FROM starttime) = 2012
   GROUP BY 1,2)

SELECT facid,
       MONTH,
       slots
FROM months
UNION ALL
SELECT facid,
       NULL,
       sum(slots)
FROM months
GROUP BY 1
UNION ALL
SELECT NULL,
       NULL,
       sum(slots)
FROM months
ORDER BY 1, -- Order by needs to happen at the very end of the UNION ALL clause
         2
