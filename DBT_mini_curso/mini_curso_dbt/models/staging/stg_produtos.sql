-- staging/stg_produtos.sql
-- Objetivo: limpar e padronizar os dados brutos de produtos
-- Materialização: view

{{ config(materialized='view') }}

WITH source AS (
    SELECT * FROM {{ source('raw', 'raw_produtos') }}
),

RENAMED AS (
     SELECT 
          -- Chaves
          produto_id,

          -- Campos de texto
          TRIM(nome)                        AS nome_produto,
          TRIM(categoria)                   AS categoria,

          -- Numéricos
          preco::numeric(10, 2)             AS preco,
          estoque::integer                  AS estoque,

          -- Booleanos
          ativo::boolean                    AS ativo,

          -- Classificação por faixa de preco
          CASE
              WHEN preco < 100 THEN 'baixo'
              WHEN preco < 500 THEN 'medio'
              WHEN preco < 1500 THEN 'alto'
              ELSE 'premium'
              END AS faixa_preco
     FROM source
)

SELECT * FROM RENAMED