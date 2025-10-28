DROP TABLE IF EXISTS garantia;
DROP TABLE IF EXISTS equipamento;
DROP TABLE IF EXISTS loja;

-- Tabela para armazenar as lojas
CREATE TABLE loja (
    id_loja SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(255)
);

-- Tabela para armazenar os equipamentos
CREATE TABLE equipamento (
    id_equipamento SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    data_compra DATE NOT NULL,
    preco NUMERIC(10, 2) NOT NULL,
    id_loja INTEGER NOT NULL,
    CONSTRAINT fk_loja
        FOREIGN KEY(id_loja) 
        REFERENCES loja(id_loja)
        ON DELETE RESTRICT
);

-- Tabela para armazenar as garantias dos equipamentos
CREATE TABLE garantia (
    id_garantia SERIAL PRIMARY KEY,
    id_equipamento INTEGER NOT NULL UNIQUE,
    data_vencimento DATE NOT NULL,
    documento_fiscal_path VARCHAR(255),
    seguradora VARCHAR(100),
    CONSTRAINT fk_equipamento
        FOREIGN KEY(id_equipamento) 
        REFERENCES equipamento(id_equipamento)
        ON DELETE CASCADE
);