-- mart/dim_produtos.sql
-- Dimensão de produtos para análise
-- Materialização: table

{{ config(materialized='table') }}

WITH produtos AS (
     SELECT * FROM {{ ref('stg_produtos') }}
),

pedidos AS (
     SELECT * FROM {{ ref('stg_pedidos') }}
),

metricas_produtos AS (
     SELECT 
          produto_id,
          count(pedido_id)                  AS total_pedidos,
          sum(CASE WHEN NOT is_cancelado
              THEN quantidade ELSE 0 end)   AS unidades_vendidas,
          sum(CASE WHEN NOT is_cancelado
              THEN valor_total ELSE 0 end)  AS receita_total,
          round(avg(dias_para_entrega), 1)  AS media_dias_entrega
     FROM pedidos
     GROUP BY 1
),

final AS (
      SELECT
           p.produto_id,
           p.nome_produto,
           p.categoria,
           p.preco,
           p.estoque,
           p.ativo,
           p.faixa_preco,

           coalesce(m.total_pedidos,0)          AS total_pedidos,
           coalesce(m.unidades_vendidas,0)      AS unidades_vendidas,
           coalesce(m.receita_total,0)          AS receita_total,
           m.media_dias_entrega
     
     FROM produtos p
     LEFT JOIN metricas_produtos m using (produto_id)
)

SELECT * FROM final