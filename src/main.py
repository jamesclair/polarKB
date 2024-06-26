# Note: the module name is psycopg, not psycopg3
from typing import Any
import psycopg

import constants as c


import logging


log = logging.getLogger(__name__)
LOG_LEVEL: str = getattr(logging, c.LOGGING_LEVEL)
log.setLevel(LOG_LEVEL)

# Connect to an existing database

print()

with psycopg.connect(c.DB_CONNECTION_STR) as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Execute a command: this creates a new table
        cur.execute(
            """
            CREATE TABLE test (
                id serial PRIMARY KEY,
                num integer,
                data text
            )
            """
        )

        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM test")
        cur.fetchone()
        # will return (1, 100, "abc'def")

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        for record in cur:
            print(record)

        # Make the changes to the database persistent
        conn.commit()
