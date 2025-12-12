from functions import (
    menu, 
    criar_registro, 
    ler_registros, 
    atualizar_registro, 
    deletar_registro
)
import mysql.connector
from mysql.connector import Error
import os
import dotenv

dotenv.load_dotenv()

def main():
    conexao = None
    cursor = None

    try:
        # Tenta estabelecer a conexão com o banco de dados
        conexao = mysql.connector.connect(
            host = os.getenv('host'),
            user = os.getenv('user'),
            password = os.getenv('password'),
            database = os.getenv('database')
        )
        print("Conexão com o banco de dados realizada com sucesso!")
        cursor = conexao.cursor()
        
        while True:
            menu()
            try:
                escolha = int(input("Digite sua escolha: "))
            except ValueError:
                print("Erro: Por favor, digite um número inteiro.")
                continue

            if escolha == 0:
                print("\nVolte Sempre! <3")
                break
                
            elif escolha == 1:
                criar_registro(cursor, conexao)

            elif escolha == 2:
                ler_registros(cursor)

            elif escolha == 3:
                atualizar_registro(cursor, conexao)

            elif escolha == 4:
                deletar_registro(cursor, conexao)
                
            else:
                print("Número inválido, escolha uma opção do menu (0 a 4)!")
                
    except Error as e:
        print(f"Erro ao conectar ou operar o banco de dados: {e}")

    finally:
        # Garante que a conexão seja sempre fechada no final.
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão com o MySQL foi encerrada.")

# Ponto de entrada do programa
if __name__ == '__main__':
    main()
    