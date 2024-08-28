import random


def rolagem():
    valor_min = 1
    valor_max = 6
    rolagem = random.randint(valor_min, valor_max)
    return rolagem


def inserir_numero_jogadores():
    while True:
        jogadores = int(input("Insira o numero de jogadores (2 - 4): "))
        if 2 <= jogadores <= 4:
            print(f"Numero de jogadores: {jogadores}")
            return jogadores
        else:
            print("Opcao invalida")


def verificar_vitoria(pontuacoes_jogador, pontuacao_maxima):
    for jogador, pontuacao in enumerate(pontuacoes_jogador):
        if pontuacao >= pontuacao_maxima:
            return jogador + 1
    return None


def rolar_dado(jogadores):
    pontuacao_maxima = 20
    pontuacoes_jogador = [0 for _ in range(jogadores)]

    while max(pontuacoes_jogador) < pontuacao_maxima:

        for jogador in range(jogadores):
            print(f"\nTurno do jogador {jogador + 1}\n")
            print(f"Sua pontuacao total: {pontuacoes_jogador[jogador]}\n")
            pontuacao_atual = 0

            while True:
                escolha = input("Rolar dado? (S - N): ")
                if escolha.lower() == "n":
                    break
                elif escolha.lower() == "s":
                    valor = rolagem()
                    if valor == 1:
                        print("Voce rolou 1! Perdeu o turno e os pontos atuais!")
                        pontuacao_atual = 0
                        break
                    else:
                        pontuacao_atual += valor
                        print(f"Voce tirou {valor}!")
                    print(f"Pontuacao atual: {pontuacao_atual}!")
                else:
                    print("Opcao invalida")

            pontuacoes_jogador[jogador] += pontuacao_atual
            print(f"Pontuacao total: {pontuacoes_jogador[jogador]}")

        vencedor = verificar_vitoria(pontuacoes_jogador, pontuacao_maxima)
        if vencedor is not None:
            print(f"O jogador {vencedor} venceu!")
            quit()


numero_de_jogadores = inserir_numero_jogadores()
rolar_dado(numero_de_jogadores)
