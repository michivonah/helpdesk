/*
SELECT ALL TICKETS FROM USER
Michi von Ah - April 2023
*/

DROP VIEW IF EXISTS "alltickets";
CREATE VIEW "alltickets" AS
	SELECT ticketid AS "Ticketnumber", ticket."name" AS "Ticketname", ticket."description" AS "Description", "customer"."name" AS "Customer", "user"."username" AS "Assigned to" FROM ticket
		JOIN customer ON customerid = fk_customerid
		JOIN "user" ON userid = fk_userid;