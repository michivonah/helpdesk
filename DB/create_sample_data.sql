/*
CREATE SAMPLE DATA
Michi von Ah - April 2023
*/

INSERT INTO "user" (username, password, mail) VALUES
    ('fritz', 'fritz', 'fritz@example.com'),
    ('max', 'max', 'max@example.com');

INSERT INTO "status" (name) VALUES
    ('Offen'),
    ('Abgeschlossen');

INSERT INTO "customer" (name) VALUES
    ('ABC Buchstaben GmbH'),
    ('XYZ Firma'),
    ('Datenbanken Inc.'),
    ('Docker4Life AG');

INSERT INTO "ticket" (name, fk_statusid, fk_userid, fk_customerid) VALUES
    ('Drucker funktioniert nicht', 1, 1, 4),
    ('Neues Smartphone', 1, 1, 2),
    ('Notebook für neue Mitarbeiterin', 1, 2, 3),
    ('Arbeitsplatz bereitstellen', 1, 2, 3);

