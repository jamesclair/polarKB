BEGIN;

CREATE TABLE
    IF NOT EXISTS job (
        guid UUID PRIMARY KEY,
        name TEXT NOT NULL CONSTRAINT name_len_check CHECK (char_length(name) <= 255),
        description TEXT CONSTRAINT name_len_check CHECK (char_length(description) <= 255),
        date_posted DATE,
        date_applied DATE,
        creation_date TIMESTAMP NOT NULL DEFAULT current_timestamp,
    );

COMMIT;