CREATE TRIGGER trigger_insertion_date
BEFORE INSERT OR UPDATE
ON country
FOR EACH ROW
EXECUTE FUNCTION add_insertion_date();