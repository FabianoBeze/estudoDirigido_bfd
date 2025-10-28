from database import Database
from models.equipamento import Equipamento
from models.garantia import Garantia
from models.loja import Loja

def main():
    db = Database(password="1234") # Lembre-se de usar sua senha correta
    if not db.conn:
        return

    print("--- Equipamentos e suas Garantias ---")
    
    query = """
    SELECT 
        e.id_equipamento, e.nome, e.descricao, e.data_compra, e.preco, e.id_loja,
        g.id_garantia, g.data_vencimento, g.documento_fiscal_path, g.seguradora
    FROM equipamento e
    JOIN garantia g ON e.id_equipamento = g.id_equipamento;
    """
    
    resultados = db.executar_consulta(query)
    
    if resultados:
        for row in resultados:
            equip = Equipamento(row[0], row[1], row[2], row[3], row[4], row[5])
            garantia = Garantia(row[6], equip.id_equipamento, row[7], row[8], row[9])
            
            print(equip)
            print(garantia)
            print("-" * 20)

    db.fechar_conexao()

if __name__ == "__main__":
    main()