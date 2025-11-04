-- Comandos de MySql: DML (Manipulação de dados) | DDL (Acesso e adm de dados)
-- SUM, COUNT, AVG, MIN E MAX;
-- SUM



-- Quantidade de produtos por marca

SELECT * FROM produtos;

SELECT Marca_Produto,
COUNT(Marca_Produto) AS 'Qtd Produtos' FROM produtos
group by Marca_Produto;


-- Exemplo 2: Criar um agrupamento que mostra a quantidade de clientes por escolaridade.

select * from clientes;

select Escolaridade, count(Escolaridade) as 'Qtd Clientes' 
from clientes 
group by Escolaridade;

-- Exemplo 3: Criar um agrupamento quie nmostre o total de receita da tabela 'pedidos' por ID da loja

select * from pedidos;
select * from lojas;

select ID_Loja, SUM(Receita_Venda) as 'Receita Total'
from pedidos
group by ID_Loja;


