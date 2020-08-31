CREATE FUNCTION add_insertion_date()
RETURNS trigger 
LANGUAGE plpgsql
AS $$
BEGIN
NEW.insertion_date := current_timestamp;
RETURN NEW;
END; $$;


CREATE TRIGGER trigger_insertion_date
BEFORE INSERT OR UPDATE
ON country
FOR EACH ROW
EXECUTE FUNCTION add_insertion_date();


