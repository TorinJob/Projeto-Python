

def calcular_imc(peso, altura):
    """Calcula o IMC com base no peso (kg) e altura (m)."""
    
    return peso / (altura ** 2)

def classificar_imc(imc):
    """Retorna a classificação do IMC com base nos valores da OMS."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso ideal Parabéns"
    elif 25 <= imc < 30:
        return "Levemente acima do peso"
    elif 30 <= imc < 35:
        return "Obesidade Grau I"
    elif 35 <= imc < 40:
        return "Obesidade Grau II (severa)"
    else: # Se for maior ou igual a 40
        return "Obesidade Grau III (mórbida)"

def main():
    """Função principal que executa o programa."""
    print("=" * 30)
    print("  Calculadora de IMC")
    print("=" * 30)

    
    while True:
        try:
            peso_str = input("Digite seu peso em kg : ").replace(',', '.')
            peso = float(peso_str)
            if peso > 0:
                break
            else:
                print("Erro: O peso deve ser um número positivo.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite apenas números.")

    
    while True:
        try:
            altura_str = input("Digite sua altura em metros: ").replace(',', '.')
            altura = float(altura_str)
            if altura > 0:
                break
            else:
                print("Erro: A altura deve ser um número positivo.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite apenas números.")

    
    imc_calculado = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc_calculado)

    
    print("\n" + "-" * 20)
    print("      RESULTADO")
    print("-" * 20)
    print(f"Seu IMC é: {imc_calculado:.1f}")
    print(f"Classificação: {classificacao}")
    print("-" * 20)



if __name__ == "__main__":
    main()