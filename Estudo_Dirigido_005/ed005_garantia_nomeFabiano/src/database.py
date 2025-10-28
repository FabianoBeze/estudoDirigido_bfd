import psycopg2

class Database:
    def __init__(self, dbname="app_garantia", user="postgres", password="sua_senha", host="localhost", port="5432"):
        try:
            self.conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
        except psycopg2.OperationalError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.conn = None

    def executar_consulta(self, query: str, params=None):
        if not self.conn:
            print("Nenhuma conexão com o banco de dados.")
            return None
        
        try:
            with self.conn.cursor() as cur:
                cur.execute(query, params)
                if cur.description:
                    return cur.fetchall()
                else:
                    self.conn.commit()
                    return None
        except Exception as e:
            print(f"Erro na consulta: {e}")
            self.conn.rollback()
            return None

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            print("Conexão com o banco de dados fechada.")