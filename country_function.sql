CREATE FUNCTION
    country_function ( [ [ modearg ] [ nomarg ] typearg [, ...] ] )
    [ RETURNS type_ret ]
  { LANGUAGE nomlang
    | IMMUTABLE | STABLE | VOLATILE
    | CALLED ON NULL INPUT | RETURNS NULL ON NULL INPUT | STRICT
    | [EXTERNAL] SECURITY INVOKER | [EXTERNAL] SECURITY DEFINER
    | COST cout_execution
    | ROWS nb_lignes_resultat
    | SET parametre { TO value | = value | FROM CURRENT }
    | AS 'definition'
    | AS 'fichier_obj', 'symbole_lien'
  } ...
    [ WITH ( attribut [, ...] ) ]


create function country_infos()
return table as $infos$
declare
infos table;
begin
select 