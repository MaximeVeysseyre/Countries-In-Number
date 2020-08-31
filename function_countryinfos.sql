CREATE OR REPLACE FUNCTION country_infos (
  country_choice VARCHAR
) 
  RETURNS TABLE (
    country_name VARCHAR,
    pop INTEGER,
    density INTEGER,
    land_area INTEGER
  ) 
  LANGUAGE plpgsql
AS $$
BEGIN
  RETURN query
    SELECT
      country.country_name,
      country.pop,
      country.density,
      country.land_area
    FROM
      country
    WHERE
      country.country_name = country_choice;
END; $$;


DROP FUNCTION country_infos (country_choice VARCHAR);


SELECT * FROM country_infos ('France');