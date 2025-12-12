def calcular_imc():
    print("\n--- CALCULADORA DE IMC --- \n")
    
    while True:
        try:
            # Pede e valida o peso
            peso_str = input("Digite seu PESO em quilogramas (ex: 75.5): ").replace(',', '.')
            peso = float(peso_str)
            if peso <= 0:
                print("ERRO: O peso deve ser um número positivo.\n")
                continue # Pula para o início do loop

            # Pede e valida a altura
            altura_str = input("Digite sua ALTURA em metros (ex: 1.80): ").replace(',', '.')
            altura = float(altura_str)
            if altura <= 0:
                print("ERRO: A altura deve ser um número positivo.\n")
                continue # Pula para o início do loop

            # --- O Cálculo ---
            imc = peso / (altura * altura)

            # --- A Classificação (lógica corrigida) ---
            # Verificamos em ordem, do menor para o maior. Fica mais simples.
            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif imc < 25: # Não precisa checar se é >= 18.5, pois se fosse menor, já teria entrado no primeiro 'if'.
                classificacao = "Peso ideal (parabéns!)"
            elif imc < 30:
                classificacao = "Levemente acima do peso (Sobrepeso)"
            elif imc < 35:
                classificacao = "Obesidade grau I"
            elif imc < 40:
                classificacao = "Obesidade grau II (severa)"
            else: # Se não for nenhum dos anteriores, é maior ou igual a 40.
                classificacao = "Obesidade grau III (mórbida)"
            
            print(f"\nSeu IMC é {imc:.2f}. Classificação: {classificacao}\n")

            # --- Loop para Calcular Novamente ---
            while True:
                continuar = input("Deseja calcular novamente? [s/n]: ").lower()
                if continuar in ['s', 'n']:
                    break
                else:
                    print("Opção inválida. Digite 's' para sim ou 'n' para não.")
            
            if continuar == 'n':
                print("\nAté logo!")
                break # Sai do loop principal

        except ValueError:
            print("ERRO: Valor inválido. Por favor, use apenas números.\n")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    calcular_imc()
    