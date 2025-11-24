-- Inner Join
-- Exemplo 1: fazer uma consulta à tabela de pedidos que retorne as colunas da loja, Data_Venda e Receita_Venda
select Loja, Data_Venda, Receita_Venda, Gerente, Endereco, Num_Funcionarios
from pedidos
inner join lojas on pedidos.ID_Loja = lojas.ID_loja;

-- Exemplo 2: Criar um agrupamento que mostre o total de receita da tabela 'pedidos' por loja

Select Loja, SUM(Receita_Venda) as 'Receita Total'
from pedidos
inner join lojas on pedidos.ID_Loja = lojas.ID_loja
group by loja;
