/*
SELECT ALL TICKETS FROM USER
Michi von Ah - April 2023
*/

DROP VIEW IF EXISTS "alltickets";
CREATE VIEW "alltickets" AS
	SELECT ticketid, ticket."name", ticket."description", "customer"."name" AS "Customer", "user"."username" AS "Assigned" FROM ticket
		JOIN customer ON customerid = fk_customerid
		JOIN "user" ON userid = fk_userid;