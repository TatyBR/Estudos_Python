
{{ config(materialized='view') }}

-- definindo a CTE
-- dentro das chaves está referenciando source.yml e apontando para o arquivo csv
WITH source AS (
    -- source() = "vou buscar de uma tabela raw"
    SELECT * FROM {{source('raw', 'raw_clientes')}}
),

-- realizando algumas tratativas
-- trim() tira espaços do início e do começo
-- :: convertendo os tipos
RENAMED AS (
    SELECT 
         cliente_id,
         trim(nome)             AS nome_cliente,
         lower(trim(email))     AS email,
         lower(trim(cidade))    AS cidade,
         upper(trim(estado))    AS estado,
         data_cadastro::date    AS data_cadastro,
         ativo:: boolean        AS ativo
    FROM source
)

SELECT * FROM renamed