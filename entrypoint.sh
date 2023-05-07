#!/bin/bash

# open app directory
cd /app/

# Create secrets.toml
echo "" > .streamlit/secrets.toml
echo 'DBHOST = "'"$DBHOST"'"' >> .streamlit/secrets.toml
echo 'DBUSER = "'"$DBUSER"'"' >> .streamlit/secrets.toml
echo 'DBPASSWORD = "'"$DBPASSWORD"'"' >> .streamlit/secrets.toml

# Run app
python3 -m streamlit run main.py