/*
SELECT ALL TICKETS FROM USER
Michi von Ah - April 2023
*/

DROP VIEW IF EXISTS "alltickets";
CREATE VIEW "alltickets" AS
	SELECT ticketid AS "Ticketnumber", ticket."name" AS "Ticketname", ticket."description" AS "Description", "customer"."name" AS "Customer", "user"."username" AS "Assigned to" FROM ticket
		JOIN customer ON customerid = fk_customerid
		JOIN "user" ON userid = fk_userid;

DROP VIEW IF EXISTS "alltickets-count";
CREATE VIEW "alltickets-count" AS
	SELECT COUNT(*) AS "Total Tickets" FROM ticket;

DROP VIEW IF EXISTS "opentickets-count";
CREATE VIEW "opentickets-count" AS
	SELECT COUNT(*) AS "Open Tickets" FROM ticket
		WHERE fk_statusid = (SELECT DISTINCT statusid FROM status WHERE "name" = 'Open');