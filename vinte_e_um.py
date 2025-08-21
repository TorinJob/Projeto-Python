import random
import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def criar_baralho():
    """Criar um baralho padrão de 52 cartas."""
    naipes = ['Copas', 'Ouros', 'Paus', 'Espada']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    baralho = []
    for naipe in naipes:
        for valor in valores:
            baralho.append({'naipe': naipe, 'valor': valor})
    return baralho
    
def obter_pontos(carta):
    """Retorna o valor em pontos de uma única carta."""
    valor = carta['valor']
    if valor in ['J', 'Q', 'K']:
        return 10
    elif valor == 'A':
        return 11  
    else:
        return int(valor)

def calcular_pontuacao(mao):
    """Calcula a pontuação total de uma mão, tratando o valor do Ás."""
    pontos = sum(obter_pontos(carta) for carta in mao)
    num_ases = sum(1 for carta in mao if carta['valor'] == 'A')
    while pontos > 21 and num_ases > 0:
        pontos -= 10
        num_ases -= 1
    return pontos
def mostrar_mao(mao, nome_jogador, esconder_primeira_carta=False):
    """Exibe as cartas e a pontuação de uma mão."""
    print(f"\n--- Mão de {nome_jogador} ---")
    if esconder_primeira_carta:
        print("  [ CARTA OCULTA ]")
        for i in range(1, len(mao)):
            print(f" {mao[i]['valor']} de {mao[i]['naipe']}")
    else:
        for carta in mao:
            print(f" {carta['valor']} de {carta['naipe']}")
            print(f"Pontuação: {calcular_pontuacao(mao)}")

def jogar_vinte_e_um():
    """Função principal que executa o jogo."""
    while True:
        limpar_tela()
        baralho = criar_baralho()
        random.shuffle(baralho)

        mao_jogador = [baralho.pop(), baralho.pop()]
        mao_dealer = [baralho.pop(), baralho.pop()]
        
        turno_jogador_ativo = True
        while turno_jogador_ativo:
            limpar_tela()
            mostrar_mao(mao_dealer, "Dealer", esconder_primeira_carta=True)
            mostrar_mao(mao_jogador, "Você")

            pontuacao_jogador = calcular_pontuacao(mao_jogador)
            if pontuacao_jogador >= 21:
                break
            escolha = input("\nVocê quer (C)omprar mais uma carta ou (P)arar? ").lower()
            if escolha == 'c':
                mao_jogador.append(baralho.pop())
            elif escolha == 'p':
                turno_jogador_ativo = False
            else:
                print("Opção inválida. tente novamente.")
                input("Pressione Enter para continuar...")
        pontuacao_jogador = calcular_pontuacao(mao_jogador)
        limpar_tela()
        if pontuacao_jogador > 21:
            print("Você estorou com mais de 21 pontos!")
        else:
            print("---Turno do Dealer---")
            while calcular_pontuacao(mao_dealer) < 17:
                mao_dealer.append(baralho.pop())
            mostrar_mao(mao_dealer, "Dealer")
            mostrar_mao(mao_jogador, "Você")

            pontuacao_dealer = calcular_pontuacao(mao_dealer)
            print("\n--- Resultado final---")
            if pontuacao_dealer > 21:
                print("O Dealer estorou! Você Venceu!")
            elif pontuacao_dealer > pontuacao_jogador:
                print("O Dealer venceu.")
            elif pontuacao_jogador > pontuacao_dealer:
                print("Parabens Você Venceu!")
            else:
                print("É eum empate")
        jogar_novamente = input("\nQuer jogar novemnte? (s/n):").lower()
        if jogar_novamente != 's':
            break

if __name__ == "__main__":
    jogar_vinte_e_um()


