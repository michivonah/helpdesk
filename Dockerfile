FROM python:3

# Create directory
RUN mkdir app
WORKDIR /app/

# Copy files
COPY . .

# Set enviromental variables
ENV DBHOST mangoticketDB
ENV DBPORT 5432
ENV DBNAME helpdesk
ENV DBUSER helpdesk
ENV DBPASSWORD helpdesk

# Install needed packages
RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN pip install streamlit
RUN pip install --no-cache-dir -r requirements.txt

# Start app
CMD ["sh","entrypoint.sh"]
