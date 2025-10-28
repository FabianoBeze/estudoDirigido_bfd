-- Inserir dados na tabela loja
INSERT INTO loja (nome, endereco) VALUES
('Loja de Eletrônicos A', 'Rua das Inovações, 123'),
('Magazine B', 'Avenida da Tecnologia, 456'),
('Ponto C', 'Praça dos Gadgets, 789');

-- Inserir dados na tabela equipamento
-- Equipamentos da Loja A
INSERT INTO equipamento (nome, descricao, data_compra, preco, id_loja) VALUES
('Notebook Gamer', 'Notebook de alta performance para jogos', '2023-01-15', 5500.00, 1),
('Smartphone XYZ', 'Smartphone com câmera de 108MP', '2023-03-20', 2500.00, 1);

-- Equipamentos da Loja B
INSERT INTO equipamento (nome, descricao, data_compra, preco, id_loja) VALUES
('Smart TV 55"', 'Televisão com resolução 4K e HDR', '2022-11-05', 3200.00, 2),
('Fone de Ouvido Bluetooth', 'Fone com cancelamento de ruído', '2023-08-01', 450.00, 2);

-- Equipamentos da Loja C
INSERT INTO equipamento (nome, descricao, data_compra, preco, id_loja) VALUES
('Tablet Pro', 'Tablet para produtividade e desenho', '2023-05-10', 1800.00, 3);

-- Inserir dados na tabela garantia
-- Garantias dos equipamentos
INSERT INTO garantia (id_equipamento, data_vencimento, documento_fiscal_path, seguradora) VALUES
(1, '2024-01-15', '/docs/nf_notebook.pdf', 'Seguradora Alfa'),
(2, '2024-03-20', '/docs/nf_smartphone.pdf', NULL),
(3, '2023-11-05', '/docs/nf_tv.pdf', 'Seguradora Beta'),
(4, '2024-08-01', '/docs/nf_fone.pdf', NULL),
(5, '2024-05-10', '/docs/nf_tablet.pdf', 'Seguradora Alfa');