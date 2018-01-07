---- CASE WHEN
SELECT name, CASE WHEN monthlymaintenance > 100 THEN 'expensive'
				ELSE 'cheap' END -- Important to use '' not ""
				FROM cd.facilities

CASE WHEN ... THEN
WHEN ... THEN
WHEN ... THEN
ELSE
END

---- TIMES
SELECT memid, surname, firstname, joindate--, to_char(joindate, 'YYYY-MM-DD') as date
FROM cd.members
WHERE --joindate >= '2012-09-01 00:00:00'
to_char(joindate, 'YYYY-MM-DD') >= '2012-09-01'
ORDER BY joindate ASC

SELECT cast(joindate as date) from cd.members -- cast also converts the timestamp data type into a date data type

---- DISTINCT
SELECT distinct surname
FROM cd.members
ORDER BY surname

SELECT distinct surname
FROM cd.members
ORDER BY surname
LIMIT 10 -- OFFSET 10

---- OFFSET 10
-- Here the offset skips the first amount of rows specified, if LIMIT and OFFSET are combined it will start
-- counting the LIMIT rows AFTER the OFFSET statement


---- UNION OPERATOR
-- The union operator only selects distincts by default, the UNION ALL takes all values
select surname
FROM cd.members
UNION -- ALL
SELECT name
from cd.facilities

---- SUBQUERIES (in where clause)
select firstname, surname, joindate
from cd.members
where joindate = (select max(joindate) from cd.members)


---- JOINS
Select starttime
from cd.bookings
join cd.members using (memid) -- join is be definition an inner join
where surname = 'Farrell' and firstname = 'David'

-- same as inner join
SElect starttime
from cd.bookings b, cd.members m
where firstname = 'David' and surname = 'Farrell'
AND b.memid = m.memid

--- Produce list with left join, like statement and to_char
SELECT starttime AS
START, f.name
FROM cd.bookings
LEFT JOIN cd.facilities f USING (facid)
WHERE to_char(starttime, 'YYYY-MM-DD') = '2012-09-21'
  AND f.name LIKE '%Tennis Court%'
ORDER BY starttime ASC;
-- similar query
select bks.starttime as start, facs.name as name
	from
		cd.facilities facs
		inner join cd.bookings bks
			on facs.facid = bks.facid
	where
		facs.facid in (0,1) and
		bks.starttime >= '2012-09-21' and
		bks.starttime < '2012-09-22'
order by bks.starttime;

-- Self join
SELECT DISTINCT originals.firstname,
                originals.surname
FROM cd.members AS recs
LEFT JOIN cd.members AS originals ON originals.memid = recs.recommendedby
ORDER BY surname,
         firstname;

select m.firstname as memfname, m.surname as memsname,
r.firstname as recfname, r.surname as recsname
from cd.members m
left join cd.members r on m.recommendedby = r.memid
order by 2,1


-- Two types of concatenates
select distinct concat(firstname,' ', surname) as member, f.name as facility
from cd.members
left join cd.bookings using (memid)
left join cd.facilities f using (facid)
where f.facid in (0,1)
order by 1

select distinct firstname || ' ' || surname as member, f.name as facility
from cd.members
left join cd.bookings using (memid)
left join cd.facilities f using (facid)
where f.facid in (0,1)
order by 1

--- Where clause needs tricky with OR and two fullfillment points
SELECT concat(firstname, ' ', surname) AS member,
       f.name AS facility,
       CASE
           WHEN memid = 0 THEN slots*guestcost
           ELSE slots*membercost
       END AS cost
FROM cd.bookings
LEFT JOIN cd.members USING (memid)
LEFT JOIN cd.facilities f USING (facid)
WHERE to_char(starttime, 'YYYY-MM-DD') = '2012-09-14'
  AND ((memid = 0
        AND slots*guestcost > 30)
       OR (memid != 0
           AND slots*membercost > 30))
ORDER BY cost DESC


--- SUBQUERIES
SELECT DISTINCT concat(m.firstname,' ', m.surname) AS member,
  (SELECT concat(r.firstname,' ', r.surname)
   FROM cd.members r
   WHERE r.memid = m.recommendedby)
FROM cd.members m

SELECT concat(m.firstname,' ', m.surname) AS member,
       sub.name AS facility,
       sub.cost
FROM cd.members m
LEFT JOIN
  (SELECT starttime,
          memid,
          CASE
              WHEN memid = 0 THEN slots*guestcost
              ELSE slots*membercost
          END AS cost,
          name
   FROM cd.bookings
   LEFT JOIN cd.facilities USING (facid)
   WHERE to_char(starttime, 'YYYY-MM-DD') = '2012-09-14') AS sub USING (memid)
WHERE sub.cost > 30
ORDER BY cost DESC

-- INSERT
INSERT INTO cd.facilities (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
VALUES (9,
        'Spa',
        20,
        30,
        100000,
        800), (10,
               'Squash Court 2',
               3.5,
               17.5,
               5000,
               80)
-- VALUES only lets us input static values. In case we want dynamic values we need to use a Sub Select statement
INSERT INTO cd.facilities (facid,name, membercost, guestcost, initialoutlay, monthlymaintenance)
	SELECT (SELECT max(facid) from cd.facilities)+1, 'Spa',20,30,100000,800;

-- UPDATE values in a TABLE
UPDATE cd.facilities
SET initialoutlay = 10000
WHERE facid = 1;
