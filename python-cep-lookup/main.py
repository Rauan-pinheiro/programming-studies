import requests

def consultar_cep():
    print("\n--- CONSULTAR CEP ---")
    
    while True: 
        cep = input("Digite o CEP (apenas números): ").strip().replace('-', '').replace('.', '')

        if not cep.isnumeric() or len(cep) != 8:
            print("CEP inválido. Por favor, digite um CEP com 8 dígitos numéricos.\n")
            continue 

        try:
            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            response.raise_for_status() # Lança um erro se a resposta for um erro de HTTP (404, 500, etc.)
            
            dados = response.json()

            if "erro" in dados:
                print(f"O CEP: '{cep}' não foi encontrado.\n")
                continue

            print("\n--- Endereço Encontrado ---")
            print(f"CEP: {dados.get('cep', '')}")
            print(f"Logradouro: {dados.get('logradouro', '')}")
            print(f"Bairro: {dados.get('bairro', '')}")
            print(f"Cidade: {dados.get('localidade', '')}")
            print(f"Estado: {dados.get('uf', '')}")
            print("--------------------------\n")
            
            while True:
                salvar = input("Deseja salvar este endereço em um arquivo? [s/n]: ").lower()
                if salvar in ['s', 'n']:
                    break
                else:
                    print("Opção inválida.")
            
            if salvar == 's':
                full_dados = (
                    f"CEP: {dados.get('cep', '')}\n"
                    f"Logradouro: {dados.get('logradouro', '')}\n"
                    f"Bairro: {dados.get('bairro', '')}\n"
                    f"Cidade: {dados.get('localidade', '')}\n"
                    f"Estado: {dados.get('uf', '')}\n"
                    "--------------------\n"
                )
                with open("enderecos_salvos.txt", 'a', encoding='utf-8') as arquivo:
                    arquivo.write(full_dados)
                print("Endereço salvo com sucesso em 'enderecos_salvos.txt'!\n")

        except requests.exceptions.RequestException as e:
            print(f"Ocorreu um erro de conexão: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

        while True:
            continuar = input("Deseja consultar outro CEP? [s/n]: ").lower()
            if continuar in ['s', 'n']:
                break
            else:
                print("Opção inválida.")
        
        if continuar == 'n':
            print("\nAté logo!")
            break

if __name__ == "__main__":
    consultar_cep()
    