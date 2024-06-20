# Use the official Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Daphne for ASGI support
RUN pip install daphne

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV PORT 8080

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the application
CMD ["daphne", "-b", "0.0.0.0", "-p", "8080", "UtmLinkBuilderApp.asgi:application"]