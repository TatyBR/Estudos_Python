
{{ config(materialized='view') }}

-- definindo a CTE
-- dentro das chaves está referenciando source.yml e apontando para o arquivo csv
WITH source AS (
    -- source() = "vou buscar de uma tabela raw"
    SELECT * FROM {{source('raw', 'raw_pedidos')}}
),

-- realizando algumas tratativas
-- trim() tira espaços do início e do começo
-- :: convertendo os tipos
RENAMED AS (
    SELECT
         -- Chaves
         pedido_id,
         cliente_id,
         produto_id,

         -- Métricas
         quantidade:: integer                               AS quantidade,
         preco_unitario:: numeric(10,2)                     AS preco_unitario,
         (quantidade*preco_unitario):: numeric(10,2)        AS valor_total,

         -- Status
         lower(trim(status))                                AS status,

         -- Flags úteis para análises
         CASE WHEN lower(trim(status)) = 'cancelado'
              THEN true ELSE false END                      AS is_cancelado,

         CASE WHEN lower(trim(status)) = 'entregue'
              THEN true ELSE false END                      AS is_entregue,
        
        -- Datas
        data_pedido:: DATE                                  AS data_pedido,
        data_entrega:: DATE                                 AS data_entrega,
       
       -- Tempo de entrega em dias (nulo se ainda não entregue)
        CASE WHEN data_entrega is not null
             THEN (data_entrega::date - data_pedido::date)
        END                                                 AS dias_para_entrega,

        -- Campos de auditoria de tempo
        extract(year FROM data_pedido)                      AS ano_pedido,
        extract(month FROM data_pedido)                     AS mes_pedido

    FROM source
)

SELECT * FROM renamed