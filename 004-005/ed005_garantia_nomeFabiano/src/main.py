from database import Database
from models.equipamento import Equipamento
from models.garantia import Garantia
from models.loja import Loja
from models.usuarios import Usuarios
from models.documentos import Documentos

def show_equipments_and_warranties(db: Database):
    """Busca e exibe equipamentos e suas garantias."""
    print("\n--- Equipamentos e Suas Garantias ---")
    
    query = """
    SELECT 
        e.id_equipamento, e.nome, e.preco, e.data_venda, e.id_loja,
        g.id_garantia, g.data_inicio, g.data_fim, g.tipo
    FROM equipamento e
    JOIN garantia g ON e.id_equipamento = g.id_equipamento;
    """
    
    resultados = db.executar_consulta(query)
    
    if resultados:
        for row in resultados:
            equip = Equipamento(row[0], row[1], row[2], row[3], row[4])
            garantia = Garantia(row[5], equip.id_equipamento, row[6], row[7], row[8])
            
            print(equip)
            print(garantia)
            print("-" * 20)

def show_lojas(db: Database):
    """Busca e exibe as lojas."""
    print("\n--- Lojas Cadastradas ---")
    query = "SELECT id_loja, nome, cnpj, endereco, telefone FROM loja;"
    resultados = db.executar_consulta(query)
    if resultados:
        for row in resultados:
            loja = Loja(row[0], row[1], row[2], row[3], row[4])
            print(loja)
            print("-" * 20)

def show_usuarios(db: Database):
    """Busca e exibe os usuários."""
    print("\n--- Usuários do Sistema ---")
    query = "SELECT id_usuario, cpf_usuario FROM usuarios;"
    resultados = db.executar_consulta(query)
    if resultados:
        for row in resultados:
            usuario = Usuarios(row[0], row[1])
            print(usuario)
            print("-" * 20)

def show_documentos(db: Database):
    """Busca e exibe os documentos."""
    print("\n--- Documentos (Notas Fiscais) ---")
    query = "SELECT id_doc, numero_nota FROM documentos;"
    resultados = db.executar_consulta(query)
    if resultados:
        for row in resultados:
            doc = Documentos(row[0], row[1])
            print(doc)
            print("-" * 20)

def main():

    db = Database(dbname="postgres", password="1234")
    if not db.conn:
        return

    show_lojas(db)
    show_equipments_and_warranties(db)
    show_usuarios(db)
    show_documentos(db)

    db.fechar_conexao()

if __name__ == "__main__":
    main()