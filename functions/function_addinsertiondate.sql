CREATE FUNCTION add_insertion_date()
RETURNS trigger 
LANGUAGE plpgsql
AS $$
BEGIN
NEW.insertion_date := current_timestamp;
RETURN NEW;
END; $$;