# mongoTicket by Michi 🥭
A simple helpdesk tool based on python3, streamlit & postgres.

## Table of contents
- [Features](#features)
- [Planend Features](#planned-features)
- [Self host](#self-host)
- [Docker](#docker)
- [Docker compose](#docker-compose)
- [Build docker image](#build-docker-image)
- [Manually run with python](#manually-run-with-python)

## Features
- Self hosted
- Free
- Open Source
- Create tickets
- Create customers
- Self register a user
- Assign a ticket to a customer and a user

## Planned features
- [ ] User management
- [ ] Disable self register for users
- [ ] Permissions
- [ ] Organizations
- [ ] Custom branding
- [ ] Add times to ticket
- [x] Self hostable

If you wish a feature or experience a bug create a issue and assign a tag to it.

# Self host
## Docker
Run container
```bash
docker run --name mangoticketAPP -p 8501:8501 -e DBHOST=mangoticketDB -e DBUSER=helpdesk -e DBPASSWORD=helpdesk michivonah/mangoticket
```

Run container for db
```bash
docker run --name mangoticketDB -e POSTGRES_DB=helpdesk -e POSTGRES_USER=helpdesk -e POSTGRES_PASSWORD=helpdesk -d postgres
```

You're done! Now visit http://localhost:8501 in your browser. The default admin credentials are **admin** with the password **admin**.

## Docker compose
Copy following yml into a file called ```docker-compose.yml```
```yml
version: '3.3'
services:
    app:
        container_name: mangoticketAPP
        ports:
            - '8501:8501'
        environment:
            - DBHOST=mangoticketDB
            - DBUSER=helpdesk
            - DBPASSWORD=helpdesk
        networks:
            - mangoticketNET
        image: michivonah/mangoticket
    db:
        container_name: mangoticketDB
        environment:
            - POSTGRES_DB=helpdesk
            - POSTGRES_USER=helpdesk
            - POSTGRES_PASSWORD=helpdesk
        networks:
            - mangoticketNET
        image: postgres
networks:
  mangoticketNET:
    name: mangoticketNET
```
> Please replace the values POSTGRES_PASSWORD & DB_PASSWORD with a secure password!

Run following command to start up the containers
```bash
docker-compose up -d
```

You're done! Now visit http://localhost:8501 in your browser. The default admin credentials are **admin** with the password **admin**.

## Build docker image
Clone git repo
```bash
git clone https://github.com/michivonah/helpdesk.git
```

Open directory
```bash
cd helpdesk
```

Build image
```bash
docker build -t mangoticket:latest .
```

Run container
```bash
docker run --name mangoticketAPP -p 8501:8501 -e DBHOST=mangoticketDB -e DBUSER=helpdesk -e DBPASSWORD=helpdesk michivonah/mangoticket
```

> Please note that you need a running postgres instance

## Manually run with python
> You need a postgres database & python3 installed on your system for continue with the following steps

Install requirements
```bash
pip3 install --upgrade pip
pip3 install pipenv
pip3 install streamlit
pip3 install --no-cache-dir -r requirements.txt
pip3 install psycopg2
pip3 install psycopg2-binary
```

Create secrets.toml file in current dirctory
```bash
nano .streamlit/secrets.toml
```

Copy following toml into the created file & change the variables
```bash
DBHOST = "YOURHOST"
DBPORT = "5321"
DBNAME = "helpdesk"
DBUSER = "YOURUSER"
DBPASSWORD = "YOURPASSWORD"
```
> Please use a secure password instead of "YOURPASSWORD"!

Run app
```bash
python3 -m streamlit run main.py
```

You're done! Now visit http://localhost:8501 in your browser. The default admin credentials are **admin** with the password **admin**.
