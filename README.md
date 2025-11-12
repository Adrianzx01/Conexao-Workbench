# Conexao-Workbench
📄 README.md
Conexão MySQL Workbench em Python
Este projeto demonstra a implementação das quatro operações básicas de banco de dados (CRUD - Create, Read, Update, Delete) usando Python e o conector oficial mysql.connector para interagir com um banco de dados MySQL (simulando um ambiente como o MySQL Workbench).

💻 Requisitos
Para executar este código, você precisará ter:

Python (Versão 3.x recomendada).

MySQL Server instalado e rodando (pode ser via MySQL Workbench, XAMPP, etc.).

Banco de Dados e Tabela configurados no MySQL com as seguintes especificações:

Database: teste_bd

Tabela: Tb_funcionario com as colunas Matricula (Primary Key, INT) e Nome_Funcionario (VARCHAR).

A biblioteca mysql.connector instalada.

Instalação da Biblioteca
Bash

pip install mysql-connector-python
⚙️ Configuração
A configuração da conexão está definida no dicionário db_config. Você deve ajustar os valores de host, database, user e password para refletir suas credenciais reais do MySQL.

Python

db_config = {
    'host': 'localhost',
    'database': 'teste_bd',
    'user': 'root',
    'password': 'auew1234' # <-- Alterar esta senha!
}
📋 Funções Implementadas (CRUD)
O script workbench.py define funções modulares para cada operação, garantindo que o código seja limpo e seguro contra SQL Injection (através do uso de placeholders %s).

1. Conexão
Função	Descrição
create_connection()	Tenta conectar ao banco de dados usando o db_config. Retorna o objeto de conexão se for bem-sucedido ou None em caso de falha.

Exportar para as Planilhas

2. Manipulação de Dados
Operação	Função	Descrição
CREATE	incluir_funcionario(conn, matricula, nome)	Insere um novo registro na tabela Tb_funcionario.
READ	consultar_funcionarios(conn)	Executa um SELECT para listar todos os funcionários.
UPDATE	alterar_funcionario(conn, matricula, novo_nome)	Atualiza o Nome_Funcionario de um registro específico baseado na matricula.
DELETE	excluir_funcionario(conn, matricula)	Remove um registro da tabela baseado na matricula.

Exportar para as Planilhas

▶️ Demonstração de Execução
O bloco principal (if __name__ == "__main__":) executa uma sequência de comandos para demonstrar todas as funções:

Estabelece a conexão.

Inclui (CREATE) 6 novos funcionários (Matrículas 102 a 107).

Consulta (READ) a lista de funcionários.

Altera (UPDATE) o nome do funcionário 107 para "MODO BUDA".

Consulta (READ) novamente para verificar a alteração.

Exclui (DELETE) todos os funcionários (incluindo uma tentativa de exclusão do 101, que deve falhar se não existir).

Consulta (READ) final para mostrar a tabela vazia.

Fecha a conexão com conn.close().

Como Rodar
Bash

python workbench.py
Exemplo de Saída Esperada (Parcial)
--- Conexão Workbench ---
... Conectando ...
... Sucesso ...

--- DEMONSTRAÇÃO CRUD ---
[C] O Funcionário Adrian (Matrícula: 102) foi incluído com sucesso.
...
[C] O Funcionário Houston (Matrícula: 107) foi incluído com sucesso.

[R] --- Lista de Funcionários ---
Matrícula: 102   | Nome: Adrian
...
Matrícula: 107   | Nome: Houston
---------------------------------
[U] Nome do funcionário com Matrícula 107 alterado para 'MODO BUDA'.

[D] Nenhum funcionário encontrado com Matrícula 101 para exclusão.
[D] O Funcionário com matrícula 102 foi excluído.
...
[D] O Funcionário com matrícula 107 foi excluído.

[R] --- Lista de Funcionários ---
Nenhum funcionário encontrado.
---------------------------------

Conexão encerrada.
