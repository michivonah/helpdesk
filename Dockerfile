FROM python:3

# Create directory
RUN mkdir app
WORKDIR /app/

# Copy files
COPY . .

# Install needed packages
RUN pip3 install pipenv
RUN pipenv shell
RUN pip install streamlit
RUN pip install --no-cache-dir -r requirements.txt

# Start app
CMD ["python3","-m","streamlit","run","main.py"]
