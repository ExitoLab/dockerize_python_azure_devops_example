# Use an official Python runtime as a parent image
FROM python:3.10.17-alpine3.21

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Use Gunicorn to run the app in production mode
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]