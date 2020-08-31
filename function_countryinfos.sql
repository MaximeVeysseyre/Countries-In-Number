CREATE FUNCTION country_infos (
  country_choice VARCHAR
) 
  RETURNS TABLE (
    country_name VARCHAR,
    pop INTEGER,
    density INTEGER,
    land_area INTEGER,
    insertion_date TIMESTAMP
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
      country.insertion_date
    FROM
      country
    WHERE
      country.country_name = country_choice;
END; $$;


SELECT * FROM country_infos ('France');


DROP FUNCTION country_infos (country_choice VARCHAR);