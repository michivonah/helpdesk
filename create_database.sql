/*
SETUP DATABASE ENVIROMENT FOR HELPDESK
Michi von Ah - April 2023
*/

-- CREATE DATABASE
USE MASTER;

DROP DATABASE IF EXISTS helpdesk;

CREATE DATABASE helpdesk;

USE helpdesk;

-- CREATE TABLES
CREATE TABLE user(
	userid INTEGER IDENTITY,
	username VARCHAR(30),
	mail VARCHAR(250),
	password VARCHAR(99),
	fk_usergroupid INTEGER,
	PRIMARY KEY(userid)
);

CREATE TABLE usergroup(
	usergroupid INTEGER IDENTITY,
	name VARCHAR(30),
	admin BOOLEAN,
	PRIMARY KEY(usergroupid)
);

CREATE TABLE ticket(
	ticketid INTEGER IDENTITY,
	name VARCHAR(120),
    description VARCHAR(240),
	fk_statusid INTEGER,
    fk_userid INTEGER,
    fk_customerid INTEGER,
	PRIMARY KEY(ticketid)
);

CREATE TABLE status(
	statusid INTEGER IDENTITY,
	name VARCHAR(30),
	PRIMARY KEY(statusid)
);

CREATE TABLE customer(
	customerid INTEGER IDENTITY,
	name VARCHAR(30),
    mail VARCHAR(250),
    phone VARCHAR(14),
    birthdate DATE,
    website VARCHAR(250),
    address VARCHAR(250),
    notes VARCHAR(250),
	PRIMARY KEY(customerid)
);

-- SET FOREIGN KEYS
ALTER TABLE user ADD FOREIGN KEY(fk_usergroupid) REFERENCES usergroup(usergroupid);
ALTER TABLE ticket ADD FOREIGN KEY(fk_statusid) REFERENCES status(statusid);
ALTER TABLE ticket ADD FOREIGN KEY(fk_userid) REFERENCES user(userid);
ALTER TABLE ticket ADD FOREIGN KEY(fk_customerid) REFERENCES customer(customerid);

-- CREATE DEFAULT USER GROUPS
INSERT INTO usergroup (name, admin)
	VALUES('SYSTEM', true);

-- CREATE DEFAULT USERS
INSERT INTO user (username, password) VALUES
    ('SYSTEM', 'SYSTEM'),
    ('admin', 'admin');
