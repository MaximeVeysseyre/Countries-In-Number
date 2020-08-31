CREATE TABLE IF NOT EXISTS "country"
(
    country_name VARCHAR PRIMARY KEY,
    pop INTEGER NOT NULL,
    density INTEGER NOT NULL,
    land_area INTEGER NOT NULL
    insertion_date TIMESTAMP DEFAULT NOW()
);