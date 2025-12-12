import mysql.connector

def adicionar_produto(config):
    conexao = None
    cursor = None
    
    try:
        nome = input("Digite o nome do produto:")
        descricao = input("Digite a descrição do produto:")
        
        while True:
            try:
                preco = float(input("Digite o preço (ex: 99.90):"))
                break
            except ValueError:
                print("Erro: Preço inválido. Por favor, use apenas números e ponto")
                
        while True:
            try:
                quantidade = int(input("Digite a quantidade em estoque:"))
                break
            except ValueError:
                print("Error: Quantidade inválida. Por favor, use apenas números inteiros (1,2,3)")
        
        conexao = mysql.connector.connect(**config)
        cursor = conexao.cursor()
        
        sql = "INSERT INTO produtos (nome, descricao, preco, quantidade) VALUES (%s, %s, %s, %s)"
        valores = (nome, descricao, preco, quantidade)
        
        cursor.execute(sql, valores)
        conexao.commit()
        
        print(f"\n ✅ Produto '{nome}' adicionado com sucesso! ID: {cursor.lastrowid}")
        
    except mysql.connector.Error as err:
        print(f"\n❌ Erro ao adicionar o produto: {err}\n")
        
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()

def listar_produto(config):
    conexao = None
    cursor = None
    try:
        conexao = mysql.connector.connect(**config)
        cursor = conexao.cursor()
        
        cursor.execute("SELECT * FROM produtos")
        resultados = cursor.fetchall()
        
        print("\n--- ESTOQUE ATUAL ---")
        if not resultados:
            print("Estoque vazio.")
        else:
            for produto in resultados:
                print(f"ID: {produto[0]} | NOME: {produto[1]} | DESCRIÇÃO: {produto[2]}| PREÇO: R${produto[3]} | QUANTIDADE: {produto[4]}")
        
        print("-----------------------------------------------------------------------------------------------------------------------------\n")

    except mysql.connector.Error as err:
        print(f"Erro ao listar produtos: {err}")
        
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()

def atualizar_produto(config):
    print("\n--- ATUALIZAR PRODUTO ---")
    listar_produto(config)
    
    conexao = None
    cursor = None
    try:
        while True:
            try:
                id_produto = int(input("Digite o ID do produto que deseja alterar:"))
                if id_produto == 0:
                    return # Volta para o menu inicial
                break
            
            except ValueError:
                print("Error: ID inválido. por favor, digite apenas um número.")
        
        print("\n Qual campo você deseja alterar?")
        print("[1] Nome\n[2] Descrição\n[3] Preço\n[4] Quantidade")
        while True:
            campo_escolhido = input("Escolha uma opção:")
            
            if campo_escolhido in ['1', '2', '3', '4']:
                break
            else:
                print("Opção inválida. Escolha de 1 a 4.")
                
        mapa_campo = {'1': 'nome', '2': 'descricao', '3': 'preco', '4': 'quantidade'}
        coluna_para_alterar = mapa_campo[campo_escolhido]
        
        novo_valor = input(f"Digite um novo valor para '{coluna_para_alterar}':")
        
        if coluna_para_alterar in ['preco', 'quantidade']:
            while True:
                try:
                    if coluna_para_alterar == 'preco':
                        novo_valor = float(novo_valor)
                    else:
                        novo_valor = int(novo_valor)    
                    break
                
                except ValueError:
                    print(f"ERROR: Valor inválido para '{coluna_para_alterar}' ")
                    novo_valor = input(f"Digite o novo valor para '{coluna_para_alterar}':")
        
        conexao = mysql.connector.connect(**config)
        cursor = conexao.cursor()
        
        sql = f"UPDATE produtos SET {coluna_para_alterar} = %s WHERE id = %s"
        valores = (novo_valor, id_produto)
        
        cursor.execute(sql, valores)
        conexao.commit()
        
        print(f"\n✅ Produto com ID {id_produto} foi atualizado com sucesso!\n")
        
    except mysql.connector.Error as err:
        print(f"\n❌ Erro ao atualizar o produto: {err}\n")
        
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()
    
def deletar_produto(config):
    print("\n--- DELETAR PRODUTO ---")
    listar_produto(config)
    
    conexao = None
    cursor = None
    try:
        while True:
            try:
                id_produto = int(input("Digite o ID do produto que deseja DELETAR (0 para cancelar): "))
                if id_produto == 0:
                    print("Operação cancelada.")
                    return
                break
            except ValueError:
                print("Erro: ID inválido. por favor, digite apenas um número.")

        confirmacao = input(f"Você tem CERTEZA que deseja deletar o produto com ID {id_produto}? [s/n]: ").lower()

        if confirmacao == 's':
            conexao = mysql.connector.connect(**config)
            cursor = conexao.cursor()
        
            sql = "DELETE FROM produtos WHERE id = %s"
            valores = (id_produto,)
        
            cursor.execute(sql, valores)
            conexao.commit()
        
            if cursor.rowcount > 0:
                print(f"\n Produto com ID {id_produto} foi deletado com sucesso!\n")
            else:
                print(f"\n Nenhum produto encontrado com o ID {id_produto}. Nenhuma alteração foi feita.\n")
        else:
            print("Deleção cancelada pelo usuário.")
            
    except mysql.connector.Error as err:
        print(f"Erro ao deletar o produto: {err}\n")
        
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()
        
def menu():
    print('''
    --- GERENCIADOR DE ESTOQUE ---
    [1] Adicionar novo produto.
    [2] Listar produtos.
    [3] Atualizar produto.
    [4] Deletar produto.
    [0] Sair do programa.
    ''')
