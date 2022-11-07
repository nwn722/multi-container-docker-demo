# syntax=docker/dockerfile:1

FROM postgres

# init script which create the hellodb and the populate the data
COPY ${PWD}/initdata.sh /docker-entrypoint-initdb.d/  

EXPOSE 5432
