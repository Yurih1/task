FROM python:3.9

# Update and install the MariaDB client
RUN apt-get update && \
    apt-get install -y mariadb-client

# Set the working directory
WORKDIR /app/taskmanager/

# Copy requirements files and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application files
COPY . /app/

# Copy the wait script to the container
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Command to start the server
CMD ["/app/wait-for-it.sh", "db", "--", "gunicorn", "taskmanager.wsgi:application", "--bind", "0.0.0.0:8000"]