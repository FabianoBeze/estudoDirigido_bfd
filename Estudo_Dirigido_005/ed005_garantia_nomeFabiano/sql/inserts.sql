-- Inserir dados na tabela loja
INSERT INTO loja (nome, cnpj, endereco, telefone) VALUES
('Loja de Eletrônicos A', '11.111.111/0001-11', 'Rua das Inovações, 123', '+55 (11) 91111-1111'),
('Magazine B', '22.222.222/0001-22', 'Avenida da Tecnologia, 456', '+55 (21) 92222-2222'),
('Ponto C', '33.333.333/0001-33', 'Praça dos Gadgets, 789', '+55 (31) 93333-3333');

-- Inserir dados na tabela equipamento
-- Equipamentos da Loja A
INSERT INTO equipamento (nome, preco, data_venda, id_loja) VALUES
('Notebook Gamer', 5500.00, '2023-01-15', 1),
('Smartphone XYZ', 2500.00, '2023-03-20', 1);

-- Equipamentos da Loja B
INSERT INTO equipamento (nome, preco, data_venda, id_loja) VALUES
('Smart TV 55"', 3200.00, '2022-11-05', 2),
('Fone de Ouvido Bluetooth', 450.00, '2023-08-01', 2);

-- Equipamentos da Loja C
INSERT INTO equipamento (nome, preco, data_venda, id_loja) VALUES
('Tablet Pro', 1800.00, '2023-05-10', 3);

-- Inserir dados na tabela garantia
-- Garantias dos equipamentos
INSERT INTO garantia (id_equipamento, data_inicio, data_fim, tipo) VALUES
(1, '2023-01-15', '2024-01-15', 'Padrão'),
(2, '2023-03-20', '2025-03-20', 'Estendida'),
(3, '2022-11-05', '2023-11-05', 'Padrão'),
(4, '2023-08-01', '2024-08-01', 'Padrão'),
(5, '2023-05-10', '2025-05-10', 'Estendida');

-- Inserir dados na tabela documentos
INSERT INTO documentos (numero_nota) VALUES
('NF-001-2023'),
('NF-002-2023'),
('NF-003-2022'),
('NF-004-2023'),
('NF-005-2023');

-- Inserir dados na tabela usuarios
INSERT INTO usuarios (cpf_usuario) VALUES
('111.111.111-11'),
('222.222.222-22'),
('333.333.333-33');