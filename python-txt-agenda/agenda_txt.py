from time import sleep

# Função que exibe o menu
def menu():
    return '''
[1] - cadastrar
[2] - listar
[3] - buscar
[4] - deletar
[0] - sair'''

# Loop principal do programa
while True:
    sleep(1.5)  # Espera 1.5 segundos entre cada execução do menu (para dar uma "pausa visual")
    print(menu())

    try:
        escolha = int(input('ESCOLHA:'))  # Lê a opção do menu
    except:
        print('Digite somente os números do menu!')
        continue  # Volta ao início do loop se o valor for inválido

    if escolha == 1:
        # Adiciona nome e senha no arquivo 'dados.txt'
        with open("dados.txt", 'a', encoding='utf-8') as arquivo:
            print('-'*15)
            nome = input('NOME:')
            senha = input('SENHA:')
            arquivo.write(f'{nome} - {senha}\n')
            print('Dados adicionados com sucesso!')

    elif escolha == 2:
        # Lê e exibe todo o conteúdo do arquivo
        print('-'*15)
        with open("dados.txt", 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            if conteudo == '':
                print('Arquivo vazio.')
            print(conteudo)

    elif escolha == 3:
        # Busca por uma palavra (nome) no arquivo
        print('-'*15)
        with open("dados.txt", 'r', encoding='utf-8') as arquivo:
            palavra_busca = input('Digite o nome da pessoa que deseja buscar:')
            dado_pessoa = arquivo.readlines()
            for linha in dado_pessoa:
                if palavra_busca in linha:
                    print(linha)

    elif escolha == 4:
        # Apaga o conteúdo do arquivo se encontrar o nome (poderia ser melhorado)
        with open("dados.txt", 'r', encoding='utf-8') as arquivo:
            nome_apagar = input('Digite o nome da pessoa que deseja apagar:')
            dado_pessoa = arquivo.readlines()
            for linha in dado_pessoa:
                if nome_apagar in linha:
                    with open("dados.txt", 'w', encoding='utf-8') as arquivo:
                        arquivo.write('')  # Apaga TODO o arquivo (isso precisa ser melhorado)

    elif escolha == 0:
        break

print('Volte sempre!')
