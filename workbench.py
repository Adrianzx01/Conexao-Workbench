# Importação da bibliotecas do mysqlconnector e de erros
import mysql.connector
from mysql.connector import Error

# Criação da conexão com o workbench
print("--- Conexão Workbench ---")

db_config = {
    'host': 'localhost',
    'database': 'teste_bd',
    'user': 'root',
    'password': 'auew1234'
}

# Criação da função para estabelecer e retornar uma conexão com um banco de dados
def create_connection():
    print("... Conectando ...")
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("... Sucesso ...")
            return connection
    except Error as e:
        print(f"Falha ao se conectar ao Banco de Dados: {e}")
        return None
    return connection

# Criação da função para inserir um novo registro na tabela
def incluir_funcionario(connection, matricula, nome):
    cursor = connection.cursor()
    sql = "INSERT INTO Tb_funcionario (Matricula, Nome_Funcionario) VALUES (%s, %s)"
    valores = (matricula, nome)
    try:
        cursor.execute(sql, valores)
        connection.commit()
        print(f"[C] O Funcionário {nome} (Matrícula: {matricula}) foi incluído com sucesso.")
    except Error as e:
        print(f"[C] Erro ao incluir funcionário: {e}")
    finally:
        cursor.close()

# Criação da função para consultar a tabela de funcionários
def consultar_funcionarios(connection):
    cursor = connection.cursor()
    sql = "SELECT Matricula, Nome_Funcionario FROM Tb_funcionario"
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        print("\n[R] --- Lista de Funcionários ---")
        if registros:
            for matricula, nome in registros:
                print(f"Matrícula: {matricula:<5} | Nome: {nome}")
        else:
            print("Nenhum funcionário encontrado.")
        print("---------------------------------")
        return registros
    except Error as e:
        print(f"[R] Erro ao consultar funcionários: {e}")
    finally:
        cursor.close()

# Criação da função para alterar um funcionario
def alterar_funcionario(connection, matricula, novo_nome):
    cursor = connection.cursor()
    sql = "UPDATE Tb_funcionario SET Nome_Funcionario = %s WHERE Matricula = %s"
    valores = (novo_nome, matricula)
    try:
        cursor.execute(sql, valores)
        connection.commit()
        if cursor.rowcount > 0:
            print(f"[U] Nome do funcionário com Matrícula {matricula} alterado para '{novo_nome}'.")
        else:
            print(f"[U] Nenhum funcionário encontrado para alteração.")
    except Error as e:
        print(f"[U] Erro ao alterar funcionário: {e}")
    finally:
        cursor.close()

# Criação da função para excluir um funcionario
def excluir_funcionario(connection, matricula):
    cursor = connection.cursor()
    sql = "DELETE FROM Tb_funcionario WHERE Matricula = %s"
    valores = (matricula,)
    try:
        cursor.execute(sql, valores)
        connection.commit()
        if cursor.rowcount > 0:
            print(f"[D] O Funcionário com matrícula {matricula} foi excluído.")
        else:
            print(f"[D] Nenhum funcionário encontrado com Matrícula {matricula} para exclusão.")
    except Error as e:
        print(f"[D] Erro ao excluir funcionário: {e}")
    finally:
        cursor.close()

# Demonstração do CRUD
if __name__ == "__main__":
    conn = create_connection()
    
    if conn:
        print("\n--- DEMONSTRAÇÃO CRUD ---")
        
        #CREATE
        incluir_funcionario(conn, 102, "Adrian")
        incluir_funcionario(conn, 103, "Davi")
        incluir_funcionario(conn, 104, "Pedro")
        incluir_funcionario(conn, 105, "Yuri")
        incluir_funcionario(conn, 106, "Matheus")
        incluir_funcionario(conn, 107, "Houston")

        # 2. READ
        consultar_funcionarios(conn)

        # 3. UPDATE
        alterar_funcionario(conn, 107, "MODO BUDA")
        
        # 2. READ
        consultar_funcionarios(conn)

        # 4. DELETE
        excluir_funcionario(conn, 101)
        excluir_funcionario(conn, 102)
        excluir_funcionario(conn, 103)
        excluir_funcionario(conn, 104)
        excluir_funcionario(conn, 105)
        excluir_funcionario(conn, 106)
        excluir_funcionario(conn, 107)
        
        # 2. READ
        consultar_funcionarios(conn)

        # Fecha a conexão ao final
        conn.close()
        print("\nConexão encerrada.")