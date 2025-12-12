from datetime import datetime
import re
from mysql.connector import Error

def obter_data_nascimento_valida():
    
    while True:
        
        data_str = input("Digite sua data de nascimento (no formato dd/mm/aaaa): ")
        
        FORMATO_DATA = '%d/%m/%Y'
        hoje = datetime.now() # Data de hoje
        
        try:
            data_nascimento = datetime.strptime(data_str, FORMATO_DATA)
        
        except ValueError:
            print(f"Error: a data {data_str} não é uma data válida\n")
            continue
            
        if data_nascimento > hoje:
            print("A data não pode ser no futuro.\n")
           
        idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
        
        if idade <= 17:
            print("Somente pessoas maiores de 18 podem continuar!\n")
        
        if idade >=18:
            return data_nascimento
              
def verificar_cpf():
    
    while True:
        cpf = input("Digite seu CPF:")
        
        cpf_limpo = re.sub('[^\d]', '', cpf)
        
        # Verifica se o CPF tem 11 dígitos
        if len(cpf_limpo) != 11:
            print("CPF inválido. Tente novamente")
            continue
        
        # Verifica se todos os dígitos são iguais (ex: 111.111.111-11)
        if len(set(cpf_limpo)) == 1:
            print("CPF inválido, todos os números iguais. Tente novamente\n")
            continue
        
        # --- Cálculo do Primeiro Dígito Verificador ---
        soma = 0
        # Pega os 9 primeiros números do CPF
        nove_digitos = cpf_limpo[:9]

        # Multiplica os 9 dígitos pela sequência decresente de 10 a 2
        for i, digito in enumerate(nove_digitos):
            soma += int(digito) * (10-i)
            
        # O resto da divisão por 11
        resto = soma % 11
        
        # Se o resto for menor que 2, o dígito é 0. Caso contrário, é 11 - resto
        digito_verificador_1  = 0 if resto < 2 else 11 - resto
        
        # Compara o dígito calculado com o 10º dígito do CPF
        if digito_verificador_1 != int(cpf_limpo[9]):
            print("CPF inválido. Tente novamente.\n")
            continue
        
        # --- Cálculo do Segundo Dígito Verificador ---
        soma = 0
        
        # Pega os 10 primeiros dígitos do CPF
        dez_digitos = cpf_limpo[:10]

        # Multiplica os 10 dígitos pela sequência decresente de 11 a 2
        for i, digito in enumerate(dez_digitos):
            soma += int(digito) * (11 - i)
            
        resto = soma % 11
        digito_verificador_2 = 0 if resto < 2 else 11 - resto
        
        # Compara o dígito calculado com o 11º dígito do CPF
        if digito_verificador_2 != int(cpf_limpo[10]):
            print("CPF inválido, tente novamente!\n")
            continue
        
        return cpf_limpo
        
def verificar_email():
    
    # Expressão regular para validação de e-mail
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    while True:
        email = input("\nDigite seu E-mail:")
        
        if re.match(padrao, email):
            return email
        
        else:
            print("E-mail inválido! Digite novamente.")
            continue

def menu():
    print("\n--- MENU CRUD ---")
    print("1. Criar novo registro (Create)")
    print("2. Ler registros (Read)")
    print("3. Atualizar registro (Update)")
    print("4. Deletar registro (Delete)")
    print("0. Sair")
    
def criar_registro(cursor, conexao):
    """Lógica para Criar um novo registro."""
    try:
        print("\n--- CADASTRAR NOVO USUÁRIO ---")
        nome = input("Digite o nome: ")
        endereco = input("Digite o endereço: ")
        data_nascimento = obter_data_nascimento_valida()
        email = verificar_email()
        cpf = verificar_cpf()
        
        # Lógica de verificação de CPF duplicado
        cursor.execute("SELECT cpf FROM dados WHERE cpf = %s", (cpf,))
        if cursor.fetchone():
            print("\nErro: Este CPF já está cadastrado.")
            input("Pressione Enter para continuar...")
            return

        create_comando = 'INSERT INTO dados(nome, endereco, data_nascimento, cpf, email) VALUES (%s, %s, %s, %s, %s)'
        adicionar_valores = (nome, endereco, data_nascimento, cpf, email)
        
        cursor.execute(create_comando, adicionar_valores)
        conexao.commit()
        
        print(f"\nUsuário '{nome}' adicionado com sucesso!")

    except Error as e:
        if e.errno == 1062:
            print("\nErro: O E-mail informado já existe no cadastro.")
        else:
            print(f"\nOcorreu um erro ao inserir os dados: {e}")
        conexao.rollback()
    
    input("Pressione Enter para continuar...")

def ler_registros(cursor):
    """Lógica para Ler todos os registros."""
    try:
        read_comando = 'SELECT id, nome, endereco, data_nascimento, cpf, email FROM dados'
        cursor.execute(read_comando)
        resultados = cursor.fetchall()

        if not resultados:
            print("\nNenhum dado cadastrado no banco de dados.")
        else:
            print("\n--- DADOS CADASTRADOS ---")
            for linha in resultados:
                id_db, nome, endereco, data_nascimento, cpf, email = linha
                data_formatada = data_nascimento.strftime('%d/%m/%Y')
                
                print(f"ID: {id_db}\nNome: {nome}\nEndereço: {endereco}\nData de Nascimento: {data_formatada}\nCPF: {cpf}\nE-mail: {email}")
                print("-" * 25)
            print("--- FIM DA LISTA ---")

    except Error as e:
        print(f"Ocorreu um erro ao tentar ler os dados: {e}")
    
    input("\nPressione Enter para voltar ao menu...")

def atualizar_registro(cursor, conexao):
    """Lógica para Atualizar um registro."""
    try:
        id_para_atualizar = int(input("Digite o ID do registro que deseja atualizar: "))
        
        cursor.execute("SELECT * FROM dados WHERE id = %s", (id_para_atualizar,))
        registro_atual = cursor.fetchone()
        
        if not registro_atual:
            print(f"Erro: Nenhum registro encontrado com o ID {id_para_atualizar}.")
            input("\nPressione Enter para voltar ao menu...")
            return

        print("\n--- DADOS ATUAIS DO REGISTRO ---")
        id_db, nome, endereco, data_nascimento, cpf, email = registro_atual
        print(f"ID: {id_db}\nNome: {nome}\nEndereço: {endereco}\nCPF: {cpf}\nE-mail: {email}")
        print("-" * 30)

        print("Qual campo você deseja atualizar?\n1. Nome\n2. Endereço\n3. E-mail\n0. Cancelar")
        escolha_campo = input("Sua escolha: ")

        mapa_colunas = {'1': 'nome', '2': 'endereco', '3': 'email'}
        if escolha_campo in mapa_colunas:
            nome_coluna = mapa_colunas[escolha_campo]
            novo_valor = input(f"Digite o novo valor para {nome_coluna}: ")

            comando_update = f"UPDATE dados SET {nome_coluna} = %s WHERE id = %s"
            valores = (novo_valor, id_para_atualizar)
            
            cursor.execute(comando_update, valores)
            conexao.commit()
            
            if cursor.rowcount > 0:
                print("\nRegistro atualizado com sucesso!")
            else:
                print("\nNenhuma alteração foi feita.")
        elif escolha_campo == '0':
            print("Operação cancelada.")
        else:
            print("Opção inválida.")
    
    except ValueError:
        print("\nErro: O ID deve ser um número inteiro.")
    except Error as e:
        print(f"\nOcorreu um erro ao atualizar o registro: {e}")
        conexao.rollback()
    
    input("\nPressione Enter para voltar ao menu...")

def deletar_registro(cursor, conexao):
    """Lógica para Deletar um registro."""
    try:
        id_para_deletar = int(input("Digite o ID do registro que deseja DELETAR: "))
        
        cursor.execute("SELECT * FROM dados WHERE id = %s", (id_para_deletar,))
        registro = cursor.fetchone()
        
        if not registro:
            print(f"Erro: Nenhum registro encontrado com o ID {id_para_deletar}.")
            input("\nPressione Enter para voltar ao menu...")
            return

        print("\n!!! ATENÇÃO: DELETANDO O REGISTRO ABAIXO !!!")
        id_db, nome, _, _, cpf, _ = registro
        print(f"ID: {id_db}\nNome: {nome}\nCPF: {cpf}")
        print("-" * 50)

        confirmacao = input("Você tem certeza? (s/n): ").lower().strip()
        
        if confirmacao == 's':
            comando_delete = "DELETE FROM dados WHERE id = %s"
            cursor.execute(comando_delete, (id_para_deletar,))
            conexao.commit()
            
            if cursor.rowcount > 0:
                print("\nRegistro deletado com sucesso!")
        else:
            print("\nOperação de exclusão cancelada.")

    except ValueError:
        print("\nErro: O ID deve ser um número inteiro.")
    except Error as e:
        print(f"\nOcorreu um erro ao deletar o registro: {e}")
        conexao.rollback()
    
    input("\nPressione Enter para voltar ao menu...")
