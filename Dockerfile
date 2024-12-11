# Use the official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . /app/

# Default command to run the application with Gunicorn (instead of Django's development server)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "bike_connect.wsgi:application"]
