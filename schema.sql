DROP TABLE IF EXISTS emotions;


CREATE TABLE emotions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    label TEXT NOT NULL,
    explanation TEXT NOT NULL,
    etymology TEXT NOT NULL,
    example TEXT NOT NULL
);