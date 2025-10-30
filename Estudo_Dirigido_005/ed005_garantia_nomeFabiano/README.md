# ED005 - Sistema de Controle de Garantia de Equipamentos

Este projeto é um estudo dirigido para a construção de um sistema de controle de garantias de equipamentos, utilizando Python e PostgreSQL. O sistema foi reestruturado para incluir novas entidades e refinar as existentes.

## Estrutura do Banco de Dados

ed005_garantia_nomeFabiano/
│
├── sql/
│   ├── schema.sql          
│   ├── inserts.sql         
│
├── src/
│   ├── main.py             
│   ├── database.py        
│   ├── models/
│   │   ├── equipamento.py
│   │   ├── garantia.py
│   │   ├── loja.py
│   │   ├── documentos.py
│   │   ├── usuarios.py
├── prints/
│   ├── modelo_logico.png           # Diagrama lógico do banco
│   ├── consultas_dbeaver.png       # Resultado da execução no DBeaver
│   ├── execucao_terminal.png       # Evidência de execução no terminal
│
└── README.md

O banco de dados utilizado é o `postgres` (padrão), que agora é composto por cinco tabelas:

-   `loja`: Armazena informações sobre as lojas (incluindo `cnpj` e `telefone`).
-   `equipamento`: Contém detalhes sobre cada equipamento (com `data_venda` em vez de `data_compra`).
-   `garantia`: Guarda as informações de garantia (com `data_inicio`, `data_fim` e `tipo`).
-   `documentos`: Armazena o número das notas fiscais associadas.
-   `usuarios`: Mantém um registro dos usuários do sistema (com `cpf_usuario`).

### Relações

-   **loja (1) -> (N) equipamento**: Uma loja pode ter vários equipamentos. A restrição `ON DELETE RESTRICT` impede que uma loja seja deletada se houver equipamentos associados a ela.
-   **equipamento (1) -> (1) garantia**: Cada equipamento possui uma única garantia. A restrição `ON DELETE CASCADE` garante que, ao deletar um equipamento, sua garantia correspondente também seja removida.

*(As tabelas `documentos` e `usuarios` estão atualmente independentes, mas prontas para serem relacionadas no futuro).*

### Modelo Lógico

(Aqui você pode inserir uma imagem atualizada do seu modelo lógico, se desejar).

## Consultas SQL Atualizadas

As consultas foram ajustadas para a nova estrutura do banco de dados.

### 1. Equipamentos por Loja

```sql
SELECT
    l.nome AS nome_loja,
    e.nome AS nome_equipamento,
    e.preco,
    e.data_venda
FROM loja l
JOIN equipamento e ON l.id_loja = e.id_loja
ORDER BY l.nome, e.nome;
```

### 2. Garantias Vencendo em 90 Dias

```sql
SELECT
    e.nome AS nome_equipamento,
    g.data_fim,
    g.tipo
FROM garantia g
JOIN equipamento e ON g.id_equipamento = e.id_equipamento
WHERE g.data_fim BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '90 days'
ORDER BY g.data_fim;
```

### 3. Loja com Mais Garantias Vencidas

```sql
SELECT
    l.nome AS nome_loja,
    COUNT(g.id_garantia) AS total_garantias_vencidas
FROM loja l
JOIN equipamento e ON l.id_loja = e.id_loja
JOIN garantia g ON e.id_equipamento = g.id_equipamento
WHERE g.data_fim < CURRENT_DATE
GROUP BY l.nome
ORDER BY total_garantias_vencidas DESC
LIMIT 1;
```

## Execução do Projeto

Para executar a aplicação, certifique-se de ter o Python 3 e o PostgreSQL instalados.

1.  **Conecte-se ao banco de dados `postgres`** no seu cliente de banco de dados (DBeaver, etc.).
2.  **Execute o script `sql/schema.sql`**. Isso irá apagar as tabelas antigas (se existirem) e criar a nova estrutura.
3.  **Execute o script `sql/inserts.sql`** para popular o banco de dados com dados de exemplo.
4.  Instale a dependência `psycopg2`, caso ainda não a tenha:
    ```bash
    pip install psycopg2-binary
    ```
5.  No arquivo `src/main.py`, certifique-se de que a senha do banco de dados na linha `db = Database(dbname="postgres", password="SUA_SENHA")` está correta.
6.  Execute o programa a partir da raiz do projeto:
    ```bash
    python src/main.py
    ```

## Reflexão Pessoal

Neste estudo dirigido, aprofundei meus conhecimentos em modelagem de banco de dados relacional com PostgreSQL e na aplicação dos conceitos de Programação Orientada a Objetos (POO) em Python.

Um dos principais desafios foi a depuração da conexão com o banco de dados, que revelou a importância de garantir que os ambientes de desenvolvimento (o cliente de banco de dados) e de execução (o script Python) estejam configurados para acessar exatamente o mesmo banco de dados. A reestruturação das tabelas e a atualização dos modelos de dados e consultas SQL reforçaram a necessidade de manter a consistência entre a camada de persistência e a camada de aplicação.

Este exercício foi fundamental para conectar a teoria da modelagem de dados com a prática de desenvolvimento e, crucialmente, com o processo de diagnóstico e resolução de problemas de configuração, uma habilidade essencial para qualquer desenvolvedor.

## Créditos

**Autor:** *Fabiano_Bezerra*  
**Disciplina:** Engenharia de Dados / Banco de Dados  
**Instituição:** *Curso_BFD_polo_itaipuaçu_maricá*  
**Ferramentas:** DBeaver, MySQL, Draw.io