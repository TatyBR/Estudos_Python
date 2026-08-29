-- Teste customizado: receita_liquida nunca pode ser negativa em pedidos não cancelados
-- O teste FALHA se retornar qualquer linha

select
    pedido_id,
    receita_liquida,
    is_cancelado
from {{ ref('fct_pedidos') }}
where receita_liquida < 0
  and not is_cancelado