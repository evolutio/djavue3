FROM node:23-alpine3.19

WORKDIR /frontend

# Copy only necessary files for installation to improve caching
COPY . /frontend

# Install dependencies
RUN apk update 

RUN npm install -g pnpm 

# Install project dependencies
RUN pnpm install

RUN pnpm run build

# Expose the application port
EXPOSE 3000

# Set the default command
CMD ["node", "/frontend/.output/server/index.mjs"]

# Set environment variables
ENV SHELL=/bin/bash LANG=en_US.UTF-8
