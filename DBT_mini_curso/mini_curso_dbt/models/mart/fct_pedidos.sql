-- mart/fct_pedidos.sql
-- Fato central do pipeline: todos os pedidos enriquecidos
-- Materialização: table (tabela principal para BI e relatórios)

WITH pedidos AS (
    SELECT * FROM {{ ref('stg_pedidos')}}
),

cliente AS (
    SELECT 
         cliente_id,
         nome_cliente,
         cidade,
         estado,
         segmento_valor

    FROM {{ ref('dim_clientes')}}
),

produtos AS (
    SELECT 
         produto_id,
         nome_produto,
         categoria,
         faixa_preco
    
    FROM {{ ref('dim_produtos')}}
),

final AS (
    SELECT
        -- Chaves
        p.pedido_id,
        p.cliente_id,
        p.produto_id,

        -- Dados do cliente(denormalizado para facilitar consultas no BI)
        c.nome_cliente,
        c.cidade,
        c.estado,
        c.segmento_valor            AS segmento_cliente,

        -- Dados do produto
        pr.nome_produto,
        pr.categoria,
        pr.faixa_preco,

        -- Métricas do pedido
        p.quantidade,
        p.preco_unitario,
        p.valor_total,
        p.status,
        p.is_entregue,
        p.is_cancelado,
        p.dias_para_entrega,

        -- Datas
        p.data_pedido,
        p.data_entrega,
        p.ano_pedido,
        p.mes_pedido,

        -- Receita líquida (zero se cancelado)
        CASE WHEN p.is_cancelado THEN 0
             ELSE p.valor_total
        END                 AS receita_liquida
    
    FROM pedidos p
    LEFT JOIN cliente c using(cliente_id)
    LEFT JOIN produtos pr using(produto_id)
)

SELECT * FROM final