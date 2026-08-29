-- mart/fct_pedidos_incremental.sql
-- Versão incremental da tabela de fatos
-- Usar quando a tabela for muito grande (milhões de linhas)
-- Incremental: só processa registros novos/alterados.

{{
    config(
        materialized='incremental',
        unique_key='pedido_id', 
        on_schema_change='fail'
    )
}}

WITH pedidos AS (

    SELECT * FROM {{ ref('stg_pedidos')}}

    -- Bloco coração do incremental:
    -- na primeira execução, traz TUDO
    -- nas seguintes, só o que é novo (criado/ alterado após o último run)
    {% if is_incremental() %}
        WHERE data_pedido > (
            SELECT max(data_pedido) FROM {{ this }}
        )
    {% endif %}
),

cliente AS (

    SELECT cliente_id, nome_cliente, cidade, estado, segmento_valor
      FROM {{ ref('dim_clientes') }} 
),

produtos AS (

    SELECT produto_id, nome_produto, categoria, faixa_preco
    FROM {{ ref('dim_produtos') }}
),

final as (

    SELECT 
          p.pedido_id,
          p.cliente_id,
          p.produto_id,
          c.nome_cliente,
          c.cidade,
          c.estado,
          c.segmento_valor          AS segmento_cliente,
          pr.nome_produto,
          pr.categoria,
          pr.faixa_preco,
          p.quantidade,
          p.preco_unitario,
          p.valor_total,
          p.status,
          p.is_entregue,
          p.is_cancelado,
          p.dias_para_entrega,
          p.data_pedido,
          p.data_entrega,
          p.ano_pedido,
          p.mes_pedido,
          CASE WHEN p.is_cancelado 
               THEN 0 ELSE p.valor_total 
               END                   AS receita_liquida
    FROM pedidos p
    LEFT JOIN cliente c using(cliente_id)
    LEFT JOIN produtos pr using(produto_id)
)

SELECT * FROM final
