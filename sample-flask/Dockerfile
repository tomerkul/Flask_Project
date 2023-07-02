# Use a base image
FROM docker/compose:1.29.2

# Set the working directory inside the container
WORKDIR /app

# Copy everything from the current directory to the container
COPY . /app

# Set the command to run the Docker Compose command
CMD ["docker-compose", "up"]
