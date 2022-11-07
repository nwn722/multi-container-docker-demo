#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE messages (
        id serial PRIMARY KEY,
        greeting VARCHAR ( 50 ) NOT NULL
        );

    insert into messages(greeting) values('Hello World!');
EOSQL