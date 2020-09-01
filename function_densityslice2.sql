CREATE FUNCTION density_slice_2 (country_choice TEXT)
RETURNS TABLE (
country_name VARCHAR,
density_slice TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
RETURN query
SELECT country.country_name,
CASE 
WHEN country.density < 500 THEN 'Slice 1'
WHEN country.density < 1000 THEN 'Slice 2'
WHEN country.density < 1500 THEN 'Slice 3'
ELSE 'Slice 4' 
END AS "density slice"
FROM country
WHERE country.country_name = country_choice;
END; $$;


SELECT * FROM density_slice_2 ('France');