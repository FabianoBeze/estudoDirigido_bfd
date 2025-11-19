-- Apaga as tabelas existentes para garantir um ambiente limpo
-- A ordem é importante por causa das chaves estrangeiras
DROP TABLE IF EXISTS garantia;
DROP TABLE IF EXISTS equipamento;
DROP TABLE IF EXISTS loja;
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS documentos;

-- Tabela para armazenar as lojas
CREATE TABLE loja (
    id_loja SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cnpj VARCHAR(18) UNIQUE, -- Formato: XX.XXX.XXX/XXXX-XX
    endereco VARCHAR(255),
    telefone VARCHAR(20) -- Formato: +XX (XX) XXXXX-XXXX
);

-- Tabela para armazenar os equipamentos
CREATE TABLE equipamento (
    id_equipamento SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco NUMERIC(10, 2) NOT NULL,
    data_venda DATE NOT NULL,
    id_loja INTEGER NOT NULL,
    CONSTRAINT fk_loja
        FOREIGN KEY(id_loja) 
        REFERENCES loja(id_loja)
        ON DELETE RESTRICT
);

-- Tabela para armazenar as garantias dos equipamentos
CREATE TABLE garantia (
    id_garantia SERIAL PRIMARY KEY,
    data_inicio DATE,
    data_fim DATE NOT NULL,
    tipo VARCHAR(50), -- Ex: 'Padrão', 'Estendida'
    id_equipamento INTEGER NOT NULL UNIQUE,
    CONSTRAINT fk_equipamento
        FOREIGN KEY(id_equipamento) 
        REFERENCES equipamento(id_equipamento)
        ON DELETE CASCADE
);

-- Tabela para armazenar os documentos (notas fiscais)
CREATE TABLE documentos (
    id_doc SERIAL PRIMARY KEY,
    numero_nota VARCHAR(255) NOT NULL
);

-- Tabela para armazenar os usuários do sistema
CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    cpf_usuario VARCHAR(14) NOT NULL UNIQUE -- Formato: XXX.XXX.XXX-XX
);

