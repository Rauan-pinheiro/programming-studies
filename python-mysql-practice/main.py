from dotenv import load_dotenv
import os
from functions.funcao import adicionar_produto, atualizar_produto, deletar_produto, listar_produto, menu

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

def main():
    
    db_config = {
        "host": DB_HOST,
        "user": DB_USER,
        "password": DB_PASSWORD,
        "database": DB_NAME
    }

    while True:
        menu()
        try:
            escolha = int(input("ESCOLHA:"))
        except:
            print("ERROR! digite um número válido")
            continue
            
        if escolha == 1:
            adicionar_produto(db_config)
        
        elif escolha == 2:
            listar_produto(db_config)
            
        elif escolha == 3:
            atualizar_produto(db_config)
        
        elif escolha == 4:
            deletar_produto(db_config)
        
        elif escolha == 0:
            print("Volte sempre!")
            break
        
        else:
            print("Opção inválida!")
        
if __name__ == "__main__":
    main()
    