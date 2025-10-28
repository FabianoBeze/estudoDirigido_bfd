# ED005 - Sistema de Controle de Garantia de Equipamentos

Este projeto é um estudo dirigido para a construção de um sistema de controle de garantias de equipamentos, utilizando Python e PostgreSQL.

## Estrutura do Banco de Dados

O banco de dados `app_garantia` é composto por três tabelas principais:

- `loja`: Armazena informações sobre as lojas onde os equipamentos foram adquiridos.
- `equipamento`: Contém detalhes sobre cada equipamento.
- `garantia`: Guarda as informações de garantia de cada equipamento.

### Relações

- **loja (1) -> (N) equipamento**: Uma loja pode ter vários equipamentos, mas cada equipamento pertence a uma única loja. A chave estrangeira `id_loja` na tabela `equipamento` estabelece essa relação. Foi utilizada a restrição `ON DELETE RESTRICT` para impedir que uma loja seja deletada se houver equipamentos associados a ela.
- **equipamento (1) -> (1) garantia**: Cada equipamento possui uma única garantia. A chave estrangeiga `id_equipamento` na tabela `garantia` é única para garantir essa relação. Foi utilizada a restrição `ON DELETE CASCADE` para que, ao deletar um equipamento, sua garantia correspondente também seja removida.

### Modelo Lógico

(Aqui você deve inserir a imagem do seu modelo lógico: `prints/modelo_logico.png`)

## Consultas SQL

A seguir estão as consultas SQL desenvolvidas para análise de dados.

### 1. Equipamentos por Loja

Lista todos os equipamentos agrupados por loja.

```sql
SELECT 
    l.nome AS nome_loja,
    e.nome AS nome_equipamento,
    e.descricao
FROM loja l
JOIN equipamento e ON l.id_loja = e.id_loja
ORDER BY l.nome, e.nome;
```

### 2. Garantias Vencendo em 30 Dias

Mostra as garantias que expiram nos próximos 30 dias a partir da data atual.

```sql
SELECT 
    e.nome AS nome_equipamento,
    g.data_vencimento
FROM garantia g
JOIN equipamento e ON g.id_equipamento = e.id_equipamento
WHERE g.data_vencimento BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '30 days'
ORDER BY g.data_vencimento;
```

### 3. Loja com Mais Garantias Vencidas

Identifica a loja com o maior número de equipamentos cuja garantia já expirou.

```sql
SELECT 
    l.nome AS nome_loja,
    COUNT(g.id_garantia) AS total_garantias_vencidas
FROM loja l
JOIN equipamento e ON l.id_loja = e.id_loja
JOIN garantia g ON e.id_equipamento = g.id_equipamento
WHERE g.data_vencimento < CURRENT_DATE
GROUP BY l.nome
ORDER BY total_garantias_vencidas DESC
LIMIT 1;
```

### 4. Tempo Médio de Garantia por Loja

Calcula a duração média do período de garantia (em dias) para os equipamentos de cada loja.

```sql
SELECT 
    l.nome AS nome_loja,
    AVG(g.data_vencimento - e.data_compra) AS tempo_medio_garantia_dias
FROM loja l
JOIN equipamento e ON l.id_loja = e.id_loja
JOIN garantia g ON e.id_equipamento = g.id_equipamento
GROUP BY l.nome
ORDER BY l.nome;
```

## Execução do Projeto

Para executar a aplicação, certifique-se de ter o Python 3 e o PostgreSQL instalados.

1.  Crie o banco de dados `app_garantia`.
2.  Execute os scripts `sql/schema.sql` e `sql/inserts.sql`.
3.  Instale a dependência `psycopg2`:
    ```bash
    pip install psycopg2-binary
    ```
4.  Atualize a senha do banco de dados nos arquivos `src/database.py` e `src/main.py`.
5.  Execute o programa:
    ```bash
    python src/main.py
    ```

## Reflexão Pessoal

Neste estudo dirigido, aprofundei meus conhecimentos em modelagem de banco de dados relacional com PostgreSQL e na aplicação dos conceitos de Programação Orientada a Objetos (POO) em Python.

Um dos principais desafios foi traduzir o modelo lógico para o modelo físico, garantindo a integridade dos dados com o uso correto de restrições como `FOREIGN KEY`, `ON DELETE CASCADE` e `ON DELETE RESTRICT`. A implementação da camada de persistência com `psycopg2` exigiu atenção ao tratamento de exceções e ao gerenciamento de conexões para evitar vazamento de recursos.

Este exercício foi fundamental para conectar a teoria da modelagem de dados com a prática de desenvolvimento de software, mostrando como as tabelas de um banco de dados podem ser representadas como classes em uma aplicação, facilitando a manipulação e a lógica de negócio. O aprendizado adquirido aqui será diretamente aplicável no projeto integrador, especialmente na construção das camadas de modelo e controle da arquitetura MVC.