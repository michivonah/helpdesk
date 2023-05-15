#!/bin/bash

# open app directory
cd /app/

# Create secrets.toml
echo "" > .streamlit/secrets.toml
echo 'DBHOST = "'"$DBHOST"'"' >> .streamlit/secrets.toml
echo 'DBPORT = "'"$DBPORT"'"' >> .streamlit/secrets.toml
echo 'DBNAME = "'"$DBNAME"'"' >> .streamlit/secrets.toml
echo 'DBUSER = "'"$DBUSER"'"' >> .streamlit/secrets.toml
echo 'DBPASSWORD = "'"$DBPASSWORD"'"' >> .streamlit/secrets.toml

# Install psql client
apt update -y
apt-get install postgresql-client -y

# Run scripts for creating db structure
echo '"'"$DBHOST"'":"'"$DBPORT"'":"'"$DBNAME"'":"'"$DBUSER"'":"'"$DBPASSWORD"'"' > /root/.pgpass
chmod 600 /root/.pgpass
psql -h $DBHOST -p $DBPORT -U $DBUSER -d $DBNAME -f "DB/create_database.sql"
psql -h $DBHOST -p $DBPORT -U $DBUSER -d $DBNAME -f "DB/create_views.sql"

# Run app
python3 -m streamlit run main.py