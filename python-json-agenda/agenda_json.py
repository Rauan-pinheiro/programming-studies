import json
import os

# Função para exibir o menu principal
def menu():
    print('''
[0] - para sair
[1] - Salvar 
[2] - Listar''')

# Verifica se o arquivo 'agenda.json' já existe
# Se sim, carrega os dados do arquivo para a variável `contatos`
# Se não, inicia uma lista vazia
if os.path.exists("agenda.json"):
    with open("agenda.json", "r", encoding='utf-8') as arquivo:
        contatos = json.load(arquivo)  # Carrega os contatos do arquivo
else:
    contatos = []  # Lista vazia para armazenar contatos

# Loop principal do programa
while True:
    menu()
    try:
        escolha = int(input('Escolha: '))  # Recebe a opção do usuário
    except:
        print('Digite somente os números mostrados!')
        continue

    if escolha == 0:
        print('Volte sempre!')  
        break  # Encerra o programa

    elif escolha == 1:
        # Salva um novo contato
        try:
            nome = input('Nome do contato: ')
            telefone = int(input('Telefone: '))
            email = input('EMAIL: ')
        except:
            print('Insira dados válidos!')
            continue

        # Cria o novo contato como dicionário
        new_contato = {"nome": nome, "telefone": telefone, "email": email}
        contatos.append(new_contato)  # Adiciona o novo contato à lista

        # Salva a lista completa no arquivo JSON
        with open("agenda.json", 'w', encoding='utf-8') as arquivo:
            json.dump(contatos, arquivo, indent=4)  # indent=4 deixa o arquivo organizado
        print('Contato salvo!')

    elif escolha == 2:
        # Lista os contatos salvos
        if not contatos:
            print('Nenhum contato salvo!')
        else:
            print('\nContatos salvos:')
            for i, contato in enumerate(contatos, start=1):
                print(f'{i}. Nome: {contato["nome"]} | Telefone: {contato["telefone"]} | Email: {contato["email"]}')

