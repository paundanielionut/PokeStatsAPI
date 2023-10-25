# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the Python virtual environment (venv) from your project directory
COPY venv /app/venv

# Install your FastAPI application dependencies from requirements.txt
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the .env file from your project directory to the container
COPY .env /app/.env

# Copy the rest of your application code into the container
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
