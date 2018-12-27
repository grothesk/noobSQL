# Specify a base image
FROM postgres

# Set environment variables
ENV POSTGRES_DB=demo
ENV POSTGRES_USER=pgdocker
ENV POSTGRES_PASSWORD=docker

# Copy files for entrypoint
COPY sql /docker-entrypoint-initdb.d
