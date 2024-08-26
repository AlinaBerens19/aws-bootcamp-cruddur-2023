# Use an official Node.js image as a base
FROM node:22.6.0-slim

# Set the working directory to /frontend-react-js
WORKDIR /frontend-react-js

# Copy package.json and package-lock.json first
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all remaining files
COPY . .

# Expose the port that the app will run on
# ARG PORT=3000
EXPOSE ${PORT}

# Command to start the app
CMD ["npm", "start"]
