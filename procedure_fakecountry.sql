CREATE PROCEDURE fake_country (
    IN fake_country_name VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
INSERT INTO country (country_name, pop, density, land_area) VALUES (fake_country_name, 10000000 * RANDOM(), 1000 * RANDOM(), 10000000 * RANDOM());
END; $$;


CALL fake_country('Kanto');
CALL fake_country('Johto');
CALL fake_country('Hoenn');