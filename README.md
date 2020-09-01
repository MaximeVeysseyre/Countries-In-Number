# Countries-In-Number

## **Description**

Projet individuel "Les pays en chiffres".

Utilisation obligatoire de PostGreSQL ainsi que du SaaS ElephantSQL. 
Interdiction de l'utilisation de Python.

Récolte d'informations basiques sur les pays ainsi que manipulation des données.


## **Pré-requis**

1. Création d'un compte ElephantSQL.
2. Création d'une instance au sein d'ElephantSQL.
3. L'ensemble du code devra être inséré au sein du "Browser" d'ElephantSQL.


## **Installation**

### Création de la table "country"

``` 
CREATE TABLE IF NOT EXISTS "country"
(
country_name VARCHAR PRIMARY KEY,
pop INTEGER NOT NULL,
density INTEGER NOT NULL,
land_area INTEGER NOT NULL,
insertion_date TIMESTAMP DEFAULT NOW()
); 
```

### Insertion des données dans la table "country"

Se rendre dans l'onglet "Backup" puis "Upload backup".
Sélectionner le fichier "country_data.sql" afin de remplir la table "country" précédemment créée.


### Création d'une fonction SQL "country_infos"

``` 
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
country.land_area,
country.insertion_date
FROM
country
WHERE
country.country_name = country_choice;
END; $$; 
```


### Création d'une procédure SQL "fake_country"

``` 
CREATE PROCEDURE fake_country (
IN fake_country_name VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
INSERT INTO country (country_name, pop, density, land_area) VALUES (fake_country_name, 10000000 * RANDOM(), 1000 * RANDOM(), 10000000 * RANDOM());
END; $$; 
```


### Création d'une fonction SQL "add_insertion_date"

``` 
CREATE FUNCTION add_insertion_date()
RETURNS trigger 
LANGUAGE plpgsql
AS $$
BEGIN
NEW.insertion_date := current_timestamp;
RETURN NEW;
END; $$; 
```


### Création d'un trigger "insertion_date"

``` 
CREATE TRIGGER trigger_insertion_date
BEFORE INSERT OR UPDATE
ON country
FOR EACH ROW
EXECUTE FUNCTION add_insertion_date(); 
```


### Création d'une fonction SQL "density_slice"

``` 
CREATE FUNCTION density_slice ()
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
END AS "density_slice"
FROM country
ORDER BY density_slice;
END; $$; 
```


## **Utilisation**



## **Auteur**



