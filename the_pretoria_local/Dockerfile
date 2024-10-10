# Use a Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project files
COPY . /app/

# Collect static files (if necessary)
RUN python manage.py collectstatic --noinput

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "the_pretoria_local.wsgi:application"]
