# helpdesk

# Requirements
- Python3 & Pip3 installed
- Streamlink & Nicegui installed
- PostgreSQL
- Docker Engine & Docker Compose

# Run app
Install python packages
```bash
pip3 install psycopg2
pip3 install psycopg2-binary
```

Run app
```bash
python3 -m streamlit run main.py
```

# Docker
Run container
```bash
docker run --name mangoticketAPP -p 8501:8501 -e DBHOST=mangoticketDB -e DBUSER=helpdesk -e DBPASSWORD=helpdesk michivonah/mangoticket
```

Run container for db
```bash
docker run --name mangoticketDB -e POSTGRES_DB=helpdesk -e POSTGRES_USER=helpdesk -e POSTGRES_PASSWORD=helpdesk -d postgres
```