FROM node:23-alpine

WORKDIR /app

# Copy package files
COPY ./frontend/package.json ./frontend/yarn.lock* ./

# Install dependencies
RUN yarn install

# Copy application code
COPY ./frontend/. /app

# Expose port
EXPOSE 3000

# Run the development server
CMD ["yarn", "dev", "-p", "3000"]

