# Use an official Node.js image as a base
FROM node:22.6.0-slim

# Copy all files from the current directory to /frontend-react-js in the container
COPY . /frontend-react-js

# Set the working directory to /frontend-react-js
WORKDIR /frontend-react-js

# Install dependencies
RUN if ! npm --version; then \
    echo "npm is not installed!"; \
    exit 1; \
    else \
    echo "npm is installed!"; \
    npm install; \
    fi

# Expose the port that the app will run on
EXPOSE ${PORT}

# Command to start the app
CMD ["npm", "start"]
