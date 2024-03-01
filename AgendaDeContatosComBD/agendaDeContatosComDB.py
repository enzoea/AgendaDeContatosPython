import mysql.connector
# Biblioteca de comandos de Sistema operacional
import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Conectar ao banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="enzo123",
    database="agenda"
)
cursor = conexao.cursor()

# Função para limpar tela de execução
def limpar_tela():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS e Linux
        os.system('clear')

# Definindo a lista de contatos
# Aqui, estamos criando uma lista vazia de contatos que iremos usar para armazenar os contatos
contatos = []

# Função para criar um novo contato
# Esta função criar_contato recebe duas parâmetros, nomee telefone, cria um dicionário com essas informações e 
# adiciona o dicionário à lista contatos. Em seguida, exibe uma mensagem informando que o contato foi criado com sucesso.
def criar_contato(nome, telefone):
    sql = "INSERT INTO contatos (nome, telefone) VALUES (%s, %s)"
    valores = (nome, telefone)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Contato criado com sucesso!")

# Função para listar todos os contatos
# A função listar_contatosverifica se a lista contatosestá vazia. Se estiver vazio, exibe uma mensagem informando que nenhum contato foi encontrado. 
# Caso contrário, ela percorre a lista de contatos e exibe os detalhes de cada contato, incluindo nome e telefone.
def listar_contatos():
    cursor.execute("SELECT * FROM contatos")
    resultados = cursor.fetchall()
    if not resultados:
        print("Nenhum contato encontrado.")
    else:
        print("Lista de contatos:")
        for resultado in resultados:
            print(f"Nome: {resultado[1]}, Telefone: {resultado[2]}")

# Função para atualizar um contato existente
# A função atualizar_contatorecebe um índice (posição na lista contatos), um novo nome e um novo telefone como parâmetros. 
# Ela verifica se o índice é válido (dentro dos limites da lista) e, para isso, atualiza o nome e o telefone do contato nessa posição. Caso contrário, informa que o índice é inválido.
def atualizar_contato(indice, novo_nome, novo_telefone):
    cursor.execute("SELECT * FROM contatos")
    resultados = cursor.fetchall()
    if indice >= 0 and indice < len(resultados):
        contato_id = resultados[indice][0]
        sql = "UPDATE contatos SET nome = %s, telefone = %s WHERE id = %s"
        valores = (novo_nome, novo_telefone, contato_id)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Contato atualizado com sucesso!")
    else:
        print("Índice inválido. Contato não encontrado.")

# Função para excluir um contato existente
# A função excluir_contatotambém recebe um índice como parâmetro. Ela verifica se o índice é válido e, se for, remova o contato na posição da lista contatosusando pop. 
# Em seguida, exibe uma mensagem informando que o contato foi excluído com sucesso.
def excluir_contato(indice):
    cursor.execute("SELECT * FROM contatos")
    resultados = cursor.fetchall()
    if indice >= 0 and indice < len(resultados):
        contato_id = resultados[indice][0]
        sql = "DELETE FROM contatos WHERE id = %s"
        valores = (contato_id,)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Contato excluído com sucesso!")
    else:
        print("Índice inválido. Contato não encontrado.")

# Loop principal do programa
# Aqui, começa o loop principal do programa que continua em execução até que o usuário escolha a opção de sair.
while True:
    #Menu de opções:
    #O programa exibe um menu de opções numeradas para o usuário:
    print("\nOpções:")
    print("1. Criar novo contato")
    print("2. Listar contatos")
    print("3. Atualizar contato")
    print("4. Excluir contato")
    print("5. Sair")

    #O usuário é solicitado a escolher uma opção de escrever o número correspondente.
    escolha = input("Escolha uma opção: ")
    limpar_tela()
    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        criar_contato(nome, telefone)
    elif escolha == "2":
        listar_contatos()
    elif escolha == "3":
        listar_contatos()
        indice = int(input("Digite o índice do contato que deseja atualizar: ")) - 1
        novo_nome = input("Digite o novo nome: ")
        novo_telefone = input("Digite o novo telefone: ")
        atualizar_contato(indice, novo_nome, novo_telefone)
    elif escolha == "4":
        listar_contatos()
        indice = int(input("Digite o índice do contato que deseja excluir: ")) - 1
        excluir_contato(indice)
    elif escolha == "5":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
    #Se o usuário inserir uma opção inválida, o programa exibirá uma mensagem de erro e solicitará que o usuário tente novamente.
