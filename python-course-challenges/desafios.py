#te dá as boas vindas.
nome=input('qual é o seu nome?')
print('é um prazer te chonher Sr(a){}'.format(nome))

#junta os dados para formar uma dara de nascimento.
data=input('em qual dia você nasceu?')
mês=input('qual mês você nasceu?')
ano=input('qual ano você nasceu?')
print('você nasceu no dia',data,'do mês',mês,'no ano de',ano)

#soma dois valores.                                                                                      
x= int(input('escolha um número'))
y=int(input('escolha outro número'))
s=x+y
print('a soma é igual a',s)

#soma dois valores.
x=int(input('escolha um número'))
y=int(input('escolha outro valor'))
s=x+y
print('a soma entre {} e {} vale {}'.format(x,y,s))

#diz tudo sobre determinada frase ou palavra.
s=input('digite qualquer coisa:')
print(type(s))
print('contem letras e números?',s.isalnum())
print('é composto apenas por letras?',s.isalpha())
print('é composto apenas por números',s.isnumeric())
print('todas as letras são minuscuslas?',s.islower())
print('é um némero decimal?',s.isdecimal())
print('está em letras maisculas?',s.isupper)
print('está capitalizada?',s.istitle)

#diz qual é o seu suscessor e seu antecessor.
n=int(input('escolha um número:'))
print('o suscessor do número {} é {}, e seu antecessor é {}'.format(n,n+1,n-1))

#calcula o dobro,triplo e a raiz quadrada de qualquer número.
n=int(input('escolha um valor:'))
print('o dobro do número {} é {}, o seu triplo é {} e sua raiz quadrada é {:.2f}'.format(n,n*2,n*3,n**(1/2)))

#calcula a média de uma prova.
p1=float(input('nota parcial:'))
p2=float(input('nota global:'))
print('a media do aluno(a) é de {}'.format((p1+p2)/2))

#conversor de metros para centímetros e para melímetros.
m=float(input('escreva o valor em metros que deseja converter.'))
print('o valor em centímetros é de {}cm e em melímetros é de {}mm'.format(m*100,m*1000))

#calculadoura do 1 ao 9.
n=int(input('escolha um numero.'))
print('{}x1={}'.format(n,n*1))
print('{}x2={}'.format(n,n*2))
print('{}x3={}'.format(n,n*3))
print('{}x4={}'.format(n,n*4))
print('{}x5={}'.format(n,n*5))
print('{}x6={}'.format(n,n*6))
print('{}x7={}'.format(n,n*7))
print('{}x8={}'.format(n,n*8))
print('{}x9={}'.format(n,n*9))

#converte real para dólar
r=float(input('quantos reias gostaria de converter?'))
print('com esse valor você teria {:.2f} dólares americano.'.format(r/6.19))

#calcula o total de tinta gasto em uma pintura.
l=float(input('qual o valor da largura em metros?'))
h=float(input('qual a altura em metros?'))
a=(l*h)
print('o total de litros de tinta é: {:.2f}'.format(a/2))

#calcula um desconto em determinado produto.
preço=float(input('qual é o preço do produto?'))
porcnt=float(input('qual é a procentagem do desconto?'))
novo=preço-(preço*porcnt/100)
print('o porudto que custava {}, na promoção com desconto de {} vai custar {}'.format(preço,porcnt,novo))

#calcula o aumento de determinado produto/salário
s=float(input('qual o valor do seu salário/produto?'))
a=float(input('quanto foi a porcentagem do aumento?'))
ns=s+(s*a/100)
print('o valor do seu salário/produto é de {}, com o aumento de {}, ele agora é {}'.format(s,a,ns))

#conversor de temperatura em C° para F°
t=float(input('qual a temperatura em C°'))
f=((9*t)/5)+32
print('a temperatura é de {:<.1f}F°'.format(f))

#calcula o total a pagar pelo total de km rodados com um carro alugado
km=float(input('quantos km foi pecorrido?'))
dia=int(input('por quantos dias ele foi alugado?'))
preço=(km*0.15)+(60*dia)
print('o total a pagar é {:.2f}R$'.format(preço))

#calcula a raiz quadrada que qualquer número.
import math
num=int(input('escolha um número para calcular a sua raiz quadrada.'))
raiz=math.sqrt(num)
print('a raiz quadrada de {} é {}'.format(num,raiz))

#arendonda qualquer número com casa decimal, para sua primeira casa
import math
n=float(input('escolha um valor:'))
aren=math.floor(n)
print('o aredondamento de {} é {}'.format(n,aren))

#calucla a hipotenusa de um triangulo retângulo.
import math
co=float(input('qual o valor do cateto osposto?'))
ca=float(input('qual o valor do cateto adjacente?'))
hip=math.hypot(co,ca)
print('o valor da hipotenusa é {}'.format(hip))


#calcula sen,cos e tangente de qualquer ângulo.
import math
a=float(input('digite o valor do ângulo:'))
cos=math.cos(a)
sen=math.sin(a)
tan=math.tan(a)
print('o valor do seno do ângulo {} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(a,sen,cos,tan))

#sorteio 1 entre 4 alunos.
import random
a1=(input('primeiro aluno.'))
a2=(input('segundo aluno.'))
a3=(input('terceiro aluno.'))
a4=(input('quarto aluno.'))
lista=[a1,a2,a3,a4]
escolhido=random.choice(lista)
print('o escolhido foi {}'.format(escolhido))

#muda a ordem de uma lista.
import random
a1=(input('primeiro nome.'))
a2=(input('segundo nome.'))
a3=(input('terceiro nome.'))
a4=(input('quarto nome.'))
lista=[a1,a2,a3,a4]
random.shuffle(lista)
print('a ordem foi de')
print(lista)

#desafio do curso de python.
nome=input('digite seu nome completo.')
md1=nome.upper()
md2=nome.lower()
md3=nome.strip(),len(nome)- nome.count(' ')
md4=nome.split()
md5=md4[0]
md6=md5,len(md5)
print('''o seu nome com todas as letras maiusculas é {}
com todas minusculas é {}
sem considerar os espaços, seu nome tem {} letras
seu primeiro nome tem {} letras'''.format(md1,md2,md3,md6))

#mostra a dezena,centena,unidade e milhar de um número de 4 dígitos
numero=str(input('digite um valor:'))
milhar=numero[0]
centena=numero[1:]
dezena=numero[2:]
unidade=numero[3:]
print('''milhar:{}.'
centena:{}
dezena:{}
unidade:{}'''.format(milhar,centena,dezena,unidade))

#desafio do curso.(ler o nome de uma cidade e diz se a palvra santo está presente na oração)
cid=str(input('escreva o nome da sua cidade.')).strip()
print(cid[:5].upper()== 'SANTO')

#desafio do curso.(afimar se a palavra Silva está presente na frase.)
nome=str(input('digite seu nome:')).strip()
resposta='SILVA' in nome.upper()
print('a palavra(Silva) está presente na frase?{}'.format(resposta))

#desafio do curso.
frase=str(input('escrava uma frase.')).upper().strip(' ')
totalA=frase.count('A')
aparece=frase.find('A')+1
final=frase.rfind('A')+1
print('''o (a) aparece {} vezes
      (a) está na posição inicial de {}
      (a) está na última posição em {}
       '''.format(totalA,aparece,final))

#diz o primeiro e o último nome do seu nome completo.
nome=str(input('escreva seu nome completo.'))
primeironome=nome.split()
primeironome1=primeironome[0]
segundonome=nome.split()
segundonome2=segundonome[-1:]
print('''seu primeiro nome é {}
      seu último nome é {}'''.format(primeironome1,segundonome2))

#diz se é par ou impar.
n=float(input('digite um número para saber se é par ou impar:'))
if n %2==0:
    print('ele é par!')
else:
    print('ele é impar!')
    
    #desafio do curso de python (casssino)
import random
num1=int(input('escolha um número de 1 a 5:'))
lista=[1,2,3,4,5]
num=random.choice(lista)
if num1==num:
    print('você ganhou! acertou o mesmo número sorteado pela máquina')
else:
    print('você perdeu!')

 #desafio do curso(de três números, ele diz o maior e o menor.)
num1=float(input('escolha um número:'))
num2=float(input('escolha outro número:'))
num3=float(input('escolha um último número:'))
if num1>num2>num3:
    print('o maior número é {} e o menor é {}'.format(num1,num3))
if num2>num1>num3:
    print('o maior número é {} e o menor é {}'.format(num2,num3))
if num3>num2>num1:
    print('o maior número é {} e o menor número é {}'.format(num3,num1))
else:
    print('todos os números são iguais.')
    
 #calcula a multa por limite de velocidade.
km=float(input('digite a quilometragem:'))
if km>80:
    print('você foi multado! a multa custa 7 reais por quilometro execido.')
    print('a multa vai custar {}'.format((km-80)*7))
else:
    print('você não foi multado, o limite da via é 80km/h')
    
#diz se um ano é bissexto ou não
from datetime import date
ano=int(input('digite um ano. ou digite 0 para saber se o ano atual é bissexto!'))
if ano ==0:
    ano=date.today().year
if ano  %4==0 and ano % 100 !=0 or ano %400 ==0:
    print('o ano de {} é bissexto'.format(ano))  
else:
    print('o ano de {} não é bissexto'.format(ano))
    
#calcula o valor de uma passem(desafio do curso)
km=float(input('qual a distância da viagem em Km?'))
if km<=200:
    print('o preço da passagem custará {}'.format(km*0.50))
else:
    print('o preço da passagem custará {}'.format(km*0.45))
    
#calcula o aumento de salário de acordo com oque você ganha(desafio do curso)
salario=float(input('qual o valor do seu salário?'))
if salario<=1250:
    print('seu novo salário com aumento de 15% é de {}'.format((salario*15/100)+salario))
else:
    print('seu novo salário com aumento de 10% é de {}'.format((salario*10/100)+salario))
    
#diz se três retas podem formar um triângulo ou não.
reta1=float(input('digite o maior valor das três retas:'))
reta2=float(input('digite o valor da segunda reta:'))
reta3=float(input('digite o valor da terceira reta:'))
if reta2+reta3>reta1:
    print('essas retas formam um triângulo!')
else:
    print('essas retas NÃO formam um triângulo!')

#desafio 38 do curso em vídeo.
num1=int(input('escolha um valor inteiro.'))
num2=int(input('escolha outro valor.'))
if num1>num2:
    print('o número {} é maior que {}.'.format(num1,num2))
elif num2>num1:
    print('o número {} é maior que {}.'.format(num2,num1))
else:
    print('os dois valores são iguais.')
    
#desafio 39 do curso em vídeo
from datetime import date
ano=int(input('em que ano você nasceu?'))
anoatual=date.today().year
idade=anoatual-ano
if idade>18:
    print('já passou {} anos, você deve se alistar'.format(idade-18))
elif idade<18:
    print('você não pode se alistar! ainda falta {} para você se alistar'.format(18-idade))
else:
    print('está na hora de se alistar!')
    
  #desafio 36 curso em vídeo.
casa=float(input('qual o valor da casa?'))
salario=float(input('qual o seu salário?'))
ano=int(input('em quantos anos você quer pagar?'))
prestação= casa/(ano*12)
minino= salario*30/100
if prestação <=minino:
    print('empréstimo aprovado!')
elif prestação > minino:
    print('empréstimo recusado!')
 
#desafio 40 curso em vídeo.
nota1=float(input('qual a primeira nota?'))
nota2=float(input('valor da segunda nota?'))
media=(nota1+nota2)/2
if media <=5:
    print('sua media é de {}, portanto está REPROVADO!'.format(media))
elif media ==7 or media >7:
    print('sua média é de {}, você PASSOU!'.format(media))
elif media == 6.9 or media > 5:
    print('sua media é de {}, portanto está de RECUPERAÇÃO!'.format(media))
    
#desafio 41 do curso em vídeo.
idade=int(input('digite a sua idade:'))
if idade <9 or idade == 9:
    print('sua categoria é MIRIM.')
elif idade <14 or idade == 14:
    print('sua categoria é INFANTIL.')
elif idade <19 or idade == 19:
    print('sua categoria é JUNIOR.')
elif idade <20 or idade == 20:
    print('sua categoria é SÊNIOR.')
elif idade >20:
    print('sua categoria é MASTER.')
    
#desafio 42 do curso em vídeo.
lado1=float(input('digite o valor do lado 1:'))
lado2=float(input('digite o valor do lado 2:'))
lado3=float(input('digite o valor do lado 3:'))
if lado1==lado2==lado3:
    print('o triângulo é EQUILÁTERO.')
elif lado1==lado2 or lado1 == lado3:
    print('o triângulo é ISÓCELES.')
elif lado1!=lado2!=lado3:
    print('o triângulo é ESCALENO.')
    
#desafio 43 curso em vídeo.
peso=float(input('qual é o seu peso?'))
altura=float(input('qual é a sua altura?'))
imc=peso/(altura**2)
if imc <18.5:
    print('seu imc é de {:.3f},você está abaixo do peso.'.format(imc))
elif imc > 18.5 or imc ==25:
    print('seu imc é de {:.3f}, peso ideal.'.format(imc))
elif imc > 25 or imc ==30:
    print('seu imc é de {:.3f}, você está com sobrepeso'.format(imc))
elif imc >30 or imc== 40:
    print('seu imc é de {:.3f},obesidade'.format(imc))
elif imc > 40:
    print('seu imc é de {:.3f}, densidade mórbida.'.format(imc))
    
#desafio 37 do curso em vídeo.
num=int(input('digite um número inteiro qualquer.'))
print('''escolha a base para conversão:
      [1] para binário.
      [2] para octal.
      [3] para hexadecimal.''')
opção=int(input('sua opção:'))
if opção == 1:
    print('o {} convertido para binário é igual a {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('o {} convertido para octal é igual a {}'.format(num,oct(opção)[2:]))
elif opção == 3:
    print('o {} convertido para hexadecimal é igual a {}'.format(num,hex(opção)[2:]))
else:
    print('opção inválida! tente novamente.')
    
#desafio 44 curso em vídeo.
pdd=float(input('Qual o valor do produto?'))
print('''Escolha uma das formas de pagamento:
      [1] avista/cheque 10% de desconto.
      [2] avista no cartão 5% de desconto.
      [3] em até 2x no cartão, preço formal.
      [4] 3x ou mais no cartão 20% de juros.''')
opçao=int(input('sua opção:'))
if opçao==1:
    print('o valor fica por {}'.format(pdd-(pdd*10/100)))
elif opçao==2:
    print('o valor do produto fica por {}'.format(pdd-(pdd*5/100)))
elif opçao==3:
    print('o valor do produto fica por 2x de {}'.format(pdd/2))
elif opçao==4:
    parcela=int(input('quantas parcelas deseja?'))
    condicao= (pdd+(pdd*20/100))
    parcelamento= condicao/parcela
    print(''''o valor do produto fica por {}, divido em {} parcelas, o valor fica {} por mês'''.format(condicao,parcela,parcelamento))

#desafio 45 curso em vídeo.
import random
itens= ('pedra','papel','tesoura')
computador= random.randint(0,2)
print('''escolha sua jogada:
      [0] pedra
      [1] papel
      [2] tesoura''')
jogador=int(input('qual a sua jogada?'))
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
if computador == 0:#computador jogou pedra
    if jogador == 0:
        print('EMPATE.')
    elif jogador == 1:
        print('JOGADOR VENCEU.')
    elif jogador ==2:
        print('COMPUTADOR VENCE.')
    else:
        print('JOGADA INVÁLIDA.')

elif computador== 1:#computador jogou papel
    if jogador ==0:
        print('COMPUTADOR VENCE.')
    elif jogador == 1:
        print('EMPATE.')
    elif jogador ==2:
        print('JOGADOR VENCE.')
    else:
        print('JOGADA INVÁLIDA.')
                
elif computador== 2:#computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador== 1:
        print('COMPUTADOR VENCE.')
    elif jogador==2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA.')

#desafio 46 do curso em vídeo.
import time
for c in range(10,0,-1):
    time.sleep(1)
    print(c)
print('Feliz ano novo! belos fogos.')

#desafio 47 curso em vídeo.
for c in range(0,51,2):
    print(c)
print('esses são os números pares entre 1 e 50.')

#desafio 48 curso em vídeo.
soma=0
for n in range(1,501,2):
    if n%3==0:
        soma= soma+n
print('a soma de todos os números divisíveis por 3 de 1 até 500 é {}'.format(soma))



#desafio 49 curso em vídeo.
numero=int(input('escolha um número para ver sua tabuada.'))
for c in range (1,11):
    print('{}x{}={}'.format(numero,c,numero*c))
    
#desafio 50 curso em vídeo.
soma=0
cont=0
for pergunta in range(1,7):
    n=int(input('digite o {} valor.'.format(pergunta)))
    if n %2==0:
     soma+= n
    cont+=1
print('você disse {} números e a soma dos números pares é de {}'.format(pergunta,soma))

#desafio 51 curso em vídeo.
termo=int(input('Digite o primeiro termo da PA?'))
razao=int(input('Qual a razão da PA?'))
decimo=termo+(10-1)*razao
for pa in range(termo,decimo+razao,razao):
    print(pa)
    
#desafio 52.
#desafio 53 curso em vídeo.
escolha=str(input('Digite qualquer coisa.')).strip().upper()
palavras= escolha.split()
junto= ''.join(palavras)
inverso=''
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]
if inverso == junto:
    print('é um palíndromo.')
else:
    print('não é um palíndromo.')
print(inverso)

#desafio 54 curso em vídeo.
from datetime import date
anoatual=date.today().year
totmaior=0
totmenor=0
for c in range(1,8):
    data=int(input('digite o ano de nascimento.'))
    if anoatual-data >=21:
        totmaior+=1
        print('essa pessoa é maior.')
    elif anoatual-data<21:
        totmenor+=1
        print('essa pessoa é menor.')
print('ao todo teve {} maior e {} menor.'.format(totmaior,totmenor))

#desafio 55 curso em vídeo.   
maior=0
menor=0
for p in range(1,6):
   peso= float(input('qual o peso da {}ª pessoa?'.format(p)))
if p ==1:
    maior=peso
    menor=peso
else:
    if peso>maior:
        maior=peso
    if peso<menor:
        menor=peso
print('o maior peso lido foi de {}kg.'.format(maior))
print('o menor peso lido foi de {}kg.'.format(menor))

#deasfio 56 do curso em vídeo
nomevelho=''
maioridadehomem=0
totmulher20=0
for c in range(1,5):
    print('------{}° pessoa-----'.format(c))
    nome=str(input('nome:')).upper()
    idade=int(input('idade:'))
    sexo=str(input('sexo [M/F]:')).upper()
    mediaidade=(idade+idade+idade+idade)/4
    if c ==1 and sexo in 'Mm':
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'fF' and idade<20:
        totmulher20+=1
print('a média de todas as idades é de {}.'.format(mediaidade))
print('o homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))

#desafio 57 curso em vídeo.
escolha=str(input('informe seu sexo [M/F]')).upper().split()[0]
while escolha not in 'MF': 
    escolha=str(input('Dados inválidos, digite novamente.')).upper().split()[0]
print('Dados {} salvos.'.format(escolha))

#desafio 58 curso em vídeo.
tentativas=2
jogador=0
import random
lista=[1,2,3,4,5,6,7,8,9,10]
computador=random.choice(lista)
primeira=int(input('Escolha um número de 1 até 10.'))
if primeira < computador:
    print('Mais... tente de novo.')
else:
    print('Menos... tente de novo')
if primeira == computador:
    print('Acertou de primeira o mesmo número que a máquina.')
if primeira !=computador:
    while jogador != computador:
        jogador=int(input('Digite outro valor.'))
        if jogador < computador:
            print('Mais... tente de novo.')
        else:
            print('Menos... tente de novo.')
        if jogador!= computador:
            tentativas+=1
    print('Você tentou {} vezes até acertar o mesmo número que eu {}'.format(tentativas,computador))

#desafio 59 curso em vídeo.
valor1=float(input('Escolha um valor:'))
valor2=float(input('Escolha outro valor:'))
stop=0
while stop ==0:
    escolha=int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
'''))
    if escolha == 4:
        print('='*12)
        nescolha=float(input('Digite um novo valor:'))
        xescolha=float(input('Digite outro valor:'))
        valor1=nescolha
        valor2=xescolha
        print('='*12)
    if escolha == 1:
        print('='*12)
        print('A soma de {}+{}={}'.format(valor1,valor2,valor1+valor2))
        print('='*12)
    if escolha == 2:
        print('='*12)
        print('A multiplicação de {}x{}={}'.format(valor1,valor2,valor1*valor2))
        print('='*12)
    if escolha == 3:
        if valor1>valor2:
            print('='*12)
            print('o maior entre {} e {} é {}'.format(valor1,valor2,valor1))
            print('='*12)
        if valor2>valor1:
            print('='*12)
            print('o maior entre {} e {} é {}'.format(valor1,valor2,valor2))
            print('='*12)
        if valor1 == valor2:
            print('='*12)
            print('Os dois valores são iguais!')
            print('='*12)
    if escolha ==5:
        stop+=5
    if escolha not in [1,2,3,4,5]:
        print('='*12)
        print('Valor inválido, tente novamente.')
        print('='*12)
        
#desafio 60 curso em vídeo.
print('Digite um número')
num=int(input('para calcular seu fatorial:'))
c=num
f=1
print('Calculando {}!='.format(num), end=" ")
while c >0:
    print('{}'.format(c), end=' ')
    print(' x ' if c>1 else '=',end=' ')
    f*=c
    c-=1
print('{}'.format(f))

#desafio 61 curso em vídeo.
print('GERADOR DE PA')
print('-='*10)
termo=int(input('Qual o primeiro termo?'))
razao=int(input('Qual a razão?'))
x=termo
contador=0
while contador <=10:
    print('{},'.format(x), end=' ')
    x +=razao
    contador=contador+1

#desafio 62 curso em vídeo.
print('GERADOR DE PA')
print('-='*10)
termo=int(input('Qual o primeiro termo?'))
razao=int(input('Qual a razão?'))
x=termo
contador=0
total=0
mais=10
while mais !=0:
    total=total+mais
    while contador <=total:
        print('{},'.format(x), end=' ')
        x +=razao
        contador=contador+1
    print('PAUSA')
    mais=int(input('Quantos termos a mais você quer?'))
    
#desafio 65 curso em vídeo.
cont=False
media=0
contador=0
maior=0
menor=0
while cont ==False:
    num=int(input('Digite um número:'))
    media=media+num
    contador+=1
    if contador ==1:
        maior=menor=num
    else:
        if num > maior:
            maior=num
        if num < maior:
            menor=num
    escolha=str(input('Quer continuar?[S/N]').lower().split()[0])
    if escolha == 'n':
        cont=True
        print('A média de todos os números foi de {}'.format(media/contador))
        print('o maior número é {} e o menor é {}'.format(maior,menor))
    elif escolha!='s':
        print('Opção inválida, tente de novo')
        
#desafio 63 curso em vídeo.
print('TABELA DE FIBONACCI')
print('=-'*10)
termo=int(input('Digite quantos termos quer ver.'))
cont=3
f1=0
f2=1
print('{},{},'.format(f1,f2),end=' ')
while cont <=termo:
    f3=f1+f2
    cont+=1
    print('{},'.format(f3), end=' ')
    f1=f2
    f2=f3
print('FIM')

#desafio 66 curso em vídeo.
soma=cont=0
while True:
    num=int(input('digite um valor. [999 para parar]'))
    if num == 999:
        break
    cont+=1
    soma=num+soma
print(f'digitou {cont} e a soma é {soma}')

#desafio 67 curso em vídeo.
cont=0
numero=int(input('escolha um número para ver sua tabuada (0)para parar.'))
while True:
    cont+=1
    mult=numero*cont
    print(f'{numero}x{cont}={mult}')
    if cont ==10:
        cont=0
        numero=int(input('digite outro valor para ver a tabuada.'))
    if numero ==0:
        break
print('FIM.')

#desafio 68 curso em vídeo.
import random
cont=0
pc= random.randint(0,10)
while True:
    num=int(input('escolha um valor:'))
    escolha=str(input('você quer par ou impar?[P/I]').upper())
    total=pc+num
    if total %2==0:
        if escolha == 'P':
            print(f'pc jogou {pc} jogador jogou {num}, total de {total}')
            print('você venceu')
            cont += 1
        if escolha == 'I':
            print(f'pc jogou {pc} jogador jogou {num}, total de {total}')
            print('você perdeu.')
            break
    if total %2 == 1:
        if escolha == 'I':
            print(f'pc jogou {pc} jogador jogou {num}, total de {total}')
            print('você ganhou.')
            cont += 1
        if escolha == 'P':
            print(f'pc jogou {pc} jogador jogou {num}, total de {total}')
            print('você perdeu.')
            break
print(f'o jogador ganhou {cont} vezes seguidas.')

#desafio 69 curso em vídeo.
print('-='*20)
print('cadastre uma pessoa')
print('-='*20)
total=0
homem=0
mulher=0
while True:
    idade=int(input('digite a idade da pessoa:'))
    if idade >= 18:
        total=total+1
    sexo=str(input('qual o sexo da pessoa [F/M]').upper() .split()[0])
    if sexo == 'M':
        homem +=1
    if sexo == 'F':
        if idade <20:
            mulher+=1
    print('-='*20)
    escolha=str(input('quer contimuar? [S/N]').upper().split()[0])
    print('-='*20)
    if escolha == 'N':
        break
    if escolha == 'S':
        print('CARREGANDO...')
print(f'ao todo, foram cadastrados {total} com mais de 18 anos.')
print(f'ao todo foram cadastrados {homem} homens.')
print(f'e {mulher} mulheres tem menos de 20 anos.')

#desafio 70 curso em vídeo.
print('-'*20)
print('Loja super baratão')
print('-'*20)
total=0
mil=0
valor=0
nome=' '
while True:
    produto=str(input('Nome do produto:'))
    nome=produto
    preço=float(input('Preço:'))
    valor=preço
    if valor<preço:
        nome==produto
    total=preço+total
    if preço >1000:
        mil+=1
    escolha=str(input('Quer continuar? [S/N]')).upper().split()[0]
    if escolha == 'N':
        break
print(f'o total da compra foi de {total}R$')
print(f'{mil} produtos são maior do que 1000R$')
print(f'o nome do produto mais barato é o(a) {nome}')

#desafio 71 curso em vídeo.
valor=int(input('digite o valor que deseja sacar.'))
total=valor
ced=50
totced=0
while True:
    if total >= ced:
        total-=ced
        totced+=1
    else:
        if totced > 0:
            print(f'total de {totced} cédulas de R${ced}')
        elif ced == 50:
            ced=20
        elif ced == 20:
            ced=10
        elif ced == 10:
            ced=1
        totced=0
        if total == 0:
            break

#desafio 72 curso em vídeo.
num= ('Zero', 'Um','Dois', 'Três','Quatro','Cinco','Seis',
'Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze',
'Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    numero=int(input('Digite um número entre 0 e 20:'))
    if numero >=0 and numero <=20:
        break
print(f'Você digitou o número {num[numero]}')

#desafio 73 curso em vídeo.
times = (
    "Botafogo",
    "Palmeiras",
    "Flamengo",
    "Fortaleza",
    "Internacional",
    "São Paulo",
    "Corinthians",
    "Bahia",
    "Cruzeiro",
    "Vasco",
    "Vitória",
    "Atlético-MG",
    "Fluminense",
    "Grêmio",
    "Juventude",
    "Bragantino",
    "Athletico-PR",
    "Criciúma",
    "Atlético-GO",
    "Cuiabá"
)
print('-='*20)
print(f'a lista dos times do brasileirão de 2024:{times}')
print('-='*20)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('-='*20)
print(f'os 4 últimos colocados são:{times[-4:]}')
print('-='*20)
print(sorted,f'lista dos times em ordem alfabética:{times}')
print('-='*20)
print(f'o fortaleza está na posição {times.index("Fortaleza")+1}')

#desafio 74 curso em vídeo.
import random
num = random.sample(range(1, 101), 5) 
print(num)
tupla=num
print(f'o maior valor foi {max(tupla)}')
print(f'o menor valor foi de {min(tupla)}')

#desafio 75 curso em vídeo.
num=(int(input('Digite um valor:')),
     int(input('Digite outro valor:')),
     int(input('Digite mais um valor:')),
     int(input('Digite o último valor:')))
par=0
print('-='*20)
print(f'o número 9 apareceu {num.count(9)}')
if 3 in num:
    print(f'O valor 3 apareceu na posição {num.index(3)+1}°')
else:
    print('O valor 3, não foi digitado nenhuam vez.')
for n in num:
    if n %2==0:
        par+=1
print(f'Apareceu {par} números pares.')

#desafio 76 curso em vídeo.
itens=(
    'Lápis', 1.75,
    'Borracha', 2,
    'Caderno', 15.90,
    'Estojo', 25,
    'Tranferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro',34.90)
print('-'*40)
print('LISTA DE PREÇO')
print('-'*40)
for pos in range(0,len(itens)):
    if pos % 2 ==0:
        print(f'{(itens[pos]):.<30}',end='')
    else:
        print(f'R${itens[pos]:>7}')
        
#desafio 77 curso em vídeo.
palavras = ("banana", "cachorro", "computador", "elefante", "girafa", "python")
for palavra in palavras:
    print(f"\nNa palavra '{palavra}' temos as vogais: ", end="")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
            
#desafio 78 curso em vídeo.
lista=[]
for c in range(0,5):
    numero=int(input(f'digite um valor para a posiçao {c}:'))
    lista.append(numero)
maior = max(lista)
menor = min(lista)
pos_maior = [i for i, v in enumerate(lista) if v == maior]
pos_menor = [i for i, v in enumerate(lista) if v == menor]
print(f'os valores digitados foram {lista}')
print(f'O maior valor foi {maior} e apareceu nas posições: {pos_maior}')
print(f'O menor valor foi {menor} e apareceu nas posições: {pos_menor}')

#desafio 79 curso em vídeo.
lista=[]
while True:
    num=int(input('Digite um valor:'))
    if num in lista:
        print('Esse número já foi adicionado, não irei adicionar de novo')
    else:
        lista.append(num)
    escolha=str(input('Quer continuar? [N/S]').lower())
    if escolha == 's':
        print('-='*15)
    if escolha == 'n':
        break
lista.sort()
print('-='*15)
print(f'Os números digitados em ordem cresente foram: {lista}')

#desafio 80 curso em vídeo.
lista = []
for _ in range(5):
    num = int(input("Digite um número: "))
    pos = 0
    while pos < len(lista):
        if num <= lista[pos]:
            break
        pos += 1
    lista.insert(pos, num)
    print(f"Número {num} adicionado na posição {pos}.")
print("\nLista ordenada:", lista)

#desafio 81 curso em vídeo.
lista=[]
while True:
    num=int(input('digite um valor:'))
    lista.append(num)
    escolha=str(input('quer continuar? [S/N]').lower())
    if escolha =='n':
        break
    if escolha == 's':
        print('-='*20)
print('-'*15)
print(f'Ao todo foram digitados {len(lista)} valores.')
lista.sort(reverse=True)
print(f'A ordem da lista de forma decresente: {lista} ')
if 5 in lista:
    print('O número 5 faz parte da lista')
else:
    print('o valor 5 não foi digitado, não está na lista.')

#desafio 82 curso em vídeo.
lista_todos=[]
lista_par=[]
lista_impar=[]
while True:
    num=int(input('Digite um valor:'))
    lista_todos.append(num)
    if num %2==0:
        lista_par.append(num)
    elif num %2==1:
        lista_impar.append(num)
    escolha=str(input('Quer continuar? [S/N]').lower())
    if escolha in 'n':
        break
    if escolha in 's':
        print('-='*15)
print('-='*15)
print(f'Foi digitado os seguintes valores: {lista_todos}')
print(f'Os valores pares digitados foram: {lista_par}')
print(f'Os valores impares foram: {lista_impar}')

#desafio 83 curso em vídeo.
expressao = input("Digite uma expressão com parênteses: ")
pilha = []
for caractere in expressao:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) ==0:
    print('expressão válida!')
else:
    print('expressão inválida!')

#desafio 84 curso em vídeo.
nome=[]
nome_pesado=[]
totpessoas=0
while True:
    nome_pessoa=str(input('Digite o nome da pessoa:'))
    totpessoas +=1
    peso_pessoa=float(input('Qual o peso da pessoa?'))
    if peso_pessoa >=100:
        nome_pesado.append(nome_pessoa)
    else:
        nome.append(nome_pessoa)
    escolha=str(input('Quer cadastrar outra pessoa? [S/N]').lower())
    if escolha in 'n':
        break
    if escolha in 's':
        print('-='*20)
print('-='*20)
print(f'Ao total foram cadastradas {totpessoas} pessoas.')
print(f'A(s) pessoa(s) mais pesada(s) foi: {nome_pesado}.')
print(f'Pessoa(s) abaixo de 100kg: {nome}.')

#desafio 85 curso em vídeo.
numeros=[[], []]
for pos in range(1,8):
    num=int(input(f'Digite um número para a posição {pos}:'))
    if num %2==0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares são {numeros[0]}')
print(f'Os números impares são {numeros[1]}')

#desafio 86 curso em vídeo.
matriz=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=input(f'digite um número para [{l},{c}]')
print('-='*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]:^5}',end='')
    print()

#desafio 87 curso em vídeo.
matriz=[[0,0,0],[0,0,0],[0,0,0]]
numeros=[[],[]]
soma=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'digite um número para [{l},{c}]'))
print('-='*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]:^5}',end='')
    print()
print('-='*30)
for l in matriz:
    for c in l:
        if c %2==0:
            numeros[0].append(c)
            soma+=c
        else:
            numeros[1].append(c)
print(f'Os números pares são: {sorted(numeros[0])}')
print(f'Os números impares são: {sorted(numeros[1])}')
print(f'A soma de todos os números pares é igual a {soma}')
print('-='*30)
soma=matriz[0][2]+matriz[1][2]+matriz[2][2]
print(f'A soma dos valores da terceira coluna é igual a: {soma}')
print('-='*30)
maior=max(matriz[1])
print(f'O maior valor da segunda linha é {maior}')
print('-='*30)

#desafio 88 curso em vídeo.
import random
print('PALPITES PARA JOGOS DA MEGA SENA!')
escolha=int(input('Quantos jogos você quer?'))
cont_jogos=0
while cont_jogos < escolha:
    listanum=[]
    while len(listanum)<6:
        numeros=random.randint(1,60)
        if numeros not in listanum:
            listanum.append(numeros)
    print(f'jogo {cont_jogos+1}:{sorted(listanum)}')
    cont_jogos +=1

#desafio 89 curso em vídeo.
ficha=list()
while True:
    nome=str(input('nome:'))
    nota1=float(input('nota1:'))
    nota2=float(input('nota2:'))
    media=(nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    escolha=str(input('Quer continuar?[s/n]').lower())
    if escolha == 'n':
        break
print('-='*20)
print(f'{"No":<4}{"nome":<10}{"media":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    num=int(input('PARA VER AS NOTAS SEPARADAMENTE DIGITE O No DO ALUNO!(999 PARA PARAR)'))
    if num ==999:
        break
    if num <= len(ficha)-1:
        print(f'as notas de {ficha[num][0]} são {ficha[num][1]}')
        
#desafio 90 curso em vídeo.
dic={}
dic['nome']=str(input('Nome:'))
dic['media']=float(input(f'Qual a média de {dic["nome"]}:'))
print('-='*30)
print(f'o nome é igual a {dic["nome"]}.')
print(f'a média é igual a {dic["media"]}.')
if dic['media'] < 6:
    print(f'situação é igual a recuperação.')
elif dic['media']>6 and dic['media']<7:
    print(f'situação é igual a recuperação.')
else:
    print(f'a situação é igual a aprovado.')
    
#desafio 90 curso em vídeo.
dic={}
dic['nome']=str(input('Nome:'))
dic['media']=float(input(f'Qual a média de {dic["nome"]}:'))
print('-='*30)
print(f'o nome é igual a {dic["nome"]}.')
print(f'a média é igual a {dic["media"]}.')
if dic['media'] < 6:
    print(f'situação é igual a recuperação.')
elif dic['media']>6 and dic['media']<7:
    print(f'situação é igual a recuperação.')
else:
    print(f'a situação é igual a aprovado.')

#desafio 91 curso em vídeo.
import random
import time
from operator import itemgetter
dic={}
rank=list()
for j in range(1,5):
    valor_do_dado= random.randint(1,6)
    print(f'jogador{j} tirou {valor_do_dado}')
    time.sleep(1)
    dic[f'jogador{j}']=valor_do_dado
print('-='*30)
print('RANKING DOS JOGADORES')
rank=sorted(dic.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(rank):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    time.sleep(1)

#desafio 92 curso em vídeo.
from datetime import datetime
dic={}
data_de_hoje=datetime.today().year
print('-='*30)
dic['nome']=str(input('Nome:'))
dic['nascimento']=int(input('Ano de nascimento:'))
dic['idade da pessoa']= data_de_hoje-dic['nascimento']
dic['carteira de trabalho']=int(input('Digite a carteira de trabalho:(0 NÃO TEM)'))
if dic['carteira de trabalho'] == 0:
    print('-='*30)
    print(f'Nome tem o valor igual a {dic["nome"]}')
    print(f'Idade tem o valor de {dic["idade da pessoa"]}')
    print('CTPS tem o valor 0')
else:
    dic['ano de contratação']=int(input('Ano de contratação:'))
    idade_de_contratação=dic['ano de contratação']-dic['nascimento']
    dic['idade de aposentadoria']=idade_de_contratação+30
    dic['salário']=float(input('Valor do salário: R$'))
    print('-='*30)
    for k,i in dic.items():
        print(f'- {k} tem valor igual a {i}')

#desafio 93 curso em vídeo.
dic = {}
dic['nome do jogador'] = str(input('Nome do jogador: '))
dic['total de partidas'] = int(input(f'Quantas partidas {dic["nome do jogador"]} jogou? '))
dic['gols'] = [] 
for pos in range(dic['total de partidas']):
    gols = int(input(f'Quantos gols na partida {pos}? '))
    dic['gols'].append(gols)
dic['total de gols']=sum(dic['gols'])
print('-='*30)
print(dic)
print('-='*30)
print(f'O campo nome tem o valor {dic["nome do jogador"]}')
print(f'o campo gols tem o valor {dic["gols"]}')
print(f'o campo total de gols tem o valor {dic["total de gols"]}')
print('-='*30)
print(f'o jogador {dic["nome do jogador"]} jogou {dic["total de partidas"]}')
for x in range(dic['total de partidas']):
    print(f'Na partida {x}, ele fez {dic["gols"][x]} gols')
print(f'um total de {dic["total de gols"]}')

#desafio 94 curso em vídeo.
pessoas = []
soma_idades = 0
while True:
    pessoa = {}
    pessoa['nome'] = input("Nome: ").strip()
    while True:
        pessoa['sexo'] = input("Sexo [M/F]: ").strip().upper()
        if pessoa['sexo'] in 'MF':
            break
        print("Erro! Digite apenas 'M' ou 'F'.")
    pessoa['idade'] = int(input("Idade: "))
    soma_idades += pessoa['idade']  
    pessoas.append(pessoa)
    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break
total_pessoas = len(pessoas)
print(f"\nA) Total de pessoas cadastradas: {total_pessoas}")
media_idade = soma_idades / total_pessoas if total_pessoas > 0 else 0
print(f"B) Média de idade: {media_idade:.2f} anos")
mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'F']
print(f"C) Lista de mulheres cadastradas: {', '.join(mulheres) if mulheres else 'Nenhuma mulher cadastrada'}")
acima_media = [p for p in pessoas if p['idade'] > media_idade]
print("D) Lista de pessoas com idade acima da média:")
for p in acima_media:
    print(f"   Nome: {p['nome']}, Idade: {p['idade']} anos")

#desafio 95 curso em vídeo.
time = list()
dic = {}
partidas = list()

while True:
    dic.clear()
    dic['nome do jogador'] = str(input('Nome do jogador: '))
    dic['total de partidas'] = int(input(f'Quantas partidas {dic["nome do jogador"]} jogou? '))
    
    partidas.clear()  
    for pos in range(dic['total de partidas']):
        gols = int(input(f'Quantos gols na partida {pos + 1}? '))
        partidas.append(gols)  
    
    dic['gols'] = partidas[:]  
    dic['total de gols'] = sum(dic['gols'])  
    
    time.append(dic.copy())

    while True:
        escolha = input('Adicionar outro jogador? [S/N] ').strip().upper()
        if escolha in ('S', 'N'):
            break
        print('Opção inválida! Tente novamente.')
    
    if escolha == 'N':
        break

print('-='*40)
print('cod', end='')
for i in dic.keys():
    print(f'{i:<15}',end='')
print()

print('-=' * 50)
print(f'{"ID":<4}{"Nome":<15}{"Gols":<20}{"Total":<10}')
print('-' * 50)

for k, v in enumerate(time):
    print(f'{k:<4}{v["nome do jogador"]:<15}{str(v["gols"]):<20}{v["total de gols"]:<10}')
print('-=' * 30)

while True:
    busca=int(input('Mostrar dados de qual jogador?(999) para parar:'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! não existe jogador {busca}')
    else:
        print(f'------  levantamento do jogador {time[busca]["nome do jogador"]}:')
        for i,g in enumerate(time[busca]["gols"]):
            print(f'   no jogo {i+1} fez {g} gols')
    print('-='*40)
print('<<< VOLTE SEMPRE >>>')

#desafio 96 curso em vídeo.
def area(l,c):
    area_do_terreno=l*c
    print(f'O terreno {l}x{c} tem área igual a {area_do_terreno}m²')
    
largura=float(input('largura(m):'))
comprimento=float(input('comprimento(m):'))

area(largura,comprimento)

#desafio 97 curso em vídeo.
def escreva(txt):
    tam=len(txt)+4
    print('-'* tam)
    print(f'  {txt}')
    print('-'* tam)

escreva('OLÁ, MUNDO')
escreva('CD')
escreva('CURSO EM VÍDEO')

#desafio 98 curso em vídeo.
import time

def contador():
    print('CONTADOR DE 1 ATÉ 10 DE 1 EM 1')
    print('-='*30)
    
    for x in range(1,11):
        time.sleep(0.5)
        print(x,end=' ', flush=True)
        
    print()
    print('-='*30)
    print('de 10 até 0, de 2 em 2  '.upper())
    print('-'*30)
    
    for c in range(10,-1,-2):
        time.sleep(0.5)
        print(c,end=' ', flush=True)
    
    print()
    print('-='*30)

    iniciopessoa=int(input('Início:'))
    fimpessoa=int(input('Fim:'))
    passopessoa=int(input('Passo:'))
    
    if passopessoa == 0:
        passopessoa =1 if iniciopessoa < fimpessoa else -1
    
    if iniciopessoa > fimpessoa and passopessoa > 0:
        passopessoa = -passopessoa

    if iniciopessoa < fimpessoa and passopessoa < 0:
        passopessoa = -passopessoa 
    
    print('-='*30)
    print(f'contagem de {iniciopessoa} até {fimpessoa} pulando de {passopessoa}')
    
    for personalizado in range(iniciopessoa, fimpessoa + (1 if passopessoa > 0 else -1), passopessoa):
        time.sleep(0.5)
        print(personalizado,end=' ', flush=True)
    
contador()

#desafio 99 curso em vídeo.
from time import sleep

def maior (*num):
    cont=maior=0
    print('-='*30)
    print('Analisando valores...')
    for valor in num:
        print(f'{valor} ',end='',flush=True)
        sleep(0.3)
        
        if cont == 0:
            maior==valor
        else:
            if valor > maior:
                maior == valor
        cont += 1
    
    print(f', Foi informados os números: {valor} números ao todo')
    print(f'O maior valor foi {maior}')
    
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)

#desafio 100 curso em vídeo.
import random

numeros=[]
par=[]

def sorteia():
    for valor in range(1,6):
       valor= random.randint(1,10)
       numeros.append(valor)
    print(f'Os valores sorteados foram {numeros}')
    
def somapar():
    for k,numero in enumerate(numeros):
        if numero % 2 == 0:
            par.append(numero)
    soma= sum(par)
    print(f'Somando os valores pares de {numeros} a soma é igual a {soma}')
        
sorteia()
somapar()    

#desafio 101 curso em vídeo.
def voto(idade=0):
    if idade < 16:
        return f'com {idade} anos o VOTO É NEGADO!'
    elif 16 <= idade <18 or idade >65:
        return f'com {idade} anos o VOTO OPCIONAL!'
    else:
        return f'com {idade} anos o VOTO É OBRIGATÓRIO!'
    
idade_pessoa=int(input('Idade:'))
print(voto(idade_pessoa))

#desafio 102 curso em vídeo.
def fatorial (num=1, show=0):
    """função para cálculo fatorial:no print final do código, se adicionar o 
    'True' ele mostra todo o cálculo do fatorial de um número
    para apenas ver o resultado fatorial do número apague o 'True' """
    f=1
    for numero in range(num,0,-1):
       f*=numero
    if show ==True:
        for c in range(num,0,-1):
            print(f'{c}x',end='')
        print('=',end='')
        return f
    else:
        return f

n=int(input('CÁLCULO FATORIAL :NÚMERO:'))
print(fatorial(n,True))
help(fatorial)

#desafio 103 curso em vídeo.
def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

nome_jogador = input('Nome do jogador: ').strip()
gols_jogador = input('Total de gols: ').strip()


if gols_jogador.isnumeric(): 
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0  


if nome_jogador == '':
    print(ficha(gols=gols_jogador)) 
else:
    print(ficha(nome_jogador, gols_jogador))

#desafio 104 curso em vídeo.

def leiaInt(msg):
    """faz a validação se o número é um número inteiro e só permite número inteiro,
    se digitar letras ou espaços o programa não segue."""
    ok=False
    valor=0
    while True:
        n=(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok= True
        else:
            print('ERRO! digite um número válido.')
        if ok:
            break
    return valor

n = leiaInt("Digite um número inteiro: ")
print(f"Você digitou o número {n}.")

#desafio 105 curso em vídeo.

def notas(*valores,sit=False):
    dicionario={}
    dicionario['total de notas'] = len(valores)
    dicionario['maior nota'] = max(valores)
    dicionario['menor nota'] = min(valores)
    dicionario['média'] = sum(valores)/len(valores)

    if sit:
        if dicionario['média'] >= 7:
            dicionario['situação'] = 'Boa'
        elif dicionario['média'] >= 5:
            dicionario['situação'] = 'Razoável'
        else:
            dicionario['situação'] = 'Ruim'

    return dicionario

resp=notas(10,8,9,4,sit=True)
print(resp)

#desafio 106 curso em vídeo.
def ajuda(com):
    help(comando)

while True:
    comando=str(input('escolha um comando para ver o "help":'))
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)

#desafio 107 curso em vídeo.
def aumentar(preço,taxa):
    res= preço+(preço*taxa/100)
    return res

def diminuir(preço,taxa):
    res = preço-(preço*taxa/100)
    return res

def dobro(preço):
    res=preço*2
    return res

def metade(preço):
    res= preço/2
    return res

#import modulo - só funciona com modularização!

#p=float(input('Digite o preço: R$'))
#print(f'A metade de {p}$ é {modulo.metade(p)}$')
#print(f'O dobro de {p}$ é {modulo.dobro(p)}$')
#print(f'Com aumento de 10% fica, {modulo.aumentar(p,10)}')
#print(f'Com 10% de desconto fica, {modulo.diminuir(p,10)}')

#desafio 108 curso em vídeo. complemento do 107
def aumentar(preço=0,taxa=0):
    res= preço+(preço*taxa/100)
    return res

def diminuir(preço=0,taxa=0):
    res = preço-(preço*taxa/100)
    return res

def dobro(preço=0):
    res=preço*2
    return res

def metade(preço=0):
    res= preço/2
    return res

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

#import modulo 

#p=float(input('Digite o preço: R$'))
#print(f'A metade de {modulo.moeda(p)} é {modulo.moeda(modulo.metade(p))}')
#print(f'O dobro de {modulo.moeda(p)} é {modulo.moeda(modulo.dobro(p))}')
#print(f'O valor de {modulo.moeda(p)} com aumento de 10% fica, {modulo.moeda(modulo.aumentar(p))}')
#print(f'O valor de {modulo.moeda(p)} com 10% de desconto fica, {modulo.moeda(modulo.diminuir(p))}')

#desafio 109 curso em vídeo.
def aumentar(preço=0,taxa=0, formato= False):
    res= preço+(preço*taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preço=0,taxa=0,formato=False):
    res = preço-(preço*taxa/100)
    return res if formato is False else moeda(res)

def dobro(preço=0,formato=False):
    res=preço*2
    return res if formato is False else moeda(res)

def metade(preço=0,formato=False):
    res= preço/2
    return res if formato is False else moeda(res)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

#import modulo 

#p=float(input('Digite o preço: R$'))
#print(f'A metade de {modulo.moeda(p)} é {modulo.metade(p, True)}')
#print(f'O dobro de {modulo.moeda(p)} é {modulo.dobro(p,True)}')
#print(f'O valor de {modulo.moeda(p)} com aumento de 10% fica, {modulo.aumentar(p,10,True)}')
#print(f'O valor de {modulo.moeda(p)} com 10% de desconto fica, {modulo.diminuir(p,10,True)}')

#desafio 111 era para transformar em pacotes.

#desafio 112 curso em vídeo.
def aumentar(preço=0,taxa=0, formato= False):
    res= preço+(preço*taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preço=0,taxa=0,formato=False):
    res = preço-(preço*taxa/100)
    return res if formato is False else moeda(res)

def dobro(preço=0,formato=False):
    res=preço*2
    return res if formato is False else moeda(res)

def metade(preço=0,formato=False):
    res= preço/2
    return res if formato is False else moeda(res)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(p=0,taxa1=0,taxa2=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'A metade de {moeda(p)} é {metade(p, True)}')
    print(f'O dobro de {moeda(p)} é {dobro(p,True)}')
    print(f'O valor de {moeda(p)} com aumento de {taxa1}% fica, {aumentar(p,taxa1 ,True)}')
    print(f'O valor de {moeda(p)} com {taxa2}% de desconto fica, {diminuir(p,taxa2,True)}')
    
#import modulo 

#while True:
    #p=input('Digite o preço: R$')
    #if p.isalpha() or p.strip()=='':
        #print(f'ERRO!\"{p}\" não é válido -> digite um valor válido')
    #else:
        #p=p.replace(',','.')
        #p=float(p)
        #break

#modulo.resumo(p,80,35)

#desafio 113 curso em vídeo.
def leiaInt(msg):
    """faz a validação se o número é um número inteiro e só permite número inteiro,
    se digitar letras ou espaços o programa não segue."""
    while True:
        try:
            valor=int(input(msg))
            return valor
        except:
            print('ERRO! digite um número inteiro válido!')
            
        
    
def leiafloat(msg):
    while True:
        try:
            valor=float(input(msg).replace(',','.'))
            return valor
        except:
            print('ERRO! digite um número real válido!')
    
num_inteiro=leiaInt('Digite um número inteiro:')
num_float=leiafloat('Digite um número real:')

print('-'*30)
print(f'O número inteiro digitado foi {num_inteiro} e o real foi {num_float}')

#desafio 114 curso em vídeo.
import urllib
import urllib.error
import urllib.request
try:
    site= urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site pudim com sucesso.')

#desafio 115 curso em vídeo.
from time import sleep

def mostrar_menu():
    print('-'*40)
    print('MENU PRINCIPAL'.center(40))
    print('-'*40)
    print('1- Ver pessoas cadastradas.')
    print('2- Cadastrar nova pessoa.')
    print('3- Sair do sistema.')
    print('-'*40)
    return ''

def arquivoexiste(nome):
    try:
        a=open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criararquivo(nome):
    try:
        a= open(nome,'wt+')
        a.close()
    except:
        print('houve um !ERRO! na criação do arquivo!')
    else:
        print(f'Arquivo {nome} cirado com sucesso!')
        
def lerarquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        print('!ERRO! ao ler o arquivo.')
    else:
        print('-'*40)
        print('PESSOAS CADASTRADAS'.center(40))
        print('-'*40)
        for linha in a:
            dado= linha.split(';')
            dado[1]= dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        
    finally:
        a.close()
        
def leiaInt(msg):
    """faz a validação se o número é um número inteiro e só permite número inteiro,
    se digitar letras ou espaços o programa não segue."""
    while True:
        try:
            valor=int(input(msg))
            return valor
        except:
            print('ERRO! digite um número inteiro válido!')
            
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a=open(arq, 'at')
    except:
        print('Houve um !ERRO! na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um !ERRO! na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
arq= 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)
        
    
mostrar_menu()

while True:
    try:
        opçao=int(input('Sua Opção:').strip())
        
        if opçao < 1 or opçao > 3:
            print('!ERRO! digite um número válido.')
            
        elif opçao == 1:
           lerarquivo(arq)
           
        elif opçao == 2:
            print('-'*40)
            print('NOVO CADASTRO'.center(40))
            nome=str(input('NOME:'))
            idade=leiaInt('idade: ')
            cadastrar(arq, nome, idade)
            
        elif opçao == 3:
            print('Saindo do sistema...',end='',flush=True)
            sleep(2)
            print('Até logo!')
            break
        
    except ValueError:
        print('!ERRO! número inválido digitado, porfavor digite um número válido.')
        sleep(2)
        mostrar_menu() 