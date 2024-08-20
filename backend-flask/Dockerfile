# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container (inside)
WORKDIR /backend-flask

# Outside -> Inside
COPY requirements.txt requirements.txt

# Copy the current directory contents into the container at /app
# everything in the current directory
# first . - /backend-flask (outside)
# second . - /backend-flask (inside)
COPY . .

# Install any needed packages specified in requirements.txt (inside container)
RUN pip3 install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE ${PORT}

# Define environment variable
# Inside the container
ENV FLASK_ENV=development

# Run app.py when the container launches
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=4567"]
