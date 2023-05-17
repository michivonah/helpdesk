/*
CREATE SAMPLE DATA
Michi von Ah - April 2023
*/

INSERT INTO "user" (username, displayname, password, mail) VALUES
    ('fritz', 'Fritz Müller', 'c40727c66d04b725818d4579040bcc69d5cfd9b430889a1af92f02e2cdb1bde2', 'fritz@example.com'),
    ('max', 'Max Mustermann', '9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6', 'max@example.com');

INSERT INTO "organization" (name, domain, fk_userid) VALUES
    ('mangoTicket Default', 'michivonah-ticket.streamlit.app', 1),
    ('mangoTicket Demo Version', 'ticket.mchvnh.ch', 1);

INSERT INTO "userorganization" (fk_userid, fk_organizationid) VALUES
    (1, 1),
    (2, 2),
    (3, 1),
    (4, 2);

INSERT INTO "customer" (name, fk_organizationid) VALUES
    ('ABC Buchstaben GmbH', 1),
    ('XYZ Firma', 1),
    ('Datenbanken Inc.', 2),
    ('Docker4Life AG', 2);

INSERT INTO "ticket" (name, fk_statusid, fk_userid, fk_customerid, fk_organizationid) VALUES
    ('Drucker funktioniert nicht', 1, 1, 4, 1),
    ('Neues Smartphone', 1, 1, 2, 1),
    ('Notebook für neue Mitarbeiterin', 1, 2, 3, 2),
    ('Arbeitsplatz bereitstellen', 1, 2, 3, 2);

