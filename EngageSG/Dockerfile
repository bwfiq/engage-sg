# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port your app runs on (default for Django is 8000)
EXPOSE 8000

# Command to run migrations, load data, and then run the server
CMD ["bash", "-c", "python engagement/load_data.py && python manage.py makemigrations engagement && python manage.py migrate && python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL && python engagement/load_data.py && python manage.py runserver 0.0.0.0:8000"]