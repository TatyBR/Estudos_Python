-- marts/dim_clientes.sql
-- dim_clientes se conecta nas tabelas/viems já prontas e na source como as stg

{{ config(materialized='table') }}

WITH clientes AS (
     SELECT * FROM {{ ref('stg_clientes')}}
),

pedidos AS (
     SELECT * FROM {{ ref('stg_pedidos')}}
),

metricas_clientes AS (

        SELECT
            cliente_id,
            count(pedido_id)                            AS total_pedidos,
            count(CASE WHEN is_entregue then 1 end)     AS pedidos_entregues,
            count(CASE WHEN is_cancelado then 1 end)    AS pedidos_cancelados,
            sum(CASE WHEN NOT is_cancelado
                     THEN valor_total ELSE 0 end)       AS valor_total_gasto,
            min(data_pedido)                            AS primeiro_pedido,
            max(data_pedido)                            AS ultimo_pedido,
            round(avg(CASE WHEN is_entregue
                      THEN dias_para_entrega END),1)    AS media_dias_entrega
            
            FROM pedidos
            GROUP BY 1
),

final as (
    SELECT
        c.cliente_id,
        c.nome_cliente,
        c.email,
        c.cidade,
        c.estado,
        c.data_cadastro,
        c.ativo,

        -- Métricas de compra
        coalesce(m.total_pedidos,0)         AS total_pedidos,
        coalesce(m.pedidos_entregues,0)     AS pedidos_entregues,
        coalesce(m.pedidos_cancelados,0)    AS pedidos_cancelados,
        coalesce(m.valor_total_gasto,0)     AS valor_total_gasto,
        m.primeiro_pedido,
        m.ultimo_pedido,
        m.media_dias_entrega,

        -- Segmentação automática por valor gasto
        CASE
            WHEN coalesce(m.valor_total_gasto,0) = 0    THEN 'sem compras'
            WHEN coalesce(m.valor_total_gasto,0) < 500    THEN 'bronze'
            WHEN coalesce(m.valor_total_gasto,0) < 2000    THEN 'prata'
            WHEN coalesce(m.valor_total_gasto,0) < 5000    THEN 'ouro'
            ELSE 'diamante'
            END AS segmento_valor
    FROM clientes c
    LEFT JOIN metricas_clientes m using(cliente_id)
)

SELECT * FROM final