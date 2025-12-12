# Função que calcula o IMC com base no peso e altura
def calcularIMC():
    imc = peso_pessoa / (altura_pessoa**2)  # Fórmula do IMC
    return f'Seu IMC é de {imc:.2f}'  # Retorna o resultado formatado com duas casas decimais

# Função que retorna a tabela de classificação do IMC
def tabela():
    return '''
Abaixo do peso: IMC < 18,5
Peso normal: IMC entre 18,5 e 24,9
Sobrepeso: IMC entre 25,0 e 29,9

OBESIDADE:
Grau I: IMC entre 30,0 e 34,9
Grau II: IMC entre 35,0 e 39,9
Grau III: IMC ≥ 40,0 '''

# Loop para garantir que o usuário insira valores válidos
while True:
    try:
        peso_pessoa = float(input('Digite seu peso em Kg:').replace(',', '.'))  # Aceita vírgula como separador decimal
        altura_pessoa = input('Digite sua altura:').replace(',', '.')
        altura_pessoa = float(altura_pessoa)
        break  # Sai do loop se tudo estiver certo
    except:
        print('!&ERRO! Tente novamente')  # Mensagem de erro genérica

# Exibe o resultado
print()
print(calcularIMC())
print()
print(tabela())
